import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Support Dictionaries and List                            --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Classes                                             --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

class Clean_Data:
    def __init__(self, df):
        """
        Initialize the Clean_Data class with a pandas DataFrame.

        :param df: pandas DataFrame to be cleaned
        """
        self.df = df

    def drop_missing_rows(self):
        """
        Drop rows with any missing values in the DataFrame.
        """
        self.df.dropna(inplace=True)

    def replace_missing_with_zero(self):
        """
        Replace missing values in the DataFrame with 0.
        """
        self.df.fillna(0, inplace=True)

    def remove_duplicates(self):
        """
        Remove duplicate rows from the DataFrame.
        """
        self.df.drop_duplicates(inplace=True)

    def replace_missing_with_value(self, value, field_name):
        """
        Replace missing values in a specified column with a given value.

        :param value: Value to replace missing values with
        :param field_name: Column in which to replace missing values
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        self.df[field_name].fillna(value, inplace=True)

    def replace_missing_with_stats(self, field_name):
        """
        Replace missing values in a specified numerical column with the column's mean.

        :param field_name: Column in which to replace missing values with mean
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.df[field_name]):
            raise ValueError(f"Field '{field_name}' is not numeric and cannot use mean for replacement.")
        self.df[field_name].fillna(self.df[field_name].mean(), inplace=True)

    def convert_datatype_column(self, field_name, datatype):
        """
        Convert the data type of a specified column.

        :param field_name: Column to convert
        :param datatype: Target data type
        """
        self.df[field_name] = self.df[field_name].astype(datatype)

    def rename_column(self, old_field_name, new_field_name):
        """
        Rename a column in the DataFrame.

        :param old_field_name: Current name of the column
        :param new_field_name: New name for the column
        """
        self.df.rename(columns={old_field_name: new_field_name}, inplace=True)

    def replace_inf_values(self, value):
        """
        Replace infinite values in the DataFrame with a specified value.

        :param value: Value to replace infinite values with
        """
        self.df.replace([np.inf, -np.inf], value, inplace=True)

    def remove_whitespaces(self, field_name):
        """
        Strip leading and trailing whitespaces from a string column.

        :param field_name: String column to remove whitespaces from
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        if not pd.api.types.is_string_dtype(self.df[field_name]):
            raise ValueError(f"Field '{field_name}' is not a string type.")
        self.df[field_name] = self.df[field_name].str.strip()

    def convert_column_lowercase(self, field_name):
        """
        Convert all characters in a string column to lowercase.

        :param field_name: String column to convert to lowercase
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        self.df[field_name] = self.df[field_name].str.lower()

    def convert_column_uppercase(self, field_name):
        """
        Convert all characters in a string column to uppercase.

        :param field_name: String column to convert to uppercase
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        self.df[field_name] = self.df[field_name].str.upper()

    def remove_outliers_column_threshold(self, field_name, threshold_lower, threshold_upper):
        """
        Remove outliers from a numerical column based on specified lower and upper thresholds.

        :param field_name: Column from which to remove outliers
        :param threshold_lower: Lower threshold for outlier removal
        :param threshold_upper: Upper threshold for outlier removal
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.df[field_name]):
            raise ValueError(f"Field '{field_name}' is not numeric and cannot be used for outlier removal.")
        self.df = self.df[(self.df[field_name] >= threshold_lower) & (self.df[field_name] <= threshold_upper)]