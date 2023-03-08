import datetime

from CheggArchivePage import CheggArchivePage


# now = datetime.datetime.now()
# print(now)


api_key = '1c69fbf45324109c8dafd910d107af7d'

url = 'https://www.chegg.com/homework-help/questions-and-answers/biology-archive-2023-march-05'
page = CheggArchivePage(api_key,url)

page.get_page_questions()