import tkinter as tk
from tkinter import ttk
import random
import time
from input_handling import validate_input
from IntSort import SortInteger 
import matplotlib.pyplot as plt
import customtkinter
from PIL import Image, ImageTk
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
import random
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# Define global variables for user input and sorting results
unsorted_array = []
user_input = ""
flag = False
time_list = {}



# Function to handle user input and validation
def handle_user_input():
    global user_input, data_type, flag
    user_input = input_field.get()
#     data_type = data_type_var.get()
    selected_data_label.config(text=f"Selected Option: {user_input}")
    if validate_input(user_input, "number"):
        error_label.config(text="Valid input", foreground="green")
        flag = False
    else:
        error_label.config(text="Invalid input. Please check your data type selection.", foreground="red")


# Function to generate a random array
def generate_array():
    global unsorted_array, flag
    array_size = array_size_entry.get()
    if array_size.isdigit():
        array_size = int(array_size)
        unsorted_array = [random.randint(1, 1000) for _ in range(array_size)]
        array_size_label.config(text="Array generated with size: " + str(array_size))
        flag = True
        # Update the generated_array_text widget with the new array
        generated_array_text.delete(1.0, tk.END)  # Clear previous content
        generated_array_text.insert(tk.END, ', '.join(map(str, unsorted_array)))
    else:
        array_size_label.config(text="Invalid input for array size")

# Display output
def display_output():
    print('Displaying the')

# Create a function to update the plot data
def update_plot(frame):
    colors = ['red', 'yellow', 'green', 'black', 'blue','pink','purple','grey','orange']  # List of colors

    # Create a bar graph
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(time_list.keys(), time_list.values(), color=colors)  # Use the colors directly
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Execution Time of Sorting Algorithms on a Sorted Array')

    # Function to update the bar heights for animation
    def update(heights):
        for bar, new_height in zip(bars, heights):
            bar.set_height(new_height)

    # Animate the graph
    def animate(frame):
        # Replace execution times with animated values (e.g., frame * 0.01 for a simple animation)
        new_execution_times = [time * (frame * 0.01) for time in time_list.values()]
        update(new_execution_times)

    ani = FuncAnimation(fig, animate, frames=100, interval=100, repeat=False)

    # Display the animated graph
    plt.xticks(rotation=15, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

# Function to toggle all checkboxes
def toggle_all_checkboxes():
    checkbox_state = select_all_var.get()
    for var in algorithm_vars:
        var.set(checkbox_state)
    # If "Select All" is unchecked, ensure the "Select All" checkbox is also unchecked
    if not checkbox_state:
        select_all_var.set(0)

# Function to reset the input field and checkboxes
def reset_values():
    input_field.delete(0, tk.END)  # Clear the input field
    array_size_entry.delete(0, tk.END)  # Clear the array size entry
    generated_array_text.delete(1.0, tk.END)  # Clear the generated array text
    select_all_var.set(0)  # Uncheck "Select All" checkbox
    for var in algorithm_vars:
        var.set(0)  # Uncheck all checkboxes
    

# Function to run selected sorting algorithms and plot results
def run_algorithms():
    time_list = {}
    global flag
    selected_algorithms = [algo_var.get() for algo_var in algorithm_vars]
    execution_times = []
    
    for algo_index, selected in enumerate(selected_algorithms):
        if selected == "1":
                 
            if(flag):
                arr_new1 = unsorted_array
            else:
                arr_input = [int(x) for x in user_input.split(",")] 
                arr_new1 = arr_input
            print(arr_new1)
            arr_new = arr_new1.copy()  # Make a copy of the input array
            start_time = time.time()
            if algo_index == 0:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "BubbleSort")
                time_list["Bubble Sort"] = time_consumed*1000000
            elif algo_index == 1:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "InsertionSort")
                time_list["Insertion Sort"] = time_consumed*1000000
            elif algo_index == 2:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "MergeSort")
                time_list["Merge Sort"] = time_consumed*1000000
            elif algo_index == 3:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "QuickSort")
                time_list["Quick Sort"] = time_consumed*1000000
            elif algo_index == 4:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "HeapSort")
                time_list["Heap Sort"] = time_consumed*1000000
            elif algo_index == 5:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "BucketSort")
                time_list["Bucket Sort"] = time_consumed*1000000
            elif algo_index == 6:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "CountingSort")
                time_list["Counting Sort"] = time_consumed*1000000
            elif algo_index == 7:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "RadixSort")
                time_list["Radix Sort"] = time_consumed*1000000
            elif algo_index == 8:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "SelectionSort")
                time_list["Selection Sort"] = time_consumed*1000000
            
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)
        
    # Plot the comparison graph
    print("Selected List:", time_list)
    print("Selected array:", sorted_array)
    print("Selected Algorithms:", selected_algorithms)

    colors = ['red', 'yellow', 'green', 'blue', 'purple', 'orange', 'pink', 'cyan', 'magenta']
 
    # Create a bar graph
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(time_list.keys(), time_list.values(), color=colors)  # Use the colors directly
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Execution Time of Sorting Algorithms on a Sorted Array')
 
    # Function to update the bar heights for animation
    def update(heights):
        for bar, new_height in zip(bars, heights):
            bar.set_height(new_height)
 
    # Animate the graph
    def animate(frame):
        # Replace execution times with animated values (e.g., frame * 0.01 for a simple animation)
        new_execution_times = [time * (frame * 0.01) for time in time_list.values()]
        update(new_execution_times)
 
    ani = FuncAnimation(fig, animate, frames=100, interval=100, repeat=False)
 
    # Display the animated graph
    plt.xticks(rotation=15, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

    # plot_comparison(selected_algorithms, execution_times)


# Create the main window
root = customtkinter.CTk()
root.title("Sorting Algorithm Efficiency Analyzer")

# configuring the grid
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)

