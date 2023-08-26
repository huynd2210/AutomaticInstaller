import subprocess
import os

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

def addBucket(bucketName):
    command = "scoop bucket add " + bucketName
    process = subprocess.run(command.split(), check = True, shell = True)
    
    return process.returncode == 0
    
def printAppInBucket(bucketName):
    bucket_name = bucketName
    bucket_path = os.path.join(os.getenv("USERPROFILE"), "scoop", "buckets", bucket_name, "bwucket")

    if os.path.exists(bucket_path):
        app_manifests = [f for f in os.listdir(bucket_path) if f.endswith(".json")]

        app = []
        for manifest in app_manifests:
            app_name = os.path.splitext(manifest)[0]
            app.append(app_name)
        return True
    else:
        if (addBucket(bucketName)):
            return printAppInBucket(bucketName)
        else: return False

def scoopInstall(program):
    # Use Scoop to install program
    command = 'scoop install ' + program
    process = subprocess.run(command.split(), check = True, shell = True )
    
    if process.returncode == 0:
        return True
    else:
        return False
        
def scoopSearch(program):
    command = 'scoop search ' + program
    process = subprocess.run(command.split(), check = True, shell = True, text = True, capture_output = True)
    
    if process.returncode == 0:
        list = process.stdout.split("\n")
        return [i for i in list[3:] if list[i] != ""]
    else:
        return []
        
    #return list