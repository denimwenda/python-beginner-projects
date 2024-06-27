import tkinter as tk
from tkinter import ttk

class ConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Converter App")
        
        # Create a dictionary for conversion functions
        self.conversions = {
            "Length": self.convert_length,
            "Temperature": self.convert_temperature,
            "Weight": self.convert_weight
        }
        
        # Conversion options for each type
        self.units = {
            "Length": [("Meters", "Feet"), ("Feet", "Meters")],
            "Temperature": [("Celsius", "Fahrenheit"), ("Fahrenheit", "Celsius")],
            "Weight": [("Kilograms", "Pounds"), ("Pounds", "Kilograms")]
        }
        
        # Type of conversion
        self.type_label = tk.Label(master, text="Conversion Type")
        self.type_label.grid(row=0, column=0, padx=10, pady=10)
        self.type_var = tk.StringVar()
        self.type_menu = ttk.Combobox(master, textvariable=self.type_var)
        self.type_menu['values'] = list(self.conversions.keys())
        self.type_menu.grid(row=0, column=1, padx=10, pady=10)
        self.type_menu.bind('<<ComboboxSelected>>', self.update_units)
        
        # From unit
        self.from_label = tk.Label(master, text="From")
        self.from_label.grid(row=1, column=0, padx=10, pady=10)
        self.from_var = tk.StringVar()
        self.from_menu = ttk.Combobox(master, textvariable=self.from_var)
        self.from_menu.grid(row=1, column=1, padx=10, pady=10)
        
        # To unit
        self.to_label = tk.Label(master, text="To")
        self.to_label.grid(row=2, column=0, padx=10, pady=10)
        self.to_var = tk.StringVar()
        self.to_menu = ttk.Combobox(master, textvariable=self.to_var)
        self.to_menu.grid(row=2, column=1, padx=10, pady=10)
        
        # Input field
        self.input_label = tk.Label(master, text="Input")
        self.input_label.grid(row=3, column=0, padx=10, pady=10)
        self.input_entry = tk.Entry(master)
        self.input_entry.grid(row=3, column=1, padx=10, pady=10)
        
        # Output field
        self.output_label = tk.Label(master, text="Output")
        self.output_label.grid(row=4, column=0, padx=10, pady=10)
        self.output_entry = tk.Entry(master, state='readonly')
        self.output_entry.grid(row=4, column=1, padx=10, pady=10)
        
        # Convert button
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=5, column=0, columnspan=2, pady=10)

    def update_units(self, event):
        """Update the units based on the selected conversion type."""
        conversion_type = self.type_var.get()
        units = self.units[conversion_type]
        self.from_menu['values'] = [unit[0] for unit in units]
        self.to_menu['values'] = [unit[1] for unit in units]
        self.from_var.set('')
        self.to_var.set('')
        self.input_entry.delete(0, tk.END)
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.config(state='readonly')

    def convert(self):
        """Perform the conversion based on the input and selected units."""
        conversion_type = self.type_var.get()
        from_unit = self.from_var.get()
        to_unit = self.to_var.get()
        input_value = self.input_entry.get()
        
        try:
            input_value = float(input_value)
        except ValueError:
            self.output_entry.config(state='normal')
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, "Invalid input")
            self.output_entry.config(state='readonly')
            return
        
        # Call the appropriate conversion function
        output_value = self.conversions[conversion_type](input_value, from_unit, to_unit)
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, str(output_value))
        self.output_entry.config(state='readonly')

    def convert_length(self, value, from_unit, to_unit):
        """Convert length between meters and feet."""
        if from_unit == "Meters" and to_unit == "Feet":
            return value * 3.28084
        elif from_unit == "Feet" and to_unit == "Meters":
            return value / 3.28084
        else:
            return "Invalid conversion"

    def convert_temperature(self, value, from_unit, to_unit):
        """Convert temperature between Celsius and Fahrenheit."""
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        else:
            return "Invalid conversion"

    def convert_weight(self, value, from_unit, to_unit):
        """Convert weight between kilograms and pounds."""
        if from_unit == "Kilograms" and to_unit == "Pounds":
            return value * 2.20462
        elif from_unit == "Pounds" and to_unit == "Kilograms":
            return value / 2.20462
        else:
            return "Invalid conversion"

# Create the main window
root = tk.Tk()
app = ConverterApp(root)
root.mainloop()
