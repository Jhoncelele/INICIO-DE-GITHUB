class ErrorSoftwareFJ(Exception):
    """Excepción base para todos los errores de nuestra aplicación."""
    pass

class ErrorCliente(ErrorSoftwareFJ):
    """Errores relacionados con datos inválidos de clientes."""
    pass

class ErrorServicio(ErrorSoftwareFJ):
    """Errores cuando un servicio no está disponible o tiene parámetros erróneos."""
    pass

class ErrorReserva(ErrorSoftwareFJ):
    """Errores al intentar crear, procesar o cancelar una reserva."""
    pass