import paramiko
import subprocess

# List of devices to connect to
devices = ['10.255.32.11', '10.255.29.94', '10.255.48.24']

# SSH username and password
username = 'cvpadmin'
password = 'cvp!123'

# Iterate through the list of devices
for device in devices:
  # Create an SSH client
  client = paramiko.SSHClient()

  # Set missing host key policy to auto-add
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  # Connect to the device
  client.connect(device, username=username, password=password)

  # Start a new iTerm2 window
  subprocess.run(['iterm2', '-e', 'ssh ' + device])

  # Close the connection
  client.close()
