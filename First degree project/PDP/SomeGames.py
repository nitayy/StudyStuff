"""Class with functions of the games"""

# imports
import U_XO.u_xo_game as ug
import Q_XO.q_xo_game as qg
import players
import xogame

NO = 1000
W = {'x':0, 'o':1 , 'd':2}


h_p = players.hum_player('x')
r_p_x = players.rand_player('x')
r_p_o = players.rand_player('o')

# ------------------------------ Classic XO: ------------------------------------------
def HumPDP():
    g = xogame.Game()
    g.game_hum_with_pdp()

def CompPDPxo(n,tree=False):
    """
    :param tree: If it's tree or random computer. 
    :return: 
    """
    wins=[0,0,0]
    g = xogame.Game()
    for i in range(n):
        g.clear()
        k=g.game_comp_with_pdp()
        wins[k-1]+=1
    print(wins)

# ------------------------------ Q XO: --------------------------------------------------
def QHumPDP():
    """
    Qxo game of a human player against PDP.
    :return: 
    """
    g=qg.Game(h_p)
    g.game_hum_with_pdp()

def CompPDP(n):
    """
    The function plays n games of QXO of random player(x) against the PDP(o).
    :param n: 
    :return: 
    """
    wins=[0,0,0]
    g=qg.Game(r_p_x)
    for i in range(n):
        if ((i+1) % 10000 == 0):
            print("---------------------------", (i+1)) # To know how far we pass...
        k=g.game_comp_with_pdp()
        wins[W[k]]+=1
        g.clear_board()
    print(wins)
    return wins

# ------------------------------ U XO: --------------------------------------------------
def UHumRand():
    g=ug.U_xo(h_p,r_p_o)
    g.game()


CompPDP(100000000)