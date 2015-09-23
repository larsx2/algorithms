class SumOfPower(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=13230 """
    
    def findSum(self, l):
        total = 0
        for i, _ in enumerate(l):
            for j in xrange(len(l[i:])):
                total += sum(l[i:i+j+1])

        return total


if __name__ == '__main__':

    params = [
        [1,2],
        [1, 1, 1],
        [3, 14, 15, 92, 65],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]

    sop = SumOfPower()
    for param in params:
        print "{} = {}".format(param, sop.findSum(param))

