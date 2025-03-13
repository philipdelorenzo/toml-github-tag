import os
import toml

def get_toml_version():
    """
    Reads the version from pyproject.toml.
    """
    pyproject_path = os.path.join(os.path.dirname(__file__), '..', 'pyproject.toml')
    with open(pyproject_path, 'r') as f:
        pyproject_data = toml.load(f)
    return pyproject_data['tool']['poetry']['version']
