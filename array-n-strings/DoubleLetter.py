class DoubleLetter(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=13378 """

    def ableToSolve(self, s):
        if len(s) % 2 != 0:
            return 'Impossible'

        s = list(s)
        
        found = True 
        while found:
            found = False

            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    found = True
                    del s[i:i+2]
                    break

        if len(s):
            return 'Impossible'

        return 'Possible'


    def ableToSolve2(self, s):
        if len(s) % 2 != 0: 
        	return 'Impossible'

        l = list(s)
        for _ in range(len(s)):
            for i in range(len(l)-1):
                if l[i] == l[i+1]:
                    del l[i:i+2]
                    break

        if len(l):
        	return 'Impossible'

        return 'Possible'


if __name__ == '__main__':
    
    double = DoubleLetter()

    params = [
        'aabccb',
        'aabccbb',
        'abcddcba',
        'abab',
        'aaaaaaaaaa',
        'aababbabbaba',
        'zzxzxxzxxzzx'
    ]

    for param in params:
        print ">> 1st way:"
        print '  "{}" = {}'.format(param, double.ableToSolve(param))
        print ">> 2nd way:"
        print '  "{}" = {}'.format(param, double.ableToSolve2(param))
        print
