from tkinter import *
from tkinter.messagebox import *
import time
from datetime import datetime, time as dt_time

host_files = {
    'Windows': r"C:\Windows\System32\drivers\etc\hosts",
    'Linux': '/etc/hosts'  
}

localhost = '127.0.0.1'

# Define blocking schedule
BLOCK_START_TIME = dt_time(9, 0)  # Default blocking starts at 9:00 AM
BLOCK_END_TIME = dt_time(17, 0)   # Default blocking ends at 5:00 PM

# Function to check if current time is within blocking schedule
def is_blocking_schedule():
    current_time = datetime.now().time()
    return BLOCK_START_TIME <= current_time <= BLOCK_END_TIME

def validate_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def block(win):
    def block_websites():
        block_option = block_option_var.get()
        end_time = end_time_entry.get()
        websites = websites_entry.get('1.0', END).strip()

        if block_option == "Always":
            block_website(websites)
        elif block_option == "Schedule" and is_blocking_schedule():
            block_website(websites)
        elif block_option == "User Specific":
            # Get the user-specified end time
            if end_time and validate_time(end_time):
                block_website(websites, end_time)
            else:
                showinfo('Invalid Time', 'Please enter a valid end time (HH:MM)')

    def block_website(websites, end_time=None):
        host_file = host_files['Windows']
        sites_to_block = list(websites.split('\n'))

        with open('blocked_websites.txt', 'a+') as blocked_websites_txt:
            for site in sites_to_block:
                blocked_websites_txt.write(site.strip() + '\n')

        with open(host_file, 'a+') as hostfile:
            content_in_file = hostfile.read()

            for site in sites_to_block:
                if site.strip() not in content_in_file:
                    hostfile.write(localhost + '\t' + site.strip() + '\n')
                    showinfo('Websites Blocked!', message='The website(s) has been blocked successfully!')
                else:
                    showinfo('Website Already Blocked!', 'The website you entered is already blocked')

    blck_wn = Toplevel(win, background='#4CAF50')
    blck_wn.title("Block a Website")
    blck_wn.geometry('400x300')
    blck_wn.resizable(False, False)

    Label(blck_wn, text='Block Websites', background='#4CAF50', font=("Arial", 18, "bold"), fg="white").pack(pady=10)

    block_option_frame = Frame(blck_wn, background='#4CAF50')
    block_option_frame.pack()

    Label(block_option_frame, text='Select Blocking Option:', background='#4CAF50', font=('Arial', 12), fg="white").pack(side=LEFT, padx=10, pady=5)
    block_option_var = StringVar(block_option_frame)
    block_option_var.set("Always")  # Default option
    block_options = ["Always", "Schedule", "User Specific"]
    OptionMenu(block_option_frame, block_option_var, *block_options, command=toggle_end_time_entry).pack(side=LEFT, padx=5, pady=5)

    websites_frame = Frame(blck_wn, background='#4CAF50')
    websites_frame.pack()

    Label(websites_frame, text='Enter the URLs (www.example.com):', background='#4CAF50', font=('Arial', 12), fg="white").pack(side=LEFT, padx=10, pady=5)
    websites_entry = Text(websites_frame, width=35, height=4)
    websites_entry.pack(side=LEFT, padx=5, pady=5)

    global end_time_frame
    end_time_frame = Frame(blck_wn, background='#4CAF50')
    end_time_frame.pack()

    global end_time_entry
    end_time_entry = Entry(end_time_frame, width=10, font=('Arial', 12))
    end_time_entry.pack(side=LEFT, padx=5, pady=5)
    end_time_frame.pack_forget()  # Initially hide the end time entry

    submit_btn = Button(blck_wn, text='Submit', bg='#1976D2', fg="white", font=('Arial', 12, 'bold'), command=block_websites)
    submit_btn.pack(pady=10)

def toggle_end_time_entry(selection):
    if selection == "User Specific":
        end_time_frame.pack()
    else:
        end_time_frame.pack_forget()

def unblock(win):
    def unblock_websites(websites_to_unblock):
        host_file = host_files['Windows']

        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.readlines()
            hostfile.seek(0)

            for line in content_in_file:
                if not any(site in line for site in websites_to_unblock):
                    hostfile.write(line)

            hostfile.truncate()

        with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
            lines = blocked_websites_txt.readlines()
            blocked_websites_txt.seek(0)

            for line in lines:
                if not any(site in line for site in websites_to_unblock):
                    blocked_websites_txt.write(line)

            blocked_websites_txt.truncate()

        showinfo('Websites Unblocked!', 'The selected website(s) has been unblocked successfully!')

    with open('blocked_websites.txt', 'r+') as blocked_websites:
        blck_sites = blocked_websites.read().splitlines()[2:]

    unblck_wn = Toplevel(win, background='#FF5722')
    unblck_wn.title("Unblock a Website")
    unblck_wn.geometry('300x200')
    unblck_wn.resizable(False, False)

    Label(unblck_wn, text='Unblock Websites', background='#FF5722', font=("Arial", 18, "bold"), fg="white").pack(pady=5)
    Label(unblck_wn, text='Select the URLs that you want to unblock:', background='#FF5722', font=('Arial', 10), fg="white").pack(pady=5)

    blck_sites_strvar = StringVar(unblck_wn)
    blck_sites_strvar.set(blck_sites[0])
    dropdown = OptionMenu(unblck_wn, blck_sites_strvar, *blck_sites)
    dropdown.config(width=25)
    dropdown.pack(pady=10)

    submit_btn = Button(unblck_wn, text='Submit', bg='#1976D2', fg="white", font=('Arial', 12, 'bold'), command=lambda: unblock_websites(blck_sites_strvar.get()))
    submit_btn.pack()

# Creating a GUI master window
root = Tk()
root.title("Website Blocker")
root.geometry('400x300')
root.configure(background='#E0E0E0')
root.wm_resizable(False, False)

Label(root, text='Website Blocker', font=("Arial", 20, "bold"), fg="#37474F", bg="#E0E0E0").place(x=100, y=20)
Label(root, text='What do you want to do?', font=("Arial", 14), fg="#37474F", bg="#E0E0E0").place(x=102, y=70)

block_btn = Button(root, text='Block a Website', font=('Arial', 14), bg='#4CAF50', fg="white", width=15, command=lambda: block(root))
block_btn.place(x=115, y=110)

unblock_btn = Button(root, text='Unblock a Website', font=('Arial', 14), bg='#FF5722', fg="white", width=15, command=lambda: unblock(root))
unblock_btn.place(x=115, y=160)

root.mainloop()
