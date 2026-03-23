# Class for form fitting

# Imports
import numpy as np
import scipy as sp

# Class
class FormSimulating:
    def LorentzianSim(self, Y, X=[]):
        if X==[]:
          X = list(range(len(Y)))

        # L = A/B
        # B = 1 + ((x-x0)/(reflectionCoefficient/2))**2
        return A, x0, reflectionCoefficient

    def PeakFinding(self, Y, X=[]):
        if X==[]:
            X = list(range(len(Y)))
        maxY = max(Y)
        return maxY
    
    def MonteCarloSim(self, X, Y):
        #do the thing
        print('sim')
            
    def ClusterSim(self, X, Y):
        #do the thing
        print('sim')
        
    
        
