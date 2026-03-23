# Class for form fitting

class PlotFunctions:
    
    def __init__(self):
        print('PlotFunctions loaded')
  
    def PlotType(self, dataDict):
        #only works for data dictionaries with the key 'dataType'
        #outputs live and print plots for live graphs and for fixed graphs for saving etc
        if 'dataType' in dataDict:
            match dataDict['dataType']:
                case 'LiveLine':
                    print('figure out with data size')
                case 'LiveColour':
                    print('Colour plot')
                case 'PrintLine':
                    print('figure out with data size')
                case 'PrintColour':
                    print('Colour plot')
                case __:
                    print('figure out with data size')
                
        
        return plotType
    
    def LinePlot(self, Y, X, title, Yaxis, Xaxis):
        if X==[]:
            X = list(range(len(Y)))
        maxY = max(Y)
        return maxY
        
    
        
