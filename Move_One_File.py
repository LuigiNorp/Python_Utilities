import shutil

# absolute path
source_path = r"E:\pynative\reports\sales.txt"
destination_path = r"E:\pynative\account\sales.txt"
shutil.move(source_path, destination_path)