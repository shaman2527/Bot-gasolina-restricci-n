from datetime import datetime, timedelta
import pandas as pd
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler
)

TOKEN = "API KEY"
INPUT_PLACA = 1

def obtener_dia_semana(fecha):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias_semana[fecha.weekday()]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("*¡Bienvenido a BOT RBS!*\n\n Ingresa el último dígito de tu placa (0-9):")
    return INPUT_PLACA

async def procesar_placa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        ultimo_digito = int(update.message.text)
        if 0 <= ultimo_digito <= 9:
            fecha_actual = datetime.now()
            datos = []
            
            for i in range(5):
                fecha_futura = fecha_actual + timedelta(days=i)
                dia_semana = obtener_dia_semana(fecha_futura)
                
                ciclo = i % 5
                placas = "1 y 2" if ciclo == 0 else \
                        "3 y 4" if ciclo == 1 else \
                        "5 y 6" if ciclo == 2 else \
                        "7 y 8" if ciclo == 3 else "9 y 0"
                
                permitido = (ultimo_digito in [1, 2] and ciclo == 0) or \
                            (ultimo_digito in [3, 4] and ciclo == 1) or \
                            (ultimo_digito in [5, 6] and ciclo == 2) or \
                            (ultimo_digito in [7, 8] and ciclo == 3) or \
                            (ultimo_digito in [9, 0] and ciclo == 4)
                
                datos.append({
                    "Fecha": fecha_futura.strftime("%Y-%m-%d"),
                    "Día": dia_semana,
                    "Placas": placas,
                    "Permitido": "✅ Sí" if permitido else "❌ No"
                })
            
            df = pd.DataFrame(datos)
            respuesta = "📅 **Resultados:**\n```\n" + df.to_string(index=False) + "\n```"
            await update.message.reply_text(respuesta, parse_mode="Markdown")
            
        else:
            await update.message.reply_text("❌ Por favor, ingresa un número entre 0 y 9.")
    
    except ValueError:
        await update.message.reply_text("❌ Entrada inválida. Debes ingresar un número.")
    
    return ConversationHandler.END

def main():
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            INPUT_PLACA: [MessageHandler(filters.TEXT & ~filters.COMMAND, procesar_placa)]
        },
        fallbacks=[]
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
    
    

#Dependencia app requirements.txt

import subprocess

with open("requirements.txt", "w") as f:
    subprocess.run(["pip", "freeze"], stdout=f)
