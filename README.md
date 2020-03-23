# physics

*Various physics simulators in python tkinter*

<hr>

## Installation

```bash
git clone 'https://github.com/lol-cubes/physics'
cd physics
python3 -m pip install -e .
```

## Usage

There are various simulators in the package, and each has its own options.

Example:
```
python3 physics projectile --angle 45 --initial_speed 500 --duration 2
```

## Simulators

All simulators have the `duration` option, which is how long the program will run for.

### Projectile:
 - `initial_speed`: Intial speed of projectile (in pixels per second). 
 - `angle`: Angle of initial velocity of projectile in degrees (relative to ground - x axis)

*initial_speed x sin(angle) must be greater than 1, or else the ball can't get off the ground*
