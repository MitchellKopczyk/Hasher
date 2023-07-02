# Hasher

Hasher is a simple application that calculates the hash value of a file using various hashing algorithms. It allows you to browse for a file, select a hashing algorithm, provide a checksum value, and then calculates the hash of the file using the selected algorithm. It compares the calculated hash with the provided checksum and displays a message indicating whether they match or not.

## Dependencies

The Hasher application relies on the following dependencies:

- `tkinter`: a standard GUI library for Python.
- `hashlib`: provides hashing algorithms for calculating hash values.
- `binascii`: a module for working with binary and ASCII data.
- `zlib`: a compression library for data integrity checking.
- `crcmod`: a module for creating CRC functions.

Make sure these dependencies are installed before running the application.

## Usage

To use the Hasher application, follow these steps:

1. Launch the application by running the Python script.
2. The main window titled "Hash Calculator" will appear.
3. Enter the checksum value in the provided input box.
4. Click the "Browse" button to select a file for hashing.
5. Choose a hashing algorithm from the drop-down menu.
6. Click the "Calculate Hash" button to calculate the hash of the selected file using the chosen algorithm.
7. A message box will appear, indicating whether the calculated hash matches the provided checksum or not.

## Example

Here's an example usage scenario:

1. Launch the application.
2. Enter the checksum value: `abcd1234`.
3. Click the "Browse" button and select a file named "example.txt".
4. Choose the "SHA256" algorithm from the drop-down menu.
5. Click the "Calculate Hash" button.
6. If the calculated hash matches the provided checksum, a message box will display "The calculated hash matches the provided checksum."
7. If the calculated hash does not match the provided checksum, a message box will display "The calculated hash does not match the provided checksum."

## Note

- The application verifies the selected file's existence and displays an error message if the file is not found.
- The hashing algorithms available in the drop-down menu include SHA1, SHA256, SHA384, SHA512, Blake2, Whirlpool, RIPEMD160, Tiger, MurmurHash, CRC16, CRC32, CRC8, and CRC64.

Feel free to customize the application or add additional features as needed!
