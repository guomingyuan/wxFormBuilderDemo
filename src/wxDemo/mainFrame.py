import wx
from .gen.frameMain import frameMain, dialogAbout

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
        self.Destroy()
        event.Skip()

    def menuItemAboutOnMenuSelection( self, event ):
        aboutPanel = AboutDialog(None)
        aboutPanel.Show()
        event.Skip()

class AboutDialog(dialogAbout):
    def __init__(self, parent):
        dialogAbout.__init__(self, parent)
        self.setVersion()

    def buttonOKOnButtonClick( self, event ):
        self.Destroy()
        event.Skip()

    def setVersion(self):
        self.staticTextVersion.LabelText = '0.0.1.dev2'