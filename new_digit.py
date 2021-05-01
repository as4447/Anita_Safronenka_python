import time
import os
import datetime


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear;')
    

list = [
    '''
 $$$$$$\\
$$$ __$$\\
$$$$\ $$ |
$$\$$\$$ |
$$ \$$$$ |
$$ |\$$$ |
\$$$$$$  /
 \______/''',
    '''
  $$\\
$$$$ |
\_$$ |
  $$ |
  $$ |
  $$ |
$$$$$$\\
\______|''',

    '''
  $$$$$$\\
$$  __$$\\
\__/  $$ |
 $$$$$$  |
$$  ____/
$$ |
$$$$$$$$\\
\________|''',
    '''
 $$$$$$\\
$$ ___$$\\
\_/   $$ |
  $$$$$ /
  \___$$\\
$$\   $$ |
\$$$$$$  |
 \______/''',
    '''
$$\   $$\\
$$ |  $$ |
$$ |  $$ |
$$$$$$$$ |
\_____$$ |
      $$ |
      $$ |
      \__|''',
    '''
$$$$$$$\\
$$  ____|
$$ |
$$$$$$$\\
\_____$$\\
$$\   $$ |
\$$$$$$  |
 \______/ ''',
    '''
 $$$$$$\\
$$  __$$\\
$$ /  \__|
$$$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
 \______/ ''',
    '''
$$$$$$$$\\
\____$$  |
    $$  /
   $$  /
  $$  /
 $$  /
$$  /
\__/''',
    '''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
$$  __$$<
$$ /  $$ |
\$$$$$$  |
 \______/ ''',
    '''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
\$$$$$$$ |
 \____$$ |
$$\   $$ |
\$$$$$$  |
 \______/ '''
]

colon = '''
$$\\
\__|
$$\\
\__|'''

while True:
    clearscreen()

    current_time = str(datetime.datetime.now().strftime("%H:%M:%S"))

    lines = ["", "", "", "", "", "", "", "", ""]
    line = 0

    numbers = [[], [], [], [], [], [], [], []]
    for x in range(8):
        if current_time[x].isdigit():
            numbers[x] = list[int(current_time[x])].splitlines()
        elif current_time[x] == ":":
            numbers[x] = colon.splitlines()

    for x in range(9):
        temp = ""
        for i in range(9):
            try:
                if i != 8:
                    temp += str(numbers[i][line]).ljust(10)
                else:
                    temp += str(numbers[i][line])
            except:
                temp += "          "
        lines[x] += temp
        line += 1

    for x in range(9):
        print(lines[x])

    print
    time.sleep(1)
