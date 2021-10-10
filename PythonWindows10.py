from winreg import *


def download_folder_path():
    with OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        downloads_folder_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    return downloads_folder_path





if __name__ == '__main__':
    print(download_folder_path())
