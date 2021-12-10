def weeklyPaid(hours_worked, wage):
    if hours_worked > 40:
        return 40 * wage + (hours_worked - 40) * wage * 1.5
    else:
        return hours_worked * wage
def getGrossPay(annual_salary, no_of_pay_peroids):
    return float(annual_salary/no_of_pay_peroids)
print("Payroll Calculator")
user = input("Enter Employee Name or '0' to Quit: ")
end = "0"
while user!=end:
        print("Select the type of employee:")
        print("1.Hourly Employee")
        print("2.Salary Employee")
        sel = int(input("Enter Choice: "))
        if sel == 1:
            Hours = float(input("Please Enter Hours worked: "))
            Rate = float(input("Please Enter Rate of Pay: ₹"))
            hourlyPay = weeklyPaid(Hours, Rate)
            print("Hourly Pay: ₹", hourlyPay)
        if sel == 2:
            annual_salary = int(input("Enter Annual Salary: "))
            no_of_pay_peroids = int(input("Enter No. of Pay Periods: "))
            GrossPay = getGrossPay(annual_salary, no_of_pay_peroids)
            print("Gross Pay: ₹", GrossPay)
        print("Employee Name: ", user)
        user = input("Enter Next Employee or type '0' to Exit: ")
else:
    print("Exiting program....")

