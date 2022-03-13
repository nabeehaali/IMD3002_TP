import maya.cmds as cmds

#UI
if 'UI' in globals():
    if cmds.window(UI, exists=True):
        cmds.deleteUI(UI, window=True)

UI = cmds.window(title='Build a Garden', width=400)

cmds.columnLayout(rowSpacing=10)
cmds.text(label='Choose what you would like to have in your garden:')

cmds.intSliderGrp('width', label='Ground Width', min=10, max=15)
cmds.intSliderGrp('height', label='Ground Height', min=10, max=15)
cmds.intSliderGrp('Vine', label='Vine Length', min=1, max=3)
cmds.checkBox('Fencing', label='Include Fencing')

cmds.button(label='Generate Garden', command='generateGarden(sentence)')

cmds.showWindow(UI)

#l-system settings
axiom = 'A'
rule1 = ['A', 'AB']
rule2 = ['B', 'A']

sentence = axiom

#create fence (poly model later)
def generateFence():
    singleFence = cmds.polyCube(n='fence', width=1, height=0.5, depth=0.1)
    return singleFence

#create tree (poly model later)    
def generateTree():
    tree = cmds.polyCube(width=0.5, height=5, depth=0.5, sy=10)
    cmds.move(0, 2.5, 0)
    #branch 1
    cmds.select(tree[0] + '.f[9]')
    cmds.polyExtrudeFacet(ltz=2.5)
    #branch 2
    cmds.select(tree[0] + '.f[11]')
    cmds.polyExtrudeFacet(ltz=2.5)
    #branch 3
    cmds.select(tree[0] + '.f[31]')
    cmds.polyExtrudeFacet(ltz=2.5)
    #branch 4
    cmds.select(tree[0] + '.f[41]')
    cmds.polyExtrudeFacet(ltz=2.5)
    
#create vine 1    
def generateVine1(workingSentence):
    x = 5
    for k in workingSentence:
        if (k == rule1[0]):
            cmds.polyCube(n='objA', width=1, height=1, depth=1)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(3, x, 0)
            x -= 0.3   
        elif (k == rule2[0]):
            cmds.polyCube(n='objB', width=0.5, height=0.5, depth=0.5)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(3, x, 0)
            x -= 0.3

#create vine 2
def generateVine2(workingSentence):
    x = 5
    for k in workingSentence:
        if (k == rule1[0]):
            cmds.polyCube(n='objA', width=1, height=1, depth=1)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(-3, x, 0)
            x -= 0.3   
        elif (k == rule2[0]):
            cmds.polyCube(n='objB', width=0.5, height=0.5, depth=0.5)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(-3, x, 0)
            x -= 0.3
            
#create vine 3
def generateVine3(workingSentence):
    x = 5
    for k in workingSentence:
        if (k == rule1[0]):
            cmds.polyCube(n='objA', width=1, height=1, depth=1)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(0, x, 3)
            x -= 0.3   
        elif (k == rule2[0]):
            cmds.polyCube(n='objB', width=0.5, height=0.5, depth=0.5)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(0, x, 3)
            x -= 0.3

#create vine 4
def generateVine4(workingSentence):
    x = 5
    for k in workingSentence:
        if (k == rule1[0]):
            cmds.polyCube(n='objA', width=1, height=1, depth=1)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(0, x, -3)
            x -= 0.3   
        elif (k == rule2[0]):
            cmds.polyCube(n='objB', width=0.5, height=0.5, depth=0.5)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(0, x, -3)
            x -= 0.3

#create garden    
def generateGarden(sentence):
    #pulling values from sliders
    width = cmds.intSliderGrp('width', query=True, value=True)
    height = cmds.intSliderGrp('height', query=True, value=True)
    
    #check if fencing is selected
    if (cmds.checkBox('Fencing', query=True, value=True) == True):
    
        side1 = generateFence()
        
        for i in range(width-1):
            cmds.move(-(width/2.0)-0.5+ (i+1), 0.25, height/2.0)
            cmds.duplicate(st=True)
         
        side2 = generateFence()    
        
        for i in range(width-1):
            cmds.move(-(width/2.0)-0.5+ (i+1), 0.25, -height/2.0)
            cmds.duplicate(st=True)
        
        side3 = generateFence()
        
        for i in range(height-1):
            cmds.move(width/2.0, 0.25, -(height/2.0)-0.5+ (i+1))
            cmds.rotate(0, 90, 0)
            cmds.duplicate(st=True)
        
        side4 = generateFence() 
        
        for i in range(height-1):
            cmds.move(-width/2.0, 0.25, -(height/2.0)-0.5+ (i+1))
            cmds.rotate(0, 90, 0)
            cmds.duplicate(st=True)
            
        cmds.select(all=True)
        cmds.group(n='fence')
        
    #create ground
    ground = cmds.polyPlane(n='ground', width=width, height=height)
    
    #tree
    generateTree()
    
    #vines
    iterations = cmds.intSliderGrp('Vine', query=True, value=True)
     
    for i in range(iterations):
        for c in sentence:
            if (c == rule1[0]):
                sentence += rule1[1]
            elif (c == rule2[0]):
                sentence += rule2[1]
    
    vine1 = generateVine1(sentence)
    vine2 = generateVine2(sentence)
    vine3 = generateVine3(sentence)
    vine4 = generateVine4(sentence)
    

    
    