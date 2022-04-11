import maya.cmds as cmds
import random
import math

#UI
if 'UI' in globals():
    if cmds.window(UI, exists=True):
        cmds.deleteUI(UI, window=True)

UI = cmds.window(title='Build a Garden', width=400)

cmds.columnLayout(rowSpacing=10, columnAlign="center")
cmds.text(label='Select the features that you would like your garden to have:')

gardenName = cmds.textFieldGrp(label='Garden Name')

cmds.text(label='Ground Settings:')

cmds.intSliderGrp('width', label='Ground Width', min=10, max=15)
cmds.intSliderGrp('height', label='Ground Height', min=10, max=15)

cmds.text(label='Gazebo Settings:')

cmds.intSliderGrp('Vine', label='Vine Length', min=1, max=3)

cmds.text(label='Decoration Settings:')

#cmds.rowColumnLayout(nc=3)
cmds.checkBox('Fencing', label='Include Fencing')
cmds.checkBox('Sunflowers', label='Include Sunflowers')
cmds.checkBox('Daisies', label='Include Daisies')

cmds.button(label='Generate Garden', width=400, command='generateGarden(sentence)')
cmds.button(label='Clear Garden', width=400, align='right', command='clear()')

cmds.showWindow(UI)

#l-system settings
axiom = 'A'
rule1 = ['A', 'AB']
rule2 = ['B', 'A']

sentence = axiom

