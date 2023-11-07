# Introduction

The Jupyter notebook `python_intro.ipynb` gives an introduction to Python. The notebook can be run either locally on your computer or in the [mybinder.org](https://mybinder.readthedocs.io/en/latest/about/about.html) cloud environment. The cloud is easy to use but can be slow to start up and has limited computational resources. To run in the cloud, simply click the following button 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uh-comp-methods1/intro/main?labpath=python_intro.ipynb)

For anything more than the bare minimum the local installation is recommended.

## Local installation

(Those preferring the Linux command line can follow these [alternative instructions](docs/install_cli.md).)

You need to first install [Anaconda](https://www.anaconda.com/products/individual). Once you have Anaconda installed, do the following: 

* Download the [environment file](https://raw.githubusercontent.com/uh-comp-methods1/intro/main/docs/environment.yml)
* Open Anaconda Navigator
* Click Environments on the left panel
* Click Import
* Choose the file `environment.yml` that you downloaded 
* Set New environment name to **comp-methods** (or whatever you want, but choose the same name below)
* Click Import

The last step takes a while so wait patiently. Once the environment is istalled, start JupyterLab in Anaconda Navigator:

* Click Home on the left panel
* Select **comp-methods** in the Applications dropdown menu
* Click the Launch button of JupyterLab 

Now you can download the notebook in JupyterLab as follows:

* Navigate to a folder where you want to store the notebook using the File Browser on the left panel
* Click the Git button on the left panel
* Click Clone a Repository
* Enter the url of this repository, that is, <https://github.com/uh-comp-methods1/intro> and click Clone

This creates a new folder called `intro`
containing a Jupyter notebook called `python_intro.ipynb`.
Open the notebook for an introduction to Python.

## About Jupyter Notebooks

The notebooks use `.ipynb` extension which stands for *Interactive Python Notebook*. It is developed by [Project Jupyter](https://jupyter.org/) and has its roots in the [iPython](https://ipython.org/)-package (for Interactive Python). The notebooks themselves are actually JSON files which contain blocks of code, visuals from plots, markdown, metadata etc. and nowadays support programming languages other than Python as well.

To edit and run the notebooks the web-based Jupyter Notebook and the more recent JupyterLab interface are used but these are not the only option. It is possible to run the notebooks with an IDE (Integrated Development Environment) such as [Visual Studio Code](https://code.visualstudio.com).

### Running Jupyter Notebooks in VS Code

There are simple instructions for running Jupyter Notebooks available on [the VS Code website](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

You'll need to install the Python and Jupyter extensions for VS Code and have the Python environment set up. Then simply launch VS Code, open a notebook and select the right kernel (Python and right environment) from top right corner.

Using an IDE instead of the web browser allows for more customization, better keyboard shortcuts and makes it harder to accidentally kill the Jupyter server when you meant to just close a web page.