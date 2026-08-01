import math

gravity = -9.80665

class falling_object:
    def __init__(self, mass, altitude, initial_y_velocity):
        self.mass = mass
        self.altitude = altitude
        self.initial_y_velocity = initial_y_velocity

class projectile_2d:
    def __init__(self, mass, altitude, initial_x_velocity, initial_y_velocity, area, drag_coeficient):
        self.mass = mass
        self.altitude = altitude
        self.initial_x_velocity = initial_x_velocity
        self.initial_y_velocity = initial_y_velocity
        self.area = area
        self.drag_coeficient = drag_coeficient

class fluid:
    def __init__(self, density):
        self.density = density

def falling_time(altitude, initial_y_velocity):
    time1 = (- (initial_y_velocity) + math.sqrt(initial_y_velocity*initial_y_velocity - 2*gravity*altitude)) / gravity
    time2 = (- (initial_y_velocity) - math.sqrt(initial_y_velocity*initial_y_velocity - 2*gravity*altitude)) / gravity

    return time1, time2

def parabolic_tragectory(initial_altitude, initial_x_velocity, initial_y_velocity):
    xy_plane = []
    time = 0
    altitude = 1

    while altitude > 0:
        altitude = initial_altitude + initial_y_velocity * time + 0.5 * gravity * time * time
        xy_plane.append([initial_x_velocity*time, altitude, time])
        time = time + 0.01

    return xy_plane

def drag_tragectory(projectile_2d, fluid):
    time = 0
    time_constant = 0.01
    xy_plane = []
    x_position = 0
    y_position = projectile_2d.altitude
    current_drag_force = 0

    while y_position > 0:
        current_drag_force = drag_force(projectile_2d.initial_x_velocity, projectile_2d.initial_y_velocity, projectile_2d.area, projectile_2d.drag_coeficient, fluid.density)
        drag_acceleration = current_drag_force / projectile_2d.mass

        acceleration_x = -drag_acceleration * projectile_2d.initial_x_velocity / (math.sqrt(projectile_2d.initial_x_velocity*projectile_2d.initial_x_velocity + projectile_2d.initial_y_velocity*projectile_2d.initial_y_velocity))
        acceleration_y = gravity - drag_acceleration * projectile_2d.initial_y_velocity / (math.sqrt(projectile_2d.initial_x_velocity*projectile_2d.initial_x_velocity + projectile_2d.initial_y_velocity*projectile_2d.initial_y_velocity))

        projectile_2d.initial_x_velocity = projectile_2d.initial_x_velocity + acceleration_x * time_constant
        projectile_2d.initial_y_velocity = projectile_2d.initial_y_velocity + acceleration_y * time_constant

        x_position = x_position + projectile_2d.initial_x_velocity * time_constant
        y_position = y_position + projectile_2d.initial_y_velocity * time_constant
        time = time + time_constant
        xy_plane.append([x_position, y_position, time])

    return xy_plane




def drag_force(velocity_x, velocity_y, area, drag_coeficient, density,):
    speed = math.sqrt(velocity_x*velocity_x + velocity_y*velocity_y)
    force = 0.5 * speed*speed * area * drag_coeficient * density 

    return force
        
        
def main():
    rock = falling_object(150, 57, -39)
    t1, t2 = falling_time(rock.altitude, rock.initial_y_velocity)

    bullet = projectile_2d(0.002, 50, 100, 10, 4*3.14159, 0.47) # Assume sphere
    xy_plane_bullet = parabolic_tragectory(bullet.altitude, bullet.initial_x_velocity, bullet.initial_y_velocity)

    air = fluid(1.225)



    print("The falling time is: " + str(t2))

    for point in xy_plane_bullet:
        print("x: " + str(point[0]) + " | y: " + str(point[1]) + " | Time: " + str(point[2]))


    return

if __name__ == "__main__":
    main()