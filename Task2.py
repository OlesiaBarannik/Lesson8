def make_country(name, capital):
    country = {}
    country['country'] = name
    country['capital'] = capital
    return country

my_country = make_country("Ukraine", "Kyiv")
print(my_country)
