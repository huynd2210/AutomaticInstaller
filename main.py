import subprocess

def instalAzulZulu():
    # Set the path to your shell script
    script_path = 'installAzulZulu.sh'

    # Run the shell script
    result = subprocess.run(script_path, shell=True)

    # Check the return code of the script to see if it ran successfully
    if result.returncode == 0:
        print("Azul Zulu has been installed.")
    else:
        print("There was an error running the script.")

def setJavaHome():
    # Set the path to your shell script
    script_path = 'setJavaHome.sh'

    # Run the shell script
    result = subprocess.run(script_path, shell=True)

    # Check the return code of the script to see if it ran successfully
    if result.returncode == 0:
        print("JAVA_HOME has been set.")
    else:
        print("There was an error running the script.")


def setMavenPath():
    # Set the path to your shell script
    script_path = 'setMavenPath.sh'

    # Run the shell script
    result = subprocess.run(script_path, shell=True)

    # Check the return code of the script to see if it ran successfully
    if result.returncode == 0:
        print("Maven has been added to your PATH.")
    else:
        print("There was an error running the script.")


def scoopInstall(program):
    # Use Scoop to install program
    command = 'scoop install ' + program
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output.decode())



if __name__ == '__main__':
    instalAzulZulu()
    # setJavaHome()
    # setMavenPath()
