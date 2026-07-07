def cuenta_atras(num_inicio: int):
    if num_inicio >= 0:
        print(num_inicio)
        cuenta_atras(num_inicio-1)

cuenta_atras(100)