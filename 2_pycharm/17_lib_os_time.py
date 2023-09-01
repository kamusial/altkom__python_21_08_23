import time
import os
#from time import *

print('Siema')
time.sleep(1)
#sleep(3)
print('miney 1 sekunda')

print(os.getcwd())
os.chdir('C:\\Users\\Student\\Desktop\\')
print(os.getcwd())
os.mkdir('new_folder')
time.sleep(1)
os.rename('new_folder', 'new_folder2')
time.sleep(1)
os.rmdir('new_folder2')
print('koniec')

os.system('cmd /c "cd C:\\Users\\Student\\Desktop"')