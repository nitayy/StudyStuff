import itertools as itr
import xogame


c=list(itr.permutations('123456789',5))

g=xogame.Game()
wins = [0,0,0]
pers=[]

"""It will prints all the board the the PDP Loses...."""
for i in range(len(c)):
    # print("Game no. ",i+1)
    w=g.game_perm_with_pdp(c[i])
    if w!= -1:
        wins[w-1]+=1
        if w==1:
            pers.append(c[i])

print(wins)
print("The amount of relevant games:",sum(wins))
print('x [perm] wins: ',wins[0], '\no [PDP] wins: ',wins[1], '\nDraws: ',wins[2])
temp=100/sum(wins)
print("At %: \nx wins:",wins[0]*temp,'\no wins: ',wins[1]*temp,'\nDraws: ',wins[2]*temp)
