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

page_by_page = {
    "www.indeed.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="viewJobSSRRoot"]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]""",
        },
        {"name": "location", "xpath": f""""""},
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
        {"name": "company", "xpath": f""""""},
    ],
    "www.amazon.jobs": [
        {
            "name": "title",
            "xpath": f"""//*[@id="job-detail"]/div[1]/div/div/div/div[1]""",
        },
        {
            "name": "location",
            "xpath": f"""//*[@id="job-detail-body"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div""",
        },
        {
            "name": "company",
            "xpath": f"""//*[@id="job-detail-body"]/div/div[2]/div/div[1]/div[2]/div[2]/div/div""",
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
            "xpath": f"""/html/body/h2""",
        },
        {"name": "location", "xpath": f"""/html/body/table[1]/tbody/tr[4]/td[2]"""},
        {"name": "company", "xpath": f"""/html/body/table[1]/tbody/tr[1]/td[2]"""},
        {
            "name": "position",
            "xpath": f"""/html/body/table[1]/tbody/tr[2]/td[2]""",
        },
        {
            "name": "type",
            "xpath": f"""/html/body/table[1]/tbody/tr[3]/td[2]""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/table[2]/tbody/tr/td/div/div/div/div/div/div""",
        },
    ],
    "apply.workable.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="8504176561492005"]/div/div/div/div/div[1]/div[2]/h2""",
        },
        {
            "name": "location",
            "xpath": f"""//*[@id="8504176561492005"]/div/div/div/div/div[1]/span/span[1]""",
        },
        {
            "name": "company",
            "xpath": f"""//*[@id="8504176561492005"]/div/div/div/div/div[1]/div[2]/h3""",
        },
        {
            "name": "position",
            "xpath": f"""//*[@id="8504176561492005"]/div/div/div/div/div[1]/div[2]/h2""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="8504176561492005"]/div/div/div/div/div[1]/span/span[3]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="8504176561492005"]/div/div/div/div/div[2]""",
        },
    ],
    "www.linkedin.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h1""",
        },
        {
            "name": "location",
            "xpath": f"""//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[2]""",
        },
        {
            "name": "company",
            "xpath": f"""//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[1]""",
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
    "careers.google.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="jump-content"]/div[1]/div/div[2]/main/div/div/div[1]/div[1]/h1""",
        },
        {
            "name": "location",
            "xpath": f"""//*[@id="jump-content"]/div[1]/div/div[2]/main/div/div/div[1]/div[1]/ul[2]/li[2]""",
        },
        {
            "name": "company",
            "xpath": f"""//*[@id="jump-content"]/div[1]/div/div[2]/main/div/div/div[1]/div[1]/ul[2]/li[1]""",
        },
        {
            "name": "position",
            "xpath": f"""//*[@id="jump-content"]/div[1]/div/div[2]/main/div/div/div[1]/div[1]/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="accordion-about"]""",
        },
    ],
    "ionq.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="job-page"]/div[1]/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="job-page"]/div[2]/p[1]"""},
        {"name": "company", "xpath": f"""Ionq"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="job-page"]/div[1]/h1""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="job-page"]/div[2]/p[3]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job-page"]/div[3]""",
        },
    ],
    "jobs.lever.co": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[3]/div/div[1]/div/div[1]/h2""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Lever"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[3]/div/div[1]/div/div[1]/h2""",
        },
        {
            "name": "type",
            "xpath": f"""/html/body/div[3]/div/div[1]/div/div[1]/div/div[3]""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/div[3]/div/div[2]/div[1]""",
        },
    ],
    "careers.honeywell.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[3]/div/div/div[1]/div[2]/section[1]/div/div/div/div[1]/h1""",
        },
        {
            "name": "location",
            "xpath": f"""/html/body/div[3]/div/div/div[1]/div[2]/section[1]/div/div/div/div[1]/section/div/div[1]/span[1]""",
        },
        {"name": "company", "xpath": f"""Quantinuum"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[3]/div/div/div[1]/div[2]/section[1]/div/div/div/div[1]/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/div[3]/div/div/div[2]/div/div/div[1]/section[1]/div/section""",
        },
    ],
    "careers.ibm.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="post-116"]/div/div[2]/div/div[1]/div/div[1]""",
        },
        {
            "name": "location",
            "xpath": f"""//*[@id="post-116"]/div/div[2]/div/div[1]/div/div[2]/div[5]/ul/li/ul/li[1]""",
        },
        {
            "name": "company",
            "xpath": f"""//*[@id="post-116"]/div/div[2]/div/div[1]/div/div[2]/div[5]/ul/li/ul/li[9]""",
        },
        {
            "name": "position",
            "xpath": f"""//*[@id="post-116"]/div/div[2]/div/div[1]/div/div[1]""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="post-116"]/div/div[2]/div/div[1]/div/div[2]/div[5]/ul/li/ul/li[7]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="post-116"]/div/div[2]/div/div[1]/div/div[4]/div""",
        },
    ],
    "www.northropgrumman.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="main"]/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="main"]/div/div[1]/ul/li[2]"""},
        {"name": "company", "xpath": f"""Northrop_Grumman"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="main"]/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="main"]/div/div[1]/div[1]""",
        },
    ],
    "jobs.recooty.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/div/div/div[2]/div/div/div/div/h4""",
        },
        {
            "name": "location",
            "xpath": f"""/html/body/div/div/div[3]/div/div/div/form/div/div[4]/table/tbody/tr[2]/td[2]""",
        },
        {"name": "company", "xpath": f""""""},
        {
            "name": "position",
            "xpath": f"""/html/body/div/div/div[3]/div/div/div/form/div/div[2]/p[1]/strong""",
        },
        {
            "name": "type",
            "xpath": f"""/html/body/div/div/div[3]/div/div/div/form/div/div[4]/table/tbody/tr[1]/td[2]""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/div/div/div[3]/div/div/div/form/div/div[2]/p[7]""",
        },
    ],
    "nvidia.wd5.myworkdayjobs.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="mainContent"]/div/div/div[1]/div[1]/div/h2""",
        },
        {
            "name": "location",
            "xpath": f"""//*[@id="mainContent"]/div/div/div[1]/div[2]/div[1]/div[1]/div""",
        },
        {"name": "company", "xpath": f"""Nvidia"""},
        {
            "name": "position",
            "xpath": f"""""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="mainContent"]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/dl/dd""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="mainContent"]/div/div/div[1]/div[3]/div[2]/div""",
        },
    ],
    "careers.toshiba.eu": [
        {
            "name": "title",
            "xpath": f"""//*[@id="alreadyloggedin"]/h2/div/div""",
        },
        {
            "name": "location",
            "xpath": f"""//*[@id="alreadyloggedin"]/div[3]/div/div[1]/p[2]""",
        },
        {"name": "company", "xpath": f"""Toshiba"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="alreadyloggedin"]/h2/div/div/text()""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="alreadyloggedin"]/div[3]/div/div[1]/p[6]/text()""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="Media_Rich_Advert"]/div""",
        },
    ],
    "pasqal.io": [
        {
            "name": "title",
            "xpath": f"""//*[@id="post-8941"]/div[1]/div/div[1]/div[1]/h1/strong""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Pasqal"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="post-8941"]/div[1]/div/div[1]/div[1]/h1/strong""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="post-8941"]/div[1]/div/div[1]/div[1]""",
        },
    ],
    "www.qcware.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[2]/h1""",
        },
        {"name": "location", "xpath": f"""/html/body/div[2]/div[2]/div"""},
        {"name": "company", "xpath": f"""Qcware"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[2]/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/div[3]/div""",
        },
    ],
    "www.comeet.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="22.135"]/div[1]/h1/span[1]""",
        },
        {"name": "location", "xpath": f"""//*[@id="22.135"]/div[1]/h3/span[1]"""},
        {"name": "company", "xpath": f"""//*[@id="22.135"]/div[1]/h3/span[3]"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="22.135"]/div[1]/h1/span[1]""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="22.135"]/div[2]/div[3]""",
        },
    ],
    "jobs.eu.lever.co": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[3]/div/div[1]/div/div[1]/h2""",
        },
        {
            "name": "location",
            "xpath": f"""/html/body/div[3]/div/div[1]/div/div[1]/div/div[1]""",
        },
        {"name": "company", "xpath": f"""Lever"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[3]/div/div[1]/div/div[1]/h2""",
        },
        {
            "name": "type",
            "xpath": f"""/html/body/div[3]/div/div[1]/div/div[1]/div/div[3]""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/div[3]/div/div[2]""",
        },
    ],
    "qblox.jobs.personio.de": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[4]/h2""",
        },
        {"name": "location", "xpath": f"""/html/body/div[4]/h6/span/text()"""},
        {"name": "company", "xpath": f"""Qblox"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[4]/h2""",
        },
        {
            "name": "type",
            "xpath": f"""/html/body/div[4]/h6/span/text()""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job-details"]/div[1]/article[1]/div""",
        },
    ],
    "careers.microsoft.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="content-1"]/div[1]/div/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="content-1"]/div[1]/div/div/span"""},
        {"name": "company", "xpath": f"""Microsoft"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="content-1"]/div[1]/div/h1""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="content-1"]/div[3]/div/ul/li[6]/span[2]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="content-1"]/div[4]""",
        },
    ],
    "xanadu.applytojob.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/main/div[2]/div/h1""",
        },
        {"name": "location", "xpath": f"""/html/body/main/div[2]/div/div[1]/div[1]"""},
        {"name": "company", "xpath": f"""Xanadu"""},
        {
            "name": "position",
            "xpath": f"""/html/body/main/div[2]/div/h1""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="resumator-job-employment"]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job-description"]""",
        },
    ],
    "careers.boozallen.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[1]/div/div/div/div/h2""",
        },
        {"name": "location", "xpath": f"""/html/body/div[1]/div/div/div/div/div[3]"""},
        {"name": "company", "xpath": f"""Boozallen"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[1]/div/div/div/div/h2""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="main"]/div/div/div/div[2]/section/div[1]/article[2]/div""",
        },
    ],
    "psiquantum.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="header"]/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="header"]/div"""},
        {"name": "company", "xpath": f"""Psiquantum"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="header"]/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="content"]""",
        },
    ],
    "zapata.bamboohr.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/h2""",
        },
        {
            "name": "location",
            "xpath": f"""/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/span""",
        },
        {"name": "company", "xpath": f"""Bamboo"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/h2""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div""",
        },
    ],
    "vescent.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="maincontent"]/div[2]/div/h1""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Vescent"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="maincontent"]/div[2]/div/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="maincontent"]""",
        },
    ],
    "jobs.keysight.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="content"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div""",
        },
        {"name": "location", "xpath": f"""//*[@id="content"]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/span[2]"""},
        {"name": "company", "xpath": f"""Keysight"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="content"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="content"]/div/div[2]/div/div[1]/div[2]/div[9]/div/div/div/span/span""",
        },
    ],
    "search.linkup.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Linkup"""},
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
    "evolutionq.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="job-section"]/div/h2""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Evolutionq"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="job-section"]/div/h2""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job-section"]/div""",
        },
    ],
    "www.qvideaslab.ca": [
        {
            "name": "title",
            "xpath": f"""//*[@id="text-block-6357928364cdd"]/p[1]/strong/u""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Qvideaslab"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="text-block-6357928364cdd"]/p[1]/strong/u""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="2"]/div""",
        },
    ],
    "apply.deloitte.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="main-panel"]/section[1]/div/div[1]/article/div/div/h2""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Deloitte"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="main-panel"]/section[1]/div/div[1]/article/div/div/h2""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="main-panel"]/section[2]/div/div[1]/div/div[1]/div/article/div[2]/div/div/span[2]""",
        },
    ],
    "www.psicorp.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="block-system-main"]/div/div[2]/div/div/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="block-system-main"]/div/div[3]/div[1]/div"""},
        {"name": "company", "xpath": f"""Psicorp"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="block-system-main"]/div/div[2]/div/div/h1""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="block-system-main"]/div/div[3]/div[2]/div/div""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="block-system-main"]/div/div[4]""",
        },
    ],
    "www.mycareersfuture.gov.sg": [
        {
            "name": "title",
            "xpath": f"""//*[@id="job_title"]""",
        },
        {"name": "location", "xpath": f"""//*[@id="job-details"]/div[1]/div[3]/div/section[1]/p"""},
        {"name": "company", "xpath": f"""//*[@id="job-details"]/div[1]/div[3]/div/section[1]/p"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="job_title"]""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job_description"]""",
        },
    ],
    "qrypt.applytojob.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/main/div[2]/div/h1""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Qrypt"""},
        {
            "name": "position",
            "xpath": f"""/html/body/main/div[2]/div/h1""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="resumator-job-employment"]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job-description"]""",
        },
    ],
    
    "www.qrypt.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/main/div[2]/div/h1""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Qrypt"""},
        {
            "name": "position",
            "xpath": f"""/html/body/main/div[2]/div/h1""",
        },
        {
            "name": "type",
            "xpath": f"""//*[@id="resumator-job-employment"]""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job-description"]""",
        },
    ],
    
    "unitary.fund": [
        {
            "name": "title",
            "xpath": f"""//*[@id="content"]/section/center/h1""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Unitary"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="content"]/section/center/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="content"]/section""",
        },
    ],
    "www.ziprecruiter.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="job_content_skip"]/article/div[1]/div[1]/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="job_content_skip"]/article/div[1]/div[2]/div[2]"""},
        {"name": "company", "xpath": f"""//*[@id="job_content_skip"]/article/div[2]/section/h2"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="job_content_skip"]/article/div[1]/div[1]/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="job_content_skip"]/article/div[2]""",
        },
    ],
    "quantumcomputingreport.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="wrapper"]/div[3]""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Quantumcomputingreport"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="wrapper"]/div[3]""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="post-9090"]/div""",
        },
    ],
    "www.aliroquantum.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="hs_cos_wrapper_widget_1628627410360"]/section/div/h2""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Aliroquantum"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="hs_cos_wrapper_widget_1628627410360"]/section/div/h2""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="hs_cos_wrapper_widget_1628627410360"]/section/div""",
        },
    ],
   
    "www.pqsecurity.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="post-541"]/div/h2[1]/span/strong""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f"""Pqsecurity"""},
        {
            "name": "position",
            "xpath": f"""//*[@id="post-541"]/div/h2[1]/span/strong""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="post-541"]/div""",
        },
    ],
    
    "jobs.boeing.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="content"]/div/div/section/div[1]/div[1]/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="content"]/div/div/section/div[1]/div[1]/h1"""},
        {"name": "company", "xpath": f"""Boeing"""},
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
            "xpath": f"""//*[@id="content"]/div/div/section/div[3]/div""",
        },
    ],
    "www.riverlane.com": [
        {
            "name": "title",
            "xpath": f"""/html/body/main/header/div/div[1]/h1/span""",
        },
        {"name": "location", "xpath": f"""/html/body/main/header/div/div[1]/div/dl[1]/dd"""},
        {"name": "company", "xpath": f"""Riverlane"""},
        {
            "name": "position",
            "xpath": f"""/html/body/main/header/div/div[1]/h1/span""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""/html/body/main/section""",
        },
    ],
    
    "www.onerh.fr": [
        {
            "name": "title",
            "xpath": f"""/html/body/div[1]/div[3]/div/div/div/h1""",
        },
        {"name": "location", "xpath": f"""//*[@id="top-anchor"]/div[1]/div[1]/div[2]"""},
        {"name": "company", "xpath": f"""Onerh"""},
        {
            "name": "position",
            "xpath": f"""/html/body/div[1]/div[3]/div/div/div/h1""",
        },
        {
            "name": "type",
            "xpath": f"""""",
        },
        {
            "name": "description",
            "xpath": f"""//*[@id="top-anchor"]""",
        },
    ],
    
    "fei.breezy.hr": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "angel.co": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "bleximo-corp.breezy.hr": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "careers-sri.icims.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "careers.bpglobal.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "careers.deloitte.ca": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "cdn2.hubspot.net": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "fr.linkedin.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.monster.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "qubitekk.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "secureservercdn.net": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "singapore.job-q.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "workforcenow.adp.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.careerbeacon.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.formfactor.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "recruitingbypaycor.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.glassdoor.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.sandboxaq.com": [
        {
            "name": "title",
            "xpath": f"""//*[@id="header"]/h1""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
        {
            "name": "position",
            "xpath": f"""//*[@id="header"]/h1""",
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
    "quantrolox.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.quantum-machines.co": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "anametric.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.quintessencelabs.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
     "job.deloitte.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.xairos.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.lockheedmartinjobs.com": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
    "www.monster.fi": [
        {
            "name": "title",
            "xpath": f"""""",
        },
        {"name": "location", "xpath": f""""""},
        {"name": "company", "xpath": f""""""},
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
}

