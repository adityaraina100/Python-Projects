# Server Status Checker
A simple Python script which checks whether a server is running or not. 
**Language:** Python
**Libraries:** requests
Code responds in accordance to the request it gets( server 200 for True)
**To schedule a script using cron, you need to create a crontab entry. Open your crontab file for editing using the command:**

```bash
crontab -e
```

Then, add a line to schedule your script once every week. The syntax is as follows:

```bash
# Minute (0 - 59) Hour (0 - 23) Day of month (1 - 31) Month (1 - 12) Day of week (0 - 6) Command
0 0 * * 0 /path/to/python3 /path/to/your/script.py
```

This crontab entry means:

- Run at 00:00 (midnight)
- Every day of the month
- Every month
- Only on Sunday (0 corresponds to Sunday in the "Day of week" field)
- Execute the specified command (replace `/path/to/python3` with the path to your Python 3 interpreter and `/path/to/your/script.py` with the actual path to your script)

After adding this line, save and exit the editor. The script will now be scheduled to run once every week at the specified time. Adjust the path to the Python interpreter and the script as needed.
