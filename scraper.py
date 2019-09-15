import time
import requests
from bs4 import BeautifulSoup as bs
import smtplib


url='https://www.amazon.in/Apple-iPhone-XR-128GB-Black/dp/B07JG7DS1T/ref=sr_1_5?crid=2KRO2LJGOYOQN&keywords=iphone%2Bxr%2B64%2Bgb&qid=1568499539&sprefix=iphone%2Caps%2C294&sr=8-5&th=1'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():
    page=requests.get(url,headers=headers)

    soup=bs(page.content, 'html.parser')

    title=soup.find(id='productTitle').get_text()

    original_price=soup.find(id='priceblock_ourprice').get_text()
    converted_price=original_price[2:8]
    p=converted_price.split(',')
    price=float(p[0]+p[1])

    if(price<60000.0):
        send_mail()


    print(price)
    print(title.strip())

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vsundar111@gmail.com','joggvkwmknycofzt')

    subject='Hey the price fell down'
    body='check the amazon link https://www.amazon.in/Apple-iPhone-XR-128GB-Black/dp/B07JG7DS1T/ref=sr_1_5?crid=2KRO2LJGOYOQN&keywords=iphone%2Bxr%2B64%2Bgb&qid=1568499539&sprefix=iphone%2Caps%2C294&sr=8-5&th=1'

    msg=f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'vsundar111@gmail.com',
        'vsundar111@gmail.com',
        msg)

    print('Hey the Email has been sent!!!!')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)