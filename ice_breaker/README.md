# LinkedIn&Twitter_LangChain_Croll

## 소개
LinkedIn, Twitter 등에서 정보를 수집하여 정보를 제공하는 에이전트 기반 Python 앱입니다.

## 폴더 구조
- `agents/`: 각종 소셜 미디어 에이전트
- `third_parties/`: 외부 API 연동 모듈
- `tools/`: 유틸리티 도구
- `static/`, `templates/`: 프론트엔드 리소스
- `app.py`: 웹 앱 실행 파일
- `LinkedIn&Twitter_LangChain_Croll.py`: 핵심 로직

## 사용법
1. 의존성 설치:
   ```
   pip install -r requirements.txt
   ```
2. API 키 파일(`LinkedIn&Twitter_LangChain_Croll_api_key.txt`) 준비
3. 앱 실행:
   ```
   python app.py
   ```
4. 웹 브라우저에서 `localhost:5000` 접속

## 의존성
- Flask
- requests
- 기타 requirements.txt 참고

## 라이선스
- LICENSE 파일 참고