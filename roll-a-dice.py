import random
import keyboard 
import time

print("Aperte Y para rolar o dado!")

def imprimir_dado(numero):
    if numero == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif numero == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif numero == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    elif numero == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif numero == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif numero == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

while True:
    if keyboard.is_pressed('y'):
        response = "y"
        time.sleep(0.2)

        no = random.randint(1, 6)
        imprimir_dado(no)

        jogar_novamente = input("Deseja jogar novamente? (y/n): ")
        if jogar_novamente.lower() != 'y':
            break
