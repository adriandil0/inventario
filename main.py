import os 
opciones = ['Gestor Clientes', 'Gestor Proveedores', 'Gestor Productos', 'Salir']
opcionClientes = ['Nuevo Cliente', 'Borrar Cliente', 'Editar Cliente', 'Buscar', 'Menu Principal']
def generarMainMenu():
    header = """ 
    +++++++++++++++++++++++++++++++++
    + SISTEMA GESTOR DE INVENTARIOS +
    +++++++++++++++++++++++++++++++++
    """
    print(header)
    for i, item in enumerate(opciones):
        print(f'{(i+1)}-{item}')
def generarClienteMenu():
    isActiveCustomer = True
    header="""
    ++++++++++++++++++++++++++++++
    + ADMINISTRACION DE CLIENTES +
    ++++++++++++++++++++++++++++++
    """
    while (isActiveCustomer):
        os.system('cls')
        print(header)
        for i, item in enumerate(opcionClientes):
            print(f'{(i+1)}- {item}')
        try:
            op = int (input(":)_"))
        except ValueError:
            print("Error en el tipo de dato")
        else:
            if(op == 1):
                pass
            if(op == 2):
                pass
            if(op == 3):
                pass
            if(op == 4):
                pass
            if(op == 5):
                isActiveCustomer = False

