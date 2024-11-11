import threading
import time

# A function to simulate a task with multithreading
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate a task taking some time
        # Yield control to allow other threads to run (mimics a yield-like behavior)
        time.sleep(0)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulate a task taking some time
        time.sleep(0)  # Yield control

# A function to simulate a background (daemon) task
def background_task():
    while True:
        print("Background task running...")
        time.sleep(2)

# Create threads for the number and letter printing functions
numbers_thread = threading.Thread(target=print_numbers)
letters_thread = threading.Thread(target=print_letters)

# Create a daemon thread for the background task
background_thread = threading.Thread(target=background_task)
background_thread.daemon = True  # Set the background thread as a daemon thread

# Start the threads
numbers_thread.start()
letters_thread.start()
background_thread.start()

# Join the threads to ensure main thread waits for them to complete
numbers_thread.join()  # Main thread waits until numbers_thread completes
letters_thread.join()  # Main thread waits until letters_thread completes

print("All tasks are complete.")
