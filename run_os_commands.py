import subprocess
from subprocess import check_output

project_path = "C:\\Users\\satishdasyam\\AndroidStudioProjects\\MyApplication"

# check_output(["cd", project_path], shell=True).decode()
# output = check_output("cd", shell=True).decode()
# output1 = check_output(["cd", project_path, "gradlew.bat", "checkstyle"], shell=True).decode()

# command = '''cd "C:\\Users\\satishdasyam\\AndroidStudioProjects\\MyApplication"; gradlew checkstyle'''
# command = 'cd'
commands = ["cd", project_path, "gradlew", "checkstyle"]
output = subprocess.run(commands, capture_output=True, shell=True).stdout.decode()

print("Output", output)
