## 소개
문서화 및 데이터 인제스천을 위한 도구와 백엔드 코드를 포함합니다.

## 폴더 구조
- `backend/`: 핵심 백엔드 로직
  - `core.py`: 주요 기능 구현
- `ingestion.py`: 데이터 인제스천 스크립트
- `langchain-docs/`: 관련 문서 저장소
- `main.py`: 진입점 스크립트

## 사용법
1. 의존성 설치:
   ```
   pip install -r requirements.txt
   ```
2. 데이터 인제스천:
   ```
   python ingestion.py
   ```
3. 백엔드 실행:
   ```
   python main.py
   ```

## 의존성
- Python 3.x
- langchain
- 기타 requirements.txt 참고