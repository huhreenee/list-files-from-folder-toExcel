import os
import pandas as pd
from time import time
import datetime

currentDT = datetime.datetime.now()
ts = currentDT.strftime("%Y_%m_%d_%H_%M_%S")
directory = input("Enter full path to list files:")
file_list = [(file,os.path.join(directory, file)) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
df = pd.DataFrame(file_list, columns =['Name', 'Path'])

def make_hyperlink(value):
    return '=HYPERLINK("%s", "%s")' % (value, "Open" )

df['hyperlink'] = df['Path'].apply(make_hyperlink)

df.to_excel("list_of_files_"+ts+".xlsx")