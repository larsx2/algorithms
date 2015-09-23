class SwappingDigits(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=12609 """

    def swap(self, s, i, j):
        l = list(s)
        l[i], l[j] = l[j], l[i]

        return ''.join(l)


    def minNumber(self, num):
        
        for i in xrange(len(num)):
            if num[i] == "0":
                continue 

            min_i = i
            for j in xrange(len(num[i:])):
                j += i

                if num[j] != "0" and num[j] <= num[min_i]:
                    min_i = j
                
            if i != min_i:
                return self.swap(num, i, min_i)

        return num


if __name__ == '__main__':
    params = [ "596", "93561", "5491727514", "10234", "93218910471211292416" ];

    sd = SwappingDigits()
    for param in params:
        print "{} = {}".format(param, sd.minNumber(param))


