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
        for i, widgetType in enumerate(widgetDict['widgetType']):
            case widgetType:
                match 'Button':
                    #create button
                match 'EntryBox':
                match 'ScrollBox':
                match 'CheckBox':
                match 'InfoBox':
                match 'DropDownMenu':
                match __:
                    print('Who''s messing up my code?')
            
        
        
    
        
