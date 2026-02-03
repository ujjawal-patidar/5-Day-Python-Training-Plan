# Write a context manager class using __enter__ and __exit__ methods to handle database connections or file operations.

class FileManager:
    """
    A context manager for safely handling file operations.
    Ensures the file is closed automatically upon exiting the 'with' block.
    """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            print("Enter called >>>>>>>>>")
            self.file = open(self.filename, self.mode)
            return self.file
        except IOError as e:
            print(f"Error opening file {e}")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the file.
        This method is called automatically when exiting the 'with' block.
        """
        if self.file:
            print("clossing file>>>>>")
            self.file.close()
        
        # You can handle exceptions here if needed.
        # Returning True from this method suppresses any exception
        # that occurred within the 'with' block.
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        # Returning False (default) allows the exception to propagate
        return False

# --- Usage Example ---
file_path = 'example.txt'

try:
    with FileManager(file_path, 'w') as f:
        if f:
            f.write('Hello, world!\n')
            f.write('This file will close automatically.')
            print("file writtern successfully")
    
    print(f"File '{file_path}' has been written to and closed....{f}")

    with FileManager(file_path, 'r') as f:
        if f:
            content = f.read()
            print(f"Content of '{file_path}':\n{content}")

except Exception as e:
    print(f"An error occurred outside the context manager: {e}")

