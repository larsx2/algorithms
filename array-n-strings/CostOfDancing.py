class CostOfDancing(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=13195 """

    def minimum(self, k, danceCost):
        return sum(sorted(danceCost)[:k])


if __name__ == '__main__':
    params = [
        [2, [1, 5, 3, 4]],
        [3, [1, 5, 4]],
        [1, [2, 2, 4, 5, 3]],
        [39, [
            973, 793, 722, 573, 521, 568, 845, 674, 595, 310, 284, 794, 913, 93, 
            129, 758, 108, 433, 181, 163, 96, 932, 703, 989, 884, 420, 615, 991, 
            364, 657, 421, 336, 801, 142, 908, 321, 709, 752, 346, 656, 413, 629, 801
            ]]
    ]

    cod = CostOfDancing()
    for k, cost in params:
        print "K:", k, "Dance Cost:", cost, cod.minimum(k, cost)
