import xo
from U_XO import u_xo_game
from random_c import randcomp


board=xo.board()
board.ins(5,'x')
board.ins(1,'o')
board.ins(2,'x')
board.ins(9,'x')
board.ins(3,'o')
board.ins(7,'x')
board.ins(8,'o')
board.ins(4,'o')
board.show()
print(u_xo_game.check_for_draw(board))

l=[1,2,3]
print(randcomp.get_sqr(l))



# xogame:

def mytest():
    key = {'Tree': 0, 'Rand': 0, 'Draw': 0}
    for i in range(1000):
        print("##########################", i, "#######################################")
        k = g.game()
        if (k == 1):
            key['Rand'] += 1
            break
        elif (k == 2):
            key['Tree'] += 1
        elif (k == 3):
            key['Draw'] += 1
        print(key)
        g.clear()
    print(key)

wins = [0,0,0]
g=Game()
for i in range(10000000):
    k = g.game_with_pdp()
    if k==1:
        break
    wins[k-1]+=1
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", i)
    print('x (random player) wins:',wins[0]\
          ,'\no (pdp) wins: ',wins[1], '\nDraws',wins[2])