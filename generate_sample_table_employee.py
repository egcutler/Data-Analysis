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
              'Supply Chain Coordinator','Quality Assurance Tester'
]

dict_jobs = {
'Business Analyst' : ['Operations Manager', 'Project Manager'],
'Data Engineer' : ['Operations Manager', 'Project Manager', 'Engineer Manager'],
'Data Analyst' : ['Operations Manager', 'Project Manager'],
'Dev Ops Engineer' : ['Operations Manager', 'Project Manager'],
'Financial Analyst' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Finance manager', ''],
'IT Specialist' : ['IT Manager'],
'Engineer Specialist' : ['Engineer Manager'],
'Sales and Stragety' : ['Sales Manager'],
'Supply Chain Coordinator' : ['Project Manager', 'Product Manager'],
'Quality Assurance Tester' : ['Project Manager', 'Product Manager'],
'Web Developer' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Marketing Manager', ''],
'Social Media Specialist' : ['Marketing Manager'],
'Customer Service Representative' : ['Customer Success Manager'],
'Human Resources' : ['Human Resources Manager'],
'Administrative Assistant' : ['IT Manager'],
'Legal Assistant' : ['Legal Manager'],
'Software Engineer' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Engineer Manager', ''],
'Graphic Designer' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Engineer Manager', ''],
'Sales Representative' : ['Sales Manager'],
'Research Scientist' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Marketing Manager', 'Engineer Manager'],
'Accountant' : ['Finance manager']  
}


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
      job_titles = list(dict_jobs.keys())
      for _ in range(num_records):
            dict_list.append(random.choice(job_titles))
      return dict_list

# Generate the Employee Email field
def generate_emp_email_field(num_records, first_name, last_name):
      dict_list = []
      for x in range(num_records):
            dict_list.append(f'{last_name[x]}.{first_name[x]}@fakemail.com')
      return dict_list

# Generate the Employee Status field
def generate_emp_status_field(num_records, weightY = 90, weightN = 10):
      dict_list = []
      status_list = ['EMPLOYEED', 'TERMINATED']
      weight_list = [weightY, weightN]
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_weighted_string_list(status_list, weight_list))
      return dict_list

# Generate the Employee Hire Date field
def generate_emp_hire_date_field(num_records, min_date = datetime(1990,1,1), max_date = datetime.now()):
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Employee Termination field
def generate_emp_termination_field(num_records, status_list, hire_date_list, max_date = datetime.now()):
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            if status_list[x] == 'TERMINATED':
                  dict_list.append(gtsf.generate_date(hire_date_list[x], max_date))
            else:
                  dict_list.append(None)
      return dict_list

# Generate the Employee Manager First name Field
def generate_emp_manager_fields(num_records, emp_first_name, emp_last_name, emp_job_title_list):
      dict_list_firstname = []
      dict_list_lastname = []
      dict_list_manager = []
      
      for x in range(num_records):
            mang_first_name = random.choice(first_names)
            while mang_first_name == emp_first_name[x]:
                  mang_first_name = random.choice(first_names)        
            dict_list_firstname.append(mang_first_name)
            
            mang_last_name = random.choice(last_names)
            while mang_last_name == emp_last_name[x]:
                  mang_last_name = random.choice(last_names)        
            dict_list_lastname.append(mang_last_name)
            
            dict_list_manager.append(random.choice(dict_jobs[emp_job_title_list[x]]))
            
      return dict_list_firstname, dict_list_lastname, dict_list_manager

# Generate the Employee Manager Security Clearance field
def generate_emp_security_clearance_field(num_records, min = 1, max = 5):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
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
      dict['Employee Email'] = generate_emp_email_field(num_records, dict['Emp First Name'], dict['Emp Last Name'])
      dict['Employee Status'] = generate_emp_status_field(num_records)
      dict['Hire Date'] = generate_emp_hire_date_field(num_records)
      dict['Termination Date'] = generate_emp_termination_field(num_records, dict['Employee Status'], dict['Hire Date'])
      dict['Manager First Name'], dict['Manager Last Name'], dict['Manager Position'] = generate_emp_manager_fields(num_records, dict['Emp First Name'], dict['Emp Last Name'], dict['Job Title'])
      dict['Security Clearance'] = generate_emp_security_clearance_field(num_records)

      
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

count_temp = 0
