# Docking on the ISS
This game has been designed by Nicolas Deschaux for the Délire d'Encre organisation.

## Description

https://www.youtube.com/watch?v=lM7SeFqJ8M4

## Usage

### Run the game
Simply run the program using the following command:
```bash
python3.6 docking_iss/main.py
```

### Re-initialisation


## Development

### Setup the RaspberryPi
The game is supposed to be ran on a RaspberryPi. Following needs to be done the first time only. On Raspbian lite, following command might be run:

1- Requirements setup:
```bash
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev
```

2- Python3.6 setup:
```bash
sudo apt-get install python3-pip python3-dev
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz  
tar xvf Python-3.6.0.tgz
cd Python-3.6.0
./configure --enable-optimizations --with-ensurepip=install
make -j4  
sudo make altinstall
```

3- Next will clone the game repository locally:
```bash
sudo apt-get install git
git clone https://github.com/NiokyWi/docking_iss.git
```

### Setup the game
You first need to install required libraries. To do so, we advice using `pipenv` as follow:
```bash
pip3 install -r requirements.txt
```

### Customize the game
Several variable are available from the `main.py` file. There you can change:
* `FULLSCREEN`: by default `True` means it will display on the whole screen size
* `DEBUG_MODE`: display debug data and target. By default `False`
* `SCALE_SPEED`: set the ATV approach speed. Nothing physical but by default `0.001`
* `INIT_DELTA_TIME`: set the delay (in seconds) the initialisation take. By default 10s.

