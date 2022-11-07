import U_XO.u_xo_game as ug
import players

p1=players.hum_player('x')
p2=players.rand_player('o')
c = ug.U_xo(p1,p2)
for i in range(1):
    c.clear_board()
    c.game()
    print(i,c.ju.winner)
    print(len(c.get_sqrs()))
    for (i,j) in zip(c.get_sqrs(),range(1,82)):
        print(j, i.get_sqr_list())
    c.bo.show()
print(c.stat.get_wins(),c.stat.get_stat())