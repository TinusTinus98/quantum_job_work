classic = [
    {
        "name": "metadata",
        "button_xpath": """""",
        "columns_xpath": [
            {
                "name": "organization",
                "xpath": f"""//*[@id="tablepress-1"]/tbody/tr[*]/td[1]""",
            },
            {
                "name": "position",
                "xpath": f"""//*[@id="tablepress-1"]/tbody/tr[*]/td[2]""",
            },
            {
                "name": "link",
                "xpath": f"""//*[@id="tablepress-1"]/tbody/tr[*]/td[3]/a""",
            },
            {
                "name": "location",
                "xpath": f"""//*[@id="tablepress-1"]/tbody/tr[*]/td[4]""",
            },
            {
                "name": "date_added",
                "xpath": f"""//*[@id="tablepress-1"]/tbody/tr[*]/td[5]""",
            },
        ],
    },
]

l = [  'careers.google.com'
 'careers.honeywell.com' 'careers.ibm.com' 'ionq.com' 'jobs.boeing.com'
 'jobs.keysight.com' 'jobs.lever.co' 'psiquantum.com'
 'qblox.jobs.personio.de' 'www.glassdoor.com'
  'www.northropgrumman.com'
 'www.qcware.com']

indeed = {
    "www.indeed.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="viewJobSSRRoot"]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]""",
        },
        {
            "name":"location",
            "xpath":f""""""
        },
        {
            "name": "position",
            "xpath": f"""//*[@id="viewJobSSRRoot"]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="jobDetailsSection"]/div[2]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="jobDescriptionText"]""",
        },
        {
            "name":"company",
            "xpath":f""""""
        }
    ],
    "www.amazon.jobs": [
        {
            "name": "title",
            "xpath": f"""//*[@id="job-detail"]/div[1]/div/div/div/div[1]""",
        },
        {
            "name":"location",
            "xpath":f"""//*[@id="job-detail-body"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div"""
        },
        {
            "name":"company",
            "xpath":f"""//*[@id="job-detail-body"]/div/div[2]/div/div[1]/div[2]/div[2]/div/div"""
        },
        {
            "name": "position",
            "xpath": f"""//*[@id="job-detail-body"]/div/div[2]/div/div[1]/div[2]/div[3]/div/div""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job-detail-body"]/div/div[1]/div""",
        },
        ],
    "academicjobsonline.org": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {
            "name":"location",
            "xpath":f""""""
        },
        {
            "name":"company",
            "xpath":f""""""
        },
        {
            "name": "position",
            "xpath": f"""""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""""",
        },
        ],
    "apply.workable.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {
            "name":"location",
            "xpath":f""""""
        },
        {
            "name":"company",
            "xpath":f""""""
        },
        {
            "name": "position",
            "xpath": f"""""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""""",
        },
        ],
    'www.linkedin.com':[
        {
            "name": "title",
            "xpath": f"""//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h1""",
        },
        {
            "name":"location",
            "xpath":f"""//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[2]"""
        },
        {
            "name":"company",
            "xpath":f"""//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[1]"""
        },
        {
            "name": "position",
            "xpath": f"""""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="main-content"]/section[1]/div/div[1]/section[1]/div/ul/li[2]/span""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="main-content"]/section[1]/div/div[1]/section[1]/div/div/section/div""",
        },
        ],
}
