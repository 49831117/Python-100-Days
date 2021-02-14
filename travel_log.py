travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_input, visits_input, cities_input):
    new_country = {}
    new_country["country"] = country_input
    new_country["visits"] = visits_input
    new_country["cities"] = cities_input

    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
