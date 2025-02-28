# Delete Empty Folders - Python Script with GUI

This is a Python script that allows users to delete empty folders within a selected directory. It uses the `tkinter` library to create a simple graphical user interface (GUI) for selecting the directory and performing the deletion. The script checks if the folder is empty and then removes it.

## Features
- **Delete Empty Folders**: Automatically detects and deletes empty folders in the selected directory.
- **GUI Interface**: Built with `tkinter` for easy folder selection and interaction.
- **Error Handling**: Displays error messages if the selected path is not a directory or if deletion fails.
- **Success Feedback**: Displays a list of deleted folders or notifies the user if no empty folders were found.

## Requirements
- Python 3.x
- `tkinter` library (Usually pre-installed with Python)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/delete-empty-folders.git
    cd delete-empty-folders
    ```

2. Make sure you have Python 3.x installed on your machine. The script uses the `os` and `tkinter` libraries, which are typically included with Python.

## How to Use

1. Run the script:

    ```bash
    python delete_empty_folders.py
    ```

2. The application window will appear with a "Select Directory" button.
3. Click on the "Select Directory" button to choose a directory from your system.
4. The script will scan the selected directory and delete any empty folders it finds.
5. If there are any deleted folders, a success message will display with the list of deleted folders. If no empty folders are found, a message will indicate that as well.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## Acknowledgements

- [tkinter documentation](https://docs.python.org/3/library/tkinter.html)
- [Python documentation](https://docs.python.org/3/)
# delete_folder_with_emptyfiles
