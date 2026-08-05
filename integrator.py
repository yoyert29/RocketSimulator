import math
import copy

#This document will perform the numeric integration: Euler, RK4, etc.

def constant_acceleration_integrator(state, time_constant):
    new_state = copy.copy(state)
    new_state.position_x = state.position_x + state.velocity_x * time_constant + 0.5 * state.acceleration_x * time_constant**2
    new_state.position_y = state.position_y + state.velocity_y * time_constant + 0.5 * state.acceleration_y * time_constant**2

    new_state.velocity_x = state.velocity_x + time_constant * state.acceleration_x
    new_state.velocity_y = state.velocity_y + time_constant * state.acceleration_y

    new_state.time = state.time + time_constant

    return new_state

def symplectic_euler_integrator(state, time_constant):
    new_state = copy.copy(state)
    new_state.velocity_x = state.velocity_x + state.acceleration_x * time_constant
    new_state.velocity_y = state.velocity_y + state.acceleration_y * time_constant

    new_state.position_x = state.position_x + new_state.velocity_x * time_constant
    new_state.position_y = state.position_y + new_state.velocity_y * time_constant

    new_state.time = state.time + time_constant

    return new_state