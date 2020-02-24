import os
import glob
from hanziconv import HanziConv
print(HanziConv.toTraditional('繁简转换器'))

base_path = '/home/leoleung/Documents/FileRenamer/Target/'

files = [f for f in glob.glob(base_path + "**/*.*", recursive=True)]

for f in files:
    print(f)
    os.rename(f,HanziConv.toTraditional(f))