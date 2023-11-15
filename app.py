import streamlit as st
import pandas as pd

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt

df = pd.read_csv("음식점_해시태그.csv", sep=",")

keyword1 = st.text_input("제주도 어디로 여행가시나요? ex) 제주시, 서귀포시")
keyword2 = st.text_input("출출한데 밥부터 먹고 시작해요. 먹고 싶은 거 있어요? ex) 회, 흑돼지")
keyword3 = st.text_input("밥 먹으면서 어떤 경치를 즐길까요? ex) 바다, 한라산")
result = []
input_keywords = []

input_keywords.append(keyword1)
input_keywords.append(keyword2)
input_keywords.append(keyword3)

# 형태소 분석기 초기화
okt = Okt()

# 키워드와 텍스트 간의 코사인 유사도 계산
def calculate_similarity(keyword_list, text):
    keyword_text = ' '.join(keyword_list)
    documents = [keyword_text, text]
    tfidf_matrix = okt.tfidf(documents)
    return cosine_similarity(tfidf_matrix)[0][1]

# 텍스트 유사도 계산 후 데이터프레임에 추가
df['Similarity'] = df['해시태그'].apply(lambda x: calculate_similarity(input_keywords, x))

# 유사도에 따라 정렬하여 인덱스 출력
sorted_df = df.sort_values(by='Similarity', ascending=False)

if keyword1 and keyword2 and keyword3:
    for i in range(5):
        result.append(df['명칭'][i])

    if len(result) == 0:
        result.append("결과가 존재하지 않습니다.")

'''
if keyword1 and keyword2 and keyword3:
    for i in range(len(df)):
        if keyword1 in str(df['해시태그'][i]) and keyword2 in str(df['해시태그'][i]) and keyword3 in str(df['해시태그'][i]):
            result.append(df['명칭'][i])
                
    if len(result) == 0:
        result.append("결과가 존재하지 않습니다.")
'''

for r in result:
    st.title(r)