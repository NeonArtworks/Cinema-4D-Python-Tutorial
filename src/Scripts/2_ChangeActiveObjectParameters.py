####################################################################################
#
# Module Name: 2_ChangeActiveObjectParameters
# Project: Changes one parameter of the active object
#
# Copyright(c) 2018 Florian Wagner
# Visit: www.neonartworks.at
#
#####################################################################################

import c4d

def main():
    
    #from sript 1_CopyActiveObject 
    myActiveObject = doc.GetActiveObject() 
    if not myActiveObject: return 
    
    ''' # INFO #
    to get a parameter what we can do is (similar like in expresso) drag and drop the desired
    parameter into the script manager.
    The parameter will appear encloesd in "[]". We need to tell the script-manager from which object
    this parameter is. Therefore we write the variable which holds our object before the "[]".
    It looks something like this: "myActiveObject[PARAMETER_ID_HERE]".
    With that in mind we can change almost any parameter from almost any object!
    ''' # INFO #
    
    myPosition = c4d.Vector(10,10,10) #creates a Cinema 4D Vector
    
    myActiveObject[c4d.ID_BASEOBJECT_REL_POSITION] = myPosition
    
    c4d.EventAdd() #from sript 1_CopyActiveObject 
    
if __name__=='__main__':
    main()
