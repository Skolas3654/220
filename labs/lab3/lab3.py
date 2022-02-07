"Andreas Dilling - Lab 3"

def DOT():

    total_cars_traveled = 0

    print("How many roads were surveyed")
    roads = eval(input(""))
    for i in range(roads):
        print("How many days was road", i+1, "surveyed?")
        days = eval(input(""))

        cars_traveled = 0
        daily_average = 0
        for j in range(days):
            print("How many cars traveled on day",j+1)
            cars = eval(input(""))
            cars_traveled = cars + cars_traveled
        total_cars_traveled = total_cars_traveled + cars_traveled
        daily_average = cars_traveled/days
        print("Road",i+1,"average vehicles per day:",daily_average)

    total_average = total_cars_traveled/roads
    print("Total numbers of vehicles traveled on all roads:",total_cars_traveled)
    print("Average number of vehicles per road:",total_average)

DOT()

