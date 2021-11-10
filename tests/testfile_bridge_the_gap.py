from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from compas.geometry import Point, Frame, Vector
from bridge_the_gap.assembly import BridgeAssembly
from bridge_the_gap.assembly import BridgeElement

my_assembly = BridgeAssembly()


myFrameSet = [
Frame(Point(13.009, 0.634, 0.000), Vector(0.987, -0.160, -0.000), Vector(-0.160, -0.987, 0.000)),
Frame(Point(11.957, 0.629, 4.000), Vector(0.987, 0.161, 0.000), Vector(0.161, -0.987, 0.000)),
Frame(Point(11.672, 0.175, 0.000), Vector(0.991, 0.132, 0.000), Vector(0.132, -0.991, 0.000)),
Frame(Point(13.295, 0.183, 0.000), Vector(0.992, -0.127, -0.000), Vector(-0.127, -0.992, 0.000)),
Frame(Point(13.766, 0.469, 0.000), Vector(0.966, -0.260, -0.000), Vector(-0.260, -0.966, 0.000)),
Frame(Point(11.186, 0.462, 0.000), Vector(0.965, 0.261, 0.000), Vector(0.261, -0.965, 0.000)),
Frame(Point(10.850, 0.067, 0.000), Vector(0.992, 0.128, 0.000), Vector(0.128, -0.992, 0.000)),
Frame(Point(14.077, 0.084, 0.000), Vector(0.992, -0.124, -0.000), Vector(-0.124, -0.992, 0.000)),
Frame(Point(14.565, 0.217, 0.000), Vector(0.941, -0.338, -0.000), Vector(-0.338, -0.941, 0.000)),
Frame(Point(10.416, 0.222, 0.000), Vector(0.943, 0.332, 0.000), Vector(0.332, -0.943, 0.000)),
Frame(Point(10.243, -0.008, 0.000), Vector(0.993, 0.115, 0.000), Vector(0.115, -0.993, 0.000)),
Frame(Point(14.718, 0.004, 0.000), Vector(0.992, -0.126, -0.000), Vector(-0.126, -0.992, 0.000)),
Frame(Point(12.498, 0.693, 0.000), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
Frame(Point(10.655, 0.191, 0.000), Vector(0.666, 0.746, 0.000), Vector(0.746, -0.666, 0.000)),
Frame(Point(11.382, 0.339, 0.000), Vector(0.633, 0.774, 0.000), Vector(0.774, -0.633, 0.000)),
Frame(Point(12.247, 0.465, 0.000), Vector(0.403, 0.915, 0.000), Vector(0.915, -0.403, 0.000)),
Frame(Point(12.751, 0.466, 0.000), Vector(0.409, -0.912, -0.000), Vector(-0.912, -0.409, 0.000)),
Frame(Point(13.553, 0.351, 0.000), Vector(0.634, -0.773, -0.000), Vector(-0.773, -0.634, 0.000)),
Frame(Point(14.290, 0.202, 0.000), Vector(0.621, -0.784, -0.000), Vector(-0.784, -0.621, 0.000)),
Frame(Point(12.500, 0.239, 0.000), Vector(1.000, 0.002, -0.000), Vector(0.002, -1.000, 0.000)),
Frame(Point(10.004, 0.023, 0.000), Vector(0.344, 0.939, -0.000), Vector(0.939, -0.344, 0.000)),
Frame(Point(14.994, 0.019, 0.000), Vector(0.437, -0.899, -0.000), Vector(-0.899, -0.437, 0.000)),
Frame(Point(14.692, 0.057, 0.000), Vector(0.998, 0.056, 0.000), Vector(0.056, -0.998, 0.000)),
Frame(Point(13.950, 0.244, 0.000), Vector(0.875, 0.483, 0.000), Vector(0.483, -0.875, 0.000)),
Frame(Point(13.110, 0.408, 0.000), Vector(0.838, 0.546, 0.000), Vector(0.546, -0.838, 0.000)),
Frame(Point(10.265, 0.054, 0.000), Vector(0.992, -0.130, -0.000), Vector(-0.130, -0.992, 0.000)),
Frame(Point(11.001, 0.235, 0.000), Vector(0.845, -0.535, -0.000), Vector(-0.535, -0.845, 0.000)),
Frame(Point(11.857, 0.402, 0.000), Vector(0.871, -0.492, -0.000), Vector(-0.492, -0.871, 0.000))
    ]
lengths = [0.72888612132232555, 0.79012319808336817, 0.95922231574812022, 0.89226783409583033, 0.82289075249600907, 0.789766110625581, 0.69778136937749724, 0.68436229107796309, 0.85475878513586756, 0.82558731651669848, 0.52654551668359806, 0.60831582360268277, 0.30194229954981111, 0.4516400184602582, 0.5862299187450738, 0.49647652761125388, 0.49639133374753358, 0.58120093519414162, 0.40792440981993494, 0.70502681708793857, 0.13115222717909872, 0.1195717848785053, 0.55203112300537804, 0.48645499694101429, 0.6161305979839532, 0.48204989073413501, 0.46314232034724573, 0.6657938136277054]


fram1 = Frame(Point(0,0,0), Vector(-1,0,0), Vector(0,1,0))
fram2 = Frame(Point(2,0,0), Vector(-1,0,0), Vector(0,1,0))
fram3 = Frame(Point(4,0,0), Vector(-1,0,0), Vector(0,1,0))

"""
my_assembly.add_element(BridgeElement(myFrameSet[0], Board_Length = 2.0, Endpoints = [Point(0,0,0),Point(1,0,0)]))
my_assembly.add_element(BridgeElement(myFrameSet[0], Board_Length = 2.0, Endpoints = [Point(1,0,0),Point(2,0,0)]))
my_assembly.add_element(BridgeElement(myFrameSet[1], Board_Length = 2.0, Endpoints = [Point(2,0,0),Point(2,2,0)]))
"""
my_assembly.add_element(BridgeElement(fram1, Board_Length = 2, Endpoints = [Point(-1,0,0),Point(1,0,0)]))
my_assembly.add_element(BridgeElement(fram2, Board_Length = 2, Endpoints = [Point(1,0,0),Point(3,0,0)]))
my_assembly.add_element(BridgeElement(fram3, Board_Length = 2, Endpoints = [Point(3,0,0),Point(5,0,0)]))


#my_assembly.prepare_robot_assembly(model_scale=1000, safety_distance=0.4, pickup_baseframe=myFrame)
my_assembly.create_network()
print(my_assembly.create_assembly_sequence())
print("hello")


