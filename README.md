# Introduction

The Jupyter notebook `python_intro.ipynb` gives an introduction to Python. The notebook can be run either in a cloud environment or locally on your computer. Below are instructions on local installation as well as on two cloud environments:
* [mybinder.org](https://mybinder.readthedocs.io/en/latest/about/about.html): easy to use but can be slow to start up and has limited computational resources
* [hub.cs.helsinki.fi](https://wiki.helsinki.fi/display/it4sci/Jupyter+Hub+User+Guide): available for participants of the computational methods course at UH, requires some setup

## Running the notebook at mybinder.org

Simply click the following button 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uh-comp-methods1/intro/main?labpath=python_intro.ipynb)

## Installation at hub.cs.helsinki.fi

Install the Python environment:

1. If you are not in the UH network, you need to establish first a VPN connection, see the [instructions](#vpn-connection) below
2. Log into `turso` by opening a terminal and running
```
ssh your_username@turso.cs.helsinki.fi
```
3. Install the Python environment on `turso` by running
```
curl -O https://raw.githubusercontent.com/uh-comp-methods1/intro/main/docs/install_turso.sh
bash install_turso.sh
```

The last step takes a while, and it is not needed to run `python_intro.ipynb`, however, it is needed to run the lectures. 
While waiting for the last step to finish, you can can proceed with the following:

* Go to the [hub](https://hub.cs.helsinki.fi) and log in
    - If you are not in the UH network, VPN connection is needed also for this
* Choose the Vorna profile with the least computational resources 
  - Do **not** choose a classic notebook profile
* Go to the `home` directory using the File Browser in JupyterLab

Now follow the instructions on [running the notebook](#running-the-notebook) below.

## Local installation

(Those preferring the Linux command line can follow these [alternative instructions](docs/install_cli.md).)

You need to install first [Anaconda](https://www.anaconda.com/products/individual). Once you have Anaconda installed, do the following: 

* Download the [environment file](https://raw.githubusercontent.com/uh-comp-methods1/intro/main/docs/environment.yml)
* Open Anaconda Navigator
* Click Environments
* Click Import
* Choose the file `environment.yml` that you downloaded and click Import

The last step takes a while so wait patiently. Once the environment is istalled, start JupyterLab in Anaconda Navigator:

* Click Home
* Select **comp-methods** in the Applications dropdown menu
* Click the Launch button of JupyterLab 

Now proceed to the next section.

## Running the notebook

* Click Terminal under Other
    - You might want to create a subdirectory for the course material, but this is optional:
```
mkdir comp-methods
cd comp-methods
```
* Run the following command 
```
git clone https://github.com/uh-comp-methods1/intro
```
* Close the terminal

This creates a new folder called `intro`
containing a Jupyter notebook called `python_intro.ipynb`.
Open the notebook for an introduction to Python.

## VPN connection

See the [instructions](https://helpdesk.it.helsinki.fi/en/help/5190) at IT-Helpdesk. Those preferring the Linux command line can use `openvpn` with this [configuration](https://cubbli.cs.helsinki.fi/hy-vpn-tun.ovpn), see the [instructions](https://wiki.helsinki.fi/display/it4sci/Remote+access+to+University+resources).
