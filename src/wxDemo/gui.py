import wx
from .mainFrame import MainFrame

class MainApp(wx.App):
	def OnInit(self):
		mainFrame = MainFrame(None)
		mainFrame.Show(True)
		return True

def show():
	app = MainApp()
	app.MainLoop()