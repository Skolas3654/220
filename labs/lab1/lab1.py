
def credit_card():
    print("We are trying to calculate your monthly interest charge")
    print("Please enter the information asked of you\n")


    #asks for the inputs needed for the calculations
    annual_interest_rate = eval(input("What is the annual interest rate:\n"))
    billing_days = eval(input("How many days are on the billing cycle (enter as a whole number):\n"))
    previous_balance = eval(input("What was the previous net balance:\n"))
    payment_amount = eval(input("What is your payment amount\n"))
    day_of_payment = eval(input("What was your day of payment (enter as a whole number):\n"))

    #calculates the monthly interest
    monthly_interest_rate = annual_interest_rate/12

    #takes all inputs and goes through the process to calculate the monthly charge

    balance = previous_balance * billing_days
    temp_x = payment_amount * day_of_payment
    result = balance - temp_x
    monthly_payment = result/31
    monthly_charge = monthly_payment * monthly_interest_rate *0.01
    print("$"+ str(monthly_charge), "is your monthly charge")

credit_card()



