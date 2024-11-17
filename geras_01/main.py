from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import Pen
from drawing_sequence import DrawingSequence
from sequences import get_initials_sequence

# Tworzenie obiektów
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
pen_in3 = Pen(INPUT_1)
motorC = LargeMotor(OUTPUT_C)

# Pobieranie sekwencji rysowania inicjałów A.B
sequence = DrawingSequence()
for step in get_initials_sequence():
    sequence.add_step(step)

# Wykonanie sekwencji
print("Start")
sequence.execute(steering_drive, pen_in3, motorC)
print("Done")