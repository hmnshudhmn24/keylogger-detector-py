import psutil
import ctypes
import win32api
import win32con
import win32gui
import time
import os

# Function to check if a process has keyboard access
def is_keylogger(process):
    try:
        # Get process name
        process_name = process.name()
        # Get process ID
        process_id = process.pid
        
        # List of known keylogger process names (expand as needed)
        known_keyloggers = ["keylogger.exe", "hooker.exe", "spyware.exe"]
        if process_name.lower() in known_keyloggers:
            return True

        # Check if process has global keyboard hooks
        hooks = ctypes.windll.user32.GetKeyboardLayoutList(0, None)
        if hooks > 1:  # Suspicious if multiple hooks exist
            return True

        return False
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False

# Function to get all active processes
def scan_processes():
    print("\n🔍 Scanning for keyloggers...\n")
    suspicious_processes = []

    for process in psutil.process_iter(attrs=['pid', 'name']):
        if is_keylogger(process):
            suspicious_processes.append(process)

    if suspicious_processes:
        print("\n⚠️ WARNING: Suspicious keylogger processes found!\n")
        for proc in suspicious_processes:
            print(f"🔴 Process: {proc.name()} | PID: {proc.pid}")

        return suspicious_processes
    else:
        print("✅ No keyloggers detected.")
        return []

# Function to terminate a suspicious process
def terminate_process(pid):
    try:
        os.kill(pid, 9)
        print(f"✅ Process {pid} terminated successfully!")
    except Exception as e:
        print(f"❌ Unable to terminate process {pid}: {e}")

# Main function
if __name__ == "__main__":
    while True:
        suspicious = scan_processes()
        
        if suspicious:
            user_input = input("\nDo you want to terminate these processes? (yes/no): ").strip().lower()
            if user_input == "yes":
                for proc in suspicious:
                    terminate_process(proc.pid)
        
        time.sleep(10)  # Scan every 10 seconds
