import tkinter as tk
from tkinter import messagebox
from recommendation_engine import get_recommendations

def recommend_material():
    try:
        # Get user input
        material_identity = material_identity_entry.get()
        density = float(density_entry.get())
        young_modulus = float(young_modulus_entry.get())
        poisson_ratio = float(poisson_ratio_entry.get())
        thermal_conductivity = float(thermal_conductivity_entry.get())
        expansion_coefficient = float(expansion_coefficient_entry.get())
        specific_heat = float(specific_heat_entry.get())

        # Prepare user requirements
        user_requirements = {
            'Material Identity': material_identity,
            'Density (kg/m^3)': density,
            'Young Modulus (MPa)': young_modulus,
            'Poisson Ratio': poisson_ratio,
            'Thermal Conductivity (W/m/K)': thermal_conductivity,
            'Expansion Coefficient (mum/m/K)': expansion_coefficient,
            'Specific Heat (J/kg/K)': specific_heat
        }
        
        # Get recommendations
        recommendations = get_recommendations(user_requirements)
        
        # Display recommendations
        messagebox.showinfo("Recommendations", recommendations)
        
    except ValueError as e:
        invalid_field = str(e).split(":")[0].strip()
        messagebox.showerror("Error", f"Invalid value in {invalid_field} field. Please enter a valid numerical value.")


# Create GUI
root = tk.Tk()
root.title("Material Recommendation System")

# Labels
tk.Label(root, text="Material Identity:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Density (kg/m^3):").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Young Modulus (MPa):").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Poisson Ratio:").grid(row=3, column=0, padx=5, pady=5)
tk.Label(root, text="Thermal Conductivity (W/m/K):").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, text="Expansion Coefficient (mum/m/K):").grid(row=5, column=0, padx=5, pady=5)
tk.Label(root, text="Specific Heat (J/kg/K):").grid(row=6, column=0, padx=5, pady=5)

# Entry fields
material_identity_entry = tk.Entry(root)
material_identity_entry.grid(row=0, column=1, padx=5, pady=5)
density_entry = tk.Entry(root)
density_entry.grid(row=1, column=1, padx=5, pady=5)
young_modulus_entry = tk.Entry(root)
young_modulus_entry.grid(row=2, column=1, padx=5, pady=5)
poisson_ratio_entry = tk.Entry(root)
poisson_ratio_entry.grid(row=3, column=1, padx=5, pady=5)
thermal_conductivity_entry = tk.Entry(root)
thermal_conductivity_entry.grid(row=4, column=1, padx=5, pady=5)
expansion_coefficient_entry = tk.Entry(root)
expansion_coefficient_entry.grid(row=5, column=1, padx=5, pady=5)
specific_heat_entry = tk.Entry(root)
specific_heat_entry.grid(row=6, column=1, padx=5, pady=5)

# Recommendation button
recommend_button = tk.Button(root, text="Get Recommendations", command=recommend_material)
recommend_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()