# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:37:02 2024

@author: CompuStore
"""

#follow LSP
class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"


def let_bird_fly(bird: Bird):
    print(bird.fly())


bird1 = Bird()
sparrow1 = Sparrow()

let_bird_fly(bird1)      
let_bird_fly(sparrow1)   

#not following LSP

class Bird:
    def fly(self):
        return "Flying"


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")


def let_bird_fly(bird: Bird):
    print(bird.fly())


bird1 = Bird()
penguin1 = Penguin()

let_bird_fly(bird1)      
let_bird_fly(penguin1)   

#edited to follow

class Bird:
    def move(self):
        pass


class Sparrow(Bird):
    def move(self):
        return "Flying"


class Penguin(Bird):
    def move(self):
        return "Swimming"


def let_bird_move(bird: Bird):
    print(bird.move())


sparrow1 = Sparrow()
penguin1 = Penguin()

let_bird_move(sparrow1)   
let_bird_move(penguin1)   


