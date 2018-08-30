####################################################################################
#
# Module Name: 0_HelloWorld
# Project: Prints "Hello World!" into a dialog.
#
# Copyright(c) 2018 Florian Wagner
# Visit: www.neonartworks.at
#
#####################################################################################

import c4d
from c4d import gui 


def main():
    gui.MessageDialog('Hello World!') #c4d.gui.MessageDialog('Hello World!')

if __name__=='__main__':
    main()
