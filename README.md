# Introduction

The Jupyter notebook `python_intro.ipynb` gives an introduction to Python. The notebook can be run either in the [mybinder.org](https://mybinder.readthedocs.io/en/latest/about/about.html) cloud environment or locally on your computer. The cloud is easy to use but can be slow to start up and has limited computational resources. To run in the cloud, simply click the following button 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uh-comp-methods1/intro/main?labpath=python_intro.ipynb)

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

Now you can download the notebook as follows:

* Click the green Code button above
* Click the button at the end of the url to copy the url
* Click the Git button on the left panel in JupyterLab
* Click Clone a Repository
* Paste the copied url and click clone

This creates a new folder called `intro`
containing a Jupyter notebook called `python_intro.ipynb`.
Open the notebook for an introduction to Python.