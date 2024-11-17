from step import Step

def get_initials_sequence():
    """
    Tworzy listę kroków do narysowania inicjałów A.B.
    :return: Obiekt DrawingSequence.
    """
    sequence = [
        # Litera A
        Step("pen", {"state": "down"}),
        Step("magnet", {"power": 100}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 3.5}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 3.5}),
        Step("pen", {"state": "up"}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 1.4}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 1.75}),
        Step("move", {"steering": -100, "speed": 30, "rotations": 0.70}),
        Step("pen", {"state": "down"}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2}),
        Step("pen", {"state": "up"}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 1.4}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2.5}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 1.6}),

        #  Litera B
        Step("move", {"steering": -100, "speed": 30, "rotations": 0.70}),
        # Drop magnet
        motorC.on(0)
        Step("move", {"steering": 0, "speed": 30, "rotations": 1}),
        Step("move", {"steering": -100, "speed": 30, "rotations": 0.70}),
        Step("pen", {"state": "down"}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 3.5}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 3.5}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2}),
        Step("pen", {"state": "up"}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2}),
        Step("move", {"steering": 100, "speed": 30, "rotations": 0.70}),
        Step("pen", {"state": "down"}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2}),
        Step("pen", {"state": "up"}),
        Step("move", {"steering": 0, "speed": 30, "rotations": 2}),
    ]
    return sequence