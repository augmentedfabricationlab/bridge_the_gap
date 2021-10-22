from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


from compas.geometry import Point, Scale, matrix_from_scale_factors
from compas.geometry import Box, Frame, Vector
from compas.datastructures import Mesh

from assembly_information_model.assembly import Assembly
from compas.geometry.transformations import scale, transformation


class BridgeAssembly(Assembly):

    def __init__(self, elements = None,
                 attributes=None, default_element_attributes=None, default_connection_attributes=None):
        super(BridgeAssembly, self).__init__(elements=elements, attributes=attributes,
                         default_element_attributes=default_element_attributes,
                         default_connection_attributes=default_connection_attributes)
        self.safety_distance = None
        self.pickup_base_frame = None


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
        safe_frame = Frame(frame[0] + safe_vector, frame[1], frame[2])
        return safe_frame

    def create_meshes(self, object):
        object.pick_box = Box(object.pickframe, object.length, object.width, object.height)
        object.pick_mesh = Mesh.from_shape(object.pick_box)

        object.drop_box = Box(object.frame, object.length, object.width, object.height)
        object.mesh = Mesh.from_shape(object.drop_box)

        object.acm_box = Box(object.frame, object.length, object.width, object.height)
        object.acm_mesh = Mesh.from_shape(object.acm_box)
        return object

    # Scales the element with a factor of your choice
    # e.g. factor 0.1 means that the element is scaled down to 10% of its original size
    def scale_assembly(self, model_scale):
        # S is a Scaling Transformation that we first define and then apply
        S = Scale.from_factors([model_scale, model_scale, model_scale])
        self.network.transform(S)
        for _k, element in self.elements(data=False):
            # This scales down the whole element
            element.transform(S)
            # Since these are not default attributes, we must scale them manually
            if element.length:
                element.length *= model_scale
            if element.width:
                element.width *= model_scale
            if element.height:
                element.height *= model_scale
        return 0

    def prepare_robot_assembly(self, safety_distance, pickup_baseframe, model_scale = None):
        self.safety_distance = safety_distance
        self.pickup_base_frame = pickup_baseframe

        if model_scale:
            self.scale_assembly(model_scale)
        for _k, element in self.elements(data=False):
            # the robot must grip the board on its top, not its very center
            # therefore, we must define a tool_frame which is height/2 higher than the center frame
            # we already defined a function for that in the element which we can call here
            element.define_tool_frame()
            # if we want to grap pieces in the center, we must adapt
            # the Frame where the robot picks up the piece every time
            # since we assume that the pieces can have various profiles
            element = self.define_pickframes(element)
            # now let's do the safety frames
            # they are located in a safe distance above the workpiece
            # to ensure the end-effector doesn't collide with the workpiece
            safety_frame_pick = self.create_safety_frame(element.pickframe)
            safety_frame_drop = self.create_safety_frame(element.tool_frame)
            # now that we have the key elements, let's create the path
            element.path = [safety_frame_pick, element.pickframe, safety_frame_pick,
                            safety_frame_drop, element.tool_frame, safety_frame_drop]
            element = self.create_meshes(element)
        return 0
