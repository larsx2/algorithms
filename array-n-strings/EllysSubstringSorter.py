from operator import itemgetter 

class EllysSubstringSorter(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=12977 """

    def getMin(self, S, L):
        if not 2 <= L <= 50:
            raise ValueError("L should be between 1-50 inclusive")

        if not L <= len(S) <= 50:
            raise ValueError("S length should be between 1-50 inclusive")

        for i, val in enumerate(sorted(S[:len(S)-L])):
            if ord(S[i]) > ord(val):
                return S[:i] + ''.join(sorted(S[i:i+L])) + S[i+L:]
    
        return S

        
if __name__ == '__main__':
    params = [
        ["TOPCODER", 4],
        ["ESPRIT", 3],
        ["AAAAAAAAA", 2],
        ["ABRACADABRA", 5],
        ["BAZINGA", 6],
        ["AAAWDIUAOIWDESBEAIWODJAWDBPOAWDUISAWDOOPAWD", 21]
    ]

    elly = EllysSubstringSorter()
    for i, param in enumerate(params):
        print "{}) {} = {}".format(i, param, elly.getMin(*param))

