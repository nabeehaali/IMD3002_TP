import maya.cmds as cmds
import random
import math

'''
def modelDaisies():
    #poly model stem
    stemHeight = random.uniform(0.3,0.5)
    stem = cmds.polyCylinder(sx=2, sy=4, sz=3, h=stemHeight, r = 0.01)
    cmds.move(0, stemHeight/2, 0)
    cmds.polyMoveEdge(stem[0] + '.e[100:119]', tz=-0.02)
    cmds.polyMoveEdge(stem[0] + '.e[60:79]', tz=-0.02)
    
   
    #poly model centre
    centre = cmds.polyCylinder(sx=1, sy=1, sz=2, h=0.02, r=0.05)
    cmds.move(0, stemHeight, 0)
    cmds.polyMoveFacet(centre[0] + '.f[80:99]', ty=0.013)
    
    
    #poly model first layer of petals
    petal = cmds.polyCube(n='daisyPetal', sx=3, sz=2, w=0.10, h=0.005, d=0.12)
    cmds.polyMoveEdge(petal[0] + '.e[43]', tx=-0.20)
    cmds.select(petal[0] + '.e[21]','.e[33]')
    cmds.scale(1,1,0.6)
    cmds.select(petal[0] + '.f[18:19]')
    cmds.polyMoveFacet(petal[0] + '.f[18:19]', tx=0.05)
    cmds.polyMoveVertex(petal[0] + '.vtx[9]', tx=-0.06)
    cmds.polyMoveVertex(petal[0] + '.vtx[21]', tx=-0.06)
    cmds.polyMoveVertex(petal[0] + '.vtx[0:2]', petal[0] + '.vtx[4:6]', petal[0] + '.vtx[9:10]', petal[0] + '.vtx[12:14]', petal[0] + '.vtx[16:18]', petal[0] + '.vtx[21:22]', ty=0.025)
    cmds.polyMoveEdge(petal[0] + '.e[18]', petal[0] + '.e[30]', tx=-0.17)
    cmds.polyMoveEdge(petal[0] + '.e[18]', tz=-0.014, ty=-0.017)
    cmds.polyMoveEdge(petal[0] + '.e[30]', tz=0.014, ty=-0.017)
    
    cmds.polyMoveVertex(petal[0] + '.vtx[1:2]', petal[0] + '.vtx[5:6]', petal[0] + '.vtx[9:10]', petal[0] + '.vtx[13:14]', petal[0] + '.vtx[17:18]', petal[0] + '.vtx[21:22]',  tx=-0.05)
    
    cmds.select(petal[0])
    cmds.move(0.2, 0, 0, petal[0] + ".scalePivot", petal[0] + ".rotatePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)

    #duplicate petal in a circle
    for i in range(9):
        cmds.rotate(0, i*-36, 0)
        cmds.duplicate(st=True)
    
    cmds.select('daisyPetal', 'daisyPetal1', 'daisyPetal2','daisyPetal3','daisyPetal3','daisyPetal4','daisyPetal5','daisyPetal6','daisyPetal7','daisyPetal8','daisyPetal9')
    petalGrp = cmds.polyUnite(n='p1')
    cmds.xform(petalGrp[0], centerPivots = True)
    cmds.move(-0.202, stemHeight-0.005, 0)
    cmds.rotate(0,10.4,0)
    cmds.scale(0.3,0.3,0.3)
        
    cmds.delete(ch=True)  
    
    #poly model second layer of petals
    petalL2 = cmds.polyCube(n='daisyPetalL2', sx=3, sz=2, w=0.10, h=0.005, d=0.12)
    cmds.polyMoveEdge(petalL2[0] + '.e[43]', tx=-0.20)
    cmds.select(petalL2[0] + '.e[21]','.e[33]')
    cmds.scale(1,1,0.6)
    cmds.select(petalL2[0] + '.f[18:19]')
   
    cmds.polyMoveEdge(petalL2[0] + '.e[18]', petalL2[0] + '.e[30]', tx=-0.17)
    cmds.polyMoveEdge(petalL2[0] + '.e[18]', tz=-0.014, ty=-0.017)
    cmds.polyMoveEdge(petalL2[0] + '.e[30]', tz=0.014, ty=-0.017)
    
    cmds.polyMoveVertex(petalL2[0] + '.vtx[1:2]', petalL2[0] + '.vtx[5:6]', petalL2[0] + '.vtx[9:10]', petalL2[0] + '.vtx[13:14]', petalL2[0] + '.vtx[17:18]', petalL2[0] + '.vtx[21:22]',  tx=-0.05)
    
  
    cmds.select(petalL2[0])
    cmds.move(0.2, 0, 0, petalL2[0] + ".scalePivot", petalL2[0] + ".rotatePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)

    #duplicate petal in a circle
    for i in range(10):
        cmds.rotate(0, i*-36, 0)
        cmds.duplicate(st=True)
    
    cmds.select('daisyPetalL2', 'daisyPetalL3','daisyPetalL4','daisyPetalL5','daisyPetalL6','daisyPetalL7','daisyPetalL8','daisyPetalL9','daisyPetalL10','daisyPetalL11', 'daisyPetalL12')
    petalGrpL2 = cmds.polyUnite(n='p2')
    cmds.xform(petalGrpL2[0], centerPivots = True)
    cmds.move(-0.202, stemHeight, 0)
    cmds.rotate(0,18,0)
    cmds.scale(0.3,0.3,0.3)
 
    cmds.delete(ch=True)
    
    #poly model third layer of petals
    petalL3 = cmds.polyCube(n='daisyPetalLB', sx=3, sz=2, w=0.10, h=0.005, d=0.12)
    cmds.polyMoveEdge(petalL3[0] + '.e[43]', tx=-0.20)
    cmds.select(petalL3[0] + '.e[21]','.e[33]')
    cmds.scale(1,1,0.6)
    cmds.select(petalL3[0] + '.f[18:19]')
   
    cmds.polyMoveEdge(petalL3[0] + '.e[18]', petalL3[0] + '.e[30]', tx=-0.17)
    cmds.polyMoveEdge(petalL3[0] + '.e[18]', tz=-0.014, ty=-0.017)
    cmds.polyMoveEdge(petalL3[0] + '.e[30]', tz=0.014, ty=-0.017)
    
    cmds.polyMoveVertex(petalL3[0] + '.vtx[1:2]', petalL3[0] + '.vtx[5:6]', petalL3[0] + '.vtx[9:10]', petalL3[0] + '.vtx[13:14]', petalL3[0] + '.vtx[17:18]', petalL3[0] + '.vtx[21:22]',  tx=-0.05)
    
  
    cmds.select(petalL3[0])
    cmds.move(0.2, 0, 0, petalL3[0] + ".scalePivot", petalL3[0] + ".rotatePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)

    #duplicate petal in a circle
    for i in range(10):
        cmds.rotate(0, i*-36, 0)
        cmds.duplicate(st=True)
    
    cmds.select('daisyPetalLB', 'daisyPetalLB1', 'daisyPetalLB2','daisyPetalLB3','daisyPetalLB4','daisyPetalLB5','daisyPetalLB6','daisyPetalLB7','daisyPetalLB8','daisyPetalLB9','daisyPetalLB10')
    petalGrpL3 = cmds.polyUnite(n='p3')
    cmds.xform(petalGrpL3[0], centerPivots = True)
    cmds.move(-0.202, stemHeight+0.006, 0)
    cmds.rotate(0,34.7,0)
    cmds.scale(0.3,0.3,0.3)
    
    cmds.delete(ch=True)
      
    cmds.select(stem,centre,'p1','p2','p3')
    daisy = cmds.polyUnite(n='daisy')

    cmds.delete(ch=True)

'''
#poly model grass patch
def modelGrassPatch():
    numRange = random.randint(10,30)    
    
    tallGrass_A = cmds.polyCone(sx=4, r=0.04, h=0.6)
    cmds.move(0,0.3,0.3)
    cmds.polyCut(cd='Y', ch=1)
    cmds.polyMoveVertex(tallGrass_A[0] + '.vtx[4]', tz=-0.05, ty=-0.3)
    cmds.polyMoveEdge(tallGrass_A[0] + '.e[12:15]', tz=-0.05, ty=-0.1)
    cmds.select(tallGrass_A[0] + '.e[12:15]')
    cmds.rotate(-30,0,0)
    cmds.scale(1.5,1.5,1.5)
    cmds.polySoftEdge(a=1)
    
    
    tallGrass_B = cmds.polyCone(sx=4, r=0.03, h=0.4)
    cmds.move(-0.2,0.2,0.1)
    cmds.polyCut(cd='Y', ch=1)
    cmds.polyMoveVertex(tallGrass_B[0] + '.vtx[4]', tx=-0.05)
    cmds.select(tallGrass_B[0] + '.e[12:15]')
    cmds.scale(1.3,1.3,1.3)
    cmds.polySoftEdge(a=1)

    tallGrass_C = cmds.polyCube(sy=2, w=0.07, h=0.1, d=0.05)
    cmds.move(0.4,0.05,0.6)
    cmds.select(tallGrass_C[0] + '.f[2]')
    cmds.scale(0.5,0.5,0.5)
    cmds.polyMoveEdge(tallGrass_C[0] + '.e[18:19]', tallGrass_C[0] + '.e[1]', tallGrass_C[0] + '.e[4]', tz=0.03)
    cmds.scale(0.7,0.7,0.7)
    cmds.polySoftEdge(a=1)
    
    tallGrass_D = cmds.polyCube(sy=2, w=0.07, h=0.3, d=0.05)
    cmds.move(0.4,0.15,-0.1)
    cmds.select(tallGrass_D[0] + '.f[2]')
    cmds.scale(0.5,0.5,0.5)
    cmds.polyMoveEdge(tallGrass_D[0] + '.e[18:19]', tallGrass_D[0] + '.e[1]', tallGrass_D[0] + '.e[4]', tz=-0.05)
    cmds.scale(0.7,0.7,0.7)
    cmds.polySoftEdge(a=1)
    
    tallGrass_E = cmds.polyCone(sx=4, r=0.03, h=0.4)
    cmds.move(0.7,0.2,0.1)
    cmds.polyCut(cd='Y', ch=1)
    cmds.polyMoveVertex(tallGrass_E[0] + '.vtx[4]', tx=-0.05)
    cmds.select(tallGrass_E[0] + '.e[12:15]')
    cmds.scale(1.3,1.3,1.3)
    cmds.polySoftEdge(a=1)
    
    tallGrass_F = cmds.polyCone(sx=4, r=0.03, h=0.4)
    cmds.move(1.2,0.2,0.2)
    cmds.polyCut(cd='Y', ch=1)
    cmds.polyMoveVertex(tallGrass_F[0] + '.vtx[4]', tx=-0.05)
    cmds.select(tallGrass_F[0] + '.e[12:15]')
    cmds.rotate(0,60,0)
    cmds.scale(1.3,1.3,1.3)
    cmds.polySoftEdge(a=1)

    tallGrass_G = cmds.polyCube(sy=2, w=0.07, h=0.3, d=0.05)
    cmds.move(0.8,0.15,-0.6)
    cmds.select(tallGrass_G[0] + '.f[2]')
    cmds.scale(0.5,0.5,0.5)
    cmds.polyMoveEdge(tallGrass_G[0] + '.e[18:19]', tallGrass_G[0] + '.e[1]', tallGrass_G[0] + '.e[4]', tz=-0.05)
    cmds.scale(0.7,0.7,0.7)
    cmds.polySoftEdge(a=1)
    
    tallGrass_H = cmds.polyCube(sy=2, w=0.07, h=0.3, d=0.05)
    cmds.move(0,0.15,0)
    cmds.select(tallGrass_H[0] + '.f[2]')
    cmds.scale(0.5,0.5,0.5)
    cmds.polyMoveEdge(tallGrass_H[0] + '.e[18:19]', tallGrass_H[0] + '.e[1]', tallGrass_H[0] + '.e[4]', tz=-0.05)
    cmds.scale(0.7,0.7,0.7)
    cmds.rotate(0,-45,0)
    cmds.polySoftEdge(a=1)
    
    tallGrass_I = cmds.polyCube(sy=2, w=0.07, h=0.6, d=0.05)
    cmds.move(0.48,0.3,0.27)
    cmds.select(tallGrass_I[0] + '.f[2]')
    cmds.scale(0.5,0.5,0.5)
    cmds.polyMoveEdge(tallGrass_I[0] + '.e[18:19]', tallGrass_I[0] + '.e[1]', tallGrass_I[0] + '.e[4]', tz=-0.05)
    cmds.scale(0.7,0.7,0.7)
    cmds.rotate(0,34,0)
    cmds.polySoftEdge(a=1)
    
    cmds.select(tallGrass_A,tallGrass_B,tallGrass_C,tallGrass_D,tallGrass_E)
    grassPatch = cmds.polyUnite()
    
    cmds.delete(ch=True)
    
    
    cmds.scale(1.3,1.3,1.3)
    
