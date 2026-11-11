import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature', lambda t: sum(map(float, t))/len(t), cities))
print()

# Print all cities in Germany
print('Cities in Germany:')
cities_in_germany = filter_items(lambda n : n['country'] == 'Germany', cities)
for city in cities_in_germany:
    print(city['city'])
print()

# Print all cities in Spain with a temperature above 12°C
print('all cities in Spain with a temperature above 12°C:')
germanycity12c = filter_items(lambda n: n['country'] == 'Spain' and float(n['temperature']) > 12, cities)
for city in germanycity12c:
    print(city['city'])
print()

# Count the number of unique countries
print('number of unique countries:')
print(aggregate('country', lambda n: len(set(n)), cities))
print()

# Print the average temperature for all the cities in Germany
print('average temperature for all the cities in Germany:')
print(aggregate('temperature', lambda n: sum(map(float,n))/len(n), cities_in_germany))
print()

# Print the max temperature for all the cities in Italy
print('max temperature for all the cities in Italy:')
cities_in_italy = filter_items(lambda n: n['country'] == 'Italy', cities)
print(aggregate('temperature', lambda n: max(map(float, n)), cities_in_italy))
print()

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
