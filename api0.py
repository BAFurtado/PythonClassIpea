import requests
import urllib.parse


def calculate_distancia(x1, y1, x2, y2):
    return f'{(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5) * 111139:,.0f} metros'


def get_lat_lon(local):
    address = f'{local}, Brasília, Brazil'
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
    response = requests.get(url).json()
    print(response[0]['display_name'])
    lat = float(response[0]['lat'])
    long = float(response[0]['lon'])
    print(f'lat: {lat:.8}, long: {long:.8}')
    return long, lat


if __name__ == '__main__':
    locais = 'Ministério da Educação', 'Ipea', 'CNPq', 'SQS 413'

    for l in locais:
        get_lat_lon(l)

    local1 = 'SQS 316'
    local2 = 'SQN 416'
    l11, l12 = get_lat_lon(local1)
    l21, l22 = get_lat_lon(local2)

    local = 'Roraima'
    get_lat_lon(local)

    print(calculate_distancia(l11, l12, l21, l22))
