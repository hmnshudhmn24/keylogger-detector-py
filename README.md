# Keylogger Detector 🔍🚀

## 📌 Overview
This **Keylogger Detector** scans running processes on a Windows system to identify and terminate potential keyloggers. 
It checks for known keylogger process names, detects global keyboard hooks, and alerts users if suspicious activity is found.

## 🛠 Features
✅ Scans active processes for known keyloggers  
✅ Detects unauthorized keyboard hooks  
✅ Alerts users if suspicious activity is found  
✅ Provides an option to **terminate** suspicious processes  
✅ Runs scans automatically every **10 seconds**  

## 📂 Project Structure
```
Keylogger-Detector/
│── keylogger_detector.py  # Main script
│── README.md              # Documentation
```

## 🚀 Installation & Usage

### Step 1: Install Dependencies
Run the following command in the terminal:
```sh
pip install psutil pywin32
```

### Step 2: Run the Keylogger Detector
```sh
python keylogger_detector.py
```

### Step 3: Monitor & Terminate Suspicious Processes
- If a keylogger is detected, the script will **display a warning**.  
- You can **choose to terminate the process** by typing **"yes"** when prompted.  

## 📌 How It Works
1. **Scans running processes** and checks for suspicious activity.  
2. **Identifies keyloggers** by analyzing known threats & keyboard hooks.  
3. **Alerts the user** and offers to terminate suspicious processes.  
4. **Repeats the scan every 10 seconds** for continuous monitoring.  

## 🔐 Security Tips
- Keep your **antivirus software updated**.  
- Regularly **check installed applications** for unknown programs.  
- Run this script frequently to detect and remove any hidden keyloggers.  
