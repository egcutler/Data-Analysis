# This class is designed to perform pre-checks on a file to 
# ensure its existence and verify certain fields.

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
# --------------                    Files and Paths Classes                                 --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class FolderPreCheck:
      def __init__(self, path):
            """_summary_

            Args:
                path (_type_): _description_

            Raises:
                an: _description_
                FileNotFoundError: _description_
                ValueError: _description_
                ValueError: _description_
            """
            self.file_path = Path(path)
            
      def search_files_with_partial_name(self, partial_name, file_type):
            """
            Check if a file with a partial name exists in the specified path. Return a
            printed details for True/False conditions.
            """
            file_pattern = f"*{partial_name}*{file_type}"
            matching_files = list(self.file_path.glob(file_pattern))
            if len(matching_files) == 0:
                  print(f'''
                  No files found with:
                  -Pathway: "{self.file_path}"
                  -Partial Name: "{partial_name}"
                  ''')
            else:
                  print(f'''
                  {len(matching_files)} files found with: 
                  -Pathway "{self.file_path}"
                  -Partial name "{partial_name}"
                  
                  Found files:
                  {matching_files}
                  ''')
            
      def check_files_with_partial_name(self, partial_name, file_type):
            """
            Check if a file with a partial name exists in the specified path. Return
            a True/False value for parameter application
            """
            file_pattern = f"*{partial_name}*{file_type}"
            matching_files = list(self.file_path.glob(file_pattern))
            if len(matching_files) > 0:
                  print("...File check: Passed")
                  return matching_files
            else:
                  raise FileNotFoundError(f'''
                  ...File existance check: Failed
                  
                  Please check the following:
                  
                  1) File is in {self.file_path}
                  2) File name is correct, including:
                        a) Spelling
                        b) Case sensitivity
                        c) Additional spacing before or after name
                        d) Other grammar situations
                  3) File extension is correct
                  ''')


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
            if filetype.startswith("."):
                  self.file_type = filetype
            else:
                  self.file_type = "." + filetype
            
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
                  2) File name is correct, including:
                        a) Spelling
                        b) Case sensitivity
                        c) Additional spacing before or after name
                        d) Other grammar situations
                  3) File extension is correct
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
            # Determine the file type based on extension
            file_type = file_types.get(file_extension, 'Unsupported')
            # Get the appropriate read function
            read_func = file_types_pd.get(file_type)
            # Construct the full file path
            full_path = self.file_path / f"{self.file_name}{self.file_type}"
            # Check if the function exists and read the file
            if read_func:
                  df = read_func(full_path)
                  missing_fields = [field for field in fields if field not in df.columns]
                  if missing_fields:
                        raise ValueError(f'Code terminated due to missing fields: {missing_fields}')
                  else:
                        print('...Field(s) name check: Passed')
            else:
                  raise ValueError(f"Unsupported file type: {file_type}")
 
      # create another one to see if a field(s) exist where a given word is provided
      def search_fields_with_partialname(self, partial_name):
            """
            Search all field names in the dataset to see if the partial name is part of any of the fields.
            - Parameter partial_name: Partial name to search for in field names.
            - Returns: List of all matching field names.
            """
            # Lowercase the file extension for consistency
            file_extension = self.file_type.lower()
            # Determine the file type based on extension
            file_type = file_types.get(file_extension, 'Unsupported')
            # Get the appropriate read function
            read_func = file_types_pd.get(file_type)
            # Construct the full file path
            full_path = self.file_path / f"{self.file_name}{self.file_type}"
            # Check if the function exists and read the file
            if read_func:
                  df = read_func(full_path)
                  # Read the file and get the column names
                  field_names = df.columns
                  # Search for matches
                  matches = [field for field in field_names if partial_name in field]
                  if len(matches) > 0:
                        print(f'''
                              {len(matches)} matches found:
                              {matches}
                              ''')
                  else:
                        raise Exception(f"Zero partial field matches found with {partial_name}.")

      # create another one to see if a field(s) exist where a given word is provided
      def check_fields_with_partialname(self, partial_name):
            """
            Search all field names in the dataset to see if the partial name is part of any of the fields.
            - Parameter partial_name: Partial name to search for in field names.
            - Returns: List of all matching field names.
            """
            # Lowercase the file extension for consistency
            file_extension = self.file_type.lower()
            # Determine the file type based on extension
            file_type = file_types.get(file_extension, 'Unsupported')
            # Get the appropriate read function
            read_func = file_types_pd.get(file_type)
            # Construct the full file path
            full_path = self.file_path / f"{self.file_name}{self.file_type}"
            # Check if the function exists and read the file
            if read_func:
                  df = read_func(full_path)
                  # Read the file and get the column names
                  field_names = df.columns
                  # Search for matches
                  matches = [field for field in field_names if partial_name in field]
                  if len(matches) > 0:
                        print("...Field(s) partial name check: Passed")
                        return len(matches) > 0
                  print("...Field(s) partial name check: Failed")
                  return len(matches) > 0