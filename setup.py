from setuptools import setup, find_packages

setup(
    name='pican_flasher',
    version='0.0.2',
    install_requires=["click"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        "console_scripts": ["pican_flasher = pican_flasher.__main__:cli"]
    },

)
