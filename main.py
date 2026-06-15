from src.graph.graph import graph
from src.graph.state import ProjectState


def main():

    state = ProjectState(
        user_request="""
GeoJSON 파일을 업로드하여 지도에 시각화하고,
속성 조회 및 면적 계산 기능을 제공하는 GIS 웹 서비스를 구축하라.
"""
    )

    result = graph.invoke(state)

    print("\n===== Workflow Complete =====\n")
    print(result)


if __name__ == "__main__":
    main()