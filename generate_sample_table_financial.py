import pandas as pd
import random
from datetime import datetime, timedelta
import generate_tables_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Finance List for Support Functions               ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

dict_finance_types = {
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

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Financial Functions for Generator               ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Generate the Financial Account field
def generate_tax_account_field(num_records, len_id_char = 7):
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




#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Financial Table                    ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_finance_build(dict, num_records):  
      dict['Tax Account'] = generate_tax_account_field(num_records)
      #dict['Sec ID'] =
      #dict['CUSIP'] = DIV or INT
      #dict['Entry CD'] =
      #dict['Currency'] =
      #dict[''] =
      #dict[''] =
      #dict['Net Amount'] =
      #dict['Withholding Amount'] = 
      #dict['Credit and Debit'] =
      #dict['Finance Type'] = 
      #dict['Finance Definition'] = 
      #dict['Transaction Date'] =
      return dict

def generate_table_tax(min_rand_record_lim = 1, max_rand_record_lim = 100000):
      finance_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
      finance_data = gtsf.table_generate_id_records(finance_num_records)
      finance_data = generate_table_finance_build(finance_data, finance_num_records)
      return finance_data

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

finance_df = pd.DataFrame(generate_table_tax(1,10))
finance_df.to_csv("data archive/tax data.csv", index=False)
print(finance_df)