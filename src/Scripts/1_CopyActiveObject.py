####################################################################################
#
# Module Name: 1_CopyActiveObject
# Project: Copies the active (selected) object into the object manager
#
# Copyright(c) 2018 Florian Wagner
# Visit: www.neonartworks.at
#
#####################################################################################

import c4d

def main():
    
    '''
    "doc" is predefined by the script-manager
    "doc" can also be retrieved by calling "c4d.documents.GetActiveDocument()"
    '''
    
    myActiveObject = doc.GetActiveObject() #returns the active object or None if no object is selected
    
    # if nothing was selected, do nothing. 
    # We could also give the user a message by using the c4d.gui.MessageDialog("MESSAGE") 
    # which we learned from 0_HelloWorld
    if not myActiveObject: return 
    
    myNewObject = myActiveObject.GetClone() #clones the active object
    doc.InsertObject(myNewObject) #inserts the cloned object into the document
    
    c4d.EventAdd() #EventAdd tells Cinema 4D that we have changed something, and that it should update
    
    
    
if __name__=='__main__':
    main()
