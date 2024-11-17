# Klasa zarządzająca sekwencją kroków
from step import Step

class DrawingSequence:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        """
        Dodaj krok do sekwencji.
        :param step: Obiekt Step.
        """
        self.steps.append(step)

    def execute(self, steering_drive, pen, motorC):
        """
        Wykonaj wszystkie kroki w sekwencji.
        :param steering_drive: Obiekt MoveSteering.
        :param pen: Obiekt Pen.
        :param motorC: Silnik magnetyczny.
        """
        for step in self.steps:
            step.execute(steering_drive, pen, motorC)