import xo
import pdp


def ins(i,s,b,p):
    b.ins(i,s)
    p.set_input(i, s)


b=xo.board()
p=pdp.Pdp()
b.show()
p.hur1()
ins(p.get_move(),p.f_sign,b,p)
p.show_pdp1()
print("---------------------------------------------------------------------------------")
ins(3,'o',b,p)
b.show()
p.hur1()
c=p.get_move()
print(c)
p.show_pdp1()


