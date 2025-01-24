
def message_refactoring(forzamento_servo):
    numero = 2
    if forzamento_servo == 'PLASTICA':
        print("plastica")
        numero = 0

    elif forzamento_servo == 'CARTA':
        print("carta")            
        numero = 1
        
    elif forzamento_servo == 'VUOTO':
        numero = 2
        
    else:
        print("Errore")

    return str(numero)+'\n'
