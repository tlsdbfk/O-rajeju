# o-rajeju
### 해시태그 기반 제주도 음식점 추천 프로젝트

## Environment

  Python version: 3.8
  

## Dataset
<img width="1362" alt="example" src="https://github.com/tlsdbfk/o-rajeju/assets/68388156/9a528e3d-6870-4366-be17-b4c6954bcfbe">


### Preprocessing
- 발화자와 청자의 감정 Label 중 발화자의 Label만 추출
- 감정 Label이 여러 개일 경우, 1개만 채택
- 한글을 제외한 단어 및 공백 제거
- 인덱스가 일치하는 텍스트 파일(.tsv), 오디오 파일(.npy) 생성

<br/>


## Description
관광 공사, 투어 API를 활용하여 제주도 지역 내 관광지 데이터 크롤링

수집한 데이터 중 음식점의 간단한 소개글을 ChatGPT API 활용하여 해시태그 형태로 변형

메뉴, 주소, 주차 가능 여부 등의 데이터를 전처리를 통해 해시태그 형태로 변형

Streamlit을 사용하여 사용자가 원하는 음식, 풍격 등을 입력하면 유사한 음식점 추천


## Result
<img width="571" alt="result2" src="https://github.com/tlsdbfk/o-rajeju/assets/68388156/de18df22-3ae5-4090-8314-15f0ae07427e">

