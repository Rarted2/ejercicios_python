for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("ALERTA: REVISIÓN TOTAL")
    elif i % 3 == 0:
        print("Revisión Rápida")
    elif i % 5 == 0:   
        print("Revisión Completa")
    else:
        print(i)