import tkinter as tk  # Import the main tkinter module for GUI creation
from tkinter import messagebox  # Import messagebox for pop up alerts
from tkinter import ttk  # Import ttk for advanced widget

# Create the main application window
window = tk.Tk()
window.title("Tournament App")  # Set the window title
window.geometry("400x500")  # Set the window size

# Lists and dictionaries to store team names and their scores
teams = []
scores = {}

# New: dictionary to store list of members for each team
team_members = {}

# New: list and dictionary for individual competitors and their scores
individuals = []
individual_scores = {}

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

    # Fill listbox with existing teams
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
            # New: create an empty members list for this team
            team_members[name] = []
            team_listbox.insert(tk.END, name)

            # Clear input field
            team_name_entry.delete(0, tk.END)

            # Confirmation message
            messagebox.showinfo("Saved", f"Team '{name}' added!")

    # Buttons for saving team and returning to menu
    tk.Button(window, text="Save Team", command=save_team).pack(pady=5)
    # New: button to go to the manage members screen
    tk.Button(window, text="Manage Team Members", command=show_manage_members).pack(pady=5)
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)


# New: Function to add members to a team
def show_manage_members():
    # Clear all existing widgets from the window
    for widget in window.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(window, text="Manage Team Members", font=("Arial", 16)).pack(pady=10)

    # If no teams exist, show warning and go back
    if not teams:
        tk.Label(window, text="No teams set up yet!", fg="red").pack(pady=10)
        tk.Button(window, text="Back", command=show_competitor_setup).pack(pady=5)
        return

    # Dropdown to select which team to add members to
    tk.Label(window, text="Select Team:").pack()
    team_var = tk.StringVar(value=teams[0])  # Default to first team
    team_dropdown = ttk.Combobox(window, textvariable=team_var, values=teams, state="readonly")
    team_dropdown.pack(pady=5)

    # Entry field to type a member name
    tk.Label(window, text="Enter Member Name:").pack()
    member_entry = tk.Entry(window, width=30)
    member_entry.pack(pady=5)

    # Listbox to display members of the selected team
    member_listbox = tk.Listbox(window, width=30, height=5)
    member_listbox.pack(pady=5)

    # Function to refresh the listbox when a different team is selected
    def refresh_members(event=None):
        member_listbox.delete(0, tk.END)  # Clear the listbox first
        selected_team = team_var.get()
        for m in team_members.get(selected_team, []):  # Loop through that team's members
            member_listbox.insert(tk.END, m)

    # Bind the dropdown so it refreshes when the user changes team
    team_dropdown.bind("<<ComboboxSelected>>", refresh_members)

    # Load members for the default team on screen open
    refresh_members()

    # Function to add a member to the selected team
    def add_member():
        selected_team = team_var.get()
        member_name = member_entry.get().strip()

        # Validation checks
        if member_name == "":
            messagebox.showerror("Error", "Member name cannot be blank")
        elif member_name in team_members[selected_team]:
            messagebox.showerror("Error", "Member already in this team")
        else:
            # Add member to that team's list in the dictionary
            team_members[selected_team].append(member_name)
            member_listbox.insert(tk.END, member_name)
            member_entry.delete(0, tk.END)  # Clear the entry field
            messagebox.showinfo("Saved", f"'{member_name}' added to '{selected_team}'!")

    # Buttons for adding a member and going back
    tk.Button(window, text="Add Member", command=add_member).pack(pady=5)
    tk.Button(window, text="Back", command=show_competitor_setup).pack(pady=5)


# New: Function to show the individual competitor setup screen
def show_individual_setup():
    # Clear all existing widgets from the window
    for widget in window.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(window, text="Set Up Individuals", font=("Arial", 16)).pack(pady=20)
    tk.Label(window, text="Enter Individual Name:").pack()

    # Entry field to input individual name
    individual_entry = tk.Entry(window, width=30)
    individual_entry.pack(pady=5)

    # Listbox to display current individuals
    individual_listbox = tk.Listbox(window, width=30, height=5)
    individual_listbox.pack(pady=5)

    # Fill listbox with existing individuals
    for i in individuals:
        individual_listbox.insert(tk.END, i)

    # Function to save a new individual
    def save_individual():
        name = individual_entry.get().strip()

        # Validation checks
        if name == "":
            messagebox.showerror("Error", "Name cannot be blank")
        elif name in individuals:
            messagebox.showerror("Error", "Individual already exists")
        elif len(individuals) >= 10:
            messagebox.showerror("Error", "Maximum 10 individuals allowed")
        else:
            # Add individual and initialize their score to 0
            individuals.append(name)
            individual_scores[name] = 0
            individual_listbox.insert(tk.END, name)
            individual_entry.delete(0, tk.END)  # Clear the entry field
            messagebox.showinfo("Saved", f"'{name}' added!")

    # Buttons for saving and going back to menu
    tk.Button(window, text="Save Individual", command=save_individual).pack(pady=5)
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


# New: Function to enter scores for individual competitors
def show_enter_individual_scores():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(window, text="Enter Individual Scores", font=("Arial", 16)).pack(pady=10)

    # If no individuals exist, show warning and return
    if not individuals:
        tk.Label(window, text="No individuals set up yet!", fg="red").pack(pady=10)
        tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)
        return

    # Dropdown selection for individuals
    tk.Label(window, text="Select Individual:").pack()
    individual_var = tk.StringVar(value=individuals[0])  # Default to first individual
    individual_dropdown = ttk.Combobox(window, textvariable=individual_var, values=individuals, state="readonly")
    individual_dropdown.pack(pady=5)

    # Entry for points input
    tk.Label(window, text="Enter Points:").pack()
    points_entry = tk.Entry(window, width=20)
    points_entry.pack(pady=5)

    # Function to save entered score for individual
    def save_individual_score():
        person = individual_var.get()
        try:
            pts = int(points_entry.get())

            # Validate positive number
            if pts < 0:
                raise ValueError

            # Add points to selected individual
            individual_scores[person] += pts

            # Show confirmation
            messagebox.showinfo("Saved", f"Added {pts} points to '{person}'. Total: {individual_scores[person]}")

            # Clear entry
            points_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number")

    # Buttons for adding points and going back
    tk.Button(window, text="Add Points", command=save_individual_score).pack(pady=5)
    tk.Button(window, text="Back to Menu", command=show_main_setup).pack(pady=5)


# Function to display final results
def show_results():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Title label
    tk.Label(window, text="Final Results", font=("Arial", 16)).pack(pady=10)

    # Team results section
    tk.Label(window, text="-- Team Standings --", font=("Arial", 13, "bold")).pack(pady=5)

    # If no scores exist, show warning
    if not scores:
        tk.Label(window, text="No team scores recorded yet.", fg="red").pack(pady=5)
    else:
        # Sort teams by score in descending order
        sort_teams = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        # Display ranked results
        for i, (team, pts) in enumerate(sort_teams, 1):
            tk.Label(window, text=f"{i}. {team} - {pts} points", font=("Arial", 12)).pack(pady=2)

            # New: show the team's members in grey text underneath
            members = team_members.get(team, [])
            if members:
                tk.Label(window, text="   Members: " + ", ".join(members), font=("Arial", 9), fg="gray").pack()

    # New: Individual results section
    tk.Label(window, text="-- Individual Standings --", font=("Arial", 13, "bold")).pack(pady=5)

    # If no individual scores exist, show warning
    if not individual_scores:
        tk.Label(window, text="No individual scores recorded yet.", fg="red").pack(pady=5)
    else:
        # Sort individuals by score in descending order
        sort_individuals = sorted(individual_scores.items(), key=lambda x: x[1], reverse=True)

        # Display ranked individual results
        for i, (person, pts) in enumerate(sort_individuals, 1):
            tk.Label(window, text=f"{i}. {person} - {pts} points", font=("Arial", 12)).pack(pady=2)

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
    tk.Button(window, text="Set Up Competitors", width=22, command=show_competitor_setup).pack(pady=7)
    # New: button to go to individual setup screen
    tk.Button(window, text="Set Up Individuals", width=22, command=show_individual_setup).pack(pady=7)
    tk.Button(window, text="Enter Event Scores", width=22, command=show_enter_scores).pack(pady=7)
    # New: button to go to individual score entry screen
    tk.Button(window, text="Enter Individual Scores", width=22, command=show_enter_individual_scores).pack(pady=7)
    tk.Button(window, text="View Results", width=22, command=show_results).pack(pady=7)

# Start by showing the main menu
show_main_setup()

# Run the Tkinter event loop making sure the app runs
window.mainloop()
