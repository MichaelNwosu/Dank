#in the command line type 'pip install PyAutoGUI' and 'pip install keyboard'
from time import sleep
import random
import keyboard
import pyautogui
import os
from ctypes import windll, Structure, c_long, byref
from datetime import datetime
import threading
s=False

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


beg = True
dig=True
hunt =True
fish=True
search=True
pm=True
sell = True
crime=True
printing=True
Setting = input('''

┏━━━┓╋╋┏┓╋┏┓
┃┏━┓┃╋┏┛┗┳┛┗┓
┃┗━━┳━┻┓┏┻┓┏╋┳━┓┏━━┳━━┓
┗━━┓┃┃━┫┃╋┃┃┣┫┏┓┫┏┓┃━━┫
┃┗━┛┃┃━┫┗┓┃┗┫┃┃┃┃┗┛┣━━┃
┗━━━┻━━┻━┛┗━┻┻┛┗┻━┓┣━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛

Type the letters of the commands you want to remove then press 'Enter' you do not
need to add any spaces if you don't want to remove any then press 'Enter' or you can
do 'n' if you do not want anything that might make you die. You can also press 'u' if 
you don't want to see the commands that were used If you leave it on it will cause a
small amount of lag.

DISCLAIMER - Regradless of what the bot does there is still a chance for you to die. So I
Reccomend you get a pet so evn if you die you gie life savers.

b ~ Beg
d ~ Dig
h ~ Hunt
f ~ Fish
s ~ Search
p ~ Pm 
c ~ Crime
                                      Input: ''')


Setting1 = input('Do you have a \'Tip Jar\' (y/n): ')
Setting3 = input('Do you have a \'Stonk Machine\' (y/n): ')
stock=False
tipjar=False
if 'b' in Setting:
  beg = False
if 'd' in Setting:
  dig = False
if 'h' in Setting:
  hunt= False
if 'f' in Setting:
  fish = False
if 's' in Setting:
  search = False
if 'p' in Setting:
  pm = False
if 'N' in Setting:
  search = False
  crime = False
if 'n' in Setting:
  search = False
  crime = False
if 'c' in Setting:
  crime = False
if 'u' in Setting:
  printing= False
if 'y' in Setting1:
  tipjar=True
else:
  tipjar == False
if 'y' in Setting3:
  stock=True
else:
  stock == False
isint = True
while (isint):
    Setting2 =input("How many 'Pizzas' do you want to use : ")
    try:
        Setting2 =int(Setting2)
        isint=False
    except ValueError:
        print("Type in a number.")
        sleep(2)
        clear()

Setting2=Setting2*15

clear()

print('''
  
██████╗░░█████╗░███╗░░██╗██╗░░██╗
██╔══██╗██╔══██╗████╗░██║██║░██╔╝
██║░░██║███████║██╔██╗██║█████═╝░
██║░░██║██╔══██║██║╚████║██╔═██╗░
██████╔╝██║░░██║██║░╚███║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

IMPORTANT: Use the command  'pls sell' and put your mouse above\nthe confirm button until it says ready and the ding sound is \nplayed you have 20 Sec.if the mouse is not moving to the right way\nstop rerun the bot

GITHUB: https://github.com/BlackRose-000/Dank-Memer-Bot

INSTALLED VERSION: v0.2.2
''')

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    sleep(20)
    windll.user32.GetCursorPos(byref(pt))
    print('Dank : READY\n')
    return pt.x, pt.y
s=True
pos=queryMousePosition()


def waste():
  profile = "pls profile"
  presteige = "pls prestige"
  shop = "pls shop"
  meme = "pls meme"
  waste = [profile,shop,meme]
  randomw = random.choice(waste)
  pyautogui.typewrite(randomw)  
def wastee():
  profile = "pls profile"
  shop = "pls shop"
  meme = "pls meme"
  waste = [profile,shop,meme]
  randomw = random.choice(waste)
  pyautogui.typewrite(randomw)  

