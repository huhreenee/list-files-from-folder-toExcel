import os
import pandas as pd
from time import time
import datetime

currentDT = datetime.datetime.now()
ts = currentDT.strftime("%Y_%m_%d_%H_%M_%S")
directory = input("Enter full path to list files:")
#file_list = [(file,os.path.join(directory, file)) for file in os.listdir(directory)]

# for top, dirs, files in os.walk(directory):
#     for dir in dirs:
#         print(dir, os.path.join(top, dir))
#     for file in files:
#         print(file, os.path.join(top, file))

result = [(dir, os.path.join(top, dir)) for top, dirs, files in os.walk(directory) for dir in dirs]
result += [(file, os.path.join(top, file)) for top, dirs, files in os.walk(directory) for file in files]

df = pd.DataFrame(result, columns =['Name', 'Path'])

def make_hyperlink(value):
    return '=HYPERLINK("%s", "%s")' % (value, "Open" )

#df['hyperlink'] = df['Path'].apply(make_hyperlink)

df.to_excel("list_of_files_"+ts+".xlsx")

