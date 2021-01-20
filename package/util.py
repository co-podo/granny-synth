
# source: https://stackoverflow.com/questions/4092528/how-to-clamp-an-integer-to-some-range/4092677#4092677
def clamp(value, minValue, maxValue):
    return sorted((value, minValue, maxValue))[1]