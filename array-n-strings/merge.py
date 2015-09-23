def merge(a, b):
 
    c = []
    while len(a) or len(b):

        if not len(a):
            return c + b

        if not len(b):
            return c + a

        if a[0] < b[0]:
            c.append(a.pop(0))

        elif a[0] > b[0]:
            c.append(b.pop(0))
    
    return c

def merge2(a, b):
    i, j = 0, 0

    c = []
    while i <= len(a) and j <= len(b):
        
        if i == len(a):
            return c + b[j:]

        if j == len(b):
            return c + a[i:]

        if a[i] < b[j]:
        	c.append(a[i])
        	i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1

    return c
            
print merge([1,3], [2,4]) == merge2([1,3], [2,4])
print merge(range(0,10,2), range(1,10,2)) == merge2(range(0,10,2), range(1,10,2))
