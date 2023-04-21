ARG PYWINE_VERSION=3.10
FROM tobix/pywine:${PYWINE_VERSION}

WORKDIR /usr/app

RUN apt-get update

ARG PYTHON_VERSION=3.10.8

RUN apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev \
    libnss3-dev libssl-dev libreadline-dev libffi-dev wget python3-dev \
    python3-pip -y
    
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
RUN tar -xf Python-${PYTHON_VERSION}.tgz
RUN ./Python-${PYTHON_VERSION}/configure --enable-optimizations --enable-shared
RUN make altinstall
RUN make install
RUN cp /usr/local/lib/libpython* /usr/lib/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pyinstaller

# Windows
RUN wine python.exe -m pip install --upgrade pip
RUN wine python.exe -m pip install pyinstaller

COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY build.py ./
RUN chmod +x build.py

ENTRYPOINT ["./entrypoint.sh"]