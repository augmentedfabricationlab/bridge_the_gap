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
    def __init__(self, ID, InputFrame, Profile, LayerZAddon = None, Layer=None):
        super(BridgeElement, self).__init__(InputFrame)

        self.center_frame = InputFrame
        self.id = ID
        self.profile = Profile
        self.length = self.profile[0]
        self.width = self.profile[1]
        self.height = self.profile[2]
        self.layer = Layer

        self.layer_z_addon = LayerZAddon
        if LayerZAddon:
            self.center_frame[0][2] += self.layer_z_addon

        # the toolframe must be z/2 higher than the object center
        self.tool_frame = self.center_frame
        # 0 = origin point of the frame; 2 = z-Value
        self.tool_frame[0][2] += self.profile[2]/2









