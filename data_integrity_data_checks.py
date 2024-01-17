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

    def id_unique_count_thresholds(self, id_col, threshold_low_id=10, threshold_high_id=500000, threshold_low_row=10, threshold_high_row=500000):
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

        # Check against low unique ID threshold
        if count_distinct_ids < threshold_low_id:
            print(f'Warning: Distinct ID count below minimum threshold ({threshold_low_id})!')

        # Check against high unique ID threshold
        if count_distinct_ids > threshold_high_id:
            print(f'Warning: Distinct ID count above maximum threshold ({threshold_high_id})!')

        # Check against high row count threshold
        if record_count > threshold_high_row:
            print(f'Warning: Record count above maximum threshold ({threshold_high_row})!')

        # Check against low row count threshold
        if record_count < threshold_low_row:
            print(f'Warning: Record count below minimum threshold ({threshold_low_row})!')
