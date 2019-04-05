This is a skeleton repo that I made for creating new python projects that run inside a Docker container. The goal is to be able to click the 
'Debug' button in VSCode and have it kick off your script inside of your Docker container, with full debugging support.

# Setup
1. Install VSCode
2. Install Python 3.7+
3. Install VSCode Extensions:
  * Docker
  * GitLens (Optional)
  * Python
4. Install PTVSD
  * pip3 install ptvsd==4.2.5 --user
5. (Optional) Install autopep8
  * pip3 install autopep8 --user


# Forking & Customizing
 * Please fork it and use it.  Any errors, please submit back to me (or a pull request!)
 * Change the name of the project folder to match your project
 * Change the Dockerfile to some more intersting container, like tensorflow
 * Delete debug_test.py, and put some interesting project in this repo

# Debugging an existing target
1. Compose your docker container (ctrl+shift+P, Docker Compose)
    This will take a few moments to run.
2. Select a debug target from the dropdown in Visual Studio Code, and hit 'Debug'.
3. Wait 5 - 7 seconds for it to time out.  Then click 'Debug Anyway' in the popup.
4. Success!

# Adding a new debug target:
1. Add an entry in tasks.json
2. Add an entry in launch.json

# Troubleshooting
  * The internet has observed that mismatching versions of PTVSD on your host environment & in the docker container can lead to problems.
  * Make sure something else isn't using port 5678, the default port