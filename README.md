# Setup
1. Install VSCode
2. Install Python 3.7+
3. Install VSCode Extensions:
  * Docker
  * GitLens (Optional)
  * Python
4. Install PTVSD
    $ pip3 install ptvsd==4.2.5 --user
5. (Optional) Install autopep8
    $ pip3 install autopep8 --user


# Debugging
1. Compose your docker container (ctrl+shift+P, Docker Compose)
    This will take a few moments to run.
2. 

# Troubleshooting
  * The internet has observed that mismatching versions of PTVSD on your host environment & in the docker container can lead to problems.