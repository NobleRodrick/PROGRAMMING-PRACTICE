# collect the necessary inputs: principal, apr, years
# calculate the monthly payment
# show the user

def main():
    print("This is the monthly payment loan calculator ")
    print("")
    
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input the amount of years: "))
    
    monthly_interest_rate = apr/1200
    amount_of_months = years*12
    monthly_payment = principal*monthly_interest_rate/(1-(1 + monthly_interest_rate) **(-amount_of_months) )
    
    print(f"the monthly payment for this loan is : {monthly_payment}")
    
    
main()