import GV, classes as c
from math import dist

def initMulti(objClass, count, *args):
        objList =  []
        while count > 0:
                obj = objClass(args, 1)
                count -= 1
                objList.append(obj)
        return objList

def collsions(object, objList):
        collision = False
        for obj in objList:
                if obj.id != object.id:
                        if dist(object.position, obj.position) <= object.size:
                                collision = True
                                ColObject = obj
                                break
        if collision:
                if object.mass == ColObject.mass:
                        temp = object.velocity
                        object.velocity = ColObject.velocity
                        ColObject.velocity = temp



        return collision

