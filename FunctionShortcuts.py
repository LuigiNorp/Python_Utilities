import shutil
from os.path import abspath
from os import getcwd, listdir
from winreg import *


def here():
    """
    Obtains the current working directory
    Returns:
         (str) Current working path without file name.
    """
    return getcwd()


def win_download_folder_path():
    """
    Returns a string variable with the directory of 'Donwloads' folder
    (Only for Microsoft Windows).

    Returns:
        download_folder_path (str): 'Downloads' folder path for Windows in a string variable
    """
    with OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        downloads_folder_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    return downloads_folder_path


def list_files_from(directory=here()):
    file_list = listdir(directory)
    return file_list


def different_values(list_a: list, list_b: list):
    """
    To return a list with the different elements between two lists.

    Parameters:
        list_a (list): This will be compared with list_b
        list_b (list): This will be compared with list_a

    Returns:
        differences (list): A list with the non repeated elements between two lists
    """
    differences = [item for item in list_b if item not in list_a]
    differences += [item for item in list_a if item not in list_b]
    return differences


def equal_values(list_a: list, list_b: list, details=False):
    """
    Returns a list with the repeated elements between two lists.
    Parameters:
        list_a (list): This will be compared with list_b
        list_b (list): This will be compared with list_a
    Returns:
          equals (list): This
    """
    equal = [item for item in list_a if item in list_b]
    if details is True:
        if len(equal) > 0:
            print('Ambas listas contienen estos elementos ')
            for item in equal:
                print('%s' % item)
                return equal
        else:
            print('No existe ningun elemento igual en las listas')
            return 0
    else:
        return equal


def raw_variable(string: str):
    """
    Turns a string into a raw string by adding r'' to the string
    Example: From "C:\pynative" turns it to r"C:\pynative"

    Parameters:
        string (str): This is the string to be converted into a raw string
    """
    return r'%s' % string


def move_one_file(source_path: str, destination_path: str):
    """
    Moves a file from source_path to the destination_path. Both paths musts to
    include file name

    Parameters:
        source_path: This is the path where the file come from, it musts to include
            file name. Example: C:\pynative\reports\sales.txt"

        destination_path: This is the path where the file will be moved to, it musts
            to include file name. Example: C:\pynative\reports\sales.txt"
    """
    # Setting absolute path
    source_path = raw_variable(source_path)
    destination_path = raw_variable(destination_path)
    # Moving File
    shutil.move(source_path, destination_path)


def move_files_to(source_folder: str, destination_folder: str, files: list):
    """
    Moves files from a source folder to a specified directory.

    Parameters:
        source_folder (str): This is the source path where files come from

        destination_folder (str): This is the path where file are moved in
        files (list): This is a list of the files that will be moved
    """
    # Setting Absolute Path
    source_folder = abspath(source_folder)
    destination_folder = abspath(destination_folder)

    # Iterate files
    for file in files:
        # construct full file path
        source = source_folder + "/" + file
        destination = destination_folder + "/" + file
        # Per file in files Move file
        shutil.move(source, destination)
        print('Moved:', file)


if __name__ == '__main__':
    files_to_move = ['MEGA-CLAVEDERECUPERACION (yahoo).txt',
                     'MEGA-CLAVEDERECUPERACION (ingjlllopezp).txt',
                     'MEGA-CLAVEDERECUPERACION_Original.txt']
    print(win_download_folder_path())
    source_files = r'C:\Users\luigi\Documents'
    dest = win_download_folder_path()
    move_files_to(source_files, dest, files_to_move)
