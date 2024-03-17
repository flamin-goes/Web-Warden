# Website Blocker

## Overview

The Website Blocker is a simple tool that allows users to block access to specific websites by manipulating the system's host file. It provides users with the ability to block and unblock websites, either permanently or during specific times.

## Features

- **Block Websites**: Users can specify the URLs of the websites to be blocked.
- **Unblock Websites**: Users can unblock previously blocked websites.
- **Blocking Options**:
   - **Always**: Websites are blocked without any interruptions.
   - **Schedule**: Websites are blocked only during specific scheduled times.
   - **User Specific**: Websites are blocked until a user-specified end time. (Starting time remains same for all i.e 9:00 AM.)
- **Automatic Blocking Schedule**: By default, the application blocks websites from 9:00 AM to 5:00 PM. This can be configured.

## Installation

1. **Install Python**: If you haven't already, you can download and install Python from the official [Python website](https://www.python.org/). Make sure to check the option to add Python to your system's PATH during installation.

2. **Download the Script**: Download the `website_blocker.py` file from this repository.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the `website_blocker.py` file is located. 
   - Run the script using the command:
     ```
     python website_blocker.py
     ```

4. **Using the Application**:
   - The application's GUI will open, allowing you to block or unblock websites as needed.
   - Follow the instructions provided in the GUI to block or unblock websites.

## Usage

1. **Block a Website**:
   - Click on the "Block a Website" button.
   - Choose the blocking option: "Always", "Schedule", or "User Specific".
   - Enter the URLs of the websites to be blocked.
   - If selecting "User Specific", enter the end time until which the websites should be blocked.
   - Click on "Submit" to block the websites.

2. **Unblock a Website**:
   - Click on the "Unblock a Website" button.
   - Select the websites to be unblocked from the dropdown menu.

## Requirements

- Python 3.x
- Tkinter (Python GUI toolkit)

## Troubleshooting

**IF THE TOOL SHOWS ERROR ON RUNTIME:**
Keep the following things in check:
- It needs to be run with admin priveleges, because changes have to be made in hosts file.

## Compatibility

- Compatible with Windows and Linux operating systems.

