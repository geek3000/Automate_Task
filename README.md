# Automate_Task
Automating 3 tasks

## STEP 1: Configuration file

Create a configuration file that tells systemd what we want it to do and when!

```bash
sudo nano /lib/systemd/system/<script_file>.service
```

Add this contain in it!
```
[Unit]
Description=My Script Service for launch My python GUY
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /<Location_To_Py_File>/script.py

[Install]
WantedBy=multi-user.target
```

Then You can save and exit the nano editor using [CTRL-X], [Y] then [ENTER]

## STEP 2: Configuration Of systemd

Tell systemd to start <script_file>.service during the boot sequence
```bash
sudo systemctl daemon-reload
sudo systemctl enable <script_file>.service
```
