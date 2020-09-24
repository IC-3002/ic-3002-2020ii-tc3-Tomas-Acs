

def sumatoria_cubica(n):
    #raise NotImplementedError()
    r = 0;
    for i in range (1,n+1):
        for j in range (1,i+1):
            for k in range (j,i+j+1):
                r += 1;
    return r







def sumatoria_constante(n):
	k = ((3*n)*(n+1)/2)
	return int (k)
    #raise NotImplementedError()

