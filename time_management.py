import re

class Time:
    """Representa una hora con formato AM/PM o 24 horas."""

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = "24 HOURS"
        Time.time_count += 1

    def __asign_format(self, pszFormat):
        fmt = pszFormat.upper()
        if fmt in Time.TIME_FORMATS:
            self.format = fmt
            return True
        return False

    def __is_24hour_format(self):
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        if not (0 <= self.minutes <= 59 and 0 <= self.seconds <= 59):
            return False
        if self.__is_24hour_format():
            return 0 <= self.hours <= 23
        else:
            return 1 <= self.hours <= 12

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        if not self.__asign_format(pszFormato):
            return False
        self.hours = nHoras
        self.minutes = nMinutos
        self.seconds = nSegundos
        return self._is_valid_time()

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        pattern = r"^(\d{1,2}):(\d{2}):(\d{2})\s*(AM|PM|24 HOURS)$"
        match = re.match(pattern, time_string.strip(), re.IGNORECASE)

        if not match:
            print("Formato de hora inválido.")
            return None

        hours, minutes, seconds, fmt = match.groups()
        new_time = cls()
        if new_time.set_time(int(hours), int(minutes), int(seconds), fmt):
            return new_time
        else:
            print("Hora fuera de rango.")
            return None

    @staticmethod
    def is_valid_format(time_format):
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        return cls.time_count

def mostrar_hora(time_obj):
    """
    Muestra la hora en una cadena con el formato correcto (12h o 24h).
    """
    horas = time_obj.hours
    minutos = time_obj.minutes
    segundos = time_obj.seconds
    formato = time_obj.format

    # Si está en formato 24 horas
    if formato == "24 HOURS":
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    # Si está en formato 12 horas (AM o PM)
    else:
        # Ajustar la hora si fuera necesario
        if horas == 0:
            horas = 12
        elif horas > 12:
            horas -= 12

        return f"{horas:02d}:{minutos:02d}:{segundos:02d} {formato}"
"""# Ejemplo de uso
t1 = Time()
t1.set_time(14, 45, 0, "24 HOURS")
print(mostrar_hora(t1))   # → 14:45:00

t2 = Time()
t2.set_time(2, 45, 0, "PM")
print(mostrar_hora(t2))   # → 02:45:00 PM"""