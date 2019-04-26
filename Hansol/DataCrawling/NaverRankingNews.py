# ---------------------
# 2019.04.26 (금)
# 한솔제지 관련 데이타 크롤링
#https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20190424
# ---------------------
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import calendar
import pandas as pd
import re


# 각 크롤링 결과 저장하기 위한 리스트 선언
contents_text = []
RESULT_PATH = '/Users/atec/Desktop/hansol_crawling/'
RESULT_FILE_NAME = 'ranking_news_title'
now = datetime.now()

def main():
    dataCount = 0
    searchDate = 0
    file = open(RESULT_PATH + RESULT_FILE_NAME, 'w')

    for mon in range(1, 13):
        strMon = ""
        strDay = ""
        if (len(str(mon)) == 1):
            strMon = "0" + str(mon)
        else:
            strMon = str(mon)

        endDay = calendar.monthrange(2018, mon)[1]
        print("------------------------------------------")
        print(strMon + "월의 마지막 날: " + str(endDay))
        print("------------------------------------------")
        for day in range(1, endDay + 1):
            if (len(str(day)) == 1):
                strDay = "0" + str(day)
            else:
                strDay = str(day)

            searchDate = "2018" + strMon + strDay
            url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=" + str(searchDate)

            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')  # print(soup)

            # title.get('속성이름'), title['속성이름'] : https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
            data = soup.select("div[class=ranking_thumb] > a")

            for data_list in data:
                # newTitleList.append(data_list.get("title"))
                print(data_list.get("title"))
                file.write(data_list.get("title") + "\n")
                dataCount += 1
    file.close()

    print("\n--------------------- 생활/문화 카테고리 뉴스 크롤링 완료 ---------------------")
    print("크롤링된 제목 수 : "+ str(dataCount))
    print("----------------------------------------------------------------------")

# 함수실행
main()
