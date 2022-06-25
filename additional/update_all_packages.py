import subprocess
import pkg_resources
import time
import os


# python -m pip install --upgrade {package_name}
# python -m pip uninstall {package_name}


start_time = time.time()
installed_packages = ['pip', 'setuptools', 'urllib3', 'pyTelegramBotAPI', 'openpyxl', 'beautifulsoup4', 'requests', 'matplotlib', 'rarfile', 'certifi', 'pywin32', 'Pillow', 'wheel']

for package_obj in pkg_resources.working_set:  # Update list of installed packages
    package_name = " ".join(str(package_obj).split()[:-1])
    if package_name not in installed_packages:
        installed_packages.append(package_name)

packages_strings_array = []
for i in range(len(installed_packages)):  # Install/upgrade packages from list
    os.system('cls')
    packages_strings_array.append(f"{str(i + 1).zfill(3)} | {str(installed_packages[i]).upper()}\n")
    print(f"WORKING ON - {i + 1} / {len(installed_packages)} PACKAGES")
    print("".join(packages_strings_array[-10:]) + "\n")
    subprocess.call(f"python -m pip install --upgrade {installed_packages[i]} --user", shell=True)
os.system('cls')
print(f"WORK DONE")
print("".join(packages_strings_array) + "\n")

print(f"STATISTICS")
print("Total time = {:.2f} s.".format(time.time() - start_time))
print(f"Amount of installed packages = {len(installed_packages)}")
print(f"Installed packages = {installed_packages}")
