#! /usr/bin/env python
'''
	Libary essential to automate a website transactions

	AUTHOR	: Vignesh Natarajan (www.vikiworks.io)

'''

from selenium import webdriver
import time
import inspect

class browser:

    driver = None
    current_element = None
    elements_list = []
    retry_attempts = 0
    retry_delay = 0

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.retry_attempts = 10
        self.retry_delay = 1 #1 seconds

    def close(self):
        self.driver.quit()

    def open_url(self, url):
        success = None
        for i in range(0, self.retry_attempts):
            try:
                print "Try open"
                self.driver.get(url)
                success = True
                break
            except:
                time.sleep(self.retry_delay)
                success = False

        if not success:
            print "ERROR : ", self.lineno()

    def str_element_attr(self, element):
        try:
            return element.get_attribute('outerHTML')
        except:
            return ""

    def str_element_text(self, element):
        try:
            return element.text
        except:
            return ""

    def find_buttons(self, pattern):
        print "searching buttons"
        del self.elements_list[:]
        result_list = []
        try:
            self.elements_list = self.driver.find_elements_by_tag_name("input")
            if not pattern:
                return self.elements_list

            i = 0
            for element in self.elements_list:
                if pattern in self.str_element_attr(element):
                    print "\tpatter exist in tag attributes", i
                    result_list.append(element)
                if pattern in self.str_element_text(element):
                    print "\tpatter exist in tag text", i
                    result_list.append(element)
                i = i + 1
        except:
            print "ERROR : ", self.lineno()

        return result_list

    def find_check_boxes(self):
        self.driver.find_element_by_xpath("")

    def find_search_boxes(self, pattern):
        print "searching input boxes"
        del self.elements_list[:]
        result_list = []
        try:
            self.elements_list = self.driver.find_elements_by_tag_name("input")
            if not pattern:
                return self.elements_list

            i = 0
            for element in self.elements_list:
                if pattern in self.str_element_attr(element):
                    print "patter exist in tag attributes", i
                    result_list.append(element)
                if pattern in self.str_element_text(element):
                    print "patter exist in tag text", i
                    result_list.append(element)
                i = i + 1
        except:
            print "ERROR : ", self.lineno()

        return result_list

    def find_radio_buttons(self):
        self.driver.find_element_by_xpath("")

    def click(self, element):
        element.click()

    def clear(self, element):
        element.clear()

    def send_text(self, element, text):
        element.send_keys(text)

    def lineno(self):
        return inspect.currentframe().f_back.f_lineno

    def print_elements_list(self):
        i = 0
        for element in self.elements_list:
            print "Tag Attributes TagList [", i, "]: ", self.str_element_attr(element)
            i+=1

        i = 0
        for element in self.elements_list:
            print "Tag Text TagList [", i, "]: ", self.str_element_text(element)
            i += 1

    def print_current_element(self):
        print "Current Tag Attributes   : ", self.str_element_attr(self.current_element)
        print "Current Tag Text         : ", self.str_element_text(self.current_element)


web_site = browser()
web_site.open_url("https://ebay.de/")
time.sleep(10) # Wait for the page to load completely
res_list = ebay.find_search_boxes("Nach irgendetwas suchen")

if len(res_list) > 1:
    print "WARN: two elements with the same pattern"
else:
    if res_list:
        web_site.click(res_list[0])

web_site.clear(res_list[0])
web_site.send_text(res_list[0], "ganesha")

res_list = web_site.find_buttons("Finden")

if len(res_list) > 1:
    print "WARN: two elements with the same pattern"
else:
    if res_list:
        web_site.click(res_list[0])





