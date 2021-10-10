import shutil

# Move a SINGLE file
source = "raw_data.csv"
destination = "data"

new_path = shutil.move(source, destination)
print(new_path)
"""
Return:
        data/raw_data.csv
"""



# Move file and CHANGE NAME
source = "raw_data.csv"
destination = "data/raw_data_2019.csv"

new_path = shutil.move(source, destination)
print(new_path)

"""
Return:
        data/raw_data_2019.csv
"""