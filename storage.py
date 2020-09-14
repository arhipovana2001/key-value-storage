import argparse, os, tempfile, json


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='key', type=str)  # добавлена опция добавления ключа
parser.add_argument('--val', help='val', type=str, default=None)  # добавлена опция добавления значения
args = parser.parse_args()  # # Namespace(key='key', val=None)
key = args.key
val = args.val
my_dict = {}

print(1, args)
print(2, key)
print(3, val)


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
