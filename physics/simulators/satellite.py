def run_satellite_simulation(duration=100):
    import time

    from physics.utils import atan, cos, distance, sin
    from physics.vectors import Vector
    from physics.bodies import Body
    from physics.canvas import canvas, root


    earth = Body(
        canvas,
        canvas.create_oval(350, 225, 600, 475, fill="red"),
        475, 350,  # center of gravity
        velocity=Vector(x=0, y=0),
        mass=100000  # arbitrary number... no units
    )

    satellite = Body(
        canvas,
        canvas.create_oval(300, 312.5, 325, 337.5, fill="red"),
        312.5, 325,
        velocity=Vector(x=0, y=0),
        mass=100
    )

    for frame in range(int(duration / 0.01)):

        # if frame == 0:
        #     satellite.push(Vector(r=1000, theta=180), 0.01)

        # distance between statellite and earth (centers of gravity)
        d = distance(satellite.coords, earth.coords)
        # angle between x-axis and vector of satellite to earth (centers of gravity)
        theta = atan((satellite.y - earth.y) / (satellite.x - earth.x))
        f = ((satellite.mass * earth.mass) / d)
        gravitational_force = Vector(
            r=f,
            theta=theta
        )

        support_force = Vector(r=0, theta=0)
        if d <= 12.5 + 125:
            # circles are intersecting (distance between centers is greater than or equal to sum of radii)
            
            # support force of earth's surface
            # has opposite direction, but same magnitude as earth's gravity
            support_force = gravitational_force * -1
        Body.push(satellite, gravitational_force + support_force, 0.01)

        
        root.update()
        time.sleep(0.01)


# TODO:
# calculate required support force to stop satellite.