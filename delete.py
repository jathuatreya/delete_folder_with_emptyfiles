import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to delete empty folders
def delete_empty_folders(directory):
    if not os.path.isdir(directory):
        messagebox.showerror("Error", "The selected path is not a directory.")
        return
    
    # Loop through all folders in the selected directory
    deleted_folders = []
    for foldername, subfolders, filenames in os.walk(directory, topdown=False):
        for folder in subfolders:
            folder_path = os.path.join(foldername, folder)
            # Check if the folder is empty
            if not os.listdir(folder_path):
                try:
                    os.rmdir(folder_path)
                    deleted_folders.append(folder_path)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete folder: {folder_path}\n{str(e)}")

    # Display success message with the list of deleted folders
    if deleted_folders:
        messagebox.showinfo("Success", f"Deleted empty folders:\n" + "\n".join(deleted_folders))
    else:
        messagebox.showinfo("No Empty Folders", "No empty folders found to delete.")

# Function to open file dialog to select directory
def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        delete_empty_folders(directory)

# Create the GUI window
root = tk.Tk()
root.title("Delete Empty Folders")
root.geometry("300x150")

# Add a button to select the directory
btn_select_dir = tk.Button(root, text="Select Directory", command=browse_directory)
btn_select_dir.pack(expand=True)

# Run the GUI
root.mainloop()
