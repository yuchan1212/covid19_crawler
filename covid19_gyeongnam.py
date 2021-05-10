# URL : http://xn--19-q81ii1knc140d892b.kr/main/main.do

from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib

# 경남 시/군별 확진자 수치가 정리된 표를 크롤링
html = urlopen('http://xn--19-q81ii1knc140d892b.kr/main/main.do')
soup = BeautifulSoup(html, 'lxml')
confirmed_table = soup.find_all('div', {'class':'table type1 pt10'})

print(len(confirmed_table))
print(type(confirmed_table))
print(type(confirmed_table[0]))

# x축 데이터 추출
gyeongnam_thead = confirmed_table[0].find_all('thead')
gyeongnam_thead_row = gyeongnam_thead[0].find_all('tr')

gyeongnam_list = []
for tr in gyeongnam_thead_row:
    th = tr.find_all('th')
    for content in th:
        if content.get_text() != '지역':
            print(content.get_text(), end = ', ')
            gyeongnam_list.append(content.get_text())

gyeongnam_list.remove(gyeongnam_list[0])    # 지역 합계 부분 제외

print('')

# y축 데이터 추출
confirmed_table_tbody = confirmed_table[0].find_all('tbody')
confirmed_table_tbody_row = confirmed_table_tbody[0].find_all('tr')

confirmed_list = []
for tr in confirmed_table_tbody_row:
    confirmed_num = []
    td = tr.find_all('td')
    for content in td:
        if content.get_text() != '총계' and content.get_text() != '금일':
            print(content.get_text(), end = ', ')
            confirmed_num.append(int(content.get_text()))
    print('')
    confirmed_list.append(confirmed_num)

confirmed_list[0].remove(confirmed_list[0][0])    # 지역 합계의 총계 부분 제외
confirmed_list[1].remove(confirmed_list[1][0])    # 지역 합계의 금일 부분 제외

print('')

confirmed_total_list = confirmed_list[0]    # 시/군별 확진자 수 총계
confirmed_today_list = confirmed_list[1]    # 금일 시/군별 확진자 수
print(gyeongnam_list)
print(confirmed_total_list)
print(confirmed_today_list)

# 그래프 그리기
matplotlib.rcParams["font.size"]=13
plt.rc('font', family='Malgun Gothic')

x = range(len(gyeongnam_list))

fig, ax1 = plt.subplots()
ax1.set_title('경상남도 지역별 확진자 수')
ax1.bar(x, confirmed_total_list, label='총계', color="red", width=-0.4, align='edge')
ax1.set_ylim(0, 1300)
ax1.set_ylabel('총계')
ax1.legend(loc=2)

ax1.set_xticks(x)
ax1.set_xticklabels(gyeongnam_list)

plt.show()