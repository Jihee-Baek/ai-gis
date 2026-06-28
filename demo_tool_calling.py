import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# ==========================================
# 1. 에이전트가 호출할 Tool (도구/함수) 정의
# 함수에 적절한 타입 힌트와 Docstring(설명)을 적어주는 것이 매우 중요합니다.
# Gemini는 이 설명을 읽고 언제 어떤 함수를 호출할지 결정합니다.
# ==========================================

def list_gis_files() -> list:
    """
    현재 프로젝트 폴더 내에 존재하는 GIS 파일(.geojson 파일) 목록을 가져옵니다.
    """
    print("\n[Tool Execution] list_gis_files() 함수가 실행되었습니다.")
    files = [f for f in os.listdir(".") if f.endswith(".geojson")]
    return files

def get_gis_file_info(filename: str) -> dict:
    """
    지정된 GIS 파일의 상세 정보(파일 크기, 피처 개수 등)를 확인합니다.
    Args:
        filename (str): 정보를 확인할 GeoJSON 파일 이름 (예: 'seoul_landmarks.geojson')
    """
    print(f"\n[Tool Execution] get_gis_file_info(filename='{filename}') 함수가 실행되었습니다.")
    if not os.path.exists(filename):
        return {"error": f"파일 '{filename}'을 찾을 수 없습니다."}
    
    file_size = os.path.getsize(filename)
    
    # GeoJSON 내용을 열어 간단히 피처(객체) 개수 카운트
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            features_count = len(data.get("features", []))
            geom_types = list(set([feat.get("geometry", {}).get("type") for feat in data.get("features", []) if feat.get("geometry")]))
    except Exception as e:
        return {"error": f"파일을 파싱하는 중 오류가 발생했습니다: {e}"}
        
    return {
        "filename": filename,
        "file_size_bytes": file_size,
        "features_count": features_count,
        "geometry_types": geom_types
    }

# 도구들을 매핑하기 위한 딕셔너리
tools_map = {
    "list_gis_files": list_gis_files,
    "get_gis_file_info": get_gis_file_info
}

# ==========================================
# 2. 메인 실행 흐름
# ==========================================

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY가 설정되지 않았습니다.")
        print("프로젝트 루트 폴더에 .env 파일을 생성하고 GEMINI_API_KEY=your_key 를 입력하세요.")
        return

    # google-genai 클라이언트 초기화
    client = genai.Client(api_key=api_key)

    # 1. 사용자 질문 정의
    user_prompt = "프로젝트 내에 어떤 geojson 파일이 있는지 목록을 확인하고, 그 중 seoul_landmarks.geojson 파일의 상세 정보를 분석해서 알려줘."
    print(f"사용자 질문: {user_prompt}")

    # 2. 첫 번째 Gemini API 호출 (도구 목록 제공)
    # config의 tools 인자에 함수 객체 목록을 전달합니다.
    config = types.GenerateContentConfig(
        tools=[list_gis_files, get_gis_file_info],
        temperature=0.0 # 일관된 결과를 위해 0.0 권장
    )
    
    print("\nGemini에게 첫 번째 요청을 보내는 중...")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_prompt,
        config=config
    )

    # 3. 모델의 응답 분석 (Tool 호출 요청이 있는지 확인)
    # Gemini가 대답하기 위해 특정 함수를 호출해야 한다고 판단하면, response.function_calls 에 정보가 담깁니다.
    print(f"Gemini 첫 응답 상태: {response.text or 'Tool 호출 요청이 있음'}")
    
    # 대화 기록을 관리하여 모델에게 도구 실행 결과를 다시 보냅니다.
    # 대화의 흐름은: [USER] -> [MODEL (Tool Call)] -> [USER (Tool Result)] -> [MODEL (Final Answer)]
    history = [
        types.Content(role="user", parts=[types.Part.from_text(text=user_prompt)]),
        response.candidates[0].content # 모델이 보낸 Tool 호출 요청 내용
    ]

    if response.function_calls:
        print("\n>>> Gemini가 다음 함수 호출을 요청했습니다:")
        tool_results_parts = []
        
        for call in response.function_calls:
            print(f"- 함수명: {call.name}")
            print(f"- 인자: {call.args}")
            
            # 실제 Python 함수 실행
            func = tools_map.get(call.name)
            if func:
                # 전달된 arguments를 이용해 함수 호출
                result = func(**call.args)
                print(f"  -> 실행 결과: {result}")
                
                # 도구 실행 결과를 Part 객체로 생성
                # 이때 call.name과 call.id(있는 경우)를 매칭해야 모델이 매핑할 수 있습니다.
                part = types.Part.from_function_response(
                    name=call.name,
                    response={"result": result}
                )
                tool_results_parts.append(part)
            else:
                print(f"에러: 등록되지 않은 함수입니다: {call.name}")
        
        # 4. 두 번째 Gemini API 호출 (도구 실행 결과를 전달)
        # 대화 기록에 도구 실행 결과(FunctionResponse)를 추가합니다.
        history.append(
            types.Content(role="user", parts=tool_results_parts)
        )
        
        print("\nGemini에게 도구 실행 결과를 전송하여 최종 답변 생성 중...")
        final_response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=history,
            config=config # 제공 가능한 도구 목록을 다시 함께 전달
        )
        
        print("\n================ 최종 답변 ================")
        print(final_response.text)
        print("===========================================")
        
    else:
        print("Gemini가 Tool을 호출할 필요가 없다고 판단했습니다.")
        print(response.text)

if __name__ == "__main__":
    main()
