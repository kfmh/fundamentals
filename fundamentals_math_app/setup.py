from setuptools import setup, find_packages

setup(
    name="fundamentals_math_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "start_math = fundamentals_math_app.main:main",
        ],
    },
)
