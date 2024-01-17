# This class is designed to perform pre-checks on a file to 
# ensure its existence and verify certain fields.

import pandas as pd
from pathlib import Path


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                   ----                                  --------------
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


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    -----                                 --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


class FilePreCheck:
      def __init__(self, path, filename, filetype):
            """
            Initialize the FilePreCheck object.
            -Parameter path: Path to the file directory.
            -Parameter filename: Name of the file.
            -Parameter filetype: Extension of the file.
            """
            self.file_path = Path(path)
            self.file_name = filename
            self.file_type = filetype
            
      def file_exist_precheck(self):
            """
            Check if the file exists. If not, raise an exception.
            """
            
            full_path = self.file_path / f"{self.file_name}{self.file_type}"
            if not full_path.exists():
                  raise FileNotFoundError(f'''
                  ...File existance check: Failed
                  
                  Please check the following:
                  
                  1) File is in {self.file_path}
                  2) File name is correct
                  3) File extension is correct
                  4) No additional spaces are at the end of the file path or name
                  ''')
            else:
                  print('...File existance check: Passed')


      def fields_exist_precheck(self, fields):
            """
            Check if desired fields exist in the file.
            -Parameter fields: List of fields to check.
            """
            # Lowercase the file extension for consistency
            file_extension = self.file_type.lower()

            # Mapping of file types to pandas read functions
            read_functions = {
                  'excel'                 : pd.read_excel,
                  'Excel'                 : pd.read_excel,
                  '.xlsx'                 : pd.read_excel,
                  'xlsx'                  : pd.read_excel,
                  'Comma-Separated Values': pd.read_csv,
                  'Comma Separated Values': pd.read_csv,
                  'Comma-Separated Value' : pd.read_csv,
                  'Comma Separated Value' : pd.read_csv,
                  '.csv'                  : pd.read_csv,
                  'csv'                   : pd.read_csv,
                  'JavaScript'            : pd.read_json,
                  '.json'                 : pd.read_json,
                  'json'                  : pd.read_json
            }
            
            # Determine the file type based on extension
            file_type = file_types.get(file_extension, 'Unsupported')
            
            # Get the appropriate read function
            read_func = read_functions.get(file_type)

            # Construct the full file path
            full_path = self.file_path / f"{self.file_name}{self.file_type}"

            # Check if the function exists and read the file
            if read_func:
                  df = read_func(full_path)
                  missing_fields = [field for field in fields if field not in df.columns]
                  if missing_fields:
                        raise ValueError(f'Code terminated due to missing fields: {missing_fields}')
                  else:
                        print('...Field(s) check: Passed')
            else:
                  raise ValueError(f"Unsupported file type: {file_type}")
 
      