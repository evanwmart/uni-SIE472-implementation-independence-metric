import tkinter as tk
import tkinter.ttk as ttk
import requests
import json
from datetime import datetime

# Link for API use and documentation (use the '+' next to 'Developers' for info):
# https://nvd.nist.gov/developers


def dateFormatter(m, d, y):
    if (m == -1):
        now = datetime.now()
        return datetime(now.year, now.month, now.day).strftime("%Y-%m-%dT%H:%M:%S.") + "000"
    else:
        return datetime(y, m, d).strftime("%Y-%m-%dT%H:%M:%S.") + "000"


def getCVEs(keyword, start_date=dateFormatter(1, 1, 2023), end_date=dateFormatter(-1, 0, 0), max_results=10):
    # url = f'https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate={}&pubEndDate={}'
    print(type(start_date))
    print(end_date)
    url = f'https://services.nvd.nist.gov/rest/json/cves/2.0/?keywordSearch={keyword}&pubStartDate={start_date}&pubEndDate={end_date}&resultsPerPage={str(max_results)}'
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        return_list = []
        data = json.loads(response.content)

        for item in data['vulnerabilities']:
            ID = item['cve']['id']
            pDate = item['cve']['published']
            description = item['cve']['descriptions'][0]['value']
            lmDate = item['cve']['lastModified']
            return_list.append([ID, pDate, description, lmDate])

        return return_list

    else:
        return ([["ERROR: ", str(response.status_code)]])


def CVEdictToList(CVE_list):
    print(CVE_list[0])
    print("\t", CVE_list[1])
    print("\t", CVE_list[2])
    print("\t", CVE_list[3])
    print("\n")

