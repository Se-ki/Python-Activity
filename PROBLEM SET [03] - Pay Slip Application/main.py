def createTextFile(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary):
    text_file = open("payslip.txt", 'w')
    display(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary, text_file)
    text_file.close()

def display(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary, text_file=None):
    print("==============PAYSLIP==============", end="\n\n", file=text_file)
    print("======EMPLOYEE INFORMATION=======", file=text_file)
    print("Employee         :  " + employee_name, end="\n", file=text_file)
    print("Rendered Hours   : ", rendered_hours, end="\n", file=text_file)
    print("Rate per Hour    : ", rate_per_hour, end="\n", file=text_file)
    print("Gross Salary     : ", gross_salary, end="\n\n", file=text_file)
    print("=============DEDUCTIONS===========", end="\n", file=text_file)
    print("SSS              : ", sss_contribution, end="\n", file=text_file)
    print("PhilHealth       : ", philhealth_contribution, end="\n", file=text_file)
    print("Loans            : ", loans, end="\n", file=text_file)
    print("Tax              : ", tax, end="\n", file=text_file)
    print("Total Deductions : ", total_deduct, end="\n\n", file=text_file)
    print("==========NET SALARY===============", end="\n", file=text_file)
    print("Php. ", net_salary, end="\n", file=text_file)

tax_percent = 0.35
employee_name = str(input("Enter Employee's name: "))
rendered_hours = int(input("Enter Rendered hours: "))
rate_per_hour = float(input("Enter Rate per hour: "))
sss_contribution = float(input("Enter SSS contribution: "))
philhealth_contribution = float(input("Enter PhilHealth contribution: "))
loans = float(input("Enter loans: "))

gross_salary = rendered_hours * rate_per_hour

tax = gross_salary * tax_percent

total_deduct = sss_contribution + philhealth_contribution + loans + tax

net_salary = gross_salary - total_deduct

display(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary)
createTextFile(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary)
