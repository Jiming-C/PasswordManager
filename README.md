# Password Manager – Python (Tkinter)

## Overview
This **Password Manager** is developed using **Python** and **Tkinter**, aimed at securely generating, storing, and managing user credentials. The application utilizes **industry-standard encryption** to protect sensitive information, ensuring data confidentiality and integrity. With a clean and intuitive graphical user interface, the Password Manager is designed for ease of use while maintaining strong security measures.

## Features
- **Secure Password Encryption**: Implements **Fernet encryption** using the `cryptography` library to securely store passwords in an encrypted JSON file.
- **Automated Password Generation**: Provides a feature to generate strong, random passwords with customizable combinations of letters, numbers, and symbols.
- **Data Validation**: Ensures no fields are left empty when saving credentials, improving reliability.
- **Search Functionality**: Allows users to search for and retrieve encrypted passwords by website name, decrypting them as needed.
- **User-Friendly Interface**: A simple yet effective Tkinter-based interface for streamlined password management.

## Technology Stack
- **Language**: Python 3.x
- **GUI Framework**: Tkinter for building the desktop interface.
- **Encryption**: `cryptography` library for secure password encryption (Fernet).
- **Data Storage**: Encrypted JSON file for storing user credentials.
- **Error Handling**: Comprehensive error messages for invalid inputs and missing data.

## How It Works
1. **Password Generation**: Users can generate a strong password by clicking the "Generate Password" button. The password will consist of letters, numbers, and symbols.
2. **Saving Credentials**: Users can enter website, email, and password information, which will be encrypted and stored in the `data.json` file.
3. **Retrieving Credentials**: The application allows users to search for stored credentials by entering the website name. If found, the password is decrypted and displayed securely.
4. **Data Validation**: Prevents saving credentials when required fields (website, email, or password) are empty.

## Installation

## Prerequisites
Ensure that **Python 3.x** is installed on your machine. Then, install the necessary dependencies:

```bash
pip install cryptography
```

### Steps to Install and Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Jiming-C/PasswordManager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PasswordManager
   ```
3. Install required dependencies:
   ```bash
   pip install cryptography
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. **Generate a Password**: Click the "Generate Password" button to create a secure password, which will automatically populate the password field.
2. **Add Credentials**: Enter the website, email, and password, then click "Add" to securely store the credentials. The password is encrypted before being saved in the `data.json` file.
3. **Search for Credentials**: Enter the website name in the search field and click "Search." If the website exists in the stored data, the password will be decrypted and displayed securely.

## File Structure

- **main.py**: Core Python file containing application logic and user interface.
- **data.json**: Stores encrypted credentials (website, email, password).
- **key.key**: Contains the encryption key used for encrypting and decrypting passwords.
- **logo.png**: Image file used for the application logo.

## Security Implementation

- **Encryption**: The application utilizes **Fernet encryption**, ensuring that all passwords are encrypted before storage. Fernet guarantees the security and integrity of encrypted messages, preventing unauthorized access or manipulation.
- **Key Management**: The encryption key is generated and stored in `key.key`. This key is required for both encryption and decryption, ensuring secure access to passwords.
- **Error Handling**: Error messages are displayed when attempting to save empty fields or when searching for non-existent websites in the database.

## Future Improvements
- **Cloud Synchronization**: Implement cloud storage to allow password syncing across devices.
- **Multi-User Support**: Add the ability to support multiple users with individual databases.
- **Password Strength Indicator**: Provide visual feedback on password strength during generation.
- **Two-Factor Authentication (2FA)**: Enhance security by adding 2FA for credential retrieval.

## Demonstration

### Password Manager Interface
1. **Launch the Application**: Run the program to bring up the Tkinter-based graphical interface.
2. **Generate a Password**: Click "Generate Password" to create a strong password. The generated password will be populated into the password field automatically.
3. **Save Credentials**: Input the website name, email, and password, then click "Add" to securely store the credentials.
4. **Search for Credentials**: Use the search functionality to retrieve credentials by website. The application will decrypt and display the password securely.

## Contact Information
For any inquiries, suggestions, or collaborations, feel free to reach out:

- **Email**: [jimingchen2015@gmail.com](mailto:jimingchen2015@gmail.com)
- **GitHub**: [Jiming-C](https://github.com/Jiming-C)

## License
This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
