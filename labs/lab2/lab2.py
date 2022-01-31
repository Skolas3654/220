import math
from math import sqrt

value_amount = eval(input("How many values are there:\n"))

basic_sum = 0 #dont print in final output unless testing is needed, used for rms average

rms_average = 0

harmonic_mean = 0
harmonic_den = 0

geometric_mean = 0
geometric_index = 1


for i in range(value_amount):
    value = eval(input("Enter value:\n"))
    basic_sum = basic_sum + value ** 2

    harmonic_den = (1/value) + harmonic_den

    geometric_mean = value

    geometric_index = geometric_index * value



basic_sum = basic_sum/value_amount
rms_average = round(sqrt(basic_sum),3)

harmonic_mean = value_amount/harmonic_den

geometric_mean = round(geometric_index**(1/value_amount),3)



print("RMS average =",rms_average)

print("Harmonic ean =",harmonic_mean)

print("Geometric Mean =",geometric_mean)
