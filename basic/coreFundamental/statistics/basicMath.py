import statistics

example_list = [4,6,6,8,6,5,56,56,565,6,654,656,56,5468,464,4]

x = statistics.mean(example_list)
print(".mean : ",x)

x1 = statistics.stdev(example_list)
print(".stdev :",x1)

x2 = statistics.variance(example_list)
print(".variance : ",x2)