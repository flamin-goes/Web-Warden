from tkinter import *
from tkinter.messagebox import *

host_files = {
    'Windows': r"C:\Windows\System32\drivers\etc\hosts",
    'Linux': '/etc/hosts'  
}
localhost = '127.0.0.1'

def block(win):
    def block_websites(websites):
        host_file = host_files['Windows']
        sites_to_block = list(websites.split(' , '))

        with open('blocked_websites.txt', 'a+') as blocked_websites_txt:
            for site in sites_to_block:
                blocked_websites_txt.write(site + '\n')

        with open(host_file, 'a+') as hostfile:
            content_in_file = hostfile.read()

            for site in sites_to_block:
                if site not in content_in_file:
                    hostfile.write(localhost + '\t' + site + '\n')
                    showinfo('Websites Blocked!', message='The website(s) has been blocked successfully!')
                else:
                    showinfo('Website Already Blocked!', 'The website you entered is already blocked')


    blck_wn = Toplevel(win, background='#4CAF50')
    blck_wn.title("Block a Website")
    blck_wn.geometry('300x200')
    blck_wn.resizable(False, False)

    Label(blck_wn, text='Block Websites', background='#4CAF50', font=("Arial", 18, "bold"), fg="white").pack(pady=5)
    Label(blck_wn, text='Enter the URLs (www.example.com):', background='#4CAF50', font=('Arial', 10), fg="white").pack(pady=5)

    sites = Text(blck_wn, width=35, height=3)
    sites.pack()

    submit_btn = Button(blck_wn, text='Submit', bg='#1976D2', fg="white", font=('Arial', 12, 'bold'),
                        command=lambda: block_websites(sites.get('1.0',END)))
    submit_btn.pack(pady=10)


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
root.geometry('400x250')
root.configure(background='#E0E0E0')
root.wm_resizable(False, False)

Label(root, text='Website Blocker', font=("Arial", 20, "bold"), fg="#37474F", bg="#E0E0E0").place(x=100, y=20)
Label(root, text='What do you want to do?', font=("Arial", 14), fg="#37474F", bg="#E0E0E0").place(x=102, y=70)

block_btn = Button(root, text='Block a Website', font=('Arial', 14), bg='#4CAF50', fg="white", width=15, command=lambda: block(root))
block_btn.place(x=115, y=110)

unblock_btn = Button(root, text='Unblock a Website', font=('Arial', 14), bg='#FF5722', fg="white", width=15, command=lambda: unblock(root))
unblock_btn.place(x=115, y=160)

root.mainloop()
