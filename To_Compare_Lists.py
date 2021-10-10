def different_values(list_a, list_b):
    differences = [item for item in list_b if item not in list_a]
    differences += [item for item in list_a if item not in list_b]
    return differences


def equal_values(list_a, list_b, details=False):
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


if __name__ == '__main__':
    lista1 = ["diego", "pepe", "luis", "mari"]
    lista2 = ["diego", "mari", "luis", "pepe"]

    print(equal_values(lista1, lista2, details=True))
    print(different_values(lista1, lista2))