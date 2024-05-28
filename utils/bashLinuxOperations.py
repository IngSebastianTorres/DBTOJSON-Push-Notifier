import subprocess, sys

command = sys.argv[1:]


def execute_shell_to_commit_push_jsonkpifile():
    print("Commiting file to remote repository ")
    try:
       global result
       result= subprocess.check_output(command, shell = True, executable="/bin/bash", stderr = subprocess.STDOUT)  
    except subprocess.CalledProcessError as cpe:
            result = cpe.output
            #print("Error executing sh commands", cpe)
    finally:
        for line in result.splitlines():
            print(line.decode())
        print("Finishing process on remote repository")