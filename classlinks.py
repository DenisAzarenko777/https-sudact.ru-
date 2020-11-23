from telnetlib import EC
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import json

class GetLinks(object):

    def __init__(self):
        self.urls=[]
        self.next_el = 0

    def main(self,vvod1,first1):
        self.driver=webdriver.Firefox()
        self.driver.get('https://sudact.ru/')

        self.btn_elem = self.driver.find_element_by_id("id_regular_topmenu")
        self.btn_elem.click()

        self.driver.implicitly_wait(100)
        self.inputtext = self.driver.find_element_by_id("id_regular-lawchunkinfo")

        self.inputtext.send_keys(vvod1)

        self.btn_el = self.driver.find_element_by_class_name("newListSelected")
        self.btn_el.click()
        self.driver.implicitly_wait(1000)
        first="Первая инстанция"
        self.instanc = self.driver.find_element_by_partial_link_text(first1).click()
        self.driver.implicitly_wait(1000)

        self.btn_element_two = self.driver.find_element_by_class_name("f-submit")
        self.btn_element_two.click()
        self.driver.implicitly_wait(10)

        while self.next_el < 50:
            self.list = self.driver.find_elements_by_xpath("//ul[@class='results']//li//a")
            for i in self.list:
                a = i.get_attribute('href')
                url = {
                    'href': a
                }
                self.urls.append(url)

            self.btn_next = self.driver.find_element_by_class_name("page-next")
            self.btn_next.click()
            self.next_el = self.next_el + 1
        print(len(self.urls))
        controller = 0

        with open('file.txt', 'w') as fw:

            json.dump(self.urls, fw)

class OpenLinks(object):
    def __init__(self):
        self.array=[]
        self.counter=0

    def main(self):

        with open('file.txt','r') as fr:
            list=json.load(fr)

        self.driver2 = webdriver.Firefox()
        print(len(list))
        try:
            for j in list:
                self.driver2.get(j['href'])
                self.text1 = self.driver2.find_element_by_xpath("//td[@class='h-col1 h-col1-inner3']").text
                self.array.append(self.text1)
                self.counter=self.counter+1
                print("Спарсилось ", self.counter)
                with open ('Статья 105. Убийство(УК РФ).txt', 'w') as fw:
                    json.dump(self.array,fw)

                    MyFile = open('output.txt', 'w')
                    for element in self.array:
                        MyFile.write(element)
                        MyFile.write('\n')
                        MyFile.write('\n')
                        MyFile.write('\n')


        except UnicodeEncodeError:
            self.driver2.refresh()
            self.driver2.quit()

            return self.counter
        MyFile.close()

        self.driver2.refresh()
        self.driver2.quit()

