import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a cero")
        self._radio = radio
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, value):
        if value <= 0:
            raise ValueError("El radio debe ser mayor a cero")
        self._radio = value
    
    def area(self):
        return math.pi * (self._radio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self._radio
    
    def __str__(self):
        return f"Circulo de radio {self._radio}"
    
    def __repr__(self):
        return f"Circulo({self._radio})"
    
    def __mul__(self, n): 
        if n <= 0:
            raise ValueError("El factor de multiplicación debe ser mayor a cero")
        return Circulo(self._radio * n)

# Instanciando un Circulo con radio 5
c1 = Circulo(5)   
print(c1)  # Circulo de radio 5

# Tratando de instanciar un Circulo con radio 0 (error)
c2 = Circulo(0)  # ValueError: El radio debe ser mayor a cero

# Obteniendo el area y perimetro de un Circulo
print(c1.area())  # 78.53981633974483
print(c1.perimetro())  # 31.41592653589793

# Modificando el radio de un Circulo
c1.radio = 10
print(c1)  # Circulo de radio 10

# Tratando de modificar el radio de un Circulo a 0 (error)
c1.radio = 0  # ValueError: El radio debe ser mayor a cero

# Multiplicando un Circulo por un factor
c3 = c1 * 2
print(c3)  # Circulo de radio 20

# Tratando de multiplicar un Circulo por un factor negativo (error)
c4 = c1 * -1  # ValueError: El factor de multiplicación debe ser mayor a cero
