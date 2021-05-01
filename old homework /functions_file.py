import time
import os
import datetime

def clear():
    system("clear")

def translate(text):
    text=str("clear")
    letters=[]
    for letter in text:
        letters.append(list[letter])
    for i in range(8):
        for letter in letters:
            print(letter.splitlines()[i])
        print()

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
 \______/ ''',
 '''
$$\\
\__|
$$\\
\__|'''
]


def clock():
    while 1:
        try:
            ctime=datetime.now()
            translate(":".join([(str(i) if len(str(i))== 2 else "0"+str(i))for i in [ctime.hour, ctime.minute, ctime.second]]))
            sleep(0.5)
        except KeyboardInterrupt:
            clear()
            break

        clock()