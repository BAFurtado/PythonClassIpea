import pandas as pd


# source: https://pbpython.com/currency-cleanup.html
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return x.replace('R$', '').replace('.', '').replace(',', '.')
    return x


if __name__ == '__main__':
    p = 'https://economia.uol.com.br'
    tabelas = pd.read_html(p)

    tabelas = pd.read_html(p, decimal=',', thousands='.')
    moedas = tabelas[0]
    moedas.columns = ['moeda', 'variacao', 'valor_reais']
    print(moedas.head())
    moedas.valor_reais = moedas.valor_reais.apply(clean_currency).astype(float)
    print(moedas)
    print(moedas.valor_reais.dtype)
