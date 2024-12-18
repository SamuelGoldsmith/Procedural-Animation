import math
import pygame

class Bone():
    

    def __init__(self, radius, center, speed = 1):
        self.center = center
        self.radius = radius
        self.child = None
        self.parent = None
        self.angle = 0 #angle
        self.speed = speed


    def add_child(self,radius):
        new_child = Bone(radius, (self.center[0] + self.radius , self.center[1]))
        new_child.parent = self
        self.child = new_child
        return new_child
    
    def draw_circle(self, surface, fill = True):
        if fill:
            trav_bone = self
            rights = []
            lefts = []
            run = True
            for point in self.get_face():
                rights.append(point)
            while(run):
                points = trav_bone.get_sides()
                rights.append(points[0])
                lefts.append(points[1])
                if trav_bone.child:
                    trav_bone = trav_bone.child
                else:
                    run = False
            if(len(rights) + len(lefts) > 3):
                lefts.reverse()
                shape = rights + lefts
                pygame.draw.polygon(surface, (10,20,200), shape)
            else: return -1
        
        else:
            pygame.draw.circle(surface,(70,70,70),self.center,self.radius,2)
            if self.child:
                self.child.draw_circle(surface, fill)

    def move(self, vector):
            self.center = (self.center[0] + vector[0], self.center[1] + vector[1])
            self.angle = math.atan2(vector[1], vector[0])
            self.child.follow_parent()
    def follow_parent(self):
        if not self.parent: return -1
        pr = self.parent.radius
        dx = self.parent.center[0] - self.center[0]
        dy = self.parent.center[1] - self.center[1] 

        pd = math.sqrt((dx**2) + (dy**2))
        if pd > pr:
            scale = pr/pd
            self.center = (self.center[0] + ((dx - (pr * math.cos(math.atan2(dy,dx)))) * scale), self.center[1] + ((dy - (pr * math.sin(math.atan2(dy,dx)))) * scale))
            self.angle = math.atan2(dy,dx)
        if self.child:
            self.child.follow_parent()
            

    # def fill(self): self.fill = not self.fill
    def get_sides(self):
        right = (self.center[0] + (self.radius * math.cos(self.angle - math.radians(90))), self.center[1] + (self.radius * math.sin(self.angle - math.radians(90))))
        left =  (self.center[0] + (self.radius * math.cos(self.angle + math.radians(90))), self.center[1] + (self.radius * math.sin(self.angle + math.radians(90))))
        return right, left

    def get_face(self):
        a = (self.center[0] + (self.radius * math.cos(self.angle - math.radians(45))), self.center[1] + (self.radius * math.sin(self.angle - math.radians(45))))
        b =  (self.center[0] + (self.radius * math.cos(self.angle)), self.center[1] + (self.radius * math.sin(self.angle)))
        c =  (self.center[0] + (self.radius * math.cos(self.angle + math.radians(45))), self.center[1] + (self.radius * math.sin(self.angle + math.radians(45))))
        return c,b,a