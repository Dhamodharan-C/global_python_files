import glob;
import os;
import shutil;
import scipy.io.wavfile;
import math;


# wav_files = '/home/damu/ISRL/Hindi_MS/rahul_gandhi/converted_files/'
wav_files = '/media/damu/Office/India_Speaks/Voice_Cloning/Nagaraja_Prakasam/'
out_audio_dir = '/home/damu/ISRL/English_MS/wav_files/'

file_list = open('/home/damu/ISRL/English_MS/files.txt', 'r').readlines()
# file_list = ['ng_8']

print(file_list)
errorCount = 0
file_idx = 0;
for file_name in file_list:
    file_conts = file_name.split('\t');
    file_id = file_conts[0]
    wav_file_name = wav_files + file_id + '.wav';
    if (not os.path.exists(wav_file_name)):
        print ('Error : ' + wav_file_name);
        errorCount += 1
        continue;
    in_fs, in_wav = scipy.io.wavfile.read(wav_file_name);
    start_sec = int(file_conts[1].replace('\n', ''))
    end_sec = int(file_conts[2].replace('\n', ''))
    out_wav_file_name = out_audio_dir + file_id + '.wav';
    start_sample_val = int(math.ceil(start_sec * in_fs));
    end_sample_val = int(math.floor(end_sec * in_fs));
    out_wav = in_wav[start_sample_val:end_sample_val];
    scipy.io.wavfile.write(out_wav_file_name, in_fs, out_wav);
    file_idx = file_idx + 1;
    print (str(file_idx) + ' : ' + file_name);
print(errorCount)


# file = '/home/damu/ISRL/Hindi_MS/rahul_gandhi/converted_files/hi_0001_rahulgandhi_0012.wav'
# out = '/home/damu/ISRL/Hindi_MS/rahul_gandhi/check.wav'
# st = 1165
# ed = 1195
# in_fs, in_wav = scipy.io.wavfile.read(file)
# start_sample_val = int(math.ceil(st * in_fs))
# end_sample_val = int(math.floor(ed * in_fs))
# out_wav = in_wav[start_sample_val:end_sample_val]
# scipy.io.wavfile.write(out, in_fs, out_wav)