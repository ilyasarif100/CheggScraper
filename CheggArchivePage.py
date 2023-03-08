import math
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree


class CheggArchivePage:
    def __init__(self, api_key, url):
        self.api_key = api_key #ScraperAPI Key Required
        self.url = f'https://api.scraperapi.com/?api_key={self.api_key}&url={url}'

        #this will allow chrome to run in the background. no pop up       
        self.options = Options()
        self.options.add_argument('--headless')

        #Chrome webdriver to retrieve page source from Chegg Link
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.url)

        self.html = self.driver.page_source #grabs webpage source

        self.soup = BeautifulSoup(self.html, features="lxml") #use webpage source and format into lxml
        self.html_txt = str(self.soup) #converted webpage source to use in etree attribute
        self.dom = etree.HTML(self.html_txt) #this etree attribue allows a user to search through an html text using XPaths
    
    # Returns element content after giving it XPath
    #Helper Method
    def get_element(self, xpath):
        return self.dom.xpath(xpath)[0]

    # Returns the total question count from the Chegg approximate date archive page
    def get_total_question_count(self):
        return int(self.get_element('//span[@class="totalItemsNum"]//text()'))

    # Returns the question count on one page from the Chegg approximate date archive page
    def get_page_question_count(self):
        try:
            return int(self.get_element('//span[@class="endNum"]//text()'))
        except:
            print('UNABLE TO RETURN QUESTION COUNT FOR THIS PAGE\n')
    #Returns the page count of the Chegg approximate date archive page
    def get_page_count(self):
        try:
            count = float(self.get_total_question_count())/float(100)
            return math.ceil(count)
        except:
            print("UNABLE TO RETURN QUESTION COUNT FOR THIS PAGE\n")

    #Returns a question from Chegg approximate date archive page using anchor tag 1
    # num can be 1 - page question count (max 100)
    #get_question_a1(33) will return the 33rd question from the table of questions on the page
    def get_question_a1(self, num):
        try:
            xpath = f'//ul[@class="questions-list"]//li[{num}]//a[1]//text()'
            question = f'{self.get_element(xpath)}'
            return question
        except:
            return f'Question {num} was not found in anchor tag 1'
        
    #Returns a question from Chegg approximate date archive page using anchor tag 2
    # num can be 1 - page question count (max 100)
    #get_question_a2(33) will return the 33rd question from the table of questions on the page
    def get_question_a2(self, num):
        try:
            xpath = f'//ul[@class="questions-list"]//li[{num}]//a[2]//text()'
            question = f'{self.get_element(xpath)}'
            return question
        except:
            return f'Question {num} was not found in anchor tag 2'
        
    #Returns a link from a specific question on the chegg approximate date archive page    
    def get_question_link(self, num):
        path = self.get_element(f'//ul[@class="questions-list"]//li[{num}]//a[1]//@href')
        return f'chegg.com{path}'

    # Returns Chegg archive questions from a single page and puts it into a txt file called Questions.txt
    def get_page_questions(self):
        
        q_count = self.get_page_question_count() #question count on page
        out = open('Question.txt', 'w')
        for i in range(1, q_count + 1):
            try:
                question_a1 =self.get_question_a1(i)
                question_a2 =self.get_question_a2(i)
                
                out.write(f'QUESTION {i}\n{question_a1}\n{question_a2}\n\n')
            except:
                out.write(f'QUESTION {i}\nCould not load question\n\n')