"""
{
    key: [list],
    key2 : {dict},
}
"""

travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Belin', 'Hamburg', 'Stuttgart'],
}

# 怎么把 France 的 value 改成 字典？
travel_log = {
    'France': {"cities_visited": ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'cities_vistied': ['Belin', 'Hamburg', 'Stuttgart'], 'total_visits': 5},
}

travel_log = [
    {
        'Country': 'France',
        "cities_visited": ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    {
        'Country': 'Germany',
        'cities_vistied': ['Belin', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    },
]

# exercise 9.2
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
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries----没做出来
# to be added to the travel_log. 👇


def add_new_country(country_visited, time_visited, cities_visited):
    new_country = {}
    new_country['country'] = country_visited
    new_country['visits'] = time_visited
    new_country['cities'] = cities_visited
    travel_log.append(new_country)

# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
