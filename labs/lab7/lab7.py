def weighted_average(in_file_name, out_file_name):
    in_file_name = open(in_file_name,'r')
    out_file_name = open(out_file_name,'w')

    average = 0
    class_average = 0
    weight_amount = 0

    for line in in_file_name:
        split_list = line.split(": ")

        names = (line.split(": ")[0])
        numbers = split_list[1].split(" ")

        for i in range(0,len(numbers),2):
            weight = int(numbers[i])
            num = int(numbers[i+1])
            weight_amount = weight_amount + weight
            average = (weight * num) + average

        average = average/100
        average = round(average, 1)

        if weight_amount == 100:
            print(names + "'s average", average, file=out_file_name)
            class_average = class_average + average
        elif weight_amount < 100:
            print("Error: The weights are less than 100.", file=out_file_name)
        else:
            print("Error: The weights are more than 100.", file=out_file_name)
        weight_amount = 0

    print("Class average:", class_average//3, file=out_file_name)

weighted_average('grades.txt', 'avg.txt')


