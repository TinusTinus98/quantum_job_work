import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import web_scrapping as ws
import webdriver_tools as wt
import time
from tqdm import tqdm

def search(queries:list):
    url_log_in = """https://www.linkedin.com/login"""
    payload = {
    'username': 'martin.lecaille@hotmail.com',
    'password': 'MaLe8478@@.Linkedin'
    }     
    url = '''https://www.linkedin.com/search/results/companies/?keywords=quantum%20brilliance&origin=GLOBAL_SEARCH_HEADER&sid=3oM'''

    # with requests.Session() as sess:
    #     res = sess.get(url_log_in)
    #     res = sess.post(url_log_in, data=payload)
    #     res_0 = sess.get(url)
    #     soup = BeautifulSoup(res_0.content, "html.parser")
    #     print(soup)

    driver = ws.Driver()
    driver.driver.get(url_log_in)
    username = driver.driver.find_element_by_xpath('//*[@id="username"]')
    username.send_keys(payload['username'])
    password = driver.driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(payload['password'])
    wt.clic(driver.driver,"""/html/body/div/main/div[3]/div[1]/form/div[3]/button""")

    # _ = input('Press entry when you are logged')
    url_0 = """https://www.linkedin.com/search/results/companies/?keywords="""
    url_1="""&origin=GLOBAL_SEARCH_HEADER&sid=3oM"""
    dic = {"query":[],"url":[],"title":[],"linkedin_industry_domain":[],"linkedin_description":[],"linkedin_location":[]}
    for _,query in tqdm(enumerate(queries)):
        dic["query"].append(query)
        url = url_0 + query + url_1
        driver.driver.get(url)
        # page_source = sess.get(url)
        page_source = driver.driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        class_0="""reusable-search__result-container"""
        categories = soup.find_all("li", class_=class_0)
        urls = []
        for line in categories:
            cat = line.find_all('a',href=True)
            urls.append(cat[0]['href'])
        first_url = urls[0]
        dic["url"].append(first_url)
        driver.driver.get(first_url)
        page_source = driver.driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        class_industry = """org-top-card-summary__tagline t-16 t-black"""
        dic["title"].append(wt.get_text(driver.driver,"""/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/h1"""))
        dic["linkedin_industry_domain"].append(wt.get_text(driver.driver,"""/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]"""))
        dic["linkedin_description"].append(wt.get_text(driver.driver,"/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/p"))
        dic["linkedin_location"].append(wt.get_text(driver.driver,"""/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div"""))
        df = pd.DataFrame.from_dict(dic)
        df.to_csv("data/linkedin/data.csv")

print(search(["quantum brillance"]))