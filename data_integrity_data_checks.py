# ----------
import pandas as pd
from pathlib import Path

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Support Dictionaries and List                            --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# ----
file_types = {
    ".xlsx": ["Excel Workbook", "Excel"],
    ".xls": "Excel Spreadsheet (Legacy)",
    ".docx": "Word Document",
    ".doc": "Word Document (Legacy)",
    ".pptx": "PowerPoint Presentation",
    ".ppt": "PowerPoint Presentation (Legacy)",
    ".pdf": "Portable Document Format",
    ".txt": "Text File",
    ".csv": "Comma-Separated Values",
    ".json": "JavaScript Object Notation",
    ".xml": "eXtensible Markup Language",
    ".html": "HyperText Markup Language",
    ".js": "JavaScript File",
    ".py": "Python Script",
    ".java": "Java Source File",
    ".c": "C Source File",
    ".cpp": "C++ Source File",
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".png": "Portable Network Graphics",
    ".gif": "Graphics Interchange Format",
    ".bmp": "Bitmap Image File",
    ".mp3": "MP3 Audio File",
    ".wav": "WAVE Audio File",
    ".mp4": "MPEG-4 Video File",
    ".avi": "Audio Video Interleave File",
    ".mov": "Apple QuickTime Movie",
    ".zip": "ZIP Archive",
    ".rar": "RAR Archive",
    ".7z": "7-Zip Archive"
}

# Mapping of file types to pandas read functions
file_types_pd = {
      'excel'                 : pd.read_excel,
      'Excel'                 : pd.read_excel,
      '.xlsx'                 : pd.read_excel,
      'xlsx'                  : pd.read_excel,
      'Comma-Separated Values': pd.read_csv,
      'JavaScript'            : pd.read_json,
      '.json'                 : pd.read_json,
      'json'                  : pd.read_json
}


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Classes                                             --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


