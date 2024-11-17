from ev3dev2.motor import SpeedPercent
# Klasa reprezentująca pojedynczy krok
class Step:
    def __init__(self, action, params):
        """
        Inicjalizacja kroku.
        :param action: Typ akcji (np. 'move', 'turn', 'pen', 'set_speed').
        :param params: Parametry akcji w formie słownika.
        """
        self.action = action
        self.params = params

    def execute(self, steering_drive, pen, motorC):
        """
        Wykonaj krok na podstawie typu akcji.
        :param steering_drive: Obiekt MoveSteering.
        :param pen: Obiekt Pen.
        :param motorC: Silnik magnetyczny.
        """
        if self.action == "move":
            steering_drive.on_for_rotations(
                self.params.get("steering", 0),
                self.params.get("speed", 50),
                self.params.get("rotations", 1)
            )
        elif self.action == "pen":
            if self.params.get("state") == "down":
                pen.down()
            elif self.params.get("state") == "up":
                pen.up()
        elif self.action == "magnet":
            motorC.on(self.params.get("power", 0))
        elif self.action == "set_speed":
            return self.params.get("speed", 50)
        else:
            print(f"Unknown action: {self.action}")