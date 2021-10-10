from os import getcwd, listdir


def here():
    return getcwd()


class SystemUtilitiesTools:
    def __init__(self):
        self.directory = here()

    def list_files_from(self, directory=here()):
        self.directory = directory
        file_list = listdir(self.directory)
        return file_list


if __name__ == '__main__':
    tools = SystemUtilitiesTools()
    print(tools.list_files_from())
