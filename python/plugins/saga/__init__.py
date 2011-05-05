# -*- coding: utf-8 -*-

def name():
    return "SAGA Module interface"

def description():
    return "Run the versatile SAGA modules. SAGA must be installed"
    
def icon():
    return "saga.png"
    
def version():
    return "Version 0.1"
    
def qgisMinimumVersion():
    return "1.0"
    
def authorName():
    return "Camilo Polymeris"
    
def classFactory(iface):
    from plugin import SAGAModulesPlugin
    return SAGAModulesPlugin(iface)