"""
* counter
* defaultdict
* ordereddict
* namedtuple
* depue
"""

from collections import Counter

device_temperatures = [16.5, 453.5, 55.58, 483.65, 54.54, 14.5, 15.5, 5, 54, 6, .654, 500,43.8]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

print(Counter({'hello': 5, 'hi': 3,})['hi'])







