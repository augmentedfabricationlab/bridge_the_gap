from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from compas.geometry import Point, Frame, Vector
from .assembly import BridgeAssembly
from .element import BridgeElement


myFrame = Frame(Point(0.2, 0.2, 0.2), Vector(-1,0,0), Vector(0,1,0))
myElement = BridgeElement(myFrame, 2, 2, [0.1, 0.1, 0.1])
myElement2 = BridgeElement(myFrame, 2, 2, [0.1, 0.1, 0.1])
myElements = [myElement, myElement2]


myAssembly = BridgeAssembly(myElements, myFrame, 0.4)
myAssembly.prepare_assembly()
print("hello")
