import pandas as pd
import os
import sys

class FilePreCheck:

    def __init__(self, path, filename, filetype):
        self.file_path = path
        self.file_name = filename
        self.file_type = filetype

    # Check if file exist in L, if it is not, code operation halts and reports the file is missing.
    def file_exist_precheck(self):
        test = True if os.path.exists(os.path.join(self.file_path, self.file_name + self.file_type)) else False
        if not test:
            sys.exit('''
            File not present, inspect situation for the following:
            
            1) Check file is present in designated pathway
            2) Check file name entered matches file name in directory
            2) Check ... (further instructions based on database infrastructure)
            ''')

    # Check if desired fields exist from the file, if they do not, code operation halts and reports
    # the missing fields.
    def fields_exist_precheck(self, fields):
        df = pd.read_excel(os.path.join(self.file_path, self.file_name + self.file_type))
        missing_fields = []
        proceed = 'Y'
        for i in fields:
            if i not in df.columns:
                missing_fields.append(i)
                proceed = 'N'

        if proceed == 'N':
            sys.exit(f'Code terminated due to missing fields: {missing_fields}')


class FilePostCheck:

    def __init__(self, df):
        self.df = df

    # Check the row count and unique ID count of the file
    # In this example, four statistics are examined
    #   1st: if the unique ID (IDs after removing duplicates) are above a minimum threshold
    #   2nd: if the unique ID (IDs after removing duplicates) are below a maximum threshold
    #   3rd: if the row count is above a minimum threshold
    #   4th: f the row count is below a maximum threshold
    #
    # The ID check for this example designates conditions as 10 unique IDs minimum threshold,
    # 500000 unique IDs maximum threshold, 500000 rows maximum threshold and 10 rows minimum threshold

    def id_numbers(self, id_col):
        ids = self.df[id_col].tolist()
        # ---Low Unique ID Threshold---
        threshold_low_id = 10
        unique_ids = list(set(ids))
        count_ids = len(unique_ids)
        if count_ids < threshold_low_id:
            print(f'''
            Flag: Unique ID count below minimum threshold!
            
            Review data source acquisition for missing data.
            ''')
        # ---High Unique ID Threshold---
        threshold_high_id = 500000
        unique_ids = list(set(ids))
        count_ids = len(unique_ids)
        if count_ids > threshold_high_id:
            print(f'''
            Flag: Unique ID count above maximum threshold!

            Review data source acquisition for missing data.
            ''')
        # ---High Row Count Threshold---
        threshold_high_row = 500000
        row_count = len(ids)
        if row_count > threshold_high_row:
            print(f'''
            Flag: Data row count above maximum threshold!
            
            Review data source acquisition for unnecessary or incorrect information
            ''')
        # ---Low Row Count Threshold---
        threshold_low_row = 10
        row_count = len(ids)
        if row_count < threshold_low_row:
            print(f'''
            Flag: Data row count below minimum threshold!

            Review data source acquisition for unnecessary or incorrect information
            ''')
    # Check the ACTIVE/CLOSED account statistics.
    # In this example, two statistics are examined
    #   1st: if number of ACTIVE accounts are below a standard number
    #   2nd: ratio of ACTIVE accounts vs CLOSED accounts exceed a standard value
    #
    # The ID check for this example designates the ACTIVE 1st condition as 10 accounts
    # and the ratio 2nd condition as 1

    def active_ids(self, id_col, active_col):
        act_threshold = 10
        df_ids = self.df[[id_col, active_col]]
        df_ids[active_col].str.upper()
        df_act_ids = df_ids[df_ids[active_col] == 'ACTIVE']
        count_act_ids = len(df_act_ids)
        df_cld_ids = df_ids[df_ids[active_col] == 'CLOSED']
        count_cld_ids = len(df_cld_ids)
        act_ratio = count_act_ids/count_cld_ids
        if count_act_ids < act_threshold:
            print('''
            Flag: Active IDs below minimum threshold.
            
            Review data source acquisition for Active ID population.
            ''')
        elif act_ratio < 1:
            print('''
            Flag: Closed IDs exceed Active IDs.
            
            Review data source acquisition for ID population.
            ''')

    # Check if the ID structure matches the regulation requirements.
    # In this example, the ID is made up of 10 characters
    #   1st: character = branch division
    #   2nd-4th: characters = branch type
    #   5th-10th: characters = unique id identity
    #
    # The ID check for this example checks if the branch division is a number, branch type are letters, the
    # id identity are numbers and the total length is 10 characters.
    def id_integrity(self, id_col):
        df_ids = self.df[id_col].tolist()
        flag_branch_d = []
        flag_branch_t = []
        flag_branch_i = []

        for i in df_ids:
            i = str(i)
            branch_d = i[0]
            branch_type = i[1:4]
            id_identity = i[5:10]

            if not branch_d.isdigit():
                flag_branch_d.append(i)

            for n in branch_type:
                if n.isdigit():
                    flag_branch_t.append(i)
                    break

            for m in id_identity:
                if n.isdigit():
                    flag_branch_i.append(i)
                    break

        if flag_branch_d:
            count_branch_d = len(flag_branch_d)
            print(f'''
            Flagged Branch Divisions: {flag_branch_d}
            
            Total Accounts: {count_branch_d}
            ''')

        if flag_branch_t:
            count_branch_t = len(flag_branch_t)
            print(f'''
            Flagged Branch Types: {flag_branch_t}

            Total Accounts: {count_branch_t}
            ''')

        if flag_branch_i:
            count_branch_i = len(flag_branch_i)
            print(f'''
            Flagged Branch Divisions: {flag_branch_i}

            Total Accounts: {count_branch_i}
            ''')
