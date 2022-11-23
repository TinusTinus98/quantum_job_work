from datetime import date

import pandas as pd
from attr import s
from selenium import webdriver
from tqdm import tqdm
import time

# from selenium.common.exceptions import NoSuchElementException

# from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
import numpy as np
import plot_tools as pt
import refs
import webdriver_tools as wt

import matplotlib.pyplot as plt

PATH = "data/consortium/"


class Driver:
    def __init__(self):
        options = Options()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        self.driver = webdriver.Firefox(
            executable_path="out/geckodriver.exe", options=options
        )

    def close(self):
        self.driver.close()


def webscrap_scholarshipdb(name_file:str, path_folder:str,url:str,max_iter:int=1000):
    """webscrap "title" "country" and "employer" categories of a page from scholarshipdb
    you have to give the link which you removed the number of the page

    Args:
        name_file (str): name of the file where the data will be stored
        path_folder (str): path of the folder to store the data
    """
    driver = Driver()
    # next_path = """//*[@id="main"]/div[2]/div[2]/div[2]/div[4]/div[2]/ul/li[6]/a"""
    out=[]
    for i in range(1,max_iter):
        url_ = url + str(i)
        driver.driver.get(url_)
        out = wt.extract_table(driver.driver,refs.scholarshipdb[0],out)
        # wt.clic(driver.driver,next_path,y_gap=0)
        df = pd.DataFrame(out)
        df=df[df['title'].notna()]
        df.to_csv(path_folder + name_file + ".csv")
    driver.close()

def webscrap_quantumconsortium(name_file, path_folder):
    driver = Driver()
    url = "https://quantumconsortium.org/quantum-jobs/"
    driver.driver.get(url)
    wt.clic(driver.driver, "/html/body/div[2]/div/div[6]/button[1]")
    xpath_0 = (
        "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/label/select"
    )
    wt.change_option(driver.driver, xpath_0, "100")
    out = []
    for _ in range(7):
        out = wt.extract_table(driver.driver, refs.classic[0]["columns_xpath"], out)
        wt.clic(driver.driver, """//*[@id="tablepress-1_next"]""", y_gap=0)
    df = pd.DataFrame(out)
    df.to_csv(path_folder + name_file + ".csv")
    driver.close()


def webscrap_real_links(name_file_in, name_file_out, path_folder=PATH):
    driver = Driver()
    df = pd.read_csv(path_folder + name_file_in + ".csv")
    links = df["link"]
    out = []
    for i, link in enumerate(links):
        link_c = ""
        dico = {}
        for col in list(df.columns[7:8]):
            dico[col] = df[col].iloc[i]
        try:
            driver.driver.get(link)
            link_c = driver.driver.current_url
        except Exception:
            pass
        dico["real_link"] = link_c
        dico["date"] = date.today().strftime(f"%d/%m/%Y")
        out.append(dico)
        if i // 10 / 1 == i / 10:
            df2 = pd.DataFrame(out)
            df2.to_csv(path_folder + name_file_out + ".csv")
            print(df2.head())
    df2 = pd.DataFrame(out)
    df2.to_csv(path_folder + name_file_out + ".csv")
    driver.close()


def webscrap_pages(df, name_file_out, col_link="link", path_folder=PATH):
    driver = Driver()
    # df = pd.read_csv(path_folder + name_file_in + ".csv")
    links = df[col_link]
    out = []
    for i, link in tqdm(enumerate(links), desc="extraction : "):
        key = ""
        url_p = ""
        try:
            driver.driver.get(link)
            url_p = driver.driver.current_url
            key = url_p.split("/")[2]
            ref = refs.page_by_page[key]
        except Exception:
            pass
        dico = {}

        for col in list(df.columns[1:]):
            dico[col] = df[col].iloc[i]
        dico["key"] = key
        dico["real_link"] = url_p
        dico = wt.add_several_elements(driver.driver, ref, dico)
        try:
            dico = wt.add_several_elements(driver.driver, ref, dico)
        except Exception:
            pass
        out.append(dico)
        df2 = pd.DataFrame(out)
        df2.to_csv(path_folder + name_file_out + ".csv")
    driver.close()


def sort_result(name_file, path_folder=PATH):
    df = pd.read_csv(path_folder + name_file + ".csv")
    print("nb begining : ", len(df["description"]))
    res = []
    res_empty = []
    for i, description in enumerate(df["description"]):
        dico = {}
        for col in list(df.columns[1:]):
            dico[col] = df[col].iloc[i]
        if len(str(description)) > 10:
            res.append(dico)
        else:
            res_empty.append(dico)
    print("nb completed : ", len(res))
    print("nb wrong : ", len(res_empty))
    pd.DataFrame(res).to_csv(path_folder + name_file + "_ok.csv")
    pd.DataFrame(res_empty).to_csv(path_folder + name_file + "_not.csv")

    out_ok = pt.set_quantity(res, "key")
    out_not = pt.set_quantity(res_empty, "key")
    out = []
    for i, key in enumerate(out_not["key"]):
        same = False
        for key_ok in out_ok["key"]:
            if key_ok == key:
                same = True
        if not same:
            out.append({"key": key, "quantity": out_not["quantity"].iloc[i]})
    out = pd.DataFrame(out)
    out.to_csv(path_folder + name_file + "_error_by_website.csv")
    out_ok.to_csv(path_folder + name_file + "_ok_by_website.csv")
    out_not.to_csv(path_folder + name_file + "_not_by_website.csv")


# df = pd.read_csv("data/scrapped_data/LIX_quantum_201329.csv")


# webscrap_pages(df, "data_201329", col_link="Link")

# df = pd.read_csv("data/consortium/data_201329.csv")
# df = df[df["description"].notna()]
# df.to_csv("data/scrapped_data/LIX_quantum_201329_description.csv")

# url = "https://scholarshipdb.net/phd-quantum-scholarships?listed=Last-30-days&page="
# webscrap_scholarshipdb("phd_quantum_last_30","data/scholarshipdb/",url,max_iter=41)

df = pd.read_csv("data/scholarshipdb/quantum_last_30.csv")
df=df[df['title'].notna()]
df.to_csv("data/scholarshipdb/quantum_last_30.csv")
print(df)