import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title("Tournament App")
window.geometry("400x450")

teams = []
scores = {}

def show_competitor_setup():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Set Up Competitors", font=("Arial", 16)).pack(pady=20)
    tk.Label(window, text="Enter Team Name:").pack()

    team_name_entry = tk.Entry(window, width=30)
    team_name_entry.pack(pady=5)

    team_listbox = tk.Listbox(window, width=30, height=5)
    team_listbox.pack(pady=5)
    for t in teams:
        team_listbox.insert(tk.END, t)

    def save_team():
        name = team_name_entry.get().strip()
        if name == "":
            messagebox.showerror("Error", "Team name cannot be blank")
        elif name in teams:
            messagebox.showerror("Error", "Team already exists")
        elif len(teams) >= 4:
            messagebox.showerror("Error", "Maximum 4 teams allowed")
        else:
            teams.append(name)
            scores[name] = 0
            team_listbox.insert(tk.END, name)
            team_name_entry.delete(0, tk.END)
            messagebox.showinfo("Saved", f"Team '{name}' added!")

    tk.Button(window, text="Save Team", command=save_team).pack(pady=5)
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)

def show_enter_scores():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Enter Event Scores", font=("Arial", 16)).pack(pady=10)

    if not teams:
        tk.Label(window, text="No teams set up yet!", fg="red").pack(pady=10)
        tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)
        return

    tk.Label(window, text="Select Team:").pack()
    team_var = tk.StringVar(value=teams[0])
    team_dropdown = ttk.Combobox(window, textvariable=team_var, values=teams, state="readonly")
    team_dropdown.pack(pady=5)
    tk.Label(window, text="Enter Points:").pack()

    points_entry = tk.Entry(window, width=20)
    points_entry.pack(pady=5)

    def save_score():
        team = team_var.get()
        try:
            pts = int(points_entry.get())
            if pts < 0:
                raise ValueError
            scores[team] += pts
            messagebox.showinfo("Saved", f"Added {pts} points to '{team}'. Total: {scores[team]}")
            points_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number")

    tk.Button(window, text="Add Points", command=save_score).pack(pady=5)
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)

def show_results():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Final Results", font=("Arial", 16)).pack(pady=10)

    if not scores:
        tk.Label(window, text="No scores recorded yet.", fg="red").pack(pady=10)
    else:
        sort_teams = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for i, (team, pts) in enumerate(sort_teams, 1):
            tk.Label(window, text=f"{i}. {team} - {pts} points", font=("Arial", 12)).pack(pady=3)

    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=15)

def show_main_setup():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Tournament Scoring System", font=("Arial", 16)).pack(pady=20)
    tk.Button(window, text="Set Up Competitors", width=20, command=show_competitor_setup).pack(pady=10)
    tk.Button(window, text="Enter Event Scores", width=20, command=show_enter_scores).pack(pady=10)
    tk.Button(window, text="View Results", width=20, command=show_results).pack(pady=10)

show_main_setup()
window.mainloop()