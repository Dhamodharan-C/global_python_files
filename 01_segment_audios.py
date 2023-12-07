import glob;
import os;
import shutil;
import scipy.io.wavfile;
import math;


wav_files = '/home/damu/ISRL/English_MS/split_files/'
in_srt_dir = '/home/damu/ISRL/English_MS/srt_files/'
out_audio_dir = '/home/damu/ISRL/English_MS/nagaraja_prakasam_english/audio_files/'
out_text_dir = '/home/damu/ISRL/English_MS/nagaraja_prakasam_english/trans_files/'
# out_batch_audio_dir = 'E:/IndiaSpeaks Research Labs/TTS/SS Fine tuning batch wise segmented files/'
# af = os.listdir(in_audio_dir)
# for file in os.listdir(in_audio_dir):
#     print(file)
#     in_file = in_audio_dir + file
#     file_name = file.replace('.mp3', '.wav')
#     conv_file_name = wav_files + file_name
#     conversion_command = 'ffmpeg -i ' + in_file + ' -acodec pcm_s16le -ac 1 -ar 48000 ' + conv_file_name;
#     os.system(conversion_command);


def get_seconds_from_timestamp(in_string):
    in_string_conts = in_string.split(',');
    in_string_conts_conts = in_string_conts[0].split(':');
    hour_val = int(in_string_conts_conts[0]);
    min_val = int(in_string_conts_conts[1]);
    sec_val = int(in_string_conts_conts[2]);
    msec_val = int(in_string_conts[1]);
    ret_secs = ((((hour_val * 60) + min_val) * 60) + sec_val) + (msec_val / 1000);
    return ret_secs;

if (os.path.exists(out_audio_dir)):
    shutil.rmtree(out_audio_dir);
os.makedirs(out_audio_dir);

if (os.path.exists(out_audio_dir)):
    shutil.rmtree(out_audio_dir);
os.makedirs(out_audio_dir);

srt_file_list = glob.glob(in_srt_dir + '*.srt');
srt_file_list.sort();
print(srt_file_list)
errorCount = 0
file_idx = 0;
for srt_file_name in srt_file_list:
    file_conts = srt_file_name.replace('\\','/').split('/');
    file_id = file_conts[-1].replace('.srt', '');
    print(file_id);
    # folder_id = out_batch_audio_dir + str(file_id[3:7]) + '/'
    # if (not os.path.exists(folder_id)):
    #     os.makedirs(folder_id);
    wav_file_name = wav_files + file_id + '.wav';
    if (not os.path.exists(wav_file_name)):
        print ('Error : ' + wav_file_name);
        errorCount += 1
        continue;
    in_fs, in_wav = scipy.io.wavfile.read(wav_file_name);
    srt_lines = list();
    line_number = 0
    txt_id = 0
    srt_contents = open(srt_file_name, 'r', encoding='utf8').readlines()
    for line in srt_contents:
        line = line.strip();
        if ('-->' in line):
            out_txt_file_name = out_text_dir + file_id + '_' + str(txt_id + 1).zfill(4) + '.txt';
            with open(out_txt_file_name, 'w', encoding='utf8') as txt_file:
                txt_file.writelines(srt_contents[line_number + 1].replace('\n', ''))
            txt_id += 1
            srt_conts = line.split('-->');
            start_string = srt_conts[0];
            end_string = srt_conts[1];
            start_sec = get_seconds_from_timestamp(start_string);
            end_sec = get_seconds_from_timestamp(end_string);
            srt_lines.append([start_sec, end_sec]);
        line_number += 1
    for segment_id in range(len(srt_lines)):
        out_wav_file_name = out_audio_dir + file_id + '_' + str(segment_id + 1).zfill(4) + '.wav';
        # out_batch_wav_file_name = folder_id + file_id + '_' + str(segment_id + 1).zfill(4) + '.wav';
        start_sample_val = int(math.ceil(srt_lines[segment_id][0] * in_fs));
        end_sample_val = int(math.floor(srt_lines[segment_id][1] * in_fs));
        out_wav = in_wav[start_sample_val:end_sample_val];
        scipy.io.wavfile.write(out_wav_file_name, in_fs, out_wav);
        # scipy.io.wavfile.write(out_batch_wav_file_name, in_fs, out_wav);
    file_idx = file_idx + 1;
    print (str(file_idx) + ' : ' + srt_file_name);
print(errorCount)
