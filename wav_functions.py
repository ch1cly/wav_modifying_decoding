from scipy.io import wavfile
import numpy as np
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import subprocess
import json
import os
import argparse


file_name = 'wav_sounds/eng.wav'
file_name_rus = 'wav_sounds/russian.wav'

model_path_rus = 'vosk-model-small-ru-0.22'
model_path_eng = 'vosk-model-small-en-us-0.15'


def modify_wav(file: str = file_name_rus, volume_shift: float = 1, speed_shift: float = 1):
    samplerate, data = wavfile.read(file)
    new_dtype = np.int16
    wavfile.write("result.wav", int(samplerate * speed_shift), \
                  np.clip(data.astype(np.int64) * volume_shift, np.iinfo(new_dtype).min,
                          np.iinfo(new_dtype).max).astype(new_dtype)
                  )
    print('modifying done!')


def check_model(model_path):
    if not os.path.exists(model_path):
        print(
            "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit(1)


def speech2text(file: str = file_name_rus, language: str = 'rus'):
    SetLogLevel(0)
    model_path = model_path_rus
    # Проверяем наличие модели
    if language == 'rus':
        check_model(model_path)
    elif language == 'eng':
        model_path = model_path_eng
        check_model(model_path_rus)
    else:
        print("unknown language")
        exit(2)

    FRAME_RATE = 44100
    CHANNELS = 1

    # Используем модель
    model = Model(model_path)
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    # Редактируем файл
    wav = AudioSegment.from_wav(file)
    wav = wav.set_channels(CHANNELS)
    wav = wav.set_frame_rate(FRAME_RATE)

    # Используем модель
    rec.AcceptWaveform(wav.raw_data)
    result = rec.Result()
    text = json.loads(result)["text"]

    # Сохраняем
    result_text = {
        "recognized text": text
    }
    with open('data.json', 'w+') as f:
        json.dump(result_text, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='simple wav modifier program')
    parser.add_argument('func_name', type=str, help='function name "modify_wav" or "speech2text"')

    parser.add_argument('--file_name', type=str, default=file_name, help='file path')
    parser.add_argument('--language', type=str,  default='eng', help='language "eng" or "rus" if speech2text')
    parser.add_argument('--volume_shift', type=float,  default='1.0', help='volume_shift if modify_wav')
    parser.add_argument('--speed_shift', type=float,  default='1.0', help='speed_shift if modify_wav')

    args = parser.parse_args()
    if args.func_name == 'speech2text':
        speech2text(file=args.file_name,language=args.language)
    elif args.func_name == 'modify_wav':
        modify_wav(file=args.file_name,volume_shift=args.volume_shift, speed_shift=args.speed_shift)
    else:
        print('input error')

