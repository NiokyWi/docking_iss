# Docking on the ISS
This game has been designed by Nicolas Deschaux for the Délire d'Encre organisation.

## Description

https://www.youtube.com/watch?v=lM7SeFqJ8M4

## Usage

### Setup
You first need to install required libraries. To do so, we advice using `pipenv` as follow:
```bash
pip install -r requirements.txt
```

### Run
Simply run the program using the following command:
```bash
python3 main.py
```

### Re-initialisation

## Development
Several variable are available from the `main.py` file. There you can change:
* `FULLSCREEN`: by default `True` means it will display on the whole screen size
* `DEBUG_MODE`: display debug data and target. By default `False`
* `SCALE_SPEED`: set the ATV approach speed. Nothing physical but by default `0.001`
* `INIT_DELTA_TIME`: set the delay (in seconds) the initialisation take. By default 10s.

