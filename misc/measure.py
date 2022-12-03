# A script for measuring motor movements in degrees.

from spike.control import wait_for_seconds, wait_until, Timer
import hub

left = hub.port.A.motor
right = hub.port.B.motor
E = hub.port.E.motor
F = hub.port.F.motor

left.float()
right.float()
E.float()
F.float()


def print_state():
    _, deg_left, _, _ = left.get()
    _, deg_right, _, _ = right.get()
    _, deg_E, _, _ = E.get()
    _, deg_F, _, _ = F.get()
    yaw, _, _ = hub.motion.yaw_pitch_roll()

    print(
        " state left=",
        deg_left,
        " right=",
        deg_right,
        " E=",
        deg_E,
        " F=",
        deg_F,
        " yaw=",
        yaw,
    )


resets = 0


def reset(a=1):
    if a == 0:
        return

    print_state()
    global resets
    print("RESET ", resets)
    resets += 1
    hub.motion.yaw_pitch_roll(0)
    left.preset(0)
    right.preset(0)
    E.preset(0)
    F.preset(0)


hub.button.left.callback(reset)
hub.button.right.callback(reset)

print("A NEW RUN")
reset()
while True:
    wait_for_seconds(2)
    print_state()
