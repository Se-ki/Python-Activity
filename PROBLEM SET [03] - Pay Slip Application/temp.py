"""
    PROBLEM SET [03] - Pay Slip Application

    Write a basic payroll application having the essential details like employee information, deduction details, rate per day and or rate per hour rendered hours or days, etc. as input and then generate the computed pay slip format result in a text file.

    It will have the following user input:
    - Employee Name
    - Rendered Hours
    - Rate per Hour
    - SSS Contribution
    - PhilHealth Contribution 
    - Loans

    Taxes can either be computed or predefined.
    The program will display/compute the employee pay in a typical PAY SLIP format shown below:

    ==============PAYSLIP==============

    ======EMPLOYEE INFORMATION=======
    Employee Name: ..........................................
    Rendered Hours: ..........................................
    Rate per Hour: ..............................................
    Gross Salary: ................................................

    =============DEDUCTIONS===========
    SSS: .............................................
    PhilHealth: ..................................
    Loans: .........................................
    Tax: .............................................
    Total Deductions: .......................

    ==========NET SALARY===============
    Php. ......................
"""
# class Payslip:
    
#     def __init__(self, employee_name, rendered_hours, rate_per_hour, sss_contribution, philhealth_contribution, loans):
#         self.employee_name = employee_name
#         self.rendered_hours = rendered_hours
#         self.rate_per_hour = rate_per_hour
#         self.sss_contribution = sss_contribution
#         self.philhealth_contribution = philhealth_contribution
#         self.loans = loans
#         self.tax_percent = 0.35
        
#     def tax(self):
#         return self.grossSalary() * self.tax_percent
    
#     def grossSalary(self):
#         return self.rendered_hours * self.rate_per_hour
    
#     def totalDeduction(self):
#         return self.sss_contribution + self.philhealth_contribution + self.loans + self.tax()
    
#     def netSalary(self):
#         return self.grossSalary() - self.totalDeduction()
    
#     def createTextFile(self, file_name):
#         text_file = open(file_name, "w")
#         self.display(text_file)
#         text_file.close()
    
#     def display(self, text_file=None):
        # print("==============PAYSLIP==============", end="\n\n", file=text_file)
        # print("======EMPLOYEE INFORMATION=======", file=text_file)
        # print("Employee         : " + self.employee_name, end="\n", file=text_file)
        # print("Rendered Hours   : ", self.rendered_hours, end="\n", file=text_file)
        # print("Rate per Hour    : ", self.rate_per_hour, end="\n", file=text_file)
        # print("Gross Salary     : ", self.grossSalary(), end="\n\n", file=text_file)
        # print("=============DEDUCTIONS===========", end="\n", file=text_file)
        # print("SSS              : ", self.sss_contribution, end="\n", file=text_file)
        # print("PhilHealth       : ", self.philhealth_contribution, end="\n", file=text_file)
        # print("Loans            : ", self.loans, end="\n", file=text_file)
        # print("Tax              : ", self.tax(), end="\n", file=text_file)
        # print("Total Deductions : ", self.totalDeduction(), end="\n\n", file=text_file)
        # print("==========NET SALARY===============", end="\n", file=text_file)
        # print("Php. ", self.netSalary(), end="\n", file=text_file)
        
# employee_name = str(input("Enter Employee's name: "))
# rendered_hours = int(input("Enter Rendered hours: "))
# rate_per_hour = float(input("Enter Rate per hour: "))
# sss_contribution = float(input("Enter SSS contribution: "))
# philhealth_contribution = float(input("Enter PhilHealth contribution: "))
# loans = float(input("Enter loans: "))
# payslip = Payslip(employee_name, rendered_hours, rate_per_hour, sss_contribution, philhealth_contribution, loans)
# payslip.display()
# payslip.createTextFile("payslip.txt")


"""if oop is not allowed so use this method"""

def createTextFile(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary):
    text_file = open("payslip.txt", "w")
    display(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary, text_file)
    text_file.close()

def display(employee_name, rendered_hours, rate_per_hour, gross_salary, sss_contribution, philhealth_contribution, loans, tax, total_deduct, net_salary, text_file=None):
    print("==============PAYSLIP==============", end="\n\n", file=text_file)
    print("======EMPLOYEE INFORMATION=======", file=text_file)
    print("Employee         : " + employee_name, end="\n", file=text_file)
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

# print("==============PAYSLIP==============", end="\n\n")
# print("======EMPLOYEE INFORMATION=======")
# print("Employee: " + employee_name, end="\n")
# print("Rendered Hours: ", rendered_hours, end="\n")
# print("Rate per Hour: ", rate_per_hour, end="\n")
# print("Gross Salary: ", gross_salary, end="\n\n")
# print("=============DEDUCTIONS===========", end="\n")
# print("SSS: ", sss_contribution, end="\n")
# print("PhilHealth: ", philhealth_contribution, end="\n")
# print("Loans: ", loans, end="\n")
# print("Tax: ", tax, end="\n")
# total_deductions = sss_contribution + philhealth_contribution + loans + tax
# print("Total Deductions: ", total_deductions, end="\n\n")
# print("==========NET SALARY===============", end="\n")
# print("Php. ", (gross_salary - total_deductions), end="\n")

# text_file = open("payslip.txt", "w")
# print("==============PAYSLIP==============", end="\n\n", file=text_file)
# print("======EMPLOYEE INFORMATION=======", file=text_file)
# print("Employee: " + employee_name, end="\n", file=text_file)
# print("Rendered Hours: ", rendered_hours, end="\n", file=text_file)
# print("Rate per Hour: ", rate_per_hour, end="\n", file=text_file)
# print("Gross Salary: ", gross_salary, end="\n\n", file=text_file)
# print("=============DEDUCTIONS===========", end="\n", file=text_file)
# print("SSS: ", sss_contribution, end="\n", file=text_file)
# print("PhilHealth: ", philhealth_contribution, end="\n", file=text_file)
# print("Loans: ", loans, end="\n", file=text_file)
# print("Tax: ", tax, end="\n", file=text_file)
# total_deductions = sss_contribution + philhealth_contribution + loans + tax
# print("Total Deductions: ", total_deductions, end="\n\n", file=text_file)
# print("==========NET SALARY===============", end="\n", file=text_file)
# print("Php. ", (gross_salary - total_deductions), end="\n", file=text_file)
# text_file.close();
