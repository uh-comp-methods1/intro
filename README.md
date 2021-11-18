# Introduction

The Jupyter notebook `python_intro.ipynb` gives an interactive introduction Python. The interactive examples can be run either in a cloud environment or locally on your computer. The former option requires no installation but, in particular in the case of mybinder.org, can be slow to start up and has limited computational resources. The latter option requires some setting up but is more convenient in the long run.

## Running at mybinder.org

Simply click the following button 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uh-comp-methods1/intro/main?labpath=python_intro.ipynb)

## Running at hub.cs.helsinki.fi

This option is available only for the participants of the computational methods course at UH. If you are not in the UH network, you need to establish first a VPN connection, see the [instructions](https://helpdesk.it.helsinki.fi/en/help/5190) on VPN connections. Those preferring the Linux command line can use `openvpn` with the [configuration](https://cubbli.cs.helsinki.fi/hy-vpn-tun.ovpn), see the [instructions](https://wiki.helsinki.fi/display/it4sci/Remote+access+to+University+resources).

If you haven't previously logged into `turso.cs.helsinki.fi`, you need to do so to create your home directory. To do this, open a terminal and run 

```
ssh your_username@turso.cs.helsinki.fi
```

No further logins to turso are required if you only wish to use the hub. 

Now 

* Go to the [hub](https://hub.cs.helsinki.fi) and log in
* Choose the Vorna profile with the least computational resources 
  - Do _not_ choose a classic notebook profile
* Go to the `home` directory using the File Browser in JupyterLab
* Click Bash under **Console**
* Run the following command by copy-pasting it into the console and pressing shift+enter
```
git clone https://github.com/uh-comp-methods1/intro.git
```
* Close the console

This creates a new folder called `intro`
containing a Jupyter notebook called `python_intro.ipynb`.
Open the notebook for an introduction to Python.


## Running locally

Install the programming environment by following these [instructions](https://github.com/uh-comp-methods1/install). Then

* Click the green Code button above
* Click the button at the end of the url to copy the url
* Click the Git button on the left panel in JupyterLab
* Click Clone a Repository
* Paste the copied url and click clone

This creates a new folder called `intro`
containing a Jupyter notebook called `python_intro.ipynb`.
Open the notebook for an introduction to Python.
