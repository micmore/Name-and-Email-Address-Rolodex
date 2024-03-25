# Name & Email Rolodex

This Python application allows users to manage a simple rolodex of names and email addresses. Users can add, look up, modify, and delete contact information, which is stored persistently using Python's `pickle` module. The program features a straightforward graphical user interface (GUI) built with Tkinter.

## Features

- **Add Contact**: Save new contact details (name and email) into the rolodex.
- **Lookup Contact**: Retrieve and display the email address associated with a given name.
- **Change Email**: Update the email address for an existing contact.
- **Delete Contact**: Remove a contact's details from the rolodex.
- **Persistent Storage**: Contact details are saved to and loaded from a file, ensuring data persistence across sessions.


The GUI window will appear, allowing you to interact with your rolodex:

- **Add a Contact**: Enter the name and email in the respective fields and click 'Add'.
- **Look Up a Contact**: Enter the name and click 'Lookup' to display the associated email.
- **Change a Contact's Email**: Enter the name and new email, then click 'Change'.
- **Delete a Contact**: Enter the name and click 'Delete' to remove the contact.

Upon closing the application, you will be prompted to save your changes. The contacts are stored in a file named `contacts.pickle`.

![Name and Email Rolodex](https://media.giphy.com/media/dQnCfVzckezYMREs13/giphy.gif)


## GitHub Repository

The source code for this application is available on GitHub: [Name and Email Address Rolodex Repository](https://github.com/micmore/Name-and-Email-Address-Rolodex)

## Contributing

Feel free to fork the repository and submit pull requests. You can also open issues for bugs, suggestions, or new feature requests.

## License

Specify the license under which your project is made available (e.g., MIT, GPL).
