import logging
from modelos import Cliente, ReservaSala, AlquilerEquipo, Asesoria, Reserva
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva

# Configuración del archivo Logs
logging.basicConfig(
    filename='registro_errores.log', 
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    # Listas en memoria (Requisito: Sin Base de Datos)
    clientes = []
    servicios = []
    reservas = []

    print("=== INICIANDO SIMULACIÓN DE 10 OPERACIONES SOFTWARE FJ ===\n")

    # OPERACIÓN 1: Creación de Cliente Válido
    try:
        print("Op 1: Creando cliente válido...")
        cliente_valido = Cliente("1001", "Ana Gomez", "ana@ejemplo.com")
        clientes.append(cliente_valido)
        print(" - Éxito.")
    except Exception as e: logging.error(e)

    # OPERACIÓN 2: Cliente Inválido (Correo sin @)
    try:
        print("Op 2: Creando cliente con correo inválido...")
        cliente_malo = Cliente("1002", "Pedro", "pedro.com")
    except ErrorCliente as e:
        print(f" - Error capturado: {e}")
        logging.error(f"Op 2: {e}")

    # OPERACIÓN 3: Creación de Servicios Válidos
    try:
        print("Op 3: Creando servicios válidos...")
        sala = ReservaSala("S01", "Sala VIP", 100000, 20)
        equipo = AlquilerEquipo("E01", "Proyector 4K", 50000, True)
        asesoria = Asesoria("A01", "Asesoría IT", 80000, "Senior")
        servicios.extend([sala, equipo, asesoria])
        print(" - Éxito.")
    except Exception as e: logging.error(e)

    # OPERACIÓN 4: Servicio Inválido (Precio negativo)
    try:
        print("Op 4: Creando servicio con precio negativo...")
        sala_mala = ReservaSala("S02", "Sala Rota", -5000, 10)
    except ErrorServicio as e:
        print(f" - Error capturado: {e}")
        logging.error(f"Op 4: {e}")

    # OPERACIÓN 5: Creación de Reserva Válida
    try:
        print("Op 5: Creando reserva válida...")
        reserva1 = Reserva("R01", clientes[0], servicios[0], 4) # 4 horas
        reservas.append(reserva1)
        print(" - Éxito.")
    except Exception as e: logging.error(e)

    # OPERACIÓN 6: Confirmar Reserva Válida
    try:
        print("Op 6: Confirmando reserva R01...")
        reservas[0].confirmar()
        print(f" - Éxito. Estado: {reservas[0].estado}")
    except Exception as e: logging.error(e)

    # OPERACIÓN 7: Reserva Inválida (Tiempo negativo)
    try:
        print("Op 7: Creando reserva con tiempo negativo...")
        reserva_mala = Reserva("R02", clientes[0], servicios[1], -2)
    except ErrorReserva as e:
        print(f" - Error capturado: {e}")
        logging.error(f"Op 7: {e}")

    # OPERACIÓN 8: Reserva Inválida (Cliente no es un objeto Cliente)
    try:
        print("Op 8: Creando reserva con cliente en texto (inválido)...")
        reserva_falsa = Reserva("R03", "Juan Perez", servicios[2], 1)
    except ErrorReserva as e:
        print(f" - Error capturado: {e}")
        logging.error(f"Op 8: {e}")

    # OPERACIÓN 9: Cancelar Reserva
    try:
        print("Op 9: Cancelando reserva R01...")
        reservas[0].cancelar()
        print(f" - Éxito. Estado: {reservas[0].estado}")
    except Exception as e: logging.error(e)

    # OPERACIÓN 10: Error de lógica de negocio (Confirmar una reserva cancelada)
    try:
        print("Op 10: Intentando confirmar una reserva que ya fue cancelada...")
        reservas[0].confirmar()
    except ErrorReserva as e:
        print(f" - Error capturado: {e}")
        logging.error(f"Op 10: {e}")
    finally:
        print("\n=== RESUMEN FINAL ===")
        print(f"El programa nunca se detuvo. Registros en memoria:")
        print(f"Clientes: {len(clientes)} | Servicios: {len(servicios)} | Reservas: {len(reservas)}")
        print("Verifica el archivo 'registro_errores.log' para ver los logs generados.")