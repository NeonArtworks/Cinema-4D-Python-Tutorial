####################################################################################
#
# Module Name: 3_CreateAndInsertObjects
# Project: create a new cube object and insert it into the active document
#
# Copyright(c) 2018 Florian Wagner
# Visit: www.neonartworks.at
#
#####################################################################################

import c4d
    


def main():
    
    myObject = c4d.BaseObject(c4d.Ocube)     # Create a new cube
    myObject.SetRelPos(c4d.Vector(20))       # Set the cubes position
    
    myObject.SetName("MY CUBE HAS A NAME!")  # Set the name of the cube
    
    doc.InsertObject(myObject)               # Insert the cube into the document
    c4d.EventAdd()                           # update Cinema 4D

if __name__=='__main__':
    main()