#create fence
def generateFence(): 
    
    #fence panels
    panel1 = cmds.polyCube(width=1, height=0.03, depth=0.03)
    cmds.move(0, 0, -0.05)
    panel2 = cmds.polyCube(width=1, height=0.03, depth=0.03)
    cmds.move(0, -0.1, -0.05)
    
    #fence pillars
    pillarA = cmds.polyCube(width=0.12, height=0.9, depth=0.05)
    cmds.move(-0.414, 0, 0)
    cmds.move(-0.414, -0.35, 0, pillarA[0] + ".scalePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)
    cmds.scale(1, 0.95, 1)
    cmds.move(0, -0.005, 0)
    
    pillarB = cmds.polyCube(width=0.12, height=0.9, depth=0.05)
    cmds.move(-0.247, 0, 0)
    cmds.move(-0.247, -0.35, 0, pillarB[0] + ".scalePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)
    cmds.scale(1, 0.9, 1)
    cmds.move(0, -0.01, 0)
    
    pillarC = cmds.polyCube(width=0.12, height=0.9, depth=0.05)
    cmds.move(-0.082, 0, 0)
    
    pillarD = cmds.polyCube(width=0.12, height=0.9, depth=0.05)
    cmds.move(0.082, 0, 0)
    
    pillarE = cmds.polyCube(width=0.12, height=0.9, depth=0.05)
    cmds.move(0.247, 0, 0)
    cmds.move(0.247, -0.35, 0, pillarE[0] + ".scalePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)
    cmds.scale(1, 0.9, 1)
    cmds.move(0, -0.01, 0)
    
    pillarF = cmds.polyCube(width=0.12, height=0.9, depth=0.05)
    cmds.move(0.414, 0, 0)
    cmds.move(0.414, -0.35, 0, pillarF[0] + ".scalePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)
    cmds.scale(1, 0.95, 1)
    cmds.move(0, -0.005, 0)
    
    #full fence
    cmds.select(panel1, panel2, pillarA, pillarB, pillarC, pillarD, pillarE, pillarF)
    singleFence = cmds.polyUnite(n='singleFence')

    return singleFence

#create tree (poly model later)    
def generateGazebo():
    
    #thick border on side
    pillar1 = cmds.polyCube(n='pillar1', width=0.3, height=6, depth=0.3)
    cmds.move(-2, 3, 0)
    pillar2 = cmds.polyCube(n='pillar2', width=0.3, height=6, depth=0.3)
    cmds.move(2, 3, 0)
    board1 = cmds.polyCube(n='board1', width=4, height=0.5, depth=0.15)
    cmds.move(0, 1, 0.075)
    board2 = cmds.polyCube(n='board2', width=5.2, height=0.5, depth=0.3)
    cmds.move(0, 6, 0)
    cmds.select(board2[0] + '.e[11]')
    cmds.polyMoveEdge(tx=-0.2)
    cmds.select(board2[0] + '.e[10]')
    cmds.polyMoveEdge(tx=0.2)
    
    #grid pattern
    #vetical
    vertical = cmds.polyCube(n='vertical', width=0.1, height=5.5, depth=0.1)
    cmds.move(-1.95, 3.1, -0.095)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    for i in range(13):
        cmds.move(i*0.3, 0, 0)
        cmds.duplicate(st=True)
    #horizontal    
    horizontal = cmds.polyCube(n='horizontal', width=4, height=0.1, depth=0.1)
    cmds.move(0, 6, -0.095)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    for i in range(17):
        cmds.move(0, i*-0.3, 0)
        cmds.duplicate(st=True)
    
    #create both sides    
    cmds.select('vertical*', 'horizontal*', pillar1, pillar2, board1, board2)
    cmds.polyUnite(n='gazeboSide1')
    cmds.delete(ch=True)
    cmds.move(0, 0, 2.5)
    cmds.duplicate(n='gazeboSide2', st=True)
    cmds.move(0, 0, -2.5)
    cmds.rotate(0, 180, 0)
    
    #top
    top = cmds.polyCube(n='top', width=5.2, height=0.2, depth=5.3, sx=15)
    cmds.move(0, 6.4, 0)
    cmds.select(top[0] + '.f[46]', top[0] + '.f[48]', top[0] + '.f[50]', top[0] + '.f[52]', top[0] + '.f[54]', top[0] + '.f[56]', top[0] + '.f[58]')
    cmds.polyExtrudeFacet(ltz=0.2)
    cmds.select(top[0] + '.f[15]', top[0] + '.f[17]', top[0] + '.f[19]', top[0] + '.f[21]', top[0] + '.f[23]', top[0] + '.f[25]', top[0] + '.f[27]', top[0] + '.f[29]')
    cmds.polyExtrudeFacet(ltz=0.09)
    
    #full gazebo
    cmds.select(top, 'gazeboSide1', 'gazeboSide2')
    cmds.polyUnite(n='gazebo')
    cmds.scale(0.72, 0.72, 0.72)
    cmds.delete(ch=True)  
    
#create vines    
def generateVine(workingSentence, posx, posz):
    y = 4.6
    for k in workingSentence:
        if (k == rule1[0]):
            leafA = cmds.polyCube(n='leafA', width=1, height=1, depth=1, sy=2)
            cmds.scale(0.15, 0.15, 0.15)
            cmds.move(posx, y, posz)
            cmds.select('.f[2]', '.f[5]')
            cmds.scale(0.3, 3.3, 0.3)
            y -= 0.3   
        elif (k == rule2[0]):
            leafB = cmds.polyCube(n='leafB', width=0.5, height=0.5, depth=0.5, sy=2)
            cmds.scale(0.25, 0.25, 0.25)
            cmds.move(posx, y, posz)
            cmds.select('.f[2]', '.f[5]')
            cmds.scale(0.3, 2.3, 0.3)
            y -= 0.3       
    
#poly model sunflowers 
def modelSunflowers():
    stemHeight = random.uniform(1,1.5)
    stem = cmds.polyCube(sy=2, w=0.07, h=stemHeight, d=0.07)
    cmds.move(0, stemHeight/2, 0)
    centre = cmds.polyCube(sy=1, w=0.2, h=0.07, d=0.2)
    cmds.move(0, stemHeight, 0)
    cmds.rotate(0,0,35)
    
    cmds.select(stem, centre)
    sunflowers = cmds.polyUnite()
     
#generate sunflowers
def generateSunflowers(width, height):
    numSunflowers = random.randint(10,30) 

    for i in range(numSunflowers):
        sunflowers = modelSunflowers()
        randX = random.uniform(((width*-1)/2)+1, (width/2)-1)  
        randY = random.uniform(0,360)
        randZ = random.uniform(((height*-1)/2)+1, (height/2)-1)
        cmds.rotate(0,randY,0)
        cmds.move(randX,0,randZ)
        cmds.delete(ch=True)   
        
#poly model daisies 
def modelDaisies():
    stemHeight = random.uniform(0.2,0.4)
    stem = cmds.polyCube(sy=2, w=0.05, h=stemHeight, d=0.05)
    cmds.move(0, stemHeight/2, 0)
    centre = cmds.polyCube(sy=1, w=0.1, h=0.05, d=0.1)
    cmds.move(0, stemHeight, 0)
    
    cmds.select(stem, centre)
    daisies = cmds.polyUnite()
     
#generate daisies
def generateDaisies(width, height):
    numDaisies = random.randint(15,40) 

    for i in range(numDaisies):
        daisies = modelDaisies()
        randX = random.uniform(((width*-1)/2)+1, (width/2)-1)  
        randY = random.uniform(0,360)
        randZ = random.uniform(((height*-1)/2)+1, (height/2)-1)
        cmds.rotate(0,randY,0)
        cmds.move(randX,0,randZ)
        cmds.delete(ch=True)   
    
#poly model grass patch
def modelGrassPatch():
    numRange = random.randint(10,30)    
    
    tallGrass_A = cmds.polyCube(sy=2, w=0.06, h=1, d=0.08)
    cmds.move(0,0.5,0.3)
    
    tallGrass_B = cmds.polyCube(sy=2, w=0.08, h=0.5, d=0.07)
    cmds.move(-0.2,0.25,0.1)
    
    tallGrass_C = cmds.polyCube(sy=2, w=0.05, h=0.8, d=0.07)
    cmds.move(0.4,0.4,0.6)
    
    tallGrass_D = cmds.polyCube(sy=2, w=0.07, h=0.3, d=0.05)
    cmds.move(0.4,0.15,-0.1)
    
    tallGrass_E = cmds.polyCube(sy=2, w=0.06, h=0.4, d=0.07)
    cmds.move(0.7,0.2,0.1)
    
    cmds.select(tallGrass_A,tallGrass_B,tallGrass_C,tallGrass_D,tallGrass_E)
    grassPatch = cmds.polyUnite()

#generate ground and grass
def generateGrasslands(width, height):
    #create ground
    ground = cmds.polyPlane(n='ground', width=width, height=height)
    area = cmds.polyEvaluate(a=True)
    print(cmds.polyEvaluate(a=True))
    print(width)
    print(height)
    
    #create tall grass
    numRange = random.randint(30,50) 
    
    #generate random number of grass patches in random positions
    for i in range(numRange):
        grassPatch = modelGrassPatch()
        randX = random.uniform(((width*-1)/2)+1, (width/2)-1)  
        randY = random.uniform(0,360)
        randZ = random.uniform(((height*-1)/2)+1, (height/2)-1)
        cmds.rotate(0,randY,0)
        cmds.move(randX,0,randZ)
        cmds.delete(ch=True)   
        

#create garden    
def generateGarden(sentence):
    #pulling values from sliders    
    width = cmds.intSliderGrp('width', query=True, value=True)
    height = cmds.intSliderGrp('height', query=True, value=True)
    
    #check if fencing is selected
    if (cmds.checkBox('Fencing', query=True, value=True) == True):
    
        side1 = generateFence()
        
        for i in range(width-1):
            cmds.move(-(width/2.0)-0.5+ (i+1), 0.45, height/2.0)
            cmds.duplicate(st=True)
        
        side2 = generateFence()
        cmds.select(side2)
        cmds.rotate(0, 180, 0)    
        
        for i in range(width-1):
            cmds.move(-(width/2.0)-0.5+ (i+1), 0.45, -height/2.0)
            cmds.duplicate(st=True)
        
        side3 = generateFence()
        
        for i in range(height-1):
            cmds.move(width/2.0, 0.45, -(height/2.0)-0.5+ (i+1))
            cmds.rotate(0, 90, 0)
            cmds.duplicate(st=True)
        
        side4 = generateFence()
     
        for i in range(height-1):
            cmds.move(-width/2.0, 0.45, -(height/2.0)-0.5+ (i+1))
            cmds.rotate(0, 270, 0)
            cmds.duplicate(st=True)
        
        cmds.select(all=True)
        cmds.delete(ch=True)
        cmds.group(n='fence')
           
    #vines
    iterations = cmds.intSliderGrp('Vine', query=True, value=True)
     
    for i in range(iterations):
        for c in sentence:
            if (c == rule1[0]):
                sentence += rule1[1]
            elif (c == rule2[0]):
                sentence += rule2[1]
    
    for i in range(20):
        vineSet1 = generateVine(sentence, i*0.25-2.5, 2.75)
        
    for i in range(20):
        vineSet2 = generateVine(sentence, i*0.25-2.5, -2.75)
    
    cmds.select('leaf*')
    cmds.polyUnite(n='vines')
    cmds.delete(ch=True)
    cmds.scale(0.7, 0.7, 0.7)
    cmds.move(0, 1.3, 0)

    
    #check if sunflowers are selected
    if (cmds.checkBox('Sunflowers', query=True, value=True) == True):
        sunflowers = generateSunflowers(width, height)
        
    #check if daisies are selected
    if (cmds.checkBox('Daisies', query=True, value=True) == True):
        daisies = generateDaisies(width, height)
        
    #ground & grass
    generateGrasslands(width, height)
    
    #tree
    generateGazebo()
    
    #group everything together
    name = cmds.textFieldGrp(gardenName, query=True, text=True)
    cmds.select(all=True)
    cmds.group(n=name)

#clear garden
def clear():
    cmds.select(all=True)
    cmds.delete()

    
    
