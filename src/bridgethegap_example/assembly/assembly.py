from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


from compas.geometry import Point
from compas.geometry import Box, Frame, Vector
from compas.datastructures import Mesh

from assembly_information_model.assembly import Assembly


class BridgeAssembly(Assembly):

    def __init__(self, elements = None, pickup_baseframe = None, safety_distance = None,
                 attributes=None, default_element_attributes=None, default_connection_attributes=None):
        super(BridgeAssembly, self).__init__(elements=elements, attributes=attributes,
                         default_element_attributes=default_element_attributes,
                         default_connection_attributes=default_connection_attributes)

        self.elements = elements
        self.pickup_base_frame = pickup_baseframe
        self.safety_distance = safety_distance

    def define_pickframes(self, object):
        # loop through the elements
        # first, we find the vector between the Pickbase and the
        # point where it should actually pick
        pickframe_translation_vector_length = self.pickup_base_frame[1] * object.length / 2
        pickframe_translation_vector_width = self.pickup_base_frame[2] * object.width / 2
        pickframe_translation_vector_height = [0, 0, object.height]
        pickframe_translation_vector = (pickframe_translation_vector_length +
                                        pickframe_translation_vector_width + pickframe_translation_vector_height)
        # once we have the vector, we change the pickframe accordingly
        Pickpoint = self.pickup_base_frame[0] + pickframe_translation_vector
        object.pickframe = Frame(Pickpoint, self.pickup_base_frame[1], self.pickup_base_frame[2])
        return object

    def create_safety_frame(self, frame):
        safe_vector = [0,0,self.safety_distance]
        print(frame)
        print(safe_vector)
        safe_frame = Frame(frame[0] + safe_vector, frame[1], frame[2])
        return safe_frame

    def create_paths(self, object):
        safety_frame_pick = self.create_safety_frame(object.pickframe)
        safety_frame_drop = self.create_safety_frame(object.tool_frame)
        object.path = [safety_frame_pick, object.pickframe, safety_frame_pick,
                       safety_frame_drop, object.tool_frame, safety_frame_drop]
        print(object.path)
        return object

    def create_meshes(self, object):
        object.pick_box = Box(object.pickframe, object.length, object.width, object.height)
        object.pick_mesh = Mesh.from_shape(object.pick_box)

        object.drop_box = Box(object.center_frame, object.length, object.width, object.height)
        object.drop_mesh = Mesh.from_shape(object.drop_box)

        object.acm_box = Box(object.center_frame, object.length, object.width, object.height)
        object.acm_mesh = Mesh.from_shape(object.acm_box)
        return object

    def prepare_assembly(self):
        for element in self.elements:
            # if we want to grap pieces in the center, we must adapt
            # the Frame where the robot picks up the piece every time
            # since we assume that the pieces can have various profiles
            element = self.define_pickframes(element)
            element = self.create_paths(element)
            element = self.create_meshes(element)
        return 0


