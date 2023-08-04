# Show a context manager for file handling in python that automatically opens and closes a file
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Example usage:
with FileHandler('simon.txt', 'r') as file:
    content = file.read()
    print(content)

# Show a context manager for managing a database connection
import mysql.connector

class DatabaseConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

# Example usage:
with DatabaseConnection('localhost', 'root', '', 'Recess') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM class_name")
    result = cursor.fetchall()
    print(result)


# Show a multithreading and multiprocessing that allows
# us to run a function for different amounts of time

import time
import threading
def some_task():
    time.sleep(1)
    print("Finished task")
if __name__ == "__main__":
    start = time.time()
    # Create two threads
    t1 = threading.Thread(target=some_task)
    t2 = threading.Thread(target=some_task)
    # Start running both threads
    t1.start()
    t2.start()
    # Wait until both threads are complete, and join the process into a single thread
    t1.join()
    t2.join()
    end = time.time()
    print(f"Finished process in {end - start} seconds")

# multiprocessing that allows us to run the function for different amounts of time
import multiprocessing
import time


def long_running_function(seconds):
    time.sleep(seconds)
    print(f"Finished running for {seconds} seconds.")


def main():
    # Create two processes that will run the long_running_function function for different amounts of time.
    process1 = multiprocessing.Process(target=long_running_function, args=(2,))
    process2 = multiprocessing.Process(target=long_running_function, args=(4,))

    # Start the processes.
    process1.start()
    process2.start()

    # Wait for the processes to finish.
    process1.join()
    process2.join()



if __name__ == "__main__":
    main()
