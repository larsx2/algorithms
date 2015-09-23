class TaroJiroDividing(object):
    """ 
    Problem Statement: 
        
        http://community.topcoder.com/stat?c=problem_statement&pm=13672 

    """

    def __init__(self, low=1, high=1000000000):
        self.low = low
        self.high = high


    def inRange(self, num):
        return self.low <= num or num >= self.high


    def getNumberChain(self, num):
        chain = [num]

        while num % 2 == 0:
            num = num / 2 
            chain.append(num)

        return set(chain)


    def getNumber(self, a, b):

        if not self.inRange(a) or not self.inRange(b):
            err = "Valid range should be between {} and {}".format(self.low, self.high)
            raise Exception(err)

        setA = self.getNumberChain(a)
        setB = self.getNumberChain(b)

        return len(setA.intersection(setB))


if __name__ == '__main__':

    taro = TaroJiroDividing()
    
    params = [
        [8, 4], 
        [4, 7],
        [12, 12],
        [24, 96],
        [1000000000, 999999999]
    ]

    for a, b in params:
    	print "{}, {} = {}".format(a, b, taro.getNumber(a, b))


