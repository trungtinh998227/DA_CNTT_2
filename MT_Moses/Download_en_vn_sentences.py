"""
To get parallel en_vn language we should:
    1. Use english word from english words folder
    2. Each word, add this to the end of baseURL -> get all of example sentences of this page
    3. Add paging to get more example sentences (1->5 page is enough)
"""
from bs4 import BeautifulSoup
import requests

baseURL = "https://glosbe.com/en/vi/"
paging = "?page=+2&tmmode=MUST"  # phân trang


def get_soup(link):
    return BeautifulSoup(requests.get(link).content, 'lxml')
    pass


def craw_data():
    en_words = []
    with open("english_words/english_words.txt", encoding="utf-8") as f:
        en_words = f.read().split()
    f.close()
    # for word in en_words:
    #     link = baseURL + word
    #     get_soup(link)
    all_html = get_soup(baseURL + en_words[0])
    content_box = all_html.find('div', {"id": "tmTable"})
    en_sentence_example = content_box.find_all('div', {"class": "span6", "lang": "en"})
    vn_sentence_example = content_box.find_all('div', {"class": "span6", "lang": "vi"})
    for index in range(len(vn_sentence_example)):
        en_sentence = en_sentence_example[index].find('span').find('span').text
        vn_sentence = vn_sentence_example[index].find('span', class_=None).find('span').text
        print(en_sentence)
        print(vn_sentence)
    pass


if __name__ == '__main__':
    craw_data()
    pass
