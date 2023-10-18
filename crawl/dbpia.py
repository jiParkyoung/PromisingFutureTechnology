from selenium import webdriver
from pandas import DataFrame
import time

Delay=2.5#time.sleep(Delay)로 일괄 적용

def Preceding_work(searchQ,startYear,endYear):#셋팅
    global driver
    global xpath

    path = './chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    xpath = driver.find_element_by_xpath

    #검색
    driver.get('https://www.dbpia.co.kr/')
    keyword = driver.find_element_by_id('keyword')
    keyword.clear()
    keyword.send_keys(searchQ)
    time.sleep(Delay)
    serach_click_btn = xpath("//*[@id='bnHead']/div[3]/div/div[1]/div[1]/a")
    driver.execute_script("arguments[0].click();",serach_click_btn)
    time.sleep(Delay)#검색시간오래 걸릴경우 늘려야함.
    
    
    # #날짜 지정
    #발행년도 클릭
    click_btn = xpath("//*[@id='newYear']")
    driver.execute_script("arguments[0].click();",click_btn)
    driver.execute_script("arguments[0].click();",click_btn)#한번만 클릭하면 창이 사라질때가 있음.
    time.sleep(Delay)

    #발행연도 날짜 삽입
    xpath("//*[@id='dev_sartYY']").send_keys(startYear)
    time.sleep(Delay)
    xpath("//*[@id='dev_endYY']").send_keys(endYear)
    time.sleep(Delay)
    click_btn = xpath("//*[@id='newYear2']/p/button/span")
    driver.execute_script("arguments[0].click();",click_btn)#재검색
    time.sleep(Delay)


    #100개씩 보기 설정
    click_btn = xpath("//*[@id='contents']/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]")
    driver.execute_script("arguments[0].click();",click_btn)
    time.sleep(Delay)
    click_btn = xpath("//*[@id='100']")
    driver.execute_script("arguments[0].click();",click_btn)
    time.sleep(Delay)
    

def DBpia_crawling(searchQ,startYear,endYear,number):#검색어,시작연도,끝연도,크롤링 갯수
    Preceding_work(searchQ,startYear,endYear)#사전 셋팅 함수
    
    page=1#페이지 수
    url=[]#url
    title=[]#제목
    year=[]#날짜
    cur_number=0#현재 크롤링수
    
    #url 및 제목 날짜 수집
    while True:
        try:
            if cur_number==number:#현재 크롤링 수가 목표 치라면:
                break
            
            titles = driver.find_elements_by_css_selector(".titWrap")#제목,url
            years=driver.find_elements_by_css_selector(".date")#날짜

            for i in range(len(titles)):
                if cur_number==number:#현재 크롤링 수가 목표 치라면:
                    break
                
                cur_number+=1#현재 크롤링수
                #url 경로 따라가기
                href=titles[i].find_element_by_tag_name('h5')
                href=href.find_element_by_tag_name('a')
                href=href.get_attribute('href')
                
                title.append(titles[i].text)#제목 수집
                url.append(href)#url수집
                year.append(years[i].text)#발행일 수집
                
            else:#한페이지 모두 크롤링 했을 시
                if page<10:#1~10페이지
                    page+=1
                    serach_click_btn = xpath("//*[@id='pcPaging{0}']".format(page))
                    driver.execute_script("arguments[0].click();",serach_click_btn)
                elif page%10==0:#10페이지째, 20페이째....
                    page+=1
                    serach_click_btn = xpath("//*[@id='next']/img")
                    driver.execute_script("arguments[0].click();",serach_click_btn)
                else:#나머지
                    page+=1
                    serach_click_btn = xpath("//*[@id='pcPaging{0}']".format(page))
                    driver.execute_script("arguments[0].click();",serach_click_btn)
            time.sleep(Delay)
            print(page,len(url))
        except:
            break

        
    #url 따라서 초록 수집
    contents=[]
    for i in url:
        driver.get(i)
        content=driver.find_elements_by_css_selector(".abstractWrap.eHideSec1.detail-con1")
        for j in content:
            contents.append(j.text)
    
    return title,url,year,contents


#main
searchQ = "6t"#검색어
startYear = 2020#시작연
endYear = 2021#끝연
number=101#크롤링 수
title,url,year,contents=DBpia_crawling(searchQ,startYear,endYear,number)#

#데이터 프레임 만들기
raw_data = {'title': title,
            'url': url,
            'year': year,
            'contnet':contents}

df=DataFrame(raw_data)
df.to_csv("./{0}.csv".format(searchQ),index=False, encoding="utf-8-sig")#csv로 저장