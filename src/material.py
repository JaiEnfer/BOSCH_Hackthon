import streamlit as st

def calculate(material_identity, density, young_modulus, posion_ratio, thermal_conductivity, expansion_coefficient, specific_heat):
    result = material_identity + density + young_modulus + posion_ratio + thermal_conductivity + expansion_coefficient + specific_heat
    return result

st.title("Simple Calculator")

material_identity = st.number_input("Material Identity:", format="%f")
density = st.number_input("Density (kg/m^3):", format="%f")
young_modulus = st.number_input("Young Modulus (Mpa):", format="%f")
posion_ratio = st.number_input("Posion Ratio:", format="%f")
thermal_conductivity = st.number_input("Thermal Conductivity (W/m/K):", format="%f")
expansion_coefficient = st.number_input("Expansion Coefficient (mum/m/K):", format="%f")
specific_heat = st.number_input("Specific Heat (J/kg/K):", format="%f")

if st.button("Calculate"):
    result = calculate(material_identity, density, young_modulus, posion_ratio, thermal_conductivity, expansion_coefficient, specific_heat)
    st.write(f"Total: {result}")