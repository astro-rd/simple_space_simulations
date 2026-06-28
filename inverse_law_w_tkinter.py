import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def simulate_stellar_flight():
    try:
        # Retrieve and parse inputs from GUI text boxes
        base_lum = float(entry_lum.get())
        start_dist = float(entry_start.get())
        end_dist = float(entry_end.get())
        steps = int(entry_steps.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values only!")
        return

    # Validation checks
    if start_dist <= 0:
        messagebox.showerror("Input Error", "Starting distance must be greater than 0.\nAn initial distance of 0 would imply infinite brightness!")
        return
    
    if steps < 2:
        messagebox.showerror("Input Error", "Number of stops must be at least 2 to calculate a journey!")
        return

    # Clear any previous results from the table view
    for row in tree.get_children():
        tree.delete(row)
        
    # Calculate initial brightness for the 100% reference point
    init_bright = base_lum / (4 * math.pi * (start_dist ** 2))
    
    # Calculate distance change per step
    step_size = (end_dist - start_dist) / (steps - 1)
    
    # Generate and display data steps
    for i in range(steps):
        current_dist = start_dist + (step_size * i)
        current_brightness = base_lum / (4 * math.pi * (current_dist ** 2))
        
        # Convert to percentage relative to the start point
        percent = (current_brightness / init_bright) * 100
        
        # Insert calculated values directly into the interactive GUI table
        tree.insert("", "end", values=(f"{current_dist:,.2f}", f"{percent:,.2f}%"))

# Create the main window application frame
root = tk.Tk()
root.title("Inverse Square Law Generation")
root.geometry("520x650")
root.resizable(False, False)

# Set a modern visual theme for elements
style = ttk.Style()
style.theme_use('clam')

# Header Information Frame
info_frame = ttk.LabelFrame(root, text="Quick Reference", padding=10)
info_frame.pack(fill="x", padx=15, pady=10)

info_msg = (
    "The INVERSE SQUARE LAW explains why a star that is twice as far away "
    "is four times dimmer.\n\n"
    "Formula: I = L / (4 * pi * d^2)\n"
    "• I = Intensity of light\n"
    "• L = Luminosity of the star\n"
    "• d = Distance from the star"
)
ttk.Label(info_frame, text=info_msg, justify="left", wraplength=480).pack()

# User Input Frame
input_frame = ttk.LabelFrame(root, text="Simulation Parameters (Omit Units)", padding=10)
input_frame.pack(fill="x", padx=15, pady=5)

# Grid Layout configuration for Labels and Input Boxes
ttk.Label(input_frame, text="Star Luminosity (Watts, e.g., 3.8e26):").grid(row=0, column=0, sticky="w", pady=4)
entry_lum = ttk.Entry(input_frame, width=22)
entry_lum.grid(row=0, column=1, sticky="e", pady=4)
entry_lum.insert(0, "3.8e26")

ttk.Label(input_frame, text="Starting Distance (AU):").grid(row=1, column=0, sticky="w", pady=4)
entry_start = ttk.Entry(input_frame, width=22)
entry_start.grid(row=1, column=1, sticky="e", pady=4)
entry_start.insert(0, "1.0")

ttk.Label(input_frame, text="Ending Distance (AU):").grid(row=2, column=0, sticky="w", pady=4)
entry_end = ttk.Entry(input_frame, width=22)
entry_end.grid(row=2, column=1, sticky="e", pady=4)
entry_end.insert(0, "10.0")

ttk.Label(input_frame, text="Number of Stops on Journey:").grid(row=3, column=0, sticky="w", pady=4)
entry_steps = ttk.Entry(input_frame, width=22)
entry_steps.grid(row=3, column=1, sticky="e", pady=4)
entry_steps.insert(0, "10")

input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

# Action Trigger Button
btn_run = ttk.Button(root, text="Run Simulation Flight", command=simulate_stellar_flight)
btn_run.pack(pady=15)

# Output Results Frame
output_frame = ttk.LabelFrame(root, text="Flight Logs (Relative Brightness)", padding=10)
output_frame.pack(fill="both", expand=True, padx=15, pady=10)

# Table display configuration using Treeview
columns = ("distance", "brightness")
tree = ttk.Treeview(output_frame, columns=columns, show="headings")
tree.heading("distance", text="Distance (AU)")
tree.heading("brightness", text="Brightness (% of Initial)")
tree.column("distance", anchor="center", width=200)
tree.column("brightness", anchor="center", width=200)

# Vertical scrollbar hookup for long multi-step tables
scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Start the interactive UI loop
root.mainloop()

#ravey_d