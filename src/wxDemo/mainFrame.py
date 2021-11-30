from .gen.frameMain import frameMain

class MainFrame(frameMain):
    def __init__(self, parent):
        frameMain.__init__(self, parent)

    def menuItemFileNewOnMenuSelection( self, event ):
        print('You pressed New button')
        event.Skip()

    def menuItemFileOpenOnMenuSelection( self, event ):
        print('You pressed Open button')
        event.Skip()

    def menuItemFileSaveOnMenuSelection( self, event ):
        print('You pressed Save On button')
        event.Skip()

    def menuItemFileSaveAsOnMenuSelection( self, event ):
        print('You pressed Save As button')
        event.Skip()

    def menuItemFileExitOnMenuSelection( self, event ):
        print('You pressed Exit button')
        event.Skip()


