from lab12.algorithms import *
from graphics import *

r1 = Rectangle(Point(5,5),Point(60,60))
r2 = Rectangle(Point(10,10),Point(11,11))
r3 = Rectangle(Point(50,50),Point(500,500))


def star_find(filename):
    file = open(filename,'r')
    file_strings = file.readlines()
    file_strings = "".join(file_strings)
    signal_list = file_strings.split()
    strong_signals = 0
    signals = 0
    length = len(signal_list) - 1
    while (strong_signals != 5) and (signals < length):
        signals += 1
        if 4000 <= float(signal_list[signals]) <= 5000:
            print(strong_signals+1,"- A pulse of",signal_list[signals],'was found on search attempt',signals)
            strong_signals += 1
    print("it took",signals,'searches to find the fifth signal')



star_find('signals.txt')
print()

                    #rectangle sort
r_lis = [r2,r3,r1]
print('original list:',r_lis)
rect_sort(r_lis)
print('sorted list:',r_lis)

print()
                    #selection sort
a = [5,8,3,5,2,1]
print('original list:',a)
selection_sort(a)
print('sorted list:',a)

print()
print("HAVE A GOOD SUMMER :)")

