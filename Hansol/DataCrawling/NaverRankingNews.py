# ---------------------
# 2019.04.26 (금)
# 한솔제지 관련 데이타 크롤링
#https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20190424
# ---------------------
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
from openpyxl import Workbook
import requests
import pandas as pd
import re


# 각 크롤링 결과 저장하기 위한 리스트 선언
contents_text = []
RESULT_PATH = '/Users/atec/Desktop/hansol_crawling/'
RESULT_FILE_NAME = 'ranking_news_title'
now = datetime.now()

# 내용 정제화 함수
def contents_cleansing(contents):
   first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '', str(contents)).strip()  # 앞에 필요없는 부분 제거
   second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '', first_cleansing_contents).strip()  # 뒤에 필요없는 부분 제거 (새끼 기사)
   third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
   contents_text.append(third_cleansing_contents)

# 크롤링
def crawler(s_date, e_date):
    s_from = s_date.replace(".", "")
    e_to = e_date.replace(".", "")
    page = 1
    dataCount = 0

    url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20190424"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') # print(soup)
    data = soup.select("div[class=ranking_thumb] > a")
    #data = soup.select("div[id=ranking_103] > ul > li > a")
    # print(" -----------------S RawData S -----------------")
    # print(data)
    # print(" -----------------E RawData E -----------------\n\n\n\n")

    # title.get('속성이름'), title['속성이름'] : https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
    newTitleList = []
    file = open(RESULT_PATH+RESULT_FILE_NAME, 'w')
    for data_list in data:
        # newTitleList.append(data_list.get("title"))
        print(data_list.get("title"))
        file.write(data_list.get("title")+"\n")
        dataCount += 1

    file.close()

    print("\n--------------------- 생활/문화 카테고리 뉴스 크롤링 완료 ---------------------")
    print("크롤링 날짜 : "+s_date+" ~ "+e_date)
    print("크롤링된 제목 수 : "+ str(dataCount))
    print("하루에 30개 * 30일 = 900개 * 12개월 = 10,800개")
    print("----------------------------------------------------------------------")

def main():
    sort = '1' # 관련도순=0  최신순=1  오래된순=2
    s_date = "2018.01.01"
    e_date = "2019.01.31"
    crawler(s_date, e_date)

# 함수실행
main()
