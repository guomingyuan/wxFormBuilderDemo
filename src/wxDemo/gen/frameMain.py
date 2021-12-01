# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CCS simulator Demo", pos = wx.DefaultPosition, size = wx.Size( 611,403 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

		bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

		self.m_panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.m_panelMain.SetSizer( bSizer3 )
		self.m_panelMain.Layout()
		bSizer3.Fit( self.m_panelMain )
		bSizerMainFrame.Add( self.m_panelMain, 1, wx.EXPAND |wx.ALL, 0 )


		bSizerFrameMain.Add( bSizerMainFrame, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizerFrameMain )
		self.Layout()
		self.menubarMain = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.menuItemFileNew = wx.MenuItem( self.menuFile, wx.ID_ANY, u"New"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileNew )

		self.menuItemFileOpen = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Open"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileOpen )

		self.menuItemFileSave = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileSave )

		self.menuItemFileSaveAs = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Save As...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileSaveAs )

		self.menuFile.AppendSeparator()

		self.menuItemFileExit = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Exit"+ u"\t" + u"Alt+F4", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileExit )

		self.menubarMain.Append( self.menuFile, u"File" )

		self.menuEdit = wx.Menu()
		self.menubarMain.Append( self.menuEdit, u"Edit" )

		self.menuHelp = wx.Menu()
		self.menuItemAbout = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"About"+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuHelp.Append( self.menuItemAbout )

		self.menubarMain.Append( self.menuHelp, u"Help" )

		self.SetMenuBar( self.menubarMain )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.menuItemFileNewOnMenuSelection, id = self.menuItemFileNew.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemFileOpenOnMenuSelection, id = self.menuItemFileOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemFileSaveOnMenuSelection, id = self.menuItemFileSave.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemFileSaveAsOnMenuSelection, id = self.menuItemFileSaveAs.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemFileExitOnMenuSelection, id = self.menuItemFileExit.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemAboutOnMenuSelection, id = self.menuItemAbout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def menuItemFileNewOnMenuSelection( self, event ):
		event.Skip()

	def menuItemFileOpenOnMenuSelection( self, event ):
		event.Skip()

	def menuItemFileSaveOnMenuSelection( self, event ):
		event.Skip()

	def menuItemFileSaveAsOnMenuSelection( self, event ):
		event.Skip()

	def menuItemFileExitOnMenuSelection( self, event ):
		event.Skip()

	def menuItemAboutOnMenuSelection( self, event ):
		event.Skip()


###########################################################################
## Class dialogAbout
###########################################################################

class dialogAbout ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 340,250 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"\nyuehengDemo:\n\nLorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis ipsam maxime cumque inventore! Facere porro cumque quidem aliquam error itaque voluptatum, animi perferendis totam, inventore, doloribus optio reprehenderit necessitatibus quisquam.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer7.Add( self.m_staticText4, 1, wx.EXPAND, 15 )

		self.staticTextVersion = wx.StaticText( self, wx.ID_ANY, u"v 0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextVersion.Wrap( -1 )

		bSizer7.Add( self.staticTextVersion, 0, wx.ALIGN_CENTER|wx.ALL, 15 )

		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonOK, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def buttonOKOnButtonClick( self, event ):
		event.Skip()


