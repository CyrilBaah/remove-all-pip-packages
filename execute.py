import subprocess

# Get the output of the "pip freeze" command
output = subprocess.run(["pip", "freeze"], capture_output=True).stdout.decode()

# Split the output into a list of package names
package_list = output.split("\n")

# Iterate over the package names and uninstall each one
for package in package_list:
    if package:  
        subprocess.run(["pip", "uninstall", "-y", package])
