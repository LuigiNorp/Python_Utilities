import shutil
import os

source = "/home/career_karma/data"
destination = "/home/career_karma/old_data"

files = os.listdir(source)

for file in files:
    new_path = shutil.move(f"{source}/{file}", destination)
    print(new_path)


"""
Return:
        /home/career_karma/old_data/data.csv
        /home/career_karma/old_data/old_data.csv
"""

# -------------------------------------------------------------- #

source_folder = r"E:\pynative\reports\\"
destination_folder = r"E:\pynative\account\\"
files_to_move = ['profit.csv', 'revenue.csv']

for file in files_to_move:
    source = source_folder + file
    destination = destination_folder + file
    shutil.move(source, destination)
    print('Moved:', file)