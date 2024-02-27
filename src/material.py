import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get inputs from entry widgets
        material_identity = float(entry1.get())
        density = float(entry2.get())
        young_modulus = float(entry3.get())
        posion_ratio = float(entry4.get())
        thermal_conductivity = float(entry5.get())
        expansion_coefficient = float(entry5.get())
        specific_heat = float(entry5.get())
        
        # Perform calculation
        result = material_identity + density + young_modulus + posion_ratio + thermal_conductivity + expansion_coefficient + specific_heat
        
        # Display result in table format
        result_text = f"{'Input':<10}{'Score':<10}\n"
        result_text += "-"*20 + "\n"
        result_text += f"{'Material Identity':<10}{material_identity:<10.2f}\n"
        result_text += f"{'Density (kg/m^3)':<10}{density:<10.2f}\n"
        result_text += f"{'Young Modulus (Mpa)':<10}{young_modulus:<10.2f}\n"
        result_text += f"{'Posion Ratio':<10}{posion_ratio:<10.2f}\n"
        result_text += f"{'Thermal Conductivity (W/m/K)':<10}{thermal_conductivity:<10.2f}\n"
        result_text += f"{'Expansion Coefficient (mum/m/K)':<10}{expansion_coefficient:<10.2f}\n"
        result_text += f"{'Specific Heat (J/kg/K)':<10}{specific_heat:<10.2f}\n"
        result_text += "-"*20 + "\n"
        result_text += f"{'Total':<10}{result:<10.2f}"
        
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input labels and entry widgets
label1 = tk.Label(root, text="Material Identity:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Density (kg/m^3):")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Young Modulus (Mpa):")
label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

label4 = tk.Label(root, text="Posion Ratio:")
label4.grid(row=3, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1)

label5 = tk.Label(root, text="Thermal Conductivity (W/m/K):")
label5.grid(row=4, column=0)
entry5 = tk.Entry(root)
entry5.grid(row=4, column=1)

label6 = tk.Label(root, text="Expansion Coefficient (mum/m/K):")
label6.grid(row=5, column=0)
entry6 = tk.Entry(root)
entry6.grid(row=5, column=1)

label7 = tk.Label(root, text="Specific Heat (J/kg/K):")
label7.grid(row=6, column=0)
entry7 = tk.Entry(root)
entry7.grid(row=6, column=1)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=7, columnspan=2)

# Create label to display result in table format
result_label = tk.Label(root, text="")
result_label.grid(row=8, columnspan=2)

# Start the main event loop
root.mainloop()
