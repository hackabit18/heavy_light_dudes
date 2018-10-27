# heavy_light_dudes

# Idea of the Project
The idea of the project involves using container technology to make the process of debugging and testing fast and reduce the time associated in building and running a certain project in a specific environment.

We present a GUI which works as a black box and can be used to import projects and perform static and dynamic testing, without going through the cumbersome task of setting up the environment manually.





# Technologies used

* Docker to create and setup environment.
* PYQt for the GUI application.
* Python for implementation.

# How does it work
### For running the application, certain criteria should be satisfied:
  * Docker should be installed. [Install on Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/) 
  * Python3 should be installed
  * **List of dependencies in python3** : docker, PyQt4, sys, os, shutil. (using pip3)
  ### Now, perform the following steps to run the application:
  1. Clone the application on your system using `git clone https://github.com/hackabit18/heavy_light_dudes`
  2. Change directory to `heavy_light_dudes` from the downloaded location.
  3. Run the command: `sudo python3 app.py`. A window will appear. [TODO: Add image here]
  4. Click on the `open` button and choose the folder containing your project.
  5. Select the file which you want to test.
  6. Choose the required configuration.
  7. Click on `compile` or `Static Analysis` for running the tests.
  
# Brief Description

  










