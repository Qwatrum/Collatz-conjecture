import tkinter as tk
import matplotlib.pyplot as plt

NUMBER_OF_STEPS = 100

current_number = -1

numbers = []

def read_input_field():
    global current_number
    current_input = int(input_field.get())
    current_number = current_input
    window.destroy()

    start()

def start():
    global current_number
    numbers.append(current_number)
    for i in range(NUMBER_OF_STEPS):

        if current_number % 2 == 0:
            current_number /= 2
        
        else:
            current_number *= 3
            current_number += 1
        
        numbers.append(current_number)
    
    plot()

def plot():

    plt.plot(numbers, "b-", label="Numbers")
    plt.ylabel("Number")
    plt.ylim(top=max(numbers)+10)
    plt.xlabel("Step")
    plt.legend(loc="upper right")
    plt.show()
    


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Collatz Conjecture")

    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack(padx=10, pady=10)
    lbl = tk.Label(frame, text="Enter your starting number:")
    lbl.grid(row=0, column=0, pady=5)

    input_field = tk.Entry(frame, width=30)
    input_field.grid(row=0, column=1, pady=5, padx=5)
    btn = tk.Button(frame, text="Start", command=read_input_field)
    btn.grid(row=1, columnspan=2, pady=10)

    window.mainloop()