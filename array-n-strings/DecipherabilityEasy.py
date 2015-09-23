from hashlib import md5

class DecipherabilityEasy(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=13658 """

    def hash(self, a):
        return md5(a).hexdigest()


    def usingStrSlices(self, s, t):
        for i, _ in enumerate(s):
            if s[:i] + s[i+1:] == t:
            	return 'Possible'

        return 'Impossible'


    def usingStrReplace(self, s, t):
        for i, _ in enumerate(s):
            if s.replace(s[i], '', 1) == t:
            	return 'Possible'

        return 'Impossible'


    def usingLists(self, s, t):
        for i, _ in enumerate(s):
            l = list(s)
            del l[i]

            # a hash comparison could be used as well
            if ''.join(l) == t:
            	return 'Possible'

        return 'Impossible'


    def check(self, *args):
        return self.usingStrReplace(*args)
        #return self.usingLists(*args)
        #return self.usingStrSlices(*args)


if __name__ == '__main__':
    dec = DecipherabilityEasy()

    params = [
        ['sunuke', 'snuke'],
        ['snuke', 'skue'],
        ['snuke', 'snuke'],
        ['sukent', 'snuke'],
        ['aaaaa', 'aaaa'],
        ['aaaaa', 'aaa'],
        ['topcoder', 'tpcoder'],
        ['singleroundmatch', 'singeroundmatc']
    ]

    for param in params:
        print "{} = {}".format(param, dec.check(*param))
