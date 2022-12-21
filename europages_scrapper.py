import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from time import sleep
 
 

def results_search(query:str)->list:
    """get the url that result from a search on the website www.europages.co.uk

    Args:
        query (str): the query you want to put in the search bar of www.europages.co.uk

    Returns:
        list: a list of url that are the results of the query
    """
    url = "https://www.europages.co.uk/companies/"+query+".html"
    page = requests.get(url)
    class_0="""ep-ecard text-start rounded theme--light text-decoration-none pa-5 ep-ecard-serp mb-3 mb-lg-6 elevation-2"""
    soup = BeautifulSoup(page.content, "html.parser")
    categories = soup.find_all("li", class_=class_0)
    urls = []
    for line in categories:
        if not ad_check(line):
            cat = line.find_all('a',href=True)
            urls.append('https://www.europages.co.uk' + cat[0]['href'])
    return urls

def ad_check(soup:BeautifulSoup)->bool:
    """check if a line of result in a www.europages.co.uk research is an ad or a normal result

    Args:
        soup (BeautifulSoup): a Beautiful soup element containing a line of result of a search on www.europages.co.uk

    Returns:
        bool: True if it's an ad
    """
    try:
        value = soup.find("span","text-decoration-underline").getText()
        return True
    except:
        return False

def scrap_page(url:str)->list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    class_title = """ep-epages-header-title text-h6 text-sm-h4"""
    header = soup.find("header",class_="ep-epages-header")
    title = header.find("h1", class_=class_title).getText().strip()
    try:
        cat = header.find("span",class_="ep-main-activity-name ma-0").getText().strip()
    except:
        cat=None

    core = soup.find("div",class_="ep-page-epage-home__content")
    class_text = "ep-text-with-overflow__text ma-0 mt-2 ep-text-with-overflow__text--ellipsis"
    try:
        text = core.find("p",class_=class_text).getText().strip()
    except:
        text=None
    dict={"title":title,
    "category":cat,
    "text":text}
    return dict


# df = pd.read_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")
# isnan = df["company_class_1"].isna()
# notna=0
# for i in tqdm(range(440,df.shape[0])):
#     sleep(.1)
#     if isnan[i]:
#         employer =df.loc[i,"employer"]
#         results = results_search(employer)
#         if len(results)>0:
#             dict = scrap_page(results[0])
#             if dict["category"]!=None:
#                 df.loc[i,"europages"] = dict["category"]
#             else:
#                 df.loc[i,"europages"] = "category other"
#     df.to_csv("data/quantumapalooza/quantumapalooza_eusnapshot_2.csv")

# query = 'airbus'
# urls = results_search(query)
# print(scrap_page(urls[0]))