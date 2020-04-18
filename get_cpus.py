import requests
from bs4 import BeautifulSoup 

r = requests.get('https://www.cpubenchmark.net/pt9_cpu_list.php')

soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find(id='cputable')
trs = table.find_all('tr')
result = []
for idx, tr in enumerate(trs):
    if idx==0:
        continue
    tds = tr.find_all('td')
    print(tds)
    result.append({
        'name': tds[0].text.strip(),
        'cpu_mark': tds[1].text.strip().replace(',',''),
        'thread_rating': tds[2].text.strip().replace(',',''),
        'samples': tds[3].text.strip(),
    })

print(len(result))
lines = []
with open('output.md', "w") as fout:
    for r in result:
        line = '|'
        line += r['name'] +'|'
        line += r['cpu_mark'] +'|'
        line += r['thread_rating'] +'|'
        line += r['samples'] +'|'
        # lines.append(line)
        fout.write(line)
        fout.write('\n')
    #line+='\r\n'
    #fout.writelines(lines)