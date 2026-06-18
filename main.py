from src.graph.graph import graph
from src.graph.state import ProjectState


def main():

    state = ProjectState(
        user_request="""
데이터 레이어에 여러개 파일을 열어두었을 때, 체크를 각각 하지 못함. 하나를 체크해제하면 다른 것들도 체크해제가 되는 상황임.
각각 데이터는 따로 볼수 있도록 해야함. 예를 들어 seoul_landmarks.geojson 체크됨, sample_seoul.geojson 체크해제 라면 seoul_landmarks 파일만 보여야함.
이 기능 수정해줘.
"""
    )

    result = graph.invoke(state)

    print("\n===== Workflow Complete =====\n")
    print(result)


if __name__ == "__main__":
    main()