import tkinter as tk  # Import the main tkinter module for GUI creation
from tkinter import messagebox  # Import messagebox for pop up alerts
from tkinter import ttk  # Import ttk for advanced widget

# Create the main application window
window = tk.Tk()
window.title("Tournament App")  # Set the window title
window.geometry("400x450")  # Set the window size

# Lists and dictionaries to store team names and their scores
teams = []
scores = {}

# Function to show the competitor setup screen
def show_competitor_setup():
    # Clear all existing widgets from the window
    for widget in window.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(window, text="Set Up Competitors", font=("Arial", 16)).pack(pady=20)
    tk.Label(window, text="Enter Team Name:").pack()

    # Entry field to input team name
    team_name_entry = tk.Entry(window, width=30)
    team_name_entry.pack(pady=5)

    # Listbox to display current teams
    team_listbox = tk.Listbox(window, width=30, height=5)
    team_listbox.pack(pady=5)

    # Populate listbox with existing teams
    for t in teams:
        team_listbox.insert(tk.END, t)

    # Function to save a new team
    def save_team():
        name = team_name_entry.get().strip()

        # Validation checks
        if name == "":
            messagebox.showerror("Error", "Team name cannot be blank")
        elif name in teams:
            messagebox.showerror("Error", "Team already exists")
        elif len(teams) >= 4:
            messagebox.showerror("Error", "Maximum 4 teams allowed")
        else:
            # Add team and initialize score
            teams.append(name)
            scores[name] = 0
            team_listbox.insert(tk.END, name)

            # Clear input field
            team_name_entry.delete(0, tk.END)

            # Confirmation message
            messagebox.showinfo("Saved", f"Team '{name}' added!")

    # Buttons for saving team and returning to menu
    tk.Button(window, text="Save Team", command=save_team).pack(pady=5)
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)

# Function to show score entry screen
def show_enter_scores():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(window, text="Enter Event Scores", font=("Arial", 16)).pack(pady=10)

    # If no teams exist, show warning and return
    if not teams:
        tk.Label(window, text="No teams set up yet!", fg="red").pack(pady=10)
        tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)
        return

    # Dropdown selection for teams
    tk.Label(window, text="Select Team:").pack()
    team_var = tk.StringVar(value=teams[0])
    team_dropdown = ttk.Combobox(window, textvariable=team_var, values=teams, state="readonly")
    team_dropdown.pack(pady=5)

    # Entry for points input
    tk.Label(window, text="Enter Points:").pack()
    points_entry = tk.Entry(window, width=20)
    points_entry.pack(pady=5)

    # Function to save entered score
    def save_score():
        team = team_var.get()
        try:
            pts = int(points_entry.get())

            # Validate positive number
            if pts < 0:
                raise ValueError

            # Add points to selected team
            scores[team] += pts

            # Show confirmation
            messagebox.showinfo("Saved", f"Added {pts} points to '{team}'. Total: {scores[team]}")

            # Clear entry
            points_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number")

    # Buttons for adding points and going back
    tk.Button(window, text="Add Points", command=save_score).pack(pady=5)
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)

# Function to display final results
def show_results():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(window, text="Final Results", font=("Arial", 16)).pack(pady=10)

    # If no scores exist, show warning
    if not scores:
        tk.Label(window, text="No scores recorded yet.", fg="red").pack(pady=10)
    else:
        # Sort teams by score in descending order
        sort_teams = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        # Display ranked results
        for i, (team, pts) in enumerate(sort_teams, 1):
            tk.Label(window, text=f"{i}. {team} - {pts} points", font=("Arial", 12)).pack(pady=3)

    # Back button
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=15)

# Function to show the main menu
def show_main_setup():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Main title
    tk.Label(window, text="Tournament Scoring System", font=("Arial", 16)).pack(pady=20)

    # Navigation buttons
    tk.Button(window, text="Set Up Competitors", width=20, command=show_competitor_setup).pack(pady=10)
    tk.Button(window, text="Enter Event Scores", width=20, command=show_enter_scores).pack(pady=10)
    tk.Button(window, text="View Results", width=20, command=show_results).pack(pady=10)

# Start by showing the main menu
show_main_setup()

# Run the Tkinter event loop making sure the app runs
window.mainloop()