import pandas as pd

class Statistics_List:
    def __init__(self, df):
        self.df = df
        
    def list_unique_values(self, field):
        """
        List all unique values in a specified field of the dataset.

        :param field: The field name whose unique values are to be listed.
        :return: A set of unique values in the specified field.
        """
        
        unique_values = set()
        for record in self.df[field]:
            if record not in unique_values:
                unique_values.add(record)
        return unique_values
        
    def count_value_occurrences(self, list_to_count, field):
        """
        Count how many times each value occurs in a specified field of a dataset.

        :param data: A list of dictionaries representing the dataset.
        :param field: The field name for which to count the occurrences.
        :return: A dictionary with values as keys and their occurrence counts as values.
        """
        value_counts = {}
        for list in list_to_count:
            value_counts[list] = 1
            for record in self.df[field]:
                if list == record:
                    value_counts[list] += 1
        return value_counts


# how many nulls
# total unique and recrod count
# how many active/closed
    
# """
# Detect outliers in a specified numerical column using Z-scores.
# - Parameter column: The column to check for outliers.
# - Flags rows where the column's value is an outlier (Z-score > 3).
# """
# if self.df[column].dtype in ['int64', 'float64']:
#     from scipy import stats
#     outliers = self.df[(np.abs(stats.zscore(self.df[column])) > 3)]
#     if not outliers.empty:
#         print("Outliers found in {}:\n".format(column), outliers)
