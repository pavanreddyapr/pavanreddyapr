
  # Import necessary modules
import tkinter as tk

# Define conversion factors
CONVERSION_FACTORS = {
    'Grams': 1000,
    'Milligrams': 1000000,
    'Micrograms': 1000000000,
    'Tonnes': 0.001,
    'Pounds': 2.20462,
    'Ounces': 35.274
}

# Define conversion function
def convert():
    try:
        value = float(entry_value.get())
        input_unit = input_unit_variable.get()
        output_unit = output_unit_variable.get()
        conversion_factor = CONVERSION_FACTORS[input_unit] / CONVERSION_FACTORS[output_unit]
        result = value * conversion_factor
        label_result.config(text=f'{result:.4g} {output_unit}')
    except ValueError:
        label_result.config(text='Invalid Input')

# Create GUI
root = tk.Tk()
root.title('Unit Converter')

# Create input field
label_value = tk.Label(root, text='Value:')
label_value.grid(row=0, column=0)
entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1)

# Create input unit dropdown menu
label_input_unit = tk.Label(root, text='Input Unit:')
label_input_unit.grid(row=1, column=0)
input_units = list(CONVERSION_FACTORS.keys())
input_unit_variable = tk.StringVar(root, input_units[0])
input_unit_menu = tk.OptionMenu(root, input_unit_variable, *input_units)
input_unit_menu.grid(row=1, column=1)

# Create output unit dropdown menu
label_output_unit = tk.Label(root, text='Output Unit:')
label_output_unit.grid(row=2, column=0)
output_units = list(CONVERSION_FACTORS.keys())
output_unit_variable = tk.StringVar(root, output_units[1])
output_unit_menu = tk.OptionMenu(root, output_unit_variable, *output_units)
output_unit_menu.grid(row=2, column=1)

# Create convert button
button_convert = tk.Button(root, text='Convert', command=convert)
button_convert.grid(row=3, column=0)

# Create result label
label_result = tk.Label(root, text='')
label_result.grid(row=3, column=1)

# Run GUI
root.mainloop()

