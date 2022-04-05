# conda install geopandas
# conda install geopandas pandas fiona gdal shapely

import matplotlib.pyplot as plt
import geopandas as gpd


def simplest_plot(shape):
    shape.plot()
    plt.show()


def plotting(shape, col, label, leg=True):
    fig, ax = plt.subplots()
    shape.plot(column=col,
               legend=leg,
               ax=ax,
               scheme='quantiles',
               cmap='inferno',  # 'veridis'
               # missing_kwds={'color': 'white'},
               legend_kwds={'fmt': '{:,.0f}', 'frameon': False}
               )
    shape.boundary.plot(ax=ax, color='white', linewidth=.5, edgecolor='grey')
    ax.set_title(label)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    bsb = gpd.read_file('data/53.shp')
    simplest_plot(bsb)
    sales = gpd.read_file('data/sales_bairros.shp')
    simplest_plot(sales)
    # Maps
    maps = {'price': 'Preço total', 'days_in_ma': 'Dias no mercado', 'price_util': 'Preço por m$^2$'}
    for each in maps:
        plotting(sales, each, maps[each])
