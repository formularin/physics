import sys

import physics.simulators


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("simulation options:\nprojectile")
    else:
        try:
            exec(f"from physics.simulators import {sys.argv[1]}")
            kwargs = {}
            for i in range(0, len(sys.argv[3:]), 2):
                kwargs[sys.argv[i + 2][2:]] = sys.argv[i + 3]
            # print(kwargs)
            eval(f"{sys.argv[1]}.run_{sys.argv[1]}_simulation(**kwargs)")
        except ModuleNotFoundError:
            print(f"no such simulation: {sys.argv[1]}")