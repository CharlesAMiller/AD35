'''
This script can be run to retrieve the relevant data files for the project.

Usage: 'python getData.py'

'''

import requests

if __name__ == '__main__':

    base_url = "https://statewidedatabase.org/pub/data/G{year}/c0{county}/c0{county}_g{year}_sov_data_by_g{year}_srprec.csv"
    base_filename = "/data/processed/c0{county}_g{year}_sov_data_by_g{year}_srprec.csv"

    for year in [12, 14, 16, 18, 20]:
        for county in [79, 83]:
            resp = requests.get(base_url.format(year=year, county=county))
            with open(base_filename.format(year=year, county=county), 'wb') as file:
                file.write(resp.content)
