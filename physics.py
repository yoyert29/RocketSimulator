import math

GRAVITY = 9.80665

def gravity_force(state):
    return (0, -GRAVITY * state.mass)

def drag_force(rocket, state, fluid):
    speed = math.hypot(state.velocity_x, state.velocity_y)
    if speed == 0:
        return (0.0, 0.0)

    drag_force = 0.5 * rocket.front_area * rocket.drag_coefficient * speed * speed * fluid.density
    drag_force_x = drag_force * -state.velocity_x / speed
    drag_force_y = drag_force * -state.velocity_y / speed

    return (drag_force_x, drag_force_y)

def net_force(gravity, drag):
    x = gravity[0] + drag[0]
    y = gravity[0] + drag[0]
    return (x, y)

def net_acceleration(force, mass):
    x = force[0] / mass
    y = force[1] / mass
    return (x, y)

