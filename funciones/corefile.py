import json
import os
MY_DATABASE = ''

def NewFile(*param):
    with open(MY_DATABASE, "w") as wf 
        json.dump(param[0],wf,ident = 4)
        wf.close()
def checkFile(*param):
    if(os.path.isfile(MY_DATABASE)):
        print("LO ENCONTRÉ")
        