from setuptools import setup, find_packages

setup(
    name="Game of Life",
    version=1.0,
    author="ziebam",
    author_email="ziebamichal@tutanota.com",
    license="MIT",
    description="Conway's Game of Life in the command-line",
    url="https://github.com/ziebam/game_of_life",
    packages=find_packages(),
    install_requires=["pygame"],
    python_requires=">=3.5",
)
