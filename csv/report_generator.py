
import csv
from email.policy import strict

def reading_data(file_location):
    employee_list = []

    read_csv = csv.DictReader(open(file_location))
        
    for row in read_csv:
        employee_list.append(row)

    return employee_list

def counting_employees_of_each_depart(employee_lst):
    departments = []
    emps_department_wise = {}

    for item in employee_lst:
        departments.append(item[" Department"])

    for item in employee_lst:
        if item[" Department"] not in emps_department_wise:
            emps_department_wise[item[" Department"]] = []
        emps_department_wise[item[" Department"]].append(item["Full Name"])

    for item in emps_department_wise:
        emps_department_wise[item].append(len(emps_department_wise[item]))

    return emps_department_wise
    
    
data_dictionary = counting_employees_of_each_depart(reading_data("D:\\pip main\\csv\\employee.csv"))
        
def generate_report(dictionary):
    heads = list(dictionary.keys())
    with open("report.csv", "w+") as file:
        write_csv = csv.DictWriter(file, fieldnames=heads)
        write_csv.writeheader()
        write_csv.writerows(dictionary)

generate_report(data_dictionary)
