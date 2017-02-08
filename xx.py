from matlib import *
from gramm import gramm

#def matprod(A, B):
#    m, n = matdim(A)
#    p, q = matdim(B)
#    print m, n
#    print p, 1

def readdat():
    f = open('dat','r')
    x, y = [], []
    f.next()
    for line in  f:
        val = line.split()
        y.append(float(val[1]))
        x.append([float(p) for p in val[2:]])
    return x, y
 
 
def qr(A, method="gramm"):
    # Performs a QR decomposition of A
    # default is via gramm-schmidt orthogonalization.
    if method == "gramm":
       Q = gramm(A)
       R = matprod(transpose(Q),A)
    return Q,R

def bsub(r, z):
    """ solves "R b = z", where r is triangular"""
    m, n = matdim(r)
    p, q = matdim(z)
    b = [[0] * n]
    pp, qq = matdim(b)
    for j in range(n-1, -1, -1):
        zz = z[0][j] - sum(r[j][k]*b[0][k] for k in range(j+1, n))
        b[0][j] = zz / r[j][j]
        print z[0][j], zz, b[0][j]
    return b

def linreg(y, x):
    # prepend x with 1

    for xx in x:
        xx.insert(0, 1.0)
    matprint(x)


    q, r = qr(x)
    print 'q'
    #print q
    matprint( q)
    print 'r'
    matprint( r)
    #qt = transpose(q)
    #print 'qt'
    #matprint( qt)
    z = mattmat(q, vec2colmat(y))
    #z = matprod( qt, vec2colmat(y))
    print 'z'
    print  matdim(z)

    matprint(z)

    b = bsub(r, transpose(z))
    print 'b'
    print  matdim(b)
    matprint(b)


def tester():
    x, y = readdat()
    # print x, y
    print 'x'
    print  matdim(x)
    print  matprint(x)
    print 'y'
    print  matdim(y)
    print  matprint(y)


    b = linreg(y, x)


 
def tester_qr():
   A =[[12, -51, 4],
       [6, 167, -68],
       [-4, 24, -41]] 
 
   print "A:"
   matprint (A)
 
   Q,R = qr(A)
   print "Q:"
 
   matprint (Q)
   print "R:"
   matprint (R)
 
   print "QR:"
   matprint(matprod(Q,R))

if __name__ == "__main__":
    tester()
