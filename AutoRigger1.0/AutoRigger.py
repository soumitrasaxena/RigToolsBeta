#AutoRigger 1.0

#Code starts here

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
	
	cmds.text(label = 'Enter the path of the code')
	cmds.textField('path')
	
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.button(label = 'Generate' , command = generate)	
	cmds.separator ( h = 30 , style = 'none')
	cmds.button(label = 'Build' , command = build)
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')	

	
	cmds.showWindow()
	
	
def generate(*pArgs):
	path = cmds.textField('path' , query = True , text = True)
	cmds.file(path+'Rig_2.mb' , i = True)
	
def build(*pArgs):	
	
	joints = cmds.ls(type = 'joint')
	
	print joints
	print len(joints)
	
	meshes = cmds.ls(type = 'mesh')
	
	print meshes
	print len(meshes)
	
	
	cmds.select(joints , meshes)
	
	for mesh in meshes :
		cmds.skinCluster(joints, mesh)
	

createUI('AutoRigger 1.0')





