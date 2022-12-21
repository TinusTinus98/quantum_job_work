import web_scrapping as ws
import webdriver_tools as wt
import time
import pandas as pd
import numpy as np

# progress bar - bar de progression
from tqdm import tqdm
from time import sleep


df = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
employer = df["employer"]

driver = ws.Driver()
# driver.driver.get('https://www.google.com/')
# xpath_cookies = """//*[@id="L2AGLb"]"""
# wt.clic(driver.driver,xpath_cookies)
# time.sleep(6)

xpath = """/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component"""
xpath2 = """/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div[2]/div/div[1]"""

# out = [np.nan for _ in range(df.shape[0])]
# df.insert(3,'sector', out )
begin = 1573
for i, emp in tqdm(enumerate(employer[begin:]), desc="charging"):
    if i % 50 == 0:
        driver.close()
        driver = ws.Driver()
        driver.driver.get("https://www.google.com/")
        xpath_cookies = """//*[@id="L2AGLb"]"""
        wt.clic(driver.driver, xpath_cookies)

    q = "What kind of company is " + emp + " ?"
    q = "+".join(q.split())
    url = "https://www.google.com/search?q=" + q + "&ie=utf-8&oe=utf-8"
    driver.driver.get(url)
    # if i==0:
    #     time.sleep(20)
    if wt.check_exists_by_xpath(driver.driver, xpath):
        try:
            text = (
                driver.driver.find_element_by_xpath(xpath)
                .find_element_by_tag_name("b")
                .text
            )
        except:
            text = np.nan
    else:
        text = np.nan
    # else:
    #     url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    #     driver.driver.get(url)
    #     if wt.check_exists_by_xpath(driver.driver,xpath2):
    #         text = wt.get_text(driver.driver,xpath2)
    #         print(text)

    df["sector"].iloc[i + begin] = text

    df.to_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
