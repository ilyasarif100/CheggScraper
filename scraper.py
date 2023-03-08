import requests
from bs4 import BeautifulSoup
from lxml import etree

# insert your ScraperAPI API Key
api_key = '1c69fbf45324109c8dafd910d107af7d'

url = 'https://www.chegg.com/homework-help/questions-and-answers/biology-archive-2023-march-05'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(f'https://api.scraperapi.com/?api_key={api_key}&url={url}', headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

dom = etree.HTML(str(soup))  
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_question(xpath):
    return dom.xpath(xpath)[0]

def extract_string(string, sub1, sub2):
    idx1 = string.index(sub1)
    idx2 = string.index(sub2)
    
    res = ''
    # getting elements in between
    for idx in range(idx1 + len(sub1) + 1, idx2):
        res = res + string[idx]
    return res



print(get_question('//span[@class=\"totalItemsNum\"]//text()'))

# out=open('out.txt','w')
# for i in range(1, 50 + 1):
#     try:
#         xpath = f'//*[@class="questions-list"]//*[{i}]//a[1]//text()'
#         question = f'{i}. {get_question(xpath)}\n\n'
#         out.write(question)
#     except:
#         print(f'Unable to find question {i} in <a>[1]\n')
#     try:
#         xpath = f'//*[@class="questions-list"]//*[{i}]//a[2]//text()'
#         question = f'{i}. {get_question(xpath)}\n\n'
#         out.write(question)
#     except:
#         print(f'Unable to find question {i} in <a>[2]\n')
#         # with open('soup.txt', 'w') as f:
#         #     f.write(get_question(xpath))
    

  


# xpath = '//*[@class="questions-list"]//*[3]//a[1]//text()'
# # print(get_question(xpath))
# with open('soup.txt', 'w') as f:
#     f.write(get_question(xpath))
    


# xpath = '//*[@class="totalItemsNum"]//text()'
# print(dom.xpath(xpath)[0])




# class_name = 'txt-body question-body'
# links = soup.find_all(class_=class_name)
# print(links)

# for link in links:
#     print(link.get('li'))