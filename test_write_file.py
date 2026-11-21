from functions.write_file import write_files 
write_files("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
write_files("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
write_files("calculator", "/tmp/temp.txt", "this should not be allowed")