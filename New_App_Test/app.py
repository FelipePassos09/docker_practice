import pandas as pd
import numpy as np
from time import sleep

df = pd.DataFrame({
    "Column_A":[1,2,3,4],
    "Column_B":["A","B","C","D"],
    "Column_C":["João", "Zequinha","Jolie", "Giovanna"]
})

print(df)

sleep_time = 5
list_operators = [1,2,3,4]

while True:
    
    print(f"Sleep: {sleep_time}.")
    
    for i in list_operators:
        if i // 2 == 0:
            print(f"Ok: {i}")
            if i*i > 4:
                print(f"Maior que 2: {i}")
            else:
                print(f"Menor ou igual a 2: {i}")
        else:
            print(f"Impar: {i}")
    
    for operator in list_operators:
        operator += 4
    
    sleep(sleep_time)
