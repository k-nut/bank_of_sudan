import json
import datetime

from bs4 import BeautifulSoup
import requests

def main():
    URL = "http://www.cbos.gov.sd/en/node/452"
    data = requests.get(URL).text
    soup = BeautifulSoup(data)
    table = soup.select("#node-452 table")[0]
    headers = [td.get_text().strip() for td in table.find("tr").find_all("td")]
    for tr in table.find_all("tr"):
        contents = [td.get_text().strip() for td in tr.find_all("td")]
        data_dict = dict(zip(headers, contents))
        data_dict.pop("", None)
        data_dict["source_url"] = URL
        data_dict["sample_date"] = datetime.datetime.now().isoformat()
        print json.dumps(data_dict)


main()