# Create a style for the input label
style = ttk.Style()
style.configure("InputLabel.TLabel", font=("Roboto", 14,"bold" ))

# Create and configure the header frame
header_frame = customtkinter.CTkFrame(root, width=140, corner_radius=10)
header_frame.pack(padx=20, pady=20)
header_image = ImageTk.PhotoImage(Image.open("img/header_image.png").resize((900,130)))
header_button = customtkinter.CTkButton(header_frame, text="",image=header_image, fg_color= "transparent" , hover_color="light blue")
header_button.grid(row=0, column=0, padx=10)
# Create and configure the input frame
input_frame = customtkinter.CTkFrame(root, width=140, corner_radius=10)
input_frame.pack(padx=20, pady=20)

# Create and configure the input field
input_label = ttk.Label(input_frame, text="Enter comma-separated input:", style="InputLabel.TLabel")
input_label.grid(row=1, column=0, sticky=tk.W, padx=(10, 10), pady=(10,10))  # Add padx for space

input_field = ttk.Entry(input_frame, width=40)
input_field.grid(row=1, column=1)

validate_image = ImageTk.PhotoImage(Image.open("img/validate_button_icon.png").resize((30,30)))
validate_button = customtkinter.CTkButton(input_frame, text="Validate Input", command=handle_user_input,image=validate_image, fg_color= "transparent" , hover_color="light blue")
validate_button.grid(row=1, column=2, padx=10)

error_label = ttk.Label(input_frame, text="", foreground="red")
error_label.grid(row=2, columnspan=3)

# Create and configure the array size field
array_size_label = ttk.Label(input_frame, text="Enter array size:  ", style="InputLabel.TLabel")
array_size_label.grid(row=3, column=0, sticky=tk.W, padx=(10, 10), pady=(10,10))

canvas = tk.Canvas(input_frame, width=200, height=30, bg="#2b2b2b", highlightthickness=0)
# canvas.grid(row=3, column=0, sticky=tk.W)

# array_size_label = canvas.create_text(0, 10, anchor=tk.W, text="Enter array size:", font=("ArcadeClassic Regular", 12, "bold"), fill="white")
array_size_label = ttk.Label(input_frame, text="Enter array size:", background="White", style="InputLabel.TLabel")




array_size_entry = ttk.Entry(input_frame, width=10)
array_size_entry.grid(row=3, column=1)

logo_image = ImageTk.PhotoImage(Image.open("img/play_button_icon.png").resize((30,30)))
generate_button = customtkinter.CTkButton(input_frame, text="Generate Array", image = logo_image,command=generate_array,fg_color= "transparent" , hover_color="light blue")
generate_button.grid(row=3, column=2, padx=10)

# Create a label to display the selected data
selected_data_label = ttk.Label(root, text="")
selected_data_label.pack(padx=20, pady=10)

# Create a label to display the generated array
generated_array_label = ttk.Label(root, text="Generated Array:")
generated_array_label.pack(pady=10)

generated_array_text = tk.Text(root, height=5, width=50)
generated_array_text.pack(pady=10)

# Create and configure the sorting algorithm checkboxes
algorithm_frame = ttk.Frame(root)
algorithm_frame.pack(padx=20, pady=10)

algorithm_labels = [
    "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Bucket Sort", "Counting Sort", "Radix Sort", "Selection Sort"
]

algorithm_vars = [tk.StringVar() for _ in algorithm_labels]

algorithm_checkboxes = [ttk.Checkbutton(algorithm_frame, text=label, variable=var) for label, var in zip(algorithm_labels, algorithm_vars)]


for i, checkbox in enumerate(algorithm_checkboxes):
    checkbox.grid(row=i, column=0, sticky=tk.W)
    

# Create a "Select All" checkbox
select_all_var = tk.IntVar()
select_all_checkbox = ttk.Checkbutton(algorithm_frame, text="Select All", variable=select_all_var)

select_all_checkbox.configure(command=toggle_all_checkboxes)
select_all_checkbox.grid(row=len(algorithm_labels), column=0, sticky=tk.W)


# Create and configure the run button
run_button = customtkinter.CTkButton(root, text="Run Algorithms & Plot Comparison", command=run_algorithms)
run_button.pack(pady=10)

# Create and configure the reset button
reset_button = customtkinter.CTkButton(root, text="Reset", command=reset_values)
reset_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()

#test