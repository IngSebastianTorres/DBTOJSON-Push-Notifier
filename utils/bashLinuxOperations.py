import subprocess, sys

command = sys.argv[1:]

def execute_shell_to_commit_push_jsonkpifile():
    print("Commiting file to remote repository ")
    try:
        subprocess.check_output(command, shell = True, executable="/bin/bash", stderr = subprocess.STDOUT)  
    except subprocess.CalledProcessError as cpe:
            print("Error executing sh commands", cpe)
    finally:
        print("Finishing process on remote repository")