def read_data(filename):
    file = open(filename, 'r')
    text = file.read()
    text = text.replace("\n"," ")
    str_list = text.split()
    return str_list

def is_in_linear(search_val, values):
    index = 0
    length = len(values)-1
    while (int(values[index]) != search_val) and (index < length):
        index += 1
        if int(values[index]) == search_val:
            return True
    return False


data = read_data('data_sorted.txt')


print(is_in_linear(75,data))
