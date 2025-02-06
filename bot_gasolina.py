from datetime import datetime, timedelta

# Función para obtener el día de la semana
def obtener_dia_semana(fecha):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias_semana[fecha.weekday()]

# Función principal del bot
def bot_restriccion_gasolina():
    print("¡Hola! Soy tu asistente para restricciones de gasolina.")
    
    # Solicitar al usuario el último dígito de la placa
    while True:
        try:
            ultimo_digito = int(input("Por favor, ingresa el último dígito de la placa de tu carro (0-9): "))
            if 0 <= ultimo_digito <= 9:
                break
            else:
                print("Por favor, ingresa un número válido entre 0 y 9.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Calcular los próximos 5 días
    print("\nEstos son los días en los que puedes echar gasolina cada 5 días:")
    for i in range(5):
        fecha_futura = fecha_actual + timedelta(days=i * 5)
        dia_semana = obtener_dia_semana(fecha_futura)
        print(f"Día {i + 1}: {fecha_futura.strftime('%Y-%m-%d')} ({dia_semana})")

# Ejecutar el bot
bot_restriccion_gasolina()