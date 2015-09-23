class SearchBox(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=8019 """

    def find(self, text, search, wholeWord, start):
        T = len(text)
        S = len(search)

        for i in xrange(start, T-S):
            if text[i:i+S] == search:
                if wholeWord == 'N':
                    return i
        
                if (i == 0 and text[S] == " ") \
                	or (i+S == T-1 and text[i-1] == " ") \
                        or (text[i+S] == " " and text[i-1] == " "):
                	return i

        return -1

if __name__ == '__main__':
    params = [
        ["We dont need no education", "ed", "N", 13],
        ["We dont need no thought control", "We", "Y", 0],
        ["No dark sarcasm in the classroom", "The", "Y", 5],
        ["Teachers leave them kids alone", "kid", "Y", 1],
        ["All in all its just another brick in the wall", "all", "Y", 9],
        ["All in all youre just another brick in the wall", "just", "Y", 17]
    ]

    sb = SearchBox()
    for param in params:
        print "{} = {}".format(param, sb.find(*param))
