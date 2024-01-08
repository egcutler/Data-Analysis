import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Tax List for Support Functions                   ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

dict_tax_types = {
      'ADJ' : 'Adjustment',
      'BEN/BENF' : 'Benefit(s)',
      'LTI' : 'Loan to Income',
      'IHT' : 'Inheritance Tax',
      'CAR' : 'Centralized Accounts Receivable',
      'FoF' : 'Fund of Funds',
      'CWP' : 'Conventional With Profits',
      'ADMIS' : 'Admission',
      'C+MV' : 'Cost Plus Market Value',
      'Q1' : 'First quarter of the year',
      'A/R' : 'Accounts Receivable',
      'WPA' : 'With Profits Actuary / With Profits Annuity',
      'NBV' : 'Net Book Value',
      'APC/APD' : 'Amended Payroll Certification/Distribution',
      'B & C' : 'Bonds And Coupons',
      'WPICC' : 'With Profits Insurance Capital Component',
      'VaR' : 'Value at Risk',
      'EC' : 'European Commission',
      'TV' : 'Transfer Value',
      'Q4' : 'Fourth quarter of the year',
      'ADDL' : 'Additional',
      'CTF' : 'Child Trust Fund',
      'CESR' : 'Committee of European Securities Regulators',
      'CIMPS' : 'Contracted-in Money Purchase Scheme',
      'CDS' : 'Credit Default Swap',
      'C/S' : 'Cost Sharing',
      'AFFRS' : 'Affairs',
      'AFD' : 'Allowance For Depreciation',
      'DGI' : 'Domestically Generated Inflation',
      'ABS' : 'Absences - As In Compensated Absences',
      'OMO' : 'Open Market Option',
      'PBT' : 'Profit before Taxes',
      'MBO' : 'Management Buy Out',
      'RCM' : 'Risk Capital Margin',
      'CAP.' : 'Capital',
      'ETF' : 'Exchange Traded Funds',
      'MBI' : 'Management Buy In',
      'BA' : 'Bank Adjustments',
      'ADT' : 'Auditing',
      'EBT' : 'Earnings Before Taxes',
      'PV' : 'Present Value',
      'RoC' : 'Return on Capital',
      'Q3' : 'Third quarter of the year',
      'PAT' : 'Profit after Taxes',
      'APPROP' : 'Appropriations',
      'COMPS' : 'Contracted-out Money Purchase Scheme',
      'ABACCR' : 'Absences Accrual - (As In Compensated Absences Accrual)',
      'CT' : 'Corporation Tax',
      'FoHF' : 'Fund of Hedge Funds',
      'UHNW' : 'Ultra High Net Worth',
      'FTT' : 'Financial Transaction Tax',
      'WoM' : 'Whole of Market',
      'NAV' : 'Net Asset Value',
      'Q2' : 'Second quarter of the year',
      'AID' : 'Agency For International Development',
      'ADMIN' : 'Administrative'
}

list_entrycd = [
      'DIV', 'INT'
]

list_cur = [
      'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'
]

list_debit_and_credit = ['Debit','Credit']
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Tax Functions for Generator                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Generate the Tax Account field
def generate_tax_account_field(num_records, len_id_char = 8):
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

# Generate the Tax Security ID field
def generate_tax_sec_id_field(num_records, min = 100000, max = 9999999):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Tax CUSIP field
def generate_tax_cusip_field(num_records, len_id_char = 7):
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

# Generate the Tax Entry CD field
def generate_tax_entrycd_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(list_entrycd))
      return dict_list

# Generate the Tax Currency field
def generate_address_original_country_field(num_records, priority_item = 'USD', weight_usd = 10, weight_oth = 1):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_unique_weighted_list(list_cur, priority_item, weight_usd, weight_oth))
      return dict_list

# Generate the Tax Net Amount field
def generate_tax_net_amount_field(num_records, min = 1, max = 99999):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Tax Withholding Amount field
def generate_tax_withholding_amount_field(num_records, min = 1, max = 9999):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Tax Debit and Credit field
def generate_tax_debit_and_credit_field(num_records):
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(list_debit_and_credit))
      return dict_list

# Generate the Tax Type field
def generate_tax_type_field(num_records):
      dict_list = []
      tax_types = list(dict_tax_types.keys())
      for _ in range(num_records):
            dict_list.append(random.choice(tax_types))
      return dict_list

# Generate the Tax Type Description field
def generate_tax_type_desc_field(num_records, tax_type_list):
      dict_list = []
      for x in range(num_records):
            dict_list.append(dict_tax_types[tax_type_list[x]])
      return dict_list

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Tax Table                          ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_tax_build(dict, num_records):  
      dict['Tax Account'] = generate_tax_account_field(num_records)
      dict['Sec ID'] = generate_tax_sec_id_field(num_records)
      dict['CUSIP'] = generate_tax_cusip_field(num_records)
      dict['Entry CD'] = generate_tax_entrycd_field(num_records)
      dict['Currency'] = generate_address_original_country_field(num_records)
      dict['Net Amount'] = generate_tax_net_amount_field(num_records)
      dict['Withholding Amount'] = generate_tax_withholding_amount_field(num_records)
      dict['Credit and Debit'] = generate_tax_debit_and_credit_field(num_records)
      dict['Tax Type'] = generate_tax_type_field(num_records)
      dict['Tax Type Definition'] = generate_tax_type_desc_field(num_records, dict['Tax Type'])
      #dict['Transaction Date'] =
      return dict

def generate_table_tax(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      tax_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      tax_data = gtsf.table_generate_id_records(tax_num_records)
      tax_data = generate_table_tax_build(tax_data, tax_num_records)
      return tax_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

tax_df = pd.DataFrame(generate_table_tax(1,100))
tax_df.to_csv("data archive/tax data.csv", index=False)
print(tax_df)