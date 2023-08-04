import subprocess

def instalAzulZulu():
    # Set the path to your shell script
    script_path = 'installAzulZulu.sh'

    # Run the shell script
    result = subprocess.run(script_path, check=True , shell = True)

    # Check the return code of the script to see if it ran successfully
    if result.returncode == 0:
        print("Azul Zulu has been installed.")
    else:
        print("There was an error running the script.")

def setJavaHome():
    # Set the path to your shell script
    script_path = 'setJavaHome.sh'

    # Run the shell script
    result = subprocess.run(script_path, check=True , shell = True)

    # Check the return code of the script to see if it ran successfully
    if result.returncode == 0:
        print("JAVA_HOME has been set.")
    else:
        print("There was an error running the script.")


def setMavenPath():
    # Set the path to your shell script
    script_path = 'setMavenPath.sh'

    # Run the shell script
    result = subprocess.run(script_path, check = True, shell = True)

    # Check the return code of the script to see if it ran successfully
    if result.returncode == 0:
        print("Maven has been added to your PATH.")
    else:
        print("There was an error running the script.")


def scoopInstall(program):
    # Use Scoop to install program
    command = 'scoop install ' + program
    process = subprocess.run(command.split(), check = True, shell = True )
    
    if process.returncode == 0:
        print(program + ' has installed successfully')
    else:
        print("There was an error installing the program.")
        
def scoopSearch(program):
    command = 'scoop search ' + program
    process = subprocess.run(command.split(), check = True, shell = True, text = True, capture_output= True)
    
    if process.returncode == 0:
        list = process.stdout.split("\n")
        i = 4
        while (list[i] != ''):
            print(list[i])
        return [i for i in list[4:] if list[i] != ""]
    else:
        print("Bucket not found")
        return []