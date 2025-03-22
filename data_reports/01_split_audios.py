import glob;
import shutil;
import os;
import scipy.io.wavfile;

# in_dir = './converted_files/';
# out_dir = './split_files/';
in_dir = "/home/damu/ISRL/English_MS/split_files/"
out_dir = "/home/damu/ISRL/English_MS/nagaraja_prakasam_english/wavs/"
split_dur_minutes = 30;

# if (os.path.exists(out_dir)):
#     shutil.rmtree(out_dir);
# os.makedirs(out_dir);

in_file_list = glob.glob(in_dir + '*.wav');

for in_file_name in in_file_list:
    file_conts = in_file_name.split('/');
    file_id = file_conts[-1].replace('.wav', '');
    print ('Processing : ' + in_file_name);
    print ('');
    in_fs, in_wav = scipy.io.wavfile.read(in_file_name);
    split_id = 0;
    start_sample = 0;
    end_sample = 0;
    process_flag = True;
    while (process_flag):
        split_id = split_id + 1;
        out_file_name = out_dir + file_id + '_split_' + str(split_id).zfill(4) + '.wav';
        start_sample = end_sample;
        end_sample = start_sample + (split_dur_minutes * 60 * in_fs);
        if (end_sample > len(in_wav)):
            end_sample = len(in_wav) - 1;
            process_flag = False;
        out_wav = in_wav[start_sample:end_sample];
        scipy.io.wavfile.write(out_file_name, in_fs, out_wav);

