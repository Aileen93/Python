# ---------------------
# 2019.04.23 (화)
# 한솔제지 관련 데이타 크롤링
# ---------------------
# 크롤링 검색 키워드
# 한솔제지 -주식 -종목
# ---------------------
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
from openpyxl import Workbook
import requests
import pandas as pd
import re


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
< naver 뉴스 검색시 리스트 크롤링하는 프로그램 > _select사용
- 크롤링 해오는 것 : 링크,제목,신문사,날짜,내용요약본
- 날짜,내용요약본  -> 정제 작업 필요
- 리스트 -> 딕셔너리 -> df -> 엑셀로 저장 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 각 크롤링 결과 저장하기 위한 리스트 선언
title_text  = []
link_text   = []
source_text = []
date_text   = []
contents_text   = []
result  = {}

RESULT_PATH = '/Users/atec/Desktop/hansol_crawling/'
now = datetime.now()

# 날짜 정제화 함수
def date_cleansing(test):
    try:
        pattern = '\d+.(\d+).(\d+).'
        r = re.compile(pattern)
        match = r.search(test).group(0)
        date_text.append(match)

    except AttributeError:
        pattern = '\w* (\d\w*)'
        r = re.compile(pattern)
        match = r.search(test).group(1)
        date_text.append(match)

# 내용 정제화 함수
def contents_cleansing(contents):
    first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '', str(contents)).strip()  # 앞에 필요없는 부분 제거
    second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '', first_cleansing_contents).strip()  # 뒤에 필요없는 부분 제거 (새끼 기사)
    third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
    contents_text.append(third_cleansing_contents)

# 크롤링
def crawler(maxpage, query, sort, s_date, e_date):
    s_from = s_date.replace(".", "")
    e_to = e_date.replace(".", "")
    page = 1
    maxpage_t = (int(maxpage) - 1) * 10 + 1  # 11= 2페이지 21=3페이지 31=4페이지  ...81=9페이지 , 91=10페이지, 101=11페이지

    print("=========== crawler start ===========")
    while page <= maxpage_t:

        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=" + str(sort) + "&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # 신문사 추출
        source_lists = soup.select('._sp_each_source')
        for source_list in source_lists:

            # 일간지(매일일보, 경향신문, 조선일보),경제IT(매일경제,블로터, 한국금융신문,한국경제, 해럴드경제)
            print(source_list.text)
            if(source_list.text == '매일일보'
                or source_list.text == '경향신문'
                or source_list.text == '매일경제'
                or source_list.text == '블로터'
                or source_list.text == '한국금융신문'
                or source_list.text == '한국경제'
                or source_list.text == '헤럴드경제'):

                source_text.append(source_list.text)  # 신문사

                # <a>태그에서 제목과 링크주소 추출
                atags = soup.select('._sp_each_title')
                for atag in atags:
                    title_text.append(atag.text)  # 제목
                    link_text.append(atag['href'])  # 링크주소
                    print(atag.text)

                # 날짜 추출
                date_lists = soup.select('.txt_inline')
                for date_list in date_lists:
                    test = date_list.text
                    date_cleansing(test)  # 날짜 정제 함수사용

                # 본문요약본
                contents_lists = soup.select('ul.type01 dl')
                for contents_list in contents_lists:
                    contents_cleansing(contents_list)  # 본문요약 정제화

                # 모든 리스트 딕셔너리형태로 저장
                result = {"source": source_text, "title": title_text, "contents": contents_text, "link": link_text}
                df = pd.DataFrame(result)  # df로 변환
                page += 10

        # 새로 만들 파일이름 지정
        outputFileName = "hansol_crawling_org.xlsx"
        df.to_excel(RESULT_PATH + outputFileName, sheet_name='sheet1')
        print("크롤링 완료")


def main():
    maxpage = 20 #input("최대 크롤링할 페이지 수 입력하시오: ")
    query = '한솔제지 -주식 -종목 -배당 -보통주'
    sort = '1' # 관련도순=0  최신순=1  오래된순=2
    s_date = "2018.01.01"
    e_date = "2018.01.31"

    crawler(maxpage, query, sort, s_date, e_date)

# 함수실행
main()