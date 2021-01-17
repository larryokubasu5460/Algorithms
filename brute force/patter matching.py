# abacaabaccabacabaabb
# abacab

def bfp(a,b):
    n,m=len(a),len(b)
    for i in range(n-m+1):
        index=i
        for j in range(m):
            if a[index]==b[j]:
                index+=1
            else:
                break
            if index-i== len(b):
                return i
            
    return "not present"

a="ADVANCED DATA STRUCTURES"
b="DATA"
print(bfp(a,b))



    