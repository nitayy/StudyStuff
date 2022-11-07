import threading
from multiprocessing import Queue

#import newgui
import GUI
import randomgame

# choose = int(input('please choose random game (1 = dumgame, 2 = NitayGame): '))

queue = Queue()
t_gui = threading.Thread(target=GUI.run_gui,args=("Gui", queue))
t_gui.start()

t_dumgame = threading.Thread(target=randomgame.run_randomgame,args=("Game", queue))
t_dumgame.start()