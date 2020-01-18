import time

from physics.vectors import Vector
from physics.bodies import Body
from physics.canvas import canvas, root


def run_projectile_simulation(angle=45, initial_speed=500, duration=2):
    """
    initial_speed * sin(angle) must be greater than 1, or else the ball can't get off the ground
    """
    canvas.create_line(0, 521, 1000, 521)

    r = int(initial_speed)
    theta = int(angle)
    t = int(duration)
    ball = Body(
        canvas, canvas.create_oval(20, 500, 40, 520, fill="red"),
        20, 500,
        velocity=Vector(
            x=Vector.get_horizontal_component(r, theta),
            y=Vector.get_vertical_component(r, theta)
        )
    )
    root.update()
    time.sleep(0.5)

    fallen = False
    for frame in range(int(t / 0.01)):
        if ball.y >= 500 and frame != 0:
            if fallen == False:
                canvas.move(ball.id, 0, 500 - ball.y)
                fallen = True
            ball.velocity.y = 0
            ball.velocity.x = 0
        else:
            ball.velocity.y += -9.8 * (frame * 0.01)

        ball.move(0.01)
        root.update()
        time.sleep(0.01)

if __name__ == "__main__":
    run_projectile_simulation()