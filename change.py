from datetime import datetime
import subprocess

subprocess.run(["git", "pull"])
with open("./change.log", "a") as file:
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
subprocess.run(["git", "add", "*"])
subprocess.run(["git", "commit", "-m", "log append"])
subprocess.run(["git", "push"])