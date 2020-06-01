import COVID19Py

country_name = input("Enter the name of the country you wish to know the code:- ")


def country_info():
    covid = COVID19Py.COVID19()
    all_details = covid.getAll()
    country_code = {}
    for key, value in all_details.items():
        if key == "locations":
            for location_list in value:
                location_list.pop("country_population")
                location_list.pop("province")
                location_list.pop("last_updated")
                location_list.pop("coordinates")
                location_list.pop("latest")
                location_list.pop("id")
                country_code[location_list["country"]] = location_list["country_code"]

    for country, code in country_code.items():
        if country == country_name.capitalize():
            # print("Your entered country name is {} and country code is {}".format(country, code))
            return code

country_info()