class Data_Check:

      def __init__(self, df):
            """
            Initialize the FilePostCheck object with a DataFrame.
            - Parameter df: The DataFrame to be checked.
            """
            self.df = df

      def id_unique_count_thresholds(self, id_col, threshold_low_id=10, threshold_high_id=500000, \
                                     threshold_low_row=10, threshold_high_row=500000):
            """
            Check the row count and unique ID count of the DataFrame.
            Flags are raised if the counts are outside the specified thresholds.
            - Parameter id_col: Column name of the ID in the DataFrame.
            - Parameter threshold_low_id: Minimum threshold for distinct ID count (default 10).
            - Parameter threshold_high_id: Maximum threshold for distinct ID count (default 500000).
            - Parameter threshold_low_row: Minimum threshold for record (row) count (default 10).
            - Parameter threshold_high_row: Maximum threshold for record (row) count (default 500000).
            """
            ids = self.df[id_col].tolist()
            unique_ids = set(ids)
            count_distinct_ids = len(unique_ids)
            record_count = len(ids)
            flag_count = 0

            # Check against low unique ID threshold
            if count_distinct_ids < threshold_low_id:
                  print(f'Warning: Distinct ID count {count_distinct_ids} is below minimum threshold ({threshold_low_id})!')
                  flag_count += 1
            # Check against high unique ID threshold
            if count_distinct_ids > threshold_high_id:
                  print(f'Warning: Distinct ID count {count_distinct_ids} is above maximum threshold ({threshold_high_id})!')
                  flag_count += 1
            # Check against high row count threshold
            if record_count > threshold_high_row:
                  print(f'Warning: Record count {record_count} is above maximum threshold ({threshold_high_row})!')
                  flag_count += 1
            # Check against low row count threshold
            if record_count < threshold_low_row:
                  print(f'Warning: Record count {record_count} is below minimum threshold ({threshold_low_row})!')
                  flag_count += 1
            # Passed/Failed message    
            if flag_count == 0:
                  print("...ID threshold check: Passed")
            else:
                  print(f"...{flag_count} ID threshold warnings triggered")
                  print(f"   Distinct ID count: {count_distinct_ids}")
                  print(f"   Record count: {record_count}")

      def active_ids(self, id_col, status_col, min_act_threshold=10, max_cld_threshold = 500000, \
                     act_ratio_threshold=0.5, cld_ratio_threshold=0.1):
            """
            Check the ACTIVE/CLOSED account statistics in the DataFrame.
            Flags are raised if the number of active accounts is below a specified threshold
            or if the ratio of ACTIVE to CLOSED accounts falls below another specified threshold.
            - Parameter id_col: Column name of the ID in the DataFrame.
            - Parameter status_col: Column name of the account status (ACTIVE/CLOSED).
            - Parameter act_threshold: Minimum number of active accounts threshold (default 10).
            - Parameter act_ratio_threshold: Minimum ratio of ACTIVE to CLOSED accounts (default 1).
            """
            # Creating a DataFrame with only ID and Active Columns
            df_ids = self.df[[id_col, status_col]]

            # Count Active and Closed IDs
            count_act_ids = df_ids[status_col].str.upper().eq('ACTIVE').sum()
            count_cld_ids = df_ids[status_col].str.upper().eq('CLOSED').sum()
            count_id_tot = len(df_ids[status_col])

            # Calculate the ratio of ACTIVE to CLOSED accounts
            act_ratio = count_act_ids / count_id_tot if count_id_tot != 0 else float('inf')
            cld_ratio = count_act_ids / count_id_tot if count_id_tot != 0 else float('inf')

            flag_count = 0
            # Check against active account threshold
            if count_act_ids < min_act_threshold:
                  print(f'FlWarningag: Active IDs below minimum threshold ({min_act_threshold})!')
                  flag_count += 1
            if count_cld_ids > max_cld_threshold:
                  print(f'Warning: Closed IDs above maximum threshold ({max_cld_threshold})!')
                  flag_count += 1
            # Check against active to total ratio threshold
            elif act_ratio < act_ratio_threshold:
                  print(f'Warning: Ratio of Active to Total IDs ({act_ratio:.2f}) is below threshold ({act_ratio_threshold})!')
                  flag_count += 1
            # Check against active to total ratio threshold
            elif cld_ratio < cld_ratio_threshold:
                  print(f'Warning: Ratio of Active to Total IDs ({act_ratio:.2f}) is below threshold ({act_ratio_threshold})!')
                  flag_count += 1
            # Passed/Failed message    
            if flag_count == 0:
                  print("...Active/Closed threshold checks: Passed")
            else:
                  print(f"...{flag_count} Active/Closed threshold warnings triggered")
                  print(f"   Active status count: {count_act_ids}")
                  print(f"   Closed status count: {count_cld_ids}")
                  print(f"   Total status count: {count_id_tot}")

      def null_check(self, null_threshold = 100):
            """
            Check for null values in the DataFrame.
            - Flags fields that are entirely null.
            - Flags fields where the count of null values exceeds the specified threshold.
            - Parameter null_threshold: Threshold for the acceptable count of null values in a field.
            """
            # Check for columns that are entirely null
            all_null_columns = self.df.columns[self.df.isnull().all()]

            if len(all_null_columns) > 0:
                  print(f'Fields entirely null: {list(all_null_columns)}')
            # Check for columns where null count exceeds the threshold
            flag_count = 0
            for column in self.df.columns:
                  null_count = self.df[column].isnull().sum()
                  if null_count > null_threshold:
                        print(f'Warning: field {column} has a null count of {null_count}, exceeding threshold {null_threshold}!')
                        flag_count += 1
            if flag_count > 0:
                  print(f"...{flag_count} null column threshold warnings triggered")

      def check_duplicate_rows(self):
            """
            Identify duplicate rows in the DataFrame.
            - Flags entire rows that are duplicates.
            """
            duplicates = self.df[self.df.duplicated()]
            if not duplicates.empty:
                  print("Duplicate rows found:\n", duplicates)
                  

      # Example of expected_type format:            
      # expected_types = {
      #     'column1 name': str,             # expecting column1 to contain strings
      #     'column2 name': int,             # expecting column2 to contain integers
      #     'column3 name': float,           # expecting column3 to contain floating point numbers
      #     'column4 name': bool,            # expecting column4 to contain boolean values
      #      etc.
      # }
      def validate_data_types(self, expected_types):
            """
            Ensure that each column contains data of the expected type.
            - Parameter expected_types: Dictionary with column names as keys and expected data types as values.
            - Flags columns with unexpected data types.
            """
            
            for column, expected_type in expected_types.items():
                  # Method with dropna used to remove missing (NA/null) values from a Series or DataFrame.
                  # -Important for data type validation because missing values don't have a data type in the 
                  #  traditional sense and can lead to incorrect type checking results.
                  # -isinstance() is used to check if the object (x) is an instance of a the class 
                  #  (expected_type in this case) for checking the data type. Returns True/False.
                  # -all() checks if all the elements in the iterable are True.
                  if not all(isinstance(x, expected_type) for x in self.df[column].dropna()):
                        print(f"Data type issue in column: {column}")

                        
      def validate_data_range(self, column, min_val, max_val):
            """
            Ensure that values in a column fall within a specified range.
            - Parameter column: The column to check.
            - Parameter min_val: Minimum acceptable value.
            - Parameter max_val: Maximum acceptable value.
            - Flags values outside the specified range.
            """
            if self.df[column].dtype in ['int64', 'float64']:
                  if not self.df[(self.df[column] < min_val) | (self.df[column] > max_val)].empty:
                        print(f"Data range issue in column: {column}")



class Data_Check_String_Format:

      # email addresses, phone numbers, postal code
      def validate_string_pattern(self, column, pattern):
            import re
            if self.df[column].dtype == 'object':
                  if not all(re.match(pattern, str(x)) for x in self.df[column].dropna()):
                        print(f"String pattern issue in column: {column}")


      def validate_against_reference(self, column, reference_data):
            if not set(self.df[column]).issubset(set(reference_data)):
                  print(f"Reference data issue in column: {column}")

class Data_Check_Time_Series:


      def analyze_time_series(self, time_column):
            """
            Check for anomalies in time-series data.
            - Parameter time_column: The column containing time-series data.
            - Implement specific time series checks.
            """
            pass

class Data_Check_Correlations:
      def analyze_correlation(self):
            """
            Identify unexpected correlations between columns.
            - Computes and prints the correlation matrix of the DataFrame.
            """
            correlation_matrix = self.df.corr()
            print(correlation_matrix)