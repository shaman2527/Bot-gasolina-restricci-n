from datetime import datetime, timedelta
import pandas as pd

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

    # Lista para almacenar los resultados
    datos = []
    
    # Calcular los próximos 5 días con sus restricciones
    for i in range(5):
        fecha_futura = fecha_actual + timedelta(days=i)
        dia_semana = obtener_dia_semana(fecha_futura)
        
        # Asignar placas según el día en el ciclo de 5 días
        ciclo = i % 5
        if ciclo == 0:
            placas = "1 y 2"
        elif ciclo == 1:
            placas = "3 y 4"
        elif ciclo == 2:
            placas = "5 y 6"
        elif ciclo == 3:
            placas = "7 y 8"
        else:
            placas = "9 y 0"
        
        # Verificar si el usuario puede echar gasolina ese día
        permitido = (ultimo_digito in [1, 2] and ciclo == 0) or \
                    (ultimo_digito in [3, 4] and ciclo == 1) or \
                    (ultimo_digito in [5, 6] and ciclo == 2) or \
                    (ultimo_digito in [7, 8] and ciclo == 3) or \
                    (ultimo_digito in [9, 0] and ciclo == 4)
        
        # Agregar datos a la lista
        datos.append({
            "Fecha": fecha_futura.strftime("%Y-%m-%d"),
            "Día": dia_semana,
            "Placas": placas,
            "Permitido": "Sí" if permitido else "No"
        })
    
    # Crear DataFrame
    df = pd.DataFrame(datos)
    
    # Mostrar el DataFrame
    print("\nResultados en formato DataFrame:")
    print(df.to_string(index=False))  # Usamos to_string para mejor formato

# Ejecutar el bot
bot_restriccion_gasolina()