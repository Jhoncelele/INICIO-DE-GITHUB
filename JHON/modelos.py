from abc import ABC, abstractmethod
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva

# --- CLASE ABSTRACTA BASE ---
class EntidadGeneral(ABC):
    @abstractmethod
    def obtener_informacion(self):
        pass

# --- CLASE CLIENTE ---
class Cliente(EntidadGeneral):
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion  # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__validar_datos()

    def __validar_datos(self):
        if not self.__correo or "@" not in self.__correo:
            raise ErrorCliente(f"El correo '{self.__correo}' no es válido para {self.__nombre}.")
        if not self.__identificacion.isdigit():
            raise ErrorCliente(f"La identificación de {self.__nombre} debe ser numérica.")

    def obtener_informacion(self):
        return f"Cliente: {self.__nombre} | ID: {self.__identificacion}"

# --- CLASE ABSTRACTA SERVICIO ---
class Servicio(EntidadGeneral):
    def __init__(self, id_servicio, nombre, precio_base):
        if precio_base <= 0:
            raise ErrorServicio(f"El precio base del servicio '{nombre}' debe ser mayor a 0.")
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad_tiempo, descuento=0.0):
        pass
    
    def obtener_informacion(self):
        return f"Servicio: {self.nombre} | Precio Base: ${self.precio_base}"

# --- 3 SERVICIOS ESPECÍFICOS (HERENCIA Y POLIMORFISMO) ---
class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, capacidad):
        super().__init__(id_servicio, nombre, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas, descuento=0.0):
        # Sobrecarga simulada: Calcula por horas
        return (self.precio_base * horas) * (1 - descuento)

class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, requiere_seguro=True):
        super().__init__(id_servicio, nombre, precio_base)
        self.requiere_seguro = requiere_seguro

    def calcular_costo(self, dias, descuento=0.0):
        # Sobrecarga simulada: Calcula por días y suma seguro si aplica
        costo = self.precio_base * dias
        if self.requiere_seguro:
            costo += 50000  # Costo fijo de seguro
        return costo * (1 - descuento)

class Asesoria(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, nivel="Senior"):
        super().__init__(id_servicio, nombre, precio_base)
        self.nivel = nivel

    def calcular_costo(self, sesiones, descuento=0.0):
        # Sobrecarga simulada: Calcula por sesiones y recargo por nivel
        recargo = 1.5 if self.nivel == "Senior" else 1.0
        return (self.precio_base * sesiones * recargo) * (1 - descuento)

# --- CLASE RESERVA ---
class Reserva(EntidadGeneral):
    def __init__(self, id_reserva, cliente, servicio, cantidad_tiempo):
        if not isinstance(cliente, Cliente):
            raise ErrorReserva("El objeto proporcionado no es un Cliente válido.")
        if not isinstance(servicio, Servicio):
            raise ErrorReserva("El objeto proporcionado no es un Servicio válido.")
        if cantidad_tiempo <= 0:
            raise ErrorReserva("El tiempo de la reserva debe ser mayor a cero.")

        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad_tiempo = cantidad_tiempo
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado == "Cancelada":
            raise ErrorReserva(f"La reserva {self.id_reserva} ya fue cancelada y no puede confirmarse.")
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def obtener_informacion(self):
        costo_total = self.servicio.calcular_costo(self.cantidad_tiempo)
        return f"Reserva {self.id_reserva} | {self.servicio.nombre} para {self.cliente.obtener_informacion()} | Total: ${costo_total} | Estado: {self.estado}"