import funciones.clientes as c
# import funciones.corefile as core 
if _name_ == '_mian_':
    if(c.cf.checkFile(c.cf.MY_DATABASE)):
        print('ok')
    else:
        print("Error")
