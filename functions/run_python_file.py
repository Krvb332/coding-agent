import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
      try:
                  working_dir_abs=os.path.abspath(working_directory)
                  target_dir:str =os.path.normpath(os.path.join(working_dir_abs, file_path))
                  valid_target_dir=os.path.commonpath(([working_dir_abs, target_dir])) == working_dir_abs
                  
                  
                  if not valid_target_dir:
                        print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
                        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
                  elif not os.path.isfile(target_dir):
                        print(f'Error: "{file_path}" does not exist or is not a regular file')
                        return f'Error: "{file_path}" does not exist or is not a regular file'
                  if str.endswith(".py", file_path):
                        print(f'Error: "{file_path}" is not a Python file')
                        return f'Error: "{file_path}" is not a Python file'
                  if valid_target_dir:
                        print(f'Success: "{file_path}" is within the working directory')
                        command = ['python', target_dir]
                        if args is not None:
                                command.extend(args)
                        ComppletedProcess = subprocess.run(command,stdout=True, stderr=True,text=True,timeout=30)    
                        output_string =""
                        if ComppletedProcess.stdout == None and ComppletedProcess.stderr==None:
                              output_string += f"\nNo output produced"
                        elif not ComppletedProcess.stdout == None :
                              output_string += f"STDOUT: {ComppletedProcess.stdout}"
                        elif not ComppletedProcess.stderr==None :
                              output_string +=f"STDERR: {ComppletedProcess.stderr}"      
                        output_string+= f"\nProcess exited with code {ComppletedProcess.returncode}"                              
                        print(output_string)      
                        return output_string
      except Exception as e:
                  
                  print(f"Error: executing Python file: {e}")
                  return f"Error: executing Python file: {e}"
      
      return ""