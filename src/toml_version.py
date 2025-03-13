import os
import pytoml

def get_toml_version():
    """
    Reads the version from pyproject.toml.
    """
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to pyproject.toml
    pyproject_path = os.path.join(os.getcwd(), 'pyproject.toml')
    with open(pyproject_path, 'r') as f:
        pyproject_data = pytoml.load(f)

    return pyproject_data['project']['version']

if __name__ == "__main__":
    print(get_toml_version())
