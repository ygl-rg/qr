"""
File    qr.py
Author  Ernesto P. Adorio, Ph.D.
        U.P. Clarkfield, Pampanga
Version 0.0.1  2009.01.16 first version.
"""
 
from matlib import *
from gramm import gramm
 
 
def qr(A, method="gramm"):
    # Performs a QR decomposition of A
    # default is via gramm-schmidt orthogonalization.
    if method == "gramm":
       Q = gramm(A)
       R = matprod(transpose(Q),A)
    return Q,R
 
if __name__ == "__main__":
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
 
