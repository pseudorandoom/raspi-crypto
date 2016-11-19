Python Crypto
=====
To build the docker image use `docker build -t pycrypto .`

The following comand mounts the current directory on /home/app and executes the script on the mounted directory (/home/app/) plus the relative path of the script (crypto/testEncriptacion.py)

`docker run --rm -w /home/app -v "$PWD":/home/app pycrypto crypto/rsacrypto.py`
