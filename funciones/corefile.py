import json
MY_DATABASE = ''

def NewFile(data:dict):
    with open(MY_DATABASE, "w") as wf 
        json.dump(data,wf,ident=3)
        wf.close()
def checkFile(archivo:str)->bool:
    try:
        with open(archivo,'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False