def waitL():
  timeL=[37,40,45,47]
  timeL = random.choice(timeL)
  sleep(timeL)

def waitS(): 
  global timeS
  timeS=[2,3.5,4.6,1]
  timeS = random.choice(timeS)
  sleep(timeS)


current_time = datetime.now()
Dank='\033[32m[Dank]\u001b[0m'
x=0
def pizza():
  global Setting2,x
  if Setting2 != x:
    pyautogui.press("enter")
    sleep(3)
    pyautogui.press("enter")
    pyautogui.typewrite('pls use pizza') 
    sleep(3)
    pyautogui.press("enter")
    Setting2 -= 1

def Clickbutn2():
  pyautogui.leftClick(865,688)
  pyautogui.leftClick(865,688)

def Clickbutn():
  waitS()
  sleep(1)
  pyautogui.leftClick(pos)
  pyautogui.leftClick(pos)
  Clickbutn2()
def hl():
  global pos
  pyautogui.press("enter")
  pyautogui.typewrite('pls hl') 
  waitS()
  pyautogui.press("enter")
  sleep(2)
  waitS()
  jackhl =[1,2,3]
  jackhl=random.choice(jackhl)
  if jackhl == 1:
    pyautogui.leftClick(pos)
  if jackhl == 2:
    pyautogui.moveTo(pos)
    pyautogui.move(75,0)
    pyautogui.leftClick()
  if jackhl == 3:
    pyautogui.moveTo(pos)
    pyautogui.move(-75,0)
    pyautogui.leftClick()
  sleep(2)
  Clickbutn2()

def stonk():
  sleep(7)
  pyautogui.press("enter")
  pyautogui.typewrite('pls use stonk') 
  sleep(7)
  pyautogui.press("enter")

def tip():
  pyautogui.press("enter")
  sleep(10)
  pyautogui.press("enter")
  pyautogui.typewrite('pls use tipjar') 
  sleep(10)
  pyautogui.press("enter")
pmin = 60*60
while (s):
  if dig == True:
    pyautogui.typewrite("pls dig")
    waitS()
    pyautogui.press("enter")
    if printing == True:
      print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls dig' ")
  if fish==True:
    pyautogui.typewrite("pls fish")
    waitS()
    pyautogui.press('enter')
    if printing == True:
      print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls fish' ")
    waitS()
    Clickbutn()
  if hunt==True:
    pyautogui.typewrite("pls hunt")
    waitS()
    pyautogui.press('enter')
    if printing == True:
      print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls hunt' ")
    waitS()
    Clickbutn()
  if beg == True:
    pyautogui.typewrite("pls beg")
    waitS()
    pyautogui.press('enter')
    if printing == True:
      print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls beg' ")
  if search == True:
    pyautogui.typewrite('pls search')
    waitS()
    pyautogui.press('enter')
    if printing == True:
      print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls search' ")
    waitS()
    Clickbutn()
  if crime == True:
    pyautogui.typewrite('pls crime')
    waitS()
    pyautogui.press('enter')
    waitS()

    Clickbutn()
    if printing == True:
      print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls crime' ")
  if pm == True:
    pyautogui.typewrite('pls pm')
    waitS()
    pyautogui.press('enter')
    waitS()
    Clickbutn()
    if printing == True:
      print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls pm' ")
  pyautogui.typewrite('pls sell')
  waitS()
  pyautogui.press('enter')
  waitS()
  Clickbutn()
  if printing == True:
    print(f"[{current_time}] - {Dank} | Successfully sent commmand 'pls sell' ")
  pyautogui.leftClick(pos)
  hl()
  waitS()
  pyautogui.typewrite('pls dep max')
  waitS()
  pyautogui.press('enter')
  waste()
  waitS()
  pyautogui.press('enter')
  if tipjar== True:
    threading.Timer(360, tip).start()
  if stock == True:
    threading.Timer(360, stonk).start()
  
  threading.Timer(720, pizza).start()
  
  waitL()

  Clickbutn2()