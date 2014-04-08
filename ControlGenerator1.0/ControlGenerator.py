import maya.cmds as cmds

object_stack = []

def create_circle(*pArgs):
	
	#Remove the previously added objects to the stack
	if len(object_stack) != 0:
		cmds.delete(object_stack.pop())
	
	selection = cmds.ls(selection= True)
	
	query_translation = cmds.xform(query = True , sp = True , ws = True)
		
	_circle = cmds.circle(r = 0.3 , n = 'control_circle' )
	
	#Add it to the stack
	object_stack.append(_circle[0])
	
	#Move and rotate it to the current position
	cmds.move(query_translation[0] , query_translation[1] , query_translation[2] ,_circle, absolute = True)
		
	#Preserve the selection
	cmds.select(selection)
	
def create_square(*pArgs):
	
	
	#Remove the previously added objects to the stack
	if len(object_stack) != 0:
		cmds.delete(object_stack.pop())
		
	
	selection = cmds.ls(selection= True)
	
	query_pivot = cmds.xform(query = True , sp = True , ws = True)
	
	square = cmds.nurbsSquare( n = 'control_square')
	
	#Add it to the stack
	object_stack.append(square[0])
	
	#Move it to the current position
	cmds.move(query_pivot[0] , query_pivot[1] , query_pivot[2] , square, absolute = True)
	#Preserve the selection
	cmds.select(selection)

def create_cube(*pArgs):	
	
	#Remove the previously added objects to the stack
	if len(object_stack) != 0:
		cmds.delete(object_stack.pop())		
	
	selection = cmds.ls(selection= True)
	
	query_pivot = cmds.xform(query = True , sp = True , ws = True)
	
	cube = cmds.curve(n = 'control_cube' , d = 1 ,  p = [(1,0.5 , 0.5) , (1,0.5 , -0.5) , (-1,0.5 , -0.5) , (-1,0.5 , 0.5) , (1,0.5 , 0.5) , 
	(1,-0.5 , 0.5) , (1,-0.5 , -0.5) , (-1,-0.5 , -0.5) ,(-1,-0.5 , 0.5) , ( 1,-0.5 , 0.5) , (1,-0.5 , -0.5) , (1,0.5 , -0.5) , (-1,0.5 , -0.5) , (-1,-0.5 , -0.5) , (-1,-0.5 , 0.5) ,(-1,0.5 , 0.5)] )

	#Add it to the stack
	object_stack.append(cube)
	
	#Move it to the current position
	cmds.move(query_pivot[0] , query_pivot[1] , query_pivot[2] , cube, absolute = True)
	#Preserve the selection
	cmds.select(selection)

	
def refresh_stack(*pArgs):
	#Empty the current stack	
	for item in object_stack:
		object_stack.remove(item)
	
	#Empty the current selection
	selection = []


def createUI( pWindowTitle):
	
	windowID = 'myWindowID'
	
	if cmds.window(windowID , exists = True):
		cmds.deleteUI(windowID)
		
	cmds.window(windowID , title = pWindowTitle , sizeable = False , resizeToFitChildren = True)
	
	cmds.rowColumnLayout( numberOfColumns = 4 , columnWidth =[(1,300) , (2,200) , (3,200), (4,200)])
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.text(label = 'Choose the desired control shape : ')
		
	cmds.radioCollection()
	cmds.radioButton(label = 'Circle' , onCommand = create_circle)
	cmds.radioButton(label = 'Square' , onCommand = create_square)
	cmds.radioButton(label = 'Cube' , onCommand = create_cube)
	
	cmds.separator ( h = 10 , style = 'none')
	cmds.separator ( h = 10 , style = 'none')
	cmds.separator ( h = 10 , style = 'none')
	cmds.separator ( h = 10 , style = 'none')
	
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.button(label = 'Done' , command = refresh_stack)	
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
		
	cmds.showWindow()
		
createUI('Control Generator 1.0')

