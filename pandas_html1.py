import pandas as pd


if __name__ == '__main__':
    p = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
    wiki_data = pd.read_html(p)
    print(f'Número tabelas: {len(wiki_data)}')

    for i in range(10):
        print(wiki_data[i].head(2))

    # A tabela 9 parece de interesse

    print(wiki_data[9].head())
    print('')
    print(f'Colunas: {wiki_data[9].columns}')

    # Ou simplesmente:
    wiki_data[9]
    wiki_data[9].iloc[:, 0]
    wiki_data[9].loc[13]
