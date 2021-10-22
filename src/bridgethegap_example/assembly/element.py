from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from assembly_information_model.assembly import Element
import json

from compas.geometry import Frame
from compas.geometry import Transformation
from compas.geometry import Rotation
from compas.geometry import Translation
from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Vector
from compas.datastructures import Mesh
from compas.datastructures import mesh_transform
from compas.geometry.primitives.plane import Plane


class BridgeElement(Element):
    def __init__(self, InputFrame, Board_Length=None, Board_Width = None,
                 Board_Height = None, Category=None, Index_In_Category = None):
        super(BridgeElement, self).__init__(InputFrame)

        self.frame = InputFrame
        self.length = Board_Length
        self.width = Board_Width
        self.height = Board_Height
        self.category = Category
        self.index_in_category = Index_In_Category

    def define_tool_frame(self):
        if self.height:
            # the tool frame must be z/2 higher than the object center
            self.tool_frame = self.frame
            # 0 = origin point of the frame; 2 = z-Value
            self.tool_frame[0][2] += self.height / 2










