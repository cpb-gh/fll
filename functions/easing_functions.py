### FUNCTION START
"""
Linear
"""
def LinearInOut(t):
	return t

"""
Quadratic easing functions
"""


def QuadEaseInOut(t):
	if t < 0.5:
	    return 2 * t * t
	return (-2 * t * t) + (4 * t) - 1


def QuadEaseIn(t):
    return t * t


def QuadEaseOut(t):
    return -(t * (t - 2))


"""
Cubic easing functions
"""


def CubicEaseIn(t):
    return t * t * t


def CubicEaseOut(t):
    return (t - 1) * (t - 1) * (t - 1) + 1


def CubicEaseInOut(t):
    if t < 0.5:
    	return 4 * t * t * t
    p = 2 * t - 2
    return 0.5 * p * p * p + 1


"""
Quartic easing functions
"""


def QuarticEaseIn(t):
    return t * t * t * t


def QuarticEaseOut(t):
    return (t - 1) * (t - 1) * (t - 1) * (1 - t) + 1


def QuarticEaseInOut(t):
    if t < 0.5:
        return 8 * t * t * t * t
    p = t - 1
    return -8 * p * p * p * p + 1


"""
Quintic easing functions
"""


def QuinticEaseIn(t):
    return t * t * t * t * t


def QuinticEaseOut(t):
    return (t - 1) * (t - 1) * (t - 1) * (t - 1) * (t - 1) + 1


def QuinticEaseInOut(t):
    if t < 0.5:
        return 16 * t * t * t * t * t
    p = (2 * t) - 2
    return 0.5 * p * p * p * p * p + 1


"""
Sine easing functions
"""


def SineEaseIn(t):
    return math.sin((t - 1) * math.pi / 2) + 1


def SineEaseOut(t):
    return math.sin(t * math.pi / 2)


def SineEaseInOut(t):
    return 0.5 * (1 - math.cos(t * math.pi))


"""
Circular easing functions
"""


def CircularEaseIn(t):
    return 1 - math.sqrt(1 - (t * t))


def CircularEaseOut(t):
    return math.sqrt((2 - t) * t)


def CircularEaseInOut(t):
    if t < 0.5:
        return 0.5 * (1 - math.sqrt(1 - 4 * (t * t)))
    return 0.5 * (math.sqrt(-((2 * t) - 3) * ((2 * t) - 1)) + 1)


"""
Exponential easing functions
"""


def ExponentialEaseIn(t):
    if t == 0:
        return 0
    return math.pow(2, 10 * (t - 1))


def ExponentialEaseOut(t):
    if t == 1:
        return 1
    return 1 - math.pow(2, -10 * t)


def ExponentialEaseInOut(t):
    if t == 0 or t == 1:
        return t

    if t < 0.5:
        return 0.5 * math.pow(2, (20 * t) - 10)
    return -0.5 * math.pow(2, (-20 * t) + 10) + 1


"""
Elastic Easing Functions
"""


def ElasticEaseIn(t):
	return math.sin(13 * math.pi / 2 * t) * math.pow(2, 10 * (t - 1))


def ElasticEaseOut(t):
    return math.sin(-13 * math.pi / 2 * (t + 1)) * math.pow(2, -10 * t) + 1


def ElasticEaseInOut(t):
    if t < 0.5:
        return (
            0.5
            * math.sin(13 * math.pi / 2 * (2 * t))
            * math.pow(2, 10 * ((2 * t) - 1))
        )
    return 0.5 * (
        math.sin(-13 * math.pi / 2 * ((2 * t - 1) + 1))
        * math.pow(2, -10 * (2 * t - 1))
        + 2
    )


"""
Back Easing Functions
"""


def BackEaseIn(t):
    return t * t * t - t * math.sin(t * math.pi)


def BackEaseOut(t):
    p = 1 - t
    return 1 - (p * p * p - p * math.sin(p * math.pi))


def BackEaseInOut(t):
    if t < 0.5:
        p = 2 * t
        return 0.5 * (p * p * p - p * math.sin(p * math.pi))

    p = 1 - (2 * t - 1)

    return 0.5 * (1 - (p * p * p - p * math.sin(p * math.pi))) + 0.5


"""
Bounce Easing Functions
"""


def BounceEaseIn(t):
    return 1 - BounceEaseOut(1 - t)


def BounceEaseOut(t):
    if t < 4 / 11:
        return 121 * t * t / 16
    elif t < 8 / 11:
        return (363 / 40.0 * t * t) - (99 / 10.0 * t) + 17 / 5.0
    elif t < 9 / 10:
        return (4356 / 361.0 * t * t) - (35442 / 1805.0 * t) + 16061 / 1805.0
    return (54 / 5.0 * t * t) - (513 / 25.0 * t) + 268 / 25.0


def BounceEaseInOut(t):
    if t < 0.5:
        return 0.5 * BounceEaseIn(t * 2)
    return 0.5 * BounceEaseOut(t * 2 - 1) + 0.5
### FUNCTION END
