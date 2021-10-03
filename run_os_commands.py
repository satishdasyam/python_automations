import subprocess
from subprocess import check_output

project_path = "C:\\Users\\satishdasyam\\AndroidStudioProjects\\MyApplication"

# check_output(["cd", project_path], shell=True).decode()
# output = check_output("cd", shell=True).decode()
# output1 = check_output(["cd", project_path, "gradlew.bat", "checkstyle"], shell=True).decode()

# command = '''cd "C:\\Users\\satishdasyam\\AndroidStudioProjects\\MyApplication"; gradlew checkstyle'''
# command = 'cd'

def run_command(command: list):
    output = subprocess.run(command, capture_output=True, shell=True, check=True, cwd=project_path).stdout.decode()
    print("Output", output)


run_command(["gradlew", "checkstyle"])
#run_command(["gradlew", "test"])
