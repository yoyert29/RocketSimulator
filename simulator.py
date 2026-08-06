from dataclasses import dataclass

@dataclass
class state:
    velocity_x:     float
    velocity_y:     float
    acceleration_x: float
    acceleration_y: float
    position_x:     float
    position_y:     float

@dataclass
class InitialCondition:
    initial_velocity_x:     float
    initial_velocity_y:     float
    initial_acceleration_x: float
    initial_acceleration_y: float
    initial_position_x:     float
    initial_position_y:     float

class Simulation:
    pass
