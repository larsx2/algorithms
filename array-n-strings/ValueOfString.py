import string

class ValueOfString(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=13678 """

    def findValue(self, s):
        val = {c:i+1 for i, c in enumerate(string.ascii_lowercase)}

        S = len(s)
        result = 0
        for i in xrange(S):
            k = len([j for j in s if val[j] <= val[s[i]]])
            result += k * val[s[i]]
    
        return result
        
   
if __name__ == '__main__':
    params = [
        'babca', 'zz',
        'y', 'aaabbc', 'topcoder', 
        'thequickbrownfoxjumpsoverthelazydog', 
        'zyxwvutsrqponmlkjihgfedcba'
    ]

    vos = ValueOfString()
    for param in params:
        print "{} = {}".format(param, vos.findValue(param))



