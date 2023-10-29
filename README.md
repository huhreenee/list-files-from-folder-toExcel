# List of Files 

This is a python project to list all the files in a folder or subfolder onto an excel sheet

## Usage

1. Download the required python script

* use the listFiles.py file to list files in 1st level of folder only
* use the listFiles_Subfolders.py to list all files in folders and subfolders of the folder 

2. Download and save the file (this is the same location where the output excel file will be saved)

3. "Run" the .py file using python IDLE.

4. It will give you a prompt to enter the full file path, Enter the required folder's full path that you want to list the files of. 

```python
Enter full path to list files:
```
## Output
This returns an Excel File with the required folder's content saved at the same location as the python script.

Name  |	Path	| hyperlink

The Excel filename has the timestamp of when the file was created.

## Alternative
If the python file is not directly downloadable in your environment, Create a python script using following steps.

1. Create a txt file in the required location where the output will be generated.
2. Copy the contents in the required .txt file (named same as the .py file, refer to Usage point 1) into the txt file you created. 
3. Save the txt file with the .py extention
4. Now Run this file using the a python IDLE

