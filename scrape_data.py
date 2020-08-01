"""
Scraping data from wikipedia table
"""

from bs4 import BeautifulSoup
import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import requests


def main():
    # TODO: Check if part behind # is needed
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_past_and_' \
          'projected_GDP_(PPP)_per_capita'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('table')
    results = results[4]

    # TODO: Join multiple tables
    # results = results[1:6]

    # for result in results:

    rows = []
    trs = results.find_all('tr')
    headers = [td.get_text(strip=True) for td in trs[0].find_all('th')]
    for tr in trs[1:]:  # for every table row
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')])

    # TODO: Merge df with world
    # TODO: Fix misalignment (use ISO code?)
    df = pd.DataFrame(rows, columns=headers)

    world = geopandas.read_file(
        geopandas.datasets.get_path('naturalearth_lowres'))
    world.plot()
    plt.show()


if __name__ == '__main__':
    main()
