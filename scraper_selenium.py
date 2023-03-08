#NECESSARRY INSTANCES 
import math
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree

api_key = '1c69fbf45324109c8dafd910d107af7d'

url = 'https://www.chegg.com/homework-help/questions-and-answers/biology-archive-2023-march-05'
url = f'https://api.scraperapi.com/?api_key={api_key}&url={url}'

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, features="lxml")
html_txt = str(soup)
dom = etree.HTML(html_txt)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# WRITE FUNCTIONS HERE

# Gets element content after giving it XPath
def get_element(xpath):
    return dom.xpath(xpath)[0]

# Gets the total question count from the Chegg specific date archive page
def get_total_question_count():
    return int(get_element('//span[@class="totalItemsNum"]//text()'))

def get_page_question_count():
    try:
        return int(get_element('//span[@class="endNum"]//text()'))
    except:
        print("UNABLE TO RETURN QUESTION COUNT FOR THIS PAGE\n")

def get_page_count():
    try:
        count = float(get_total_question_count())/float(100)
        return math.ceil(count)
    except:
        print("UNABLE TO RETURN QUESTION COUNT FOR THIS PAGE\n")

#Gets a question from chegg specific date archive page using anchor tag 1
# num can be 1 - page question count
def get_question_a1(num):
    try:
        xpath = f'//ul[@class="questions-list"]//li[{num}]//a[1]//text()'
        question = f'{get_element(xpath)}'
        return question
    except:
        return f'Question {num} was not found in anchor tag 1'
    
#Gets a question from chegg specific date archive page using anchor tag 2
# num can be 1 - page question count
def get_question_a2(num):
    try:
        xpath = f'//ul[@class="questions-list"]//li[{num}]//a[2]//text()'
        question = f'{get_element(xpath)}'
        return question
    except:
        return f'Question {num} was not found in anchor tag 2'
    
def get_question_link(num):
    path = get_element(f'//ul[@class="questions-list"]//li[{num}]//a[1]//@href')
    return f'chegg.com{path}'

# Gets chegg archive questions from a single page and puts it into a txt file called Questions.txt
def get_page_questions():
    
    q_count = get_page_question_count() #question count on page
    out = open('Question.txt', 'w')
    for i in range(1, q_count + 1):
        try:
            question_a1 =get_question_a1(i)
            question_a2 =get_question_a2(i)
            
            out.write(f'QUESTION {i}\n{question_a1}\n{question_a2}\n\n')
        except:
            out.write(f'QUESTION {i}\nCould not load question\n\n')
        

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# WRITE CODE HERE

print(get_question_link(7))

