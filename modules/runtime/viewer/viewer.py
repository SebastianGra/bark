# Copyright (c) 2019 fortiss GmbH
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np
from bark.viewer import Viewer
from bark.geometry import *
from bark.models.dynamic import *


class BaseViewer(Viewer):
    def __init__(self, params=None):
        Viewer.__init__(self)
        # color parameters
        # agents
        self.color_agents = params["Visualization"]["Agents"]["ColorVehicle", "Color of agents", (0,102/255,0)]
        self.alpha_agents = params["Visualization"]["Agents"]["AlphaVehicle", "Alpha of agents", 0.8]
        self.route_color =  params["Visualization"]["Agents"]["ColorRoute", "Color of agents routes", (0.2,0.2,0.2)]
        self.draw_route = params["Visualization"]["Agents"]["DrawRoute", "Draw Route of each agent", True]
        # map
        self.color_lane_boundaries = params["Visualization"]["Map"]["Lanes"]["Boundaries"]["Color", "Color of agents except ego vehicle", (0.7,0.7,0.7)]
        self.alpha_lane_boundaries = params["Visualization"]["Map"]["Lanes"]["Boundaries"]["Alpha", "Color of agents except ego vehicle", 1.0]
        self.plane_color = params["Visualization"]["Map"]["Plane"]["Color", "Color of the background plane", (1, 1, 1, 1)]
        self.plane_alpha = params["Visualization"]["Map"]["Plane"]["Alpha", "Alpha of the background plane", 1.0]


        self.parameters = params

    def drawPoint2d(self, point2d, color, alpha):
        pass

    def drawLine2d(self, line2d, color, alpha):
        pass

    def drawPolygon2d(self, polygon, color, alpha):
        pass

    def drawTrajectory(self, trajectory, color):
        pass

    def drawObstacle(self, obstacle):
        pass

    def getColor(self, color):
        pass

    def show(self,block=False):
        pass

    def clear(self):
        pass

    def drawAgents(self, world):
        for id, agent in world.agents.items():
            self.drawAgent(agent)
            
    def drawWorld(self, world):
        # draw agents
        for id, agent in world.agents.items():
            self.drawAgent(agent)

        self.drawMap(world.map.get_open_drive_map())

    def drawMap(self, map):
        # draw the boundary of each lane
        for i, road in map.get_roads().items():
            for lane_section in road.lane_sections:
                for _, lane in lane_section.get_lanes().items():
                    self.drawLine2d(lane.line, self.color_lane_boundaries, self.alpha_lane_boundaries)


    def drawAgent(self , agent):
        shape = agent.shape
        if isinstance(shape, Polygon2d):
            pose = np.zeros(3)
            # pybind creates column based vectors, initialization maybe row-based -> we consider both
            state = agent.followed_trajectory[-1,:]
            pose[0] = state[int(StateDefinition.X_POSITION)]
            pose[1] = state[int(StateDefinition.Y_POSITION)]
            pose[2] = state[int(StateDefinition.THETA_POSITION)]
            transformed_polygon = shape.transform(pose)
            self.drawPolygon2d(transformed_polygon, self.color_agents, 1.0)
        
        if self.draw_route:
            self.drawRoute(agent)


    def drawRoute(self, agent):
        route_center_line = agent.route.center_line
        self.drawLine2d(route_center_line,self.route_color, 0)


