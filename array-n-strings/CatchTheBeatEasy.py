class CatchTheBeatEasy(object):
    """ Div2 250 http://community.topcoder.com/stat?c=problem_statement&pm=13208 """

    def ableToCatchAll(self, x, y, debug=False):
        fruits = [[xf,yf] for xf, yf in sorted(zip(x,y), key=lambda k: k[1])]
        p = [0,0]
        j = 0

        for i in xrange(1, fruits[-1][1]+1):
            q = fruits[j][:]

            if p[0] < q[0]:
                p[0] += 1
            if p[0] > q[0]:
                p[0] -= 1
        
            if q[1]-i <= 0:
                if p[0] != q[0]:
                    return "Not able to catch"

                j += 1

        return "Able to catch"


ctbe = CatchTheBeatEasy()
params = [
    [[-1,1,0], [1,3,4]],
    [[-3], [2]],
    [[-1,1,0], [1,2,4]],
    [[0,-1,1], [9,1,3]],
    [[70,-108,52,-70,84,-29,66,-33], [141,299,402,280,28,363,427,232]],
    [[-175,-28,-207,-29,-43,-183,-175,-112,-183,-31,-25,-66,-114,-116,-66],
     [320,107,379,72,126,445,318,255,445,62,52,184,247,245,185]],
    [[0,0,0,0], [0,0,0,0]],
]
for i, param in enumerate(params):
    print "{}) {} = {}".format(i, param, ctbe.ableToCatchAll(*param))
