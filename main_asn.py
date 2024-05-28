import requests
import pandas as pd

asn_list = str(open('./asn_id_list.txt', 'r').read()).split('\n')

print(asn_list)

def get_asn_data(asn_id: str):
    url = f"https://2ip.ru/as/{asn_id}/"
    response = requests.request("GET", url)
    analiz_data = response.text
    re = pd.read_html(analiz_data)[1][1]
    return re




for i in range(len(asn_list)):
    try:
        r = get_asn_data(asn_list[i])
        r.to_csv(f'result{asn_list[i]}.csv', sep=',', encoding='utf-8')
        print(f'{i+1} in {len(asn_list)}')
    except:
        print(f'error {asn_list[i]}')