'''
    cmds.duplicate(st=True)
    cmds.move(-0.378,0,-0.107)
    cmds.rotate(-2.7,-36,0.35)
    
    
    cmds.duplicate()
    cmds.move(0.01,0,-0.155)
    cmds.rotate(0,-70,0)
    
    cmds.duplicate()
    cmds.move(0.035,0,0.027)
    cmds.rotate(0,-111,0)
    
    cmds.duplicate()
    cmds.move(0.092,0,0.028)
    cmds.rotate(0,-37,0)
    
    cmds.scale(1.5,1.5,1.5)
    
    cmds.delete(ch=True)
    
    cmds.select(all=True)
    bigGrassPatch = cmds.polyUnite(n='bigGrassPatch')



def modelSunflowers():
    #poly model stem
    stemHeight = random.uniform(1.3,1.5)
    stem = cmds.polyCylinder(sx=2, sy=4, sz=3, h=stemHeight, r = 0.02)
    cmds.move(0, stemHeight/2, 0)
    cmds.polyMoveEdge(stem[0] + '.e[100:119]', tz=0.04)
    
    #poly model leaves
    leaf = cmds.polyCube(sx=3, sz=2, w=0.5, h=0.005, d=0.3)
    cmds.polyMoveEdge(leaf[0] + '.e[43]', tx=-0.20)
    cmds.select(leaf[0] + '.e[21]','.e[33]')
    cmds.scale(1,1,0.05)
    cmds.select(leaf[0] + '.f[18:19]')
    cmds.polyMoveFacet(leaf[0] + '.f[18:19]', tx=0.05)
    cmds.polyMoveVertex(leaf[0] + '.vtx[9]', tx=-0.06)
    cmds.polyMoveVertex(leaf[0] + '.vtx[21]', tx=-0.06)
    cmds.polyMoveVertex(leaf[0] + '.vtx[0:2]', leaf[0] + '.vtx[4:6]', leaf[0] + '.vtx[9:10]', leaf[0] + '.vtx[12:14]', leaf[0] + '.vtx[16:18]', leaf[0] + '.vtx[21:22]', ty=0.04)
    cmds.polyExtrudeFacet(leaf[0] + '.f[18:19]', ltz=0.1)
    cmds.polyMoveFacet(ty=-0.05)
    cmds.select(leaf[0] + '.f[1]', leaf[0] + '.f[10]')
    cmds.scale(1,1,1.2)
    cmds.select(leaf[0] + '.vtx[1]', leaf[0] + '.vtx[5]', leaf[0] + '.vtx[13]', leaf[0] + '.vtx[17]')
    cmds.scale(1,1,1.2)
    cmds.polyMoveVertex(leaf[0] + '.vtx[1]', leaf[0] + '.vtx[5]', leaf[0] + '.vtx[13]', leaf[0] + '.vtx[17]', tx=-0.05)
    cmds.polyMoveVertex(leaf[0] + '.vtx[9]', leaf[0] + '.vtx[10]', leaf[0] + '.vtx[21]', leaf[0] + '.vtx[22]', ty=0.05)
    cmds.select(leaf[0])
    cmds.scale(0.9,0.7,0.7)
    cmds.rotate(-132,32,-114)
    cmds.move(0.107,stemHeight-0.9,0.166)
    
    leaf_B = cmds.duplicate(st=True)
    cmds.rotate(-214,-14,-118)
    cmds.move(0.145,stemHeight-0.6,-0.075)
    
    
    leaf_C = cmds.duplicate(st=True)
    cmds.rotate(-129,27,-108)
    cmds.move(0.055,stemHeight-0.4,0.098)
    cmds.scale(0.5,0.4,0.4)
    
    leaves = cmds.group(leaf[0], leaf_B[0], leaf_C[0])
    
    #poly model centre
    centre = cmds.polyCylinder(sx=1, sy=1, sz=2, h=0.02, r=0.15)
    cmds.move(-0.01, stemHeight, 0)
    cmds.rotate(0,0,35)
    cmds.polyExtrudeFacet(centre[0] + '.f[60:79]', ltz=0.01)
    cmds.select(centre[0] + '.f[80:99]')
    cmds.scale(1.7,1,1.7)
    cmds.move(-0.01, 0.01, 0, relative=True)
    cmds.polyExtrudeFacet(centre[0] + '.f[80:99]')
    cmds.scale(0.7,1,0.7)
    cmds.polyExtrudeFacet(centre[0] + '.f[80:99]')
    cmds.move(0, -0.01, 0, relative=True)
    
    
    #poly model first layer of petals
    petal = cmds.polyCube(n='sunPetal', sx=3, sz=2, w=0.10, h=0.005, d=0.12)
    cmds.polyMoveEdge(petal[0] + '.e[43]', tx=-0.20)
    cmds.select(petal[0] + '.e[21]','.e[33]')
    cmds.scale(1,1,0.6)
    cmds.select(petal[0] + '.f[18:19]')
    cmds.polyMoveFacet(petal[0] + '.f[18:19]', tx=0.05)
    cmds.polyMoveVertex(petal[0] + '.vtx[9]', tx=-0.06)
    cmds.polyMoveVertex(petal[0] + '.vtx[21]', tx=-0.06)
    cmds.polyMoveVertex(petal[0] + '.vtx[0:2]', petal[0] + '.vtx[4:6]', petal[0] + '.vtx[9:10]', petal[0] + '.vtx[12:14]', petal[0] + '.vtx[16:18]', petal[0] + '.vtx[21:22]', ty=0.025)

    cmds.select(petal[0])
    cmds.move(0.25, 0, 0, petal[0] + ".scalePivot", petal[0] + ".rotatePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)

    #duplicate petal in a circle
    for i in range(9):
        cmds.rotate(0, i*-36, 0)
        cmds.duplicate(st=True)
    
    cmds.select('sunPetal', 'sunPetal1','sunPetal2','sunPetal3','sunPetal4','sunPetal5','sunPetal6','sunPetal7','sunPetal8','sunPetal9')
    petalGrp = cmds.polyUnite()
    cmds.xform(petalGrp[0], centerPivots = True)
    cmds.move(-0.263, stemHeight, 0)
    cmds.rotate(0,0,35)
    cmds.scale(0.7,0.7,0.7)
        
    cmds.delete(ch=True)  
    
    #poly model second layer of petals
    petalL2 = cmds.polyCube(n='sunPetalL2', sx=3, sz=2, w=0.10, h=0.005, d=0.12)
    cmds.polyMoveEdge(petalL2[0] + '.e[43]', tx=-0.20)
    cmds.select(petalL2[0] + '.e[21]','.e[33]')
    cmds.scale(1,1,0.6)
    cmds.select(petalL2[0] + '.f[18:19]')
    cmds.polyMoveFacet(petalL2[0] + '.f[18:19]', tx=0.05)
    cmds.polyMoveVertex(petalL2[0] + '.vtx[9]', tx=-0.06)
    cmds.polyMoveVertex(petalL2[0] + '.vtx[21]', tx=-0.06)

    cmds.select(petalL2[0])
    cmds.move(0.25, 0, 0, petalL2[0] + ".scalePivot", petalL2[0] + ".rotatePivot", absolute=True)
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)

    #duplicate petal in a circle
    for i in range(9):
        cmds.rotate(0, i*-36, 0)
        cmds.duplicate(st=True)
    
    cmds.select('sunPetalL2', 'sunPetalL3','sunPetalL4','sunPetalL5','sunPetalL6','sunPetalL7','sunPetalL8','sunPetalL9','sunPetalL10','sunPetalL11')
    petalGrpL2 = cmds.polyUnite()
    cmds.xform(petalGrpL2[0], centerPivots = True)
    cmds.move(-0.263, stemHeight, 0)
    cmds.rotate(0,15,35)
    cmds.scale(0.7,0.7,0.7)
    
    cmds.select(stem,leaves,centre,petalGrp,petalGrpL2)
    sunflowers = cmds.polyUnite(n='sunflower')
    cmds.delete(ch=True)
   
modelSunflowers()
'''

modelGrassPatch()