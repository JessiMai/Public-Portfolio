# Class for creating the application window/s

# Imports
import Tkinter as tk
import threading

class WindowFunctions:
    
    def _init_(self):
        self.Defaults()
        self.CreateGUI()
        
        
  
    def Defaults(self):
        self.widgetDict = {
            'widgetType' = [],
            'widgetVar' = [],
            'widgetName' = [],
            'widgetValue' = [],
            'widgetPosition' = [],
            'widgetParentFrame' = []
        }
    
    def CreateGUI(self):
        for i, widgetType in enumerate(self.widgetDict['widgetType']):
            match widgetType:
                case 'Button':
                    #create button
                    pass
                case 'EntryBox':
                    pass
                case 'ScrollBox':
                    pass
                case 'CheckBox':
                    pass
                case 'InfoBox':
                    pass
                case 'DropDownMenu':
                    pass
                case __:
                    print('Who''s messing up my code?')
            
        
        
    
        
