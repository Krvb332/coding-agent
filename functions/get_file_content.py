import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
      file_content_string = ""
      try:
                  working_dir_abs=os.path.abspath(working_directory)
                  target_dir:str =os.path.normpath(os.path.join(working_dir_abs, file_path))
                  
                  valid_target_dir=os.path.commonpath(([working_dir_abs, target_dir])) == working_dir_abs
                  if not valid_target_dir:
                        print(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
                  elif not os.path.isfile(target_dir):
                        print(f'Error: "File not found or is not a regular file: "{file_path}"')
                  elif valid_target_dir:
                        print(f'Success: "{file_path}" is within the working directory')
                        print(f"Result for '{file_path}' file:")
                        with open(target_dir, "r") as f:
                              file_content_string = f.read(MAX_CHARS)
                              if f.read(1):
                                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                              print("\n"+file_content_string)
      except Exception as e:
             print(f"{e}")
             
      return file_content_string