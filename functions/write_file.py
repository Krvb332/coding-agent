import os



def write_files(working_directory:str, file_path:str, content:str) -> str:
      try:
            working_dir_abs=os.path.abspath(working_directory)
            target_dir:str =os.path.normpath(os.path.join(working_dir_abs, file_path))
            valid_target_dir=os.path.commonpath(([working_dir_abs, target_dir])) == working_dir_abs
            print(target_dir)
            
            if not valid_target_dir:
                  print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
            elif os.path.isdir(target_dir):
                  print(f'Error: Cannot write to "{file_path}" as it is a directory')
            elif valid_target_dir:
                  print(f'Success: "{file_path}" is within the working directory')
                  print(f"Result for '{file_path}' file:")
                  with open(target_dir, "w") as f:
                        f.write(content)
                        print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
                        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
      except Exception as e:
            print(f"{e}")
      return ""
                   
            