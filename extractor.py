import os
import json
import platform
from shutil import copyfile

# This is where vanilla Minecraft stores its assets
if platform.system() == 'Windows':
    assets_path = os.path.expanduser("~/AppData/Roaming/.minecraft/assets")
elif platform.system() == 'Linux':
    assets_path = os.path.expanduser("~/.minecraft/assets")
elif platform.system() == 'Darwin':
    assets_path = os.path.expanduser("~/Library/Application Support/minecraft/assets")

indices_dir = os.path.join(assets_path, "indexes")
indices = os.listdir(indices_dir)

print('Available versions (1.16 recommended!): ')
for index in indices:
    if index.endswith('.json'):
        print(index[:-5])

version = str(input('MC Installed Version? '))
output_dir = os.getcwd()

index_file = f'{version}.json'
index_path = os.path.join(indices_dir, index_file)

try:
    with open(index_path, "r") as read_file:
        objects = json.load(read_file)["objects"]
except:
    print('Error! Version doesn\'t exist')
    exit()

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

for k in objects:
    if "music" not in k: continue
    asset_path = find(objects[k]["hash"], assets_path)
    outfile = os.path.join(output_dir, k)
    print(objects[k]["hash"], '->', k)

    if not os.path.exists(os.path.dirname(outfile)):
        os.makedirs(os.path.dirname(outfile))
    copyfile(asset_path, outfile)