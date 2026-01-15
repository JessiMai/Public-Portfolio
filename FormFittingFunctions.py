# Class for form fitting

class FormFitting:
  def LorentzianFitting(self, Y, X=[]):
    if X==[]:
      X = list(range(len(Y)))

    # L = A/B
    # B = 1 + ((x-x0)/(reflectionCoefficient/2))**2
    return A, x0, reflectionCoefficient

    def PeakFinding(self, Y, X=[]):
        if X==[]:
            X = list(range(len(Y)))
        maxY = max(Y)
        
        
    
        
