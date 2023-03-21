def sort_dictionary(dict):
    sorted_dictionary = sorted(dict.items(), key = lambda x: x[1][1])
    result = [(name, phone) for name, (phone, age) in sorted_dictionary]
    return result