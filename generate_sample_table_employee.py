import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Employee List for Support Functions              ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Expanded lists of first and last names
first_names = ["John", "Jane", "Alex", "Emily", "David", "Sarah", "Michael", "Olivia", 
               "Daniel", "Emma", "Chris", "Anna", "James", "Sophia", "Robert", "Isabella", 
               "William", "Mia", "Joseph", "Amelia", "Richard", "Evelyn", "Charles", 
               "Abigail", "Thomas", "Harper", "Mary", "Ethan", "Jessica", "Benjamin"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", 
              "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", 
              "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
              "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", 
              "Walker", "Perez", "Hall"]

job_titles = ['Software Engineer','Marketing Manager','Sales Representative',
              'Graphic Designer','Data Analyst','Human Resources Manager',
              'Project Manager','Accountant','Customer Service Representative',
              'Operations Manager','Product Manager','Business Analyst','Web Developer',
              'Social Media Specialist','Data Engineer','Administrative Assistant',
              'Financial Analyst','IT Specialist','Legal Assistant','Research Scientist',
              'Supply Chain Coordinator','Quality Assurance Tester',
]

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Employee Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Generate the Employee ID field
def generate_emp_id_field(num_records, len_id_char = 7):
      dict_list = []
      if type(len_id_char) == str:
            if len_id_char.isdigit():
                  zeros_req = int(len_id_char)-1
            else:
                  return Exception(f'Cannot convert the numeric string to a numeric value: {len_id_char}')
      else:
            zeros_req = len_id_char - 1
            
      zeros = "0" * zeros_req
      min = int("1"+zeros)
      max = int("9"*len_id_char) 
      for _ in range(num_records):
            dict_list.append(random.randint(min, max))
      return dict_list

# Generate the Employee First Name field
def generate_emp_first_name_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(first_names))
      return dict_list

# Generate the Employee First Name field
def generate_emp_last_name_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(last_names))
      return dict_list

# Generate the Employee Phone Number field
def generate_emp_phone_number_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_phone_number())
      return dict_list

# Generate the Employee Job Title field
def generate_emp_job_title_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(job_titles))
      return dict_list



#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Employee Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_employee_build(dict, num_records):  
      
      dict['Employee ID'] = generate_emp_id_field(num_records)
      dict['Emp First Name'] = generate_emp_first_name_field(num_records)
      dict['Emp Last Name'] = generate_emp_last_name_field(num_records)
      dict['Emp Phone Number'] = generate_emp_phone_number_field(num_records)
      dict['Job Title'] = generate_emp_job_title_field(num_records)
      
      return dict

def generate_table_employee(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      emp_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      emp_data = gtsf.table_generate_id_records(emp_num_records)
      emp_data = generate_table_employee_build(emp_data, emp_num_records)
      return emp_data


#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

emp_df = pd.DataFrame(generate_table_employee())
emp_df.to_csv("data archive/employee data.csv", index=False)
print(emp_df)