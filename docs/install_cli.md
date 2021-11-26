# Installation using Linux command line

Install the Conda environment manager:
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

Once you have Conda, download the file [environment.yml](https://raw.githubusercontent.com/uh-comp-methods1/intro/main/docs/environment.yml) and install the environment it specifies by
```
conda env create -f environment.yml
```
Now we can test that JupyterLab works by running
```
conda activate comp-methods
jupyter-lab
```

## How to create an environment file

This is just for the curious, and describes how `environment.yml` was created.

1. Create an environment called **comp-methods**
```
conda create -n comp-methods
```
2. Activate the **comp-methods** environment
```
conda activate comp-methods
```
3. Install some of the tools that we need (have a look at the `environment.yml` for the rest)
```
conda config --env --add channels conda-forge
conda install numpy
conda install matplotlib
```

The simplest way to create an environment file is
```
conda env export --from-history > environment.yml
```
However, explicit versions of installed packages are not listed in the resulting environment file, and whence the environment imported from this file will change over time. To avoid this, we need to tease out the versions of the packages. There seems to be no easy way to do this, but for example the following shell script will do the job (this is in [fish](https://fishshell.com/))
```fish
function conda-share-env --description \
'Create environment.yml file with explicit versions' 

    conda env export --from-history | sed -n '1,/dependencies/p'
    set packages (conda env export --from-history \
        | sed -n '/dependencies/,/prefix/p' \
        | sed -n 's/  - \(.*\)/\1/p')
    for package in $packages
        set ver (conda list $package \
            | sed -n '/^'$package'[[:space:]]/p' \
            | awk '{print $2}')
        echo "  - $package=$ver"
    end
end
```
Note that importing `environment.yml` will not add the conda-forge channel in the environment.
