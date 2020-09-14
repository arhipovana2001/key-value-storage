import argparse
import os
import tempfile
import json


def update_dict(dict, key, value):
    if key not in dict:
        dict[key] = value
    else:
        new_value = [dict[key]]
        new_value.append(value)
        dict[key] = new_value
    return dict


def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='key', type=str)  # добавлена опция добавления ключа
    parser.add_argument('--val', help='val', type=str, default=None)  # добавлена опция добавления значения
    args = parser.parse_args()  # Namespace(key='key', val=None)
    key = args.key
    val = args.val
    return key, val


def main():
    key, val = parsing()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.isfile('storage.data') is True:
        #print("ФАЙЛ ЕСТЬ")
        # передан только ключ
        if val is None:
            with open('storage.data', 'r') as file:
                data = json.load(file)
                if type(data[key]) is list:
                    data = [str(i) for i in data[key]]
                    print(', '.join(data))
                else:
                    print(data[key])

        # переданы ключ и значение
        elif val is not None and key is not None:
            # считываем данные из файла
            with open('storage.data', 'r') as file:
                data = json.load(file)
                data = update_dict(data, key, val)
            with open('storage.data', 'w') as file:
                json.dump(data, file)

    else:
        # первая запись в файл
        with open('storage.data', 'w') as file:
            json.dump(dict(), file)

        with open('storage.data', 'r') as file:
            data = json.load(file)  # загрузили данные из файла
            data = update_dict(data, key, val)  # обновили данные

        with open('storage.data', 'w') as file:  # добавили данные в файл
            json.dump(data, file)

        if val is None:
            print(None)


main()
