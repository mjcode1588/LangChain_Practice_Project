# Code Interprinter

## 소개
QR코드 이미지와 에피소드 정보를 활용하는 Python 스크립트를 포함합니다.

## 주요 파일
- `main.py`: QR코드 이미지와 CSV 파일을 처리하는 메인 스크립트
- `too_call_main.py`: 추가 기능 또는 테스트용 스크립트
- `episode_info.csv`: 에피소드 정보 데이터
- `langchain_qrcode_*.png`: 각 에피소드에 해당하는 QR코드 이미지

## 사용법
1. 필요한 패키지 설치:  
   ```
   pip install -r requirements.txt
   ```
2. `main.py` 실행:  
   ```
   python main.py
   ```

## 의존성
- Python 3.x
- pandas
- 기타 필요시 requirements.txt 참고

## 기타
- QR코드 이미지는 자동 생성됩니다.