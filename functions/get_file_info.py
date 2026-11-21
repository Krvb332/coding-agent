import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
      directory_details:list[str]= []
      try:
            working_dir_abs=os.path.abspath(working_directory)
            target_dir:str =os.path.normpath(os.path.join(working_dir_abs, directory))
            
            valid_target_dir=os.path.commonpath(([working_dir_abs, target_dir])) == working_dir_abs
            if not valid_target_dir:
                  print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            elif not os.path.isdir(target_dir):
                  print(f'Error: "{directory} is not a directory"')
            elif valid_target_dir:
                  print(f'Success: "{directory}" is within the working directory')
                  print(f"Result for '{directory}' directory:")

                  for items in os.listdir(target_dir):
                        directory_details.append(f"-{items}: file_size={os.path.getsize(os.path.join(target_dir,items))} bytes, is_dir={os.path.isdir(os.path.join(target_dir,items))}")
                  print("\n".join(directory_details))
      except Exception as e:
            print(f"Error:{e}")
      return "\n".join(directory_details)
 
      
     