docker build -t pyinstaller_build:latest . && \
docker run --name pyinstaller_build -v $(pwd)/src:/usr/app/src pyinstaller_build second.py
