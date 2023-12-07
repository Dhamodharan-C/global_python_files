from scipy.io import wavfile
import argparse
import os
from pydub.silence import detect_nonsilent
from pydub import AudioSegment
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Create sil_wavs/ with silence trimmed wavs")
parser.add_argument("-p","--path", help="Path")

args = parser.parse_args()
src_path = args.path

def remove_sil(path_in, path_out, format="wav"):
    sound = AudioSegment.from_file(path_in, format=format)
    non_sil_times = detect_nonsilent(sound, min_silence_len=50, silence_thresh=sound.dBFS * 1.5)
    if len(non_sil_times) > 0:
        non_sil_times_concat = [non_sil_times[0]]
        if len(non_sil_times) > 1:
            for t in non_sil_times[1:]:
                if t[0] - non_sil_times_concat[-1][-1] < 200:
                    non_sil_times_concat[-1][-1] = t[1]
                else:
                    non_sil_times_concat.append(t)
        non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 350]
        sound[non_sil_times[0][0]: non_sil_times[-1][1]].export(path_out, format='wav')

def findwavfiles(dir):
    files = []
    for dirpath, _, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith(".wav"):
                files.append(os.path.join(dirpath, filename))
    return files

fl = findwavfiles(src_path+'/wavs')
tt = 0
err = []

sil_path = src_path+'/silrem_wavs/'
os.system('rm -rf '+sil_path+' && mkdir '+sil_path)

for i in tqdm(range(0,len(fl))):
    try:
        j = sil_path +fl[i].strip().split('/')[-1]
        remove_sil(path_in=fl[i],path_out=j)
        #print(i,fl[i])
    except Exception as e:
        print(e)
        err.append(fl[i])

print('Error occured while trimming in ')
print(err)
