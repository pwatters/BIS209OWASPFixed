import subprocess

host = input("Host to ping: ")
command = ["ping", "-c", "1", host]
print("\nArguments passed directly to ping:\n", command, "\n")
subprocess.run(command, check=False)
