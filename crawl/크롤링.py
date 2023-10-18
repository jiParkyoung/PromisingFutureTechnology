import requests
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os

def get_url(query,news_num):#네이버 뉴스 검색해서 원하는 갯수 만큼 url 얻어오기
    query = query.replace(' ', '+')
    # date = str(datetime.now())
    # date = date[:date.rfind(':')].replace(' ', '_')
    # date = date.replace(':','시') + '분'

    news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'

    req = requests.get(news_url.format(query))
    soup = BeautifulSoup(req.text, 'html.parser')


    news_dict = {}
    idx = 0
    cur_page = 1
    
    while idx < news_num:
    ### 네이버 뉴스 웹페이지 구성이 바뀌어 태그명, class 속성 값 등을 수정함(20210126) ###
        
        table = soup.find('ul',{'class' : 'list_news'})
        li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
        area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]
        a_list = [area.find('a', {'class' : 'news_tit'}) for area in area_list]
        
        for n in a_list[:min(len(a_list), news_num-idx)]:
            
            news_dict[idx] = {'title' : n.get('title'),
                            'url' : n.get('href') }
            idx += 1

        cur_page += 1

        pages = soup.find('div', {'class' : 'sc_page_inner'})
        next_page_url = [p for p in pages.find_all('a') if p.text == str(cur_page)][0].get('href')
        
        req = requests.get('https://search.naver.com/search.naver' + next_page_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
    url=[]
    for i in news_dict:
        url.append(news_dict[i]['url'])
    
    return url

def _news_crawling(url):#크롤링
    
        def _clean_text(text):#전처리
            text = re.sub('[a-zA-Z]', "", text)#한글만
            text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>◀◁▷▶■♥⑤◆※@\#$%&\\\=\(\"\"(\n)(\t)]', "", text)
            text = text.replace("오류를 우회하기 위한 함수 추가", "")
            text = text.replace("사진연합뉴스", "")
            text = text.replace("무단 전재 및 재배포 금지", "")
            text = text.replace("동영상 뉴스", "")
            cleaned_text = text.replace("앵커", "")

            return cleaned_text
    
        headers = {"User-Agent": "Mozilla/5.0"}

        html = requests.get(url, headers=headers,allow_redirects=False)
        soup = BeautifulSoup(html.text, 'html.parser')
        

        #############
        # 이 부분이 언론사별, 기자별 조금 씩 다름...(태그,id값, 클래스 등 요소가 너무 다양함. 같은 언론사라도 기자별로 다름.)
        try:#크롤링시 오류나면 우선 x,x 리턴하게 해놈...
            title = soup.find(id="articleTitle").get_text().strip()#제목 얻어오기
            all_news = soup.find(id="articleBodyContents").get_text()#뉴스전문 얻어오기
        except:
            return "x","x"   
        ###################
        all_news = _clean_text(all_news).strip()#전처리
        return title,all_news 

        
url_list=get_url("6T 기술",30)#검색어, 갯수

news_list=[]
title_list=[]

for url in url_list:#얻은 url을 하나씩
    title,news = _news_crawling(url)#크롤링
    news_list.append(news)
    title_list.append(title)

print(news_list)
print(title_list)