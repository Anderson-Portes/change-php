import os
import sys

def change_xampp_symlin(version):
  base_dir = "C:/xampp"
  link_name = "C:/xampp"
  new_path = os.path.join(base_dir + version)
  if not os.path.exists(new_path):
    print(f"The {version} version directory does not exist.")
    return
  if(os.path.exists(link_name)):
    os.rmdir(link_name)
  os.symlink(new_path, link_name)
  if not os.path.exists(link_name):
    print("Failed to create the symbolic link.")
    return
  try:
    os.system("taskkill /F /IM mysqld.exe")
  except:
    pass
  input("Symbolic link created successfully.")

if len(sys.argv) < 2:
  input("Xampp version not specified.")
else:
  change_xampp_symlin(sys.argv[1])