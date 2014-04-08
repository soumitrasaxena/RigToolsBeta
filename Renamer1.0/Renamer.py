import maya.cmds as cmds

def createUI( pWindowTitle):
	
	windowID = 'myWindowID'
	
	if cmds.window(windowID , exists = True):
		cmds.deleteUI(windowID)
		
	cmds.window(windowID , title = pWindowTitle , sizeable = False , resizeToFitChildren = True)
	
	cmds.rowColumnLayout( numberOfColumns = 3 , columnWidth =[(1,200) , (2,200) , (3,200)])
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.text(label = 'Enter the prefix (if any)')
	cmds.textField('prefix')
	
	cmds.separator ( h = 30 , style = 'none')
	
	
	cmds.text(label = 'Enter the suffix (if any)')
	cmds.textField('suffix')
	
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.button(label = 'Add Prefix/Suffix to selected' , command = renameSelected)	
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')	
	
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.button(label = 'Add Prefix/Suffix to entire chain' , command = renameChain)	
	cmds.separator ( h = 30 , style = 'none')

	
	cmds.showWindow()
	
def renameSelected(*pArgs):
	
	selection = cmds.ls(selection = True)
	print selection
	
	prefix = cmds.textField('prefix' , query = True , text = True)
	suffix = cmds.textField('suffix' , query = True , text = True)
	
	for i , name in enumerate(selection):
		cmds.select(name)
		newname = prefix + name + suffix
		cmds.rename(newname)
		

def renameChain(*pArgs):
	
	selection = cmds.ls(selection = True)
	print selection
	
	oldnames = cmds.listRelatives(selection , ad = True)
	
	print oldnames
	print len(oldnames) 
	
	prefix = cmds.textField('prefix' , query = True , text = True)
	suffix = cmds.textField('suffix' , query = True , text = True)
	
	for i , name in enumerate(oldnames):
		cmds.select(name)
		newname = prefix + name + suffix
		cmds.rename(newname)
	
	for i , name in enumerate(selection):
		cmds.select(name)
		newname = prefix + name + suffix
		cmds.rename(newname)
		
createUI('Renamer 1.0')