import pandas as pd
from pprint import pprint

import COVID19Py
from country_code_finder import country_info


covid = COVID19Py.COVID19()


def by_country():
    option = input("""
                    1. with timeline
                    2. without timeline
                    ----> """)
    if int(option) == 1:
        location = covid.getLocationByCountryCode("{}".format(country_info()), timelines=True)
        for latest_data in location:
            latest_data.pop("country_population")
            latest_data.pop("province")
            latest_data.pop("last_updated")
            latest_data.pop("coordinates")
            latest_data.pop("id")
            latest_data.pop("country")
            latest_data.pop("country_code")

        pprint(location)
    if int(option) == 2:
        location = covid.getLocationByCountryCode("{}".format(country_info()))
        for latest_data in location:
            latest_data.pop("country_population")
            latest_data.pop("province")
            latest_data.pop("last_updated")
            latest_data.pop("coordinates")
            latest_data.pop("id")
            latest_data.pop("country")
            latest_data.pop("country_code")
            df = pd.DataFrame(latest_data)
            print(df)


by_country()
