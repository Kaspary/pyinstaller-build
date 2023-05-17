[commit-shield]: https://img.shields.io/github/last-commit/Kaspary/pyinstaller-build?style=for-the-badge&logo=GitHub
[commit-url]: https://github.com/Kaspary/pyinstaller-build/commits/main
[linkedin-shield]: https://img.shields.io/badge/-João%20Pedro%20Kaspary-6633cc?style=for-the-badge&logo=Linkedin&colorB=2366c2
[linkedin-url]: https://linkedin.com/in/joao-pedro-kaspary
[github-shield]: https://img.shields.io/github/followers/Kaspary?label=João%20Pedro%20Kaspary&style=for-the-badge&logo=GitHub
[github-url]: https://github.com/Kaspary

[![commit-shield]][commit-url]
[![linkedin-shield]][linkedin-url]
[![GitHub followers][github-shield]][github-url]

# Docker Image for Building Python Scripts with PyInstaller

This Docker image provides an easy and reliable way to build Python scripts for both Linux and Windows platforms using PyInstaller. With this image, you can quickly build standalone executable files (.exe for Windows and ELF binary for Linux) from your Python scripts without worrying about platform-specific dependencies.

## Prerequisites

To use this Docker image, you need to have Docker installed on your system. You can download and install Docker from the [official website](https://www.docker.com/get-started).

## Usage

To use this Docker image, you need to mount the directory containing your Python script(s) to the `/src` directory in the Docker container, and then run the `pyinstaller` command with appropriate options.

Here's an example command to build an executable file for a Python script named `my_script.py` located in the current directory:

```bash
docker run -v $(pwd)/src:/usr/app/src kaspary/pyinstaller_build my_script.py
```
This command will mount the current directory to `/src` in the Docker container, and then run the `pyinstaller` command with the `my_script.py` file as input. \
After running the container, you can find the executable file in the `/src/build/dist/` directory. This file can be distributed and run on the appropriate platform without any further dependencies.

## Building the Docker Image
If you want to build the Docker image yourself, you can clone this repository and run the following command in the cloned directory:

```bash
docker build -t pyinstaller_build:latest .
```

This command will build the Docker image with the name `pyinstaller_build`. You can replace `pyinstaller_build` with any name you prefer.

## References
- https://hub.docker.com/r/kaspary/pyinstaller_build
- https://github.com/cdrx/docker-pyinstaller
- https://github.com/webcomics/pywine
