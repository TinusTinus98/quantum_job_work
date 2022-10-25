import time

import pandas as pd
from attr import s
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
import numpy as np
import plot_tools as pt
import refs
import webdriver_tools as wt
import matplotlib.pyplot as plt

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(executable_path="out/geckodriver.exe", options=options)


def webscrap_quantumconsortium():
    url = "https://quantumconsortium.org/quantum-jobs/"
    driver.get(url)
    time.sleep(10)
    # wt.clic(driver, """/html/body/div[2]/div/div[6]/button[1]""")
    # wt.clic(driver, """//*[@id="tablepress-1_length"]/label/select/option[5]""")
    # time.sleep(5)
    out = []
    for _ in range(7):
        out = wt.extract_table(driver, refs.classic[0]["columns_xpath"], out)
        wt.clic(driver, """//*[@id="tablepress-1_next"]""", y_gap=0)
    df = pd.DataFrame(out)
    df.to_csv("data/consortium/data.csv")


def webscrap_real_links():
    df = pd.read_csv("data/consortium/metadata.csv")
    links = df["link"]
    out = []
    for i, link in enumerate(links):
        driver.get(link)
        # ref = refs.indeed[0]["columns_xpath"]
        dico = {}
        for col in list(df.columns[1:]):
            dico[col] = df[col].iloc[i]
        # dico = wt.add_several_elements(driver, ref, dico)
        dico["real_link"] = driver.current_url
        out.append(dico)
        if i // 10 / 1 == i / 10:
            df2 = pd.DataFrame(out)
            df2.to_csv("data/consortium/matadata_2.csv")
            print(df2.head())
    df2 = pd.DataFrame(out)
    df2.to_csv("data/consortium/metadata_2.csv")


def webscrap_pages():
    df = pd.read_csv("data/consortium/metadata_2.csv")
    links = df["real_link"]
    out = []
    for i, link in enumerate(links):
        time.sleep(3)
        driver.get(link)
        key = link.split("/")[2]
        ref = refs.page_by_page[key]
        dico = {}
        for col in list(df.columns[1:]):
            dico[col] = df[col].iloc[i]
        dico = wt.add_several_elements(driver, ref, dico)
        dico["key"] = key
        dico["real_link"] = driver.current_url
        out.append(dico)
        if i // 10 / 1 == i / 10:
            df2 = pd.DataFrame(out)
            df2.to_csv("data/consortium/metadata_3.csv")
            print(df2.head())
    df2 = pd.DataFrame(out)
    df2.to_csv("data/consortium/metadata_3.csv")


df = pd.read_csv("data/consortium/metadata_2.csv")
r = [x.split("/")[2] for x in df["real_link"]]

webscrap_pages()
driver.close()
