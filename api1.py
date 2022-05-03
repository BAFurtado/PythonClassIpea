import urllib.request

import requests
from bs4 import BeautifulSoup as BS


def get_page(url, endpoint, params):
    if 'territory_id' in params:
        requests.get(f"{url}{endpoint}/{params['territory_id']}", params=params).json()
    return requests.get(f'{url}{endpoint}', params=params).json()


def simple_url(url):
    response = urllib.request.urlopen(url)
    print(response.status)
    if response.status == 200:
        txt = BS(response, 'html5lib')
        print(txt)


if __name__ == '__main__':

    u = 'https://queridodiario.ok.org.br/api/'
    e = 'gazettes/'

    p = {'since': '2021-12-15',
         'until': '2022-04-01',
         'keywords': ['pandemia']}

    r = get_page(u, e, p)
    print(r)

    textos = list()
    for gazette in r['gazettes']:
        try:
            textos.append(gazette['file_raw_txt'])
        except KeyError:
            pass
    #
    print(textos)
    #
    simple_url(textos[0])
    #
    # # Exemplo 2. APIs Diários
    # territory_id usa o código do IBGE 7 dígitos
    p2 = {'territory_id': '3304557',
          'since': '2022-01-01',
          'until': '2022-04-27',
          'keywords': ['ITBI']}

    r = get_page(u, e, p2)
    print(r)
    #
    simple_url(r['gazettes'][0]['file_raw_txt'])

