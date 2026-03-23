# Class for form fitting

# Imports
import numpy as np
import scipy as sp

# Class
class FormFitting:
    def LorentzianFitting(self, Y, X=[]):
        if X==[]:
          X = list(range(len(Y)))
        # These are placeholders!!!!
        A = 1
        x0 = np.mean(X) 
        reflectionCoefficient = 1

        L = A/B
        B = 1 + ((X-x0)/(reflectionCoefficient/2))**2
        return A, x0, reflectionCoefficient

    def PeakFinding(self, Y, X=[]):
        if X==[]:
            X = list(range(len(Y)))
        maxY = max(Y)
        return maxY
    
    def MonteCarlo(self, X, Y):
        #do the thing
            
    def ClusterIdentification(self, X, Y):
        #do the thing
        
    
        
