### Speech to text recognition

Based VOSK vosk [models](https://alphacephei.com/vosk/models)

Sound from [freesound](https://freesound.org/people/balloonhead/sounds/362501/) and [youtube](https://www.youtube.com/watch?v=VI1bR9fj6cs)


make sure you have *make*, [*python*](runtime.txt) and *uzip*
or you can try on linux

```cmd
sudo apt-get update && sudo apt upgrade -y
sudo apt-get install unzip
sudo apt-get install make
sudo apt-get install python3.10
```

#### To download models
```cmd
make download
```

#### Examples of usage
```cmd
python wav_functions.py modify_wav --file_name=wav_sounds/russian.wav --volume_shift=10 --speed_shift=2
```
```cmd
 python wav_functions.py speech2text  --file_name=wav_sounds/russian.wav --language=rus
```


#### Options
```cmd
python wav_functions.py <modify_wav/speech2text> [OPTIONS]
```
Options list
```cmd
--file_name=(str)
--language=(rus/eng)
--volume_shift=(float)
--speed_shift=(float)
```

### How to setup environment 
#### Lunux:
    python3 -m venv env
    source env/bin/activate
    python3 -m pip install -r requirements.txt
#### Windows:
    python -m venv env
    .\env\Scripts\activate.bat
    python -m pip install -r requirements.txt
#### For deactivate the Python venv:
    deactivate
#### Update requirements
    pip freeze > requirements.txt
