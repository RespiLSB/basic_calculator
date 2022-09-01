#Developer: WrenSec a.k.a Dovydas Rybakas
#Developed on: 31/08/2022
#IDE used: PyCharm Community Edition 2022.2.1
#Application: Basic Calculator

#Linkedin: https://www.linkedin.com/in/dovydas-rybakas-00157516b/
#GitHub: https://github.com/RespiLSB

#tkinter imported for GUI
import tkinter as tk

#calculation is given name for the.
calculation = ""

#function to add text into text area
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#performs the equation using the input numbers in the text area, deletes the text and displays the end result
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    #if in any case the program cannot solve the input values, it will display the "error" text in the text area
    except:
        clear_field()
        text_result.insert(1.0, "error")

#function to clear the text area.
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#giving the application a resolution and name
root = tk.Tk()
root.title("Basic Calculator 0.1v")
root.geometry("300x275")

#setting the text area size and style of text
text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan = 5)

#Adding buttons, setting their positions, labeling them with correct sizes and fonts.
btn_1 = tk.Button(root, text ="1", command=lambda:add_to_calculation(1), width=5, font=("Arial",14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text ="2", command=lambda:add_to_calculation(2), width=5, font=("Arial",14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text ="3", command=lambda:add_to_calculation(3), width=5, font=("Arial",14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text ="4", command=lambda:add_to_calculation(4), width=5, font=("Arial",14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text ="5", command=lambda:add_to_calculation(5), width=5, font=("Arial",14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text ="6", command=lambda:add_to_calculation(6), width=5, font=("Arial",14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text ="7", command=lambda:add_to_calculation(7), width=5, font=("Arial",14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text ="8", command=lambda:add_to_calculation(8), width=5, font=("Arial",14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text ="9", command=lambda:add_to_calculation(9), width=5, font=("Arial",14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text ="0", command=lambda:add_to_calculation(0), width=5, font=("Arial",14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text ="+", command=lambda:add_to_calculation("+"), width=5, font=("Arial",14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text ="-", command=lambda:add_to_calculation("-"), width=5, font=("Arial",14))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text ="*", command=lambda:add_to_calculation("*"), width=5, font=("Arial",14))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text ="/", command=lambda:add_to_calculation("/"), width=5, font=("Arial",14))
btn_div.grid(row=5, column=4)
btn_open = tk.Button(root, text ="(", command=lambda:add_to_calculation("("), width=5, font=("Arial",14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text =")", command=lambda:add_to_calculation(")"), width=5, font=("Arial",14))
btn_close.grid(row=5, column=3)
btn_clear = tk.Button(root, text ="C", command=clear_field, width=11, font=("Arial",14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equals = tk.Button(root, text ="=", command=evaluate_calculation, width=11, font=("Arial",14))
btn_equals.grid(row=6, column=3, columnspan=2)

root.mainloop()
