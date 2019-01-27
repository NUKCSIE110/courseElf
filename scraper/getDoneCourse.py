# 修過的課
import bs4
import requests
import json
doneCourse = []
req = requests.Session()
# if you wanna test this code, please input your account and password
req.post('https://aca.nuk.edu.tw/Student2/Menu1.asp',{'Account':'','Password':''})
# Classno is your student ID
r = req.post('https://aca.nuk.edu.tw/Student2/SO/ScoreQuery.asp',data={'Classno':''})
r.encoding = 'big5'
soup = bs4.BeautifulSoup(r.text,'html.parser')
soup = soup.select('table[border="1"] tr[align="center"] td')
for i in range(int(len(soup)/7)):
    doneCourse.append([soup[i*7].text,soup[i*7+1].text,soup[i*7+2].text,soup[i*7+5].text])
for r in doneCourse:
    print(r)
# with open('test.html','w',encoding='big5') as web:
#     web.write(r.text)