from tkinter import *
from tkinter import messagebox
import mysql.connector
import main

def login_success():
    # Close the login window
    root.destroy()
    # Run the main application
    # Replace 'main.main()' with your main application function call
    main.main()
   
def login_failed():
    messagebox.showerror("Login Failed", "Invalid username or password")

def login():
    # Retrieve username and password from entry widgets
    username = username_label.get()
    password = password_label.get()

    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Insert your password here
            database="login_db"
        )
        
        cursor = conn.cursor()

        # Execute a query to retrieve the user with the given username and password
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Check if a user with the given credentials exists
        if user:
            login_success()
        else:
            login_failed()
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")

root = Tk()
root.title('Login')
root.configure(bg="#fff")
root.geometry("1100x650")  # Set the window size

# Function to handle window maximize event
def on_maximize(event):
    root.attributes("-fullscreen", True)

# Function to handle window restore event
def on_restore(event):
    root.attributes("-fullscreen", False)

# Binding maximize and restore events to the root window
root.bind("<F11>", on_maximize)
root.bind("<Escape>", on_restore)

img = PhotoImage(file='output.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=450,height=450,bg="white")
frame.place(x=680,y=150)
heading=Label(frame,text="Login",fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=150,y=7)

username_label = Entry(frame, width=45, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 12), highlightbackground="white")
username_label.place(x=30, y=80)
username_label.insert(0, "Username")

Frame(frame, width=295, height=2, bg="black").place(x=35, y=107)

password_label = Entry(frame, width=45, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 12), show='*', highlightbackground="white")
password_label.place(x=30, y=150)
password_label.insert(0, "Password")
Frame(frame,width=295,height=2,bg="black").place(x=35,y=177)

button_canvas = Canvas(frame, width=150, height=50, bg='#57a1f8', highlightthickness=0)
button_canvas.place(x=100, y=220)

# Draw text on the canvas
button_text = button_canvas.create_text(75, 25, text="Login", fill='#fff', font=('Microsoft Yahei UI Light', 12, 'bold'))

# Bind the login function to the button
button_canvas.bind("<Button-1>", lambda event: login())

root.mainloop()
