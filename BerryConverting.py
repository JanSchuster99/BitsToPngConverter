import math
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time
# Es öffnet sich ein kleines Fenster mit einem Button "Generate Image"
# Nach Druck auf den Button öffnet sich der Explorer 
# Wähle eine TXT  DATEI welche NUR EINSEN UND NULLEN beinhaltet (KEINE LEERZEICHEN ODER UMBRÜCHE)
# Wenn alles gucci läuft wird ein PNG mit dem aktuellen Timestamp als namen erzeugt
# Die Größe des Bilds wird definiert durch die Anzahl der Chars im txt file. Es nimmt die sqrt der nächst größten Quadratzahl als länge und Breite
# Bsp: file hat 5 chars => nächste größte Quadratzahl = 9 => 3x3 pixel (bitte nutzt das programm nicht nur mit ner sample size von 5 bits)
# Beispiel einer Text Datei und dem dazugehörigen Bild hier mit im Repo
# Wenn nicht = der Fehler sitzt vor dem PC
# Hab überlegt drag and drop zu supporten, fuck that shit tho
# Programm wurde 100% von mir geschrieben und komplett ohne hilfe von CHAT GPT ;) shit ist auch überhaupt nicht optimized oder gut geschrieben aber reicht lmao
# Falls es irgendwelche Probleme gibt. fragt CHAT GPT oder schreibts einfach selbst um. CHAT GPT ist noch kostenlos o<()8°)
# Hier sind 100% typos und Rechtschreibfehler, idc ty



# Define a function to handle button click event
def generate_image():
    try:
        # Get the path to the input file from file dialog
        input_file = filedialog.askopenfilename(title="Select input file")

        # Open the text file and read all the bits
        with open(input_file, 'r') as f:
            bits = f.read()

        # Calculate the dimensions of the image based on the square root of the number of bits
        dim = int(math.ceil(math.sqrt(len(bits))))

        # Create a dim x dim image with white background
        img = Image.new('1', (dim, dim), color=1)

        # Convert the string of bits into a list of integers
        bits = [int(bit) for bit in bits]

        # Iterate over the list of bits and set the corresponding pixel in the image
        for i, bit in enumerate(bits):
            row = i // dim
            col = i % dim
            img.putpixel((col, row), bit)

        # Get the path to the output file based on current time
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        output_file = f"image_{timestamp}.png"

        # Save the image as a PNG file in the same directory as the program
        img.save(output_file)

        # Show a message box to confirm that the image was saved
        messagebox.showinfo("Image saved", f"Image saved to {output_file}")
    except Exception as e:
        # Show an error message if something goes wrong
        messagebox.showerror("Error", f"Failed to generate image: {str(e)}")

# Create a GUI window
root = tk.Tk()

# Add a button to generate the image
generate_button = tk.Button(root, text="Generate Image", command=generate_image)
generate_button.pack(pady=10)

# Start the main event loop
root.mainloop()
