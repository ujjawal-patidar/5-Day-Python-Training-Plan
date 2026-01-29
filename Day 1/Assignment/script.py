import sys
import os
import subprocess

def script():
    try:
        # Check if Python is installed and print version
        print(f"current version of python is - {sys.version_info.major}:{sys.version_info.minor}:{sys.version_info.micro}")
    
        # Validate Python version (must be 3.00 or higher)
        required_version = 3

        if sys.version_info.major < required_version:
            print(f"Update the python to version")
            return
        
        # os.chdir('/')
        directory = {
            "src":["api", "core", 'db', "models", "services"],
            "tests":[],
            "docs": [],
            "logs" : []
        }

        for key,value in directory.items():
            current_dir = os.getcwd()
            directory = key
            path = os.path.join(current_dir, directory)
            os.mkdir(path)

            for subfolder in value:
                current_dir = path
                directory = subfolder
                path = os.path.join(current_dir, directory)
                os.mkdir(path)


        # now making requirement.txt file and writting some essential packages
        requirement_list = [
            "requests==2.25.1\n",
            "bcrypt\n"
            "python-.env"
        ]

        try:
            with open("requirements.txt", "w") as file:
                file.writelines(requirement_list)
            print("Successfull created and wrote requirements.txt")
        except IOError as e:
            print("Error in file requirements.txt writing", e)

        # now we are creating the virtual enviroment
        
        # print("Creating virtual Enviroment......")
        # subprocess.run(["python3", "-m", "venv", ".venv"])
        # print("virtual Enviroment Created!!")

        # print("Activating virtual Enviroment")
        # subprocess.run(["python3","-m", "source", ".venv/bin/activate"])
        # print("virtual Enviroment Activate")

        # print("Installing all the requirement......")
        # subprocess.run(["python3","-m", "pip", "install", "-r", "requirements.txt"])
        # print("Requirement Installed")


        # create the virtual environment
        print("Creating virtual Environment......")
        try:
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        except Exception as e:
            print("Error in creating virtual enviroment", e)
        print("virtual Environment Created!!")

        # find path venv's Python binary
        venv_python = os.path.join(".venv", "bin", "python3")

        # Use the venv's own python to install requirements,
        # whrn we activate the venv basically the path in the os enviroment changed to our full_path/.venv/bin/python3 interpreter therefore all the dependencieds then starts to install in the venv folder
        # (ye basically of activating + installing)
        print("Installing all the requirements......")
        try:
            subprocess.run([venv_python, "-m", "pip","install", "-r","requirements.txt"], check=True)
        except Exception as e:
            print("Error in activating and installing requirements", e)
        print("Requirements Installed")
        

        gitignore_list = [
            ".venv\n",
            ".env"
        ]

        try:
            with open(".gitignore", "w") as file:
                file.writelines(gitignore_list)
            print("Successfull created and wrote .gitignore")
        except IOError as e:
            print("Error in file .gitignore writing", e)


    except Exception as e:
        print("Error occured : ", e)


print("Script Started....")
script()
print("Script finished, Enjoy coding")





# output
# lap-51@lap-51-HP-EliteBook-840-G7-Notebook-PC:~/Desktop/5-Day-Python-Training-Plan/Day 1/Assignment$ python3 script.py
# Script Started....
# current version of python is - 3:12:3
# Successfull created and wrote requirements.txt
# Creating virtual Environment......
# virtual Environment Created!!
# Installing all the requirements......
# Collecting requests==2.25.1 (from -r requirements.txt (line 1))
#   Downloading requests-2.25.1-py2.py3-none-any.whl.metadata (4.2 kB)
# Collecting bcrypt (from -r requirements.txt (line 2))
#   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
# Collecting python-.env (from -r requirements.txt (line 3))
#   Downloading python-env-1.0.0.tar.gz (2.1 kB)
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Preparing metadata (pyproject.toml) ... done
# Collecting chardet<5,>=3.0.2 (from requests==2.25.1->-r requirements.txt (line 1))
#   Downloading chardet-4.0.0-py2.py3-none-any.whl.metadata (3.5 kB)
# Collecting idna<3,>=2.5 (from requests==2.25.1->-r requirements.txt (line 1))
#   Downloading idna-2.10-py2.py3-none-any.whl.metadata (9.1 kB)
# Collecting urllib3<1.27,>=1.21.1 (from requests==2.25.1->-r requirements.txt (line 1))
#   Downloading urllib3-1.26.20-py2.py3-none-any.whl.metadata (50 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.1/50.1 kB 1.9 MB/s eta 0:00:00
# Collecting certifi>=2017.4.17 (from requests==2.25.1->-r requirements.txt (line 1))
#   Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
# Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 kB 5.6 MB/s eta 0:00:00
# Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 278.2/278.2 kB 7.0 MB/s eta 0:00:00
# Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 152.9/152.9 kB 10.2 MB/s eta 0:00:00
# Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 178.7/178.7 kB 9.7 MB/s eta 0:00:00
# Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.8/58.8 kB 4.3 MB/s eta 0:00:00
# Downloading urllib3-1.26.20-py2.py3-none-any.whl (144 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 144.2/144.2 kB 7.6 MB/s eta 0:00:00
# Building wheels for collected packages: python-.env
#   Building wheel for python-.env (pyproject.toml) ... done
#   Created wheel for python-.env: filename=python_env-1.0.0-py3-none-any.whl size=2461 sha256=a89c4385024145bbd50dec9d2426522ee02c54760dc84cff499601a62c6302dc
#   Stored in directory: /home/lap-51/.cache/pip/wheels/19/06/51/75aa7599efaaa837fd2d785b36db857bf7a15cd381ddfd079e
# Successfully built python-.env
# Installing collected packages: python-.env, urllib3, idna, chardet, certifi, bcrypt, requests
# Successfully installed bcrypt-5.0.0 certifi-2026.1.4 chardet-4.0.0 idna-2.10 python-.env-1.0.0 requests-2.25.1 urllib3-1.26.20
# Requirements Installed
# Successfull created and wrote .gitignore
# Script finished, Enjoy coding


