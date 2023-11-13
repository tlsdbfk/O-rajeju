import pandas as pd
import re

df = pd.read_csv("음식점.csv", sep=",")

df = df[['명칭', '주소', '주차 시설', '취급메뉴', '개요']]

df = df.astype(str)

def process_text(text):
    if text != "nan":
        split_text = text.split()
        processed_text = "#" + split_text[1]
    else:
        processed_text = " "
    return processed_text

def process_text2(text):
    if text != "nan":
        replacetext = text.replace(" ", "")
        if "있음" in replacetext or "가능" in replacetext:
            processed_text2 = "#주차가능"
        elif "없음" in replacetext or "불가" in replacetext:
            processed_text2 = "#주차불가능"
        else:
            processed_text2 = "#" + replacetext
    else:
        processed_text2 = " "
    return processed_text2

def process_text3(text):
    if text != "nan":
        replacetext = text.replace(" ", "")
        replacetext2 = replacetext.replace(",", "/")
        split_text = replacetext2.split("/")

        result = "#" + ' #'.join(split_text)
    else:
        result = " "
    return result

df['주소'] = df['주소'].apply(process_text)
df['주차 시설'] = df['주차 시설'].apply(process_text2)
df['취급메뉴'] = df['취급메뉴'].apply(process_text3)

df['해시태그'] = df['주소'].astype(str) + " " + df['주차 시설'].astype(str) + " " + df['취급메뉴'].astype(str)

df = df[['명칭', '해시태그', '개요']]
df.to_csv('음식점_1.csv', encoding='utf-8')