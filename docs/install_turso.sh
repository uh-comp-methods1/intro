# Install and init conda
cd $PROJ
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $PROJ/miniconda
source miniconda/etc/profile.d/conda.sh
# Install the Python environment
curl -O https://raw.githubusercontent.com/uh-comp-methods1/intro/main/docs/env_jupyterhub.yml
conda env create -f env_jupyterhub.yml
conda activate comp-methods
python -m ipykernel install --user --name comp-methods --display-name "Python 3.9 (comp-methods)"