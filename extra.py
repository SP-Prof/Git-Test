from setup import sum_two_numbs

def sum_three_numbs(x, y, z):
    return sum_two_numbs(x, y) + z

def sum_four_numbs(x, y, z, ab):
    return sum_three_numbs(x, y, z) + ab