import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#window setup and size
window = tk.Tk()
window.title("Tournament App")
window.geometry("400x400")

# Screen 2 - Competitor Setup
def show_competitor_setup():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Set Up Competitors", font=("Arial", 16)).pack(pady=20)

    # Team name input
    tk.Label(window, text="Enter Team 1 Name:").pack()
    team_name_entry = tk.Entry(window, width=30)
    team_name_entry.pack(pady=5)

    def save_team():
        name = team_name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Team name cannot be blank")
        else:
            messagebox.showinfo("Saved", f"Team name '{name}' saved!")

    tk.Button(window, text="Save Team Name", command=save_team).pack(pady=10)
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)

#mainmenu setup
def show_main_setup():
    for widget in window.winfo_children():
        #to clear the window
        widget.destroy()

    #creating the main menu title
    tk.Label(window, text="Tournament Scoring System", font=("Arial", 16)).pack(pady=20)

    #creating buttons for the menu
    tk.Button(window, text="Set Up Competitors", width=15, command=show_competitor_setup).pack(pady=10)
    tk.Button(window, text="Enter Event Scores", width=15).pack(pady=10)
    tk.Button(window, text="View Results", width=15).pack(pady=10)

show_main_setup()

window.mainloop()