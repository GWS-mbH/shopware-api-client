# fix permissions
sudo chown -R vscode:vscode /home/vscode/
sudo chmod -R a+rw /workspaces/.data

# Add bash-completion's
echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc

# install deps
pip config set global.cache-dir /workspaces/.cache/pip
pip install -r /workspaces/.devcontainer/requirements.txt

pre-commit install
