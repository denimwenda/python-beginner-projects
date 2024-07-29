import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    # Get the input data from the user
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data to generate a QR code.")
        return
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the generated QR code as an image file
    img.save("qrcode.png")
    
    # Display the QR code image in the Tkinter window
    img = Image.open("qrcode.png")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the input field and button
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=10)
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Create and place the label to display the QR code
qr_label = tk.Label(root)
qr_label.pack(padx=10, pady=10)

# Run the application
root.mainloop()