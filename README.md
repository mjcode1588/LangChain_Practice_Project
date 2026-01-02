# LangChain Application 모음

이 저장소는 LangChain을 활용한 다양한 LLM 애플리케이션 실습 및 예제 코드를 포함하고 있습니다. 에이전트(Agent), RAG(Retrieval-Augmented Generation), 벡터 데이터베이스 등 LangChain의 핵심 기능들을 구현한 프로젝트들로 구성되어 있습니다.

## 프로젝트 구성

### 1. Ice Breaker (ice_breaker)
이름만으로 인물의 LinkedIn과 Twitter 정보를 검색 및 수집하여 요약 정보를 제공하는 웹 애플리케이션입니다. "아이스 브레이킹"을 위한 대화 소재를 찾아줍니다.
- **기술 스택**: Flask, LangChain, OpenAI GPT / Ollama, Tavily API
- **주요 기능**:
  - 이름으로 소셜 미디어 프로필 URL 자동 탐색 에이전트
  - 프로필 데이터 스크래핑 (Mock 데이터 지원)
  - 인물 요약 및 흥미로운 사실 생성

### 2. Code Interpreter (code_interprinter)
사용자의 자연어 질문을 이해하고 Python 코드를 직접 작성하여 실행하거나, CSV 데이터를 분석하는 똑똑한 에이전트입니다.
- **기술 스택**: LangChain ReAct Agent, PythonREPLTool, Pandas DataFrame Agent
- **주요 기능**:
  - 복잡한 계산 문제 Python 코드로 해결
  - CSV 파일(episode_info.csv) 분석 및 질의응답
  - QR 코드 생성 등 유틸리티 작업 수행

### 3. Documentation Helper (documentation-helper)
특정 문서나 강의 내용을 기반으로 답변해주는 RAG 기반의 챗봇 서비스입니다.
- **기술 스택**: Streamlit (UI), Pinecone (Vector DB), OpenAI Embeddings
- **주요 기능**:
  - LangChain 문서/강의 내용 벡터화 및 저장
  - 대화형 문답 인터페이스
  - 답변의 출처(Source) 제공

### 4. React LangChain (react_langchain)
LangChain의 핵심인 **ReAct(Reasoning + Acting)** 패턴을 라이브러리에 의존하지 않고 개념적으로 직접 구현해보며 학습하는 프로젝트입니다.
- **주요 내용**:
  - ReAct 프롬프트 엔지니어링
  - 독자적인 Agent Loop 구현

### 5. Vector Store 예제
RAG 구현을 위한 벡터 데이터베이스 활용 예제들입니다.
- **vector_store_in_memory**: **FAISS**를 사용하여 로컬 메모리 기반의 검색 시스템을 구현.
- **intro-to-vector-dbs**: **Pinecone**을 사용하여 클라우드 기반 벡터 데이터베이스에 데이터를 업로드(Ingestion)하고 검색(Retrieval)하는 과정 실습.

## 시작하기

각 프로젝트 폴더로 이동하여 개별 설정(환경 변수 등)을 확인하세요. 공통적으로 .env 파일에 API Key 설정이 필요합니다.

```bash
# 예시: 의존성 설치
pip install -r requirements.txt
# 또는
pipenv install
```
