import requests
import json
from bs4 import BeautifulSoup 

def main():
    r = requests.get('https://www.cpubenchmark.net/pt9_cpu_list.php')

    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id='cputable')
    trs = table.find_all('tr')
    result = []
    for idx, tr in enumerate(trs):
        if idx==0:
            continue
        tds = tr.find_all('td')
        # print(tds)
        result.append({
            'name': tds[0].text.strip(),
            'cpu_mark': tds[1].text.strip().replace(',',''),
            'thread_rating': tds[2].text.strip().replace(',',''),
            'samples': tds[3].text.strip(),
        })


    with open('cpus.json', "w") as fout:
        fout.write(json.dumps(result, indent=2))    

if __name__ == '__main__':
    main()