import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print('Cities in Germany:')
for city in cities:
    if city['country'] == 'Germany':
        print(city['city'])
print()

# Print all cities in Spain with a temperature above 12°C
print('all cities in Spain with a temperature above 12°C:')
for city in cities:
    if (city['country'] == 'Spain') and (float(city['temperature']) > 12):
        print(city['city'])
print()

# Count the number of unique countries
print('number of unique countries:')
list = []
for city in cities:
    if city['country'] not in list:
        list.append(city['country'])
print(len(list))
print()


# Print the average temperature for all the cities in Germany
print('average temperature for all the cities in Germany:')
cities_in_germany = []
for city in cities:
    if city['country'] =='Germany':
        cities_in_germany.append(city)
num_cities = len(cities_in_germany)
sum_temp = 0
for city in cities_in_germany:
    sum_temp += float(city['temperature'])
print(sum_temp/num_cities)
print()

# Print the max temperature for all the cities in Italy
print('max temperature for all the cities in Italy:')
italy = []
for city in cities:
    if city['country'] == 'Italy':
        italy.append(city)
temp = []
for city in italy:
    temp.append(float(city['temperature']))

print(max(temp))
