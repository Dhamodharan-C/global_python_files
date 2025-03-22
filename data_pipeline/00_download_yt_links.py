from __future__ import unicode_literals
import youtube_dl
import glob;
import os;
import shutil;

in_file = '/home/damu/ISRL/English_MS/english_ms_tts_yt_links.txt';
out_dir = '/home/damu/ISRL/English_MS/downloaded_files/';
conv_dir = '/home/damu/ISRL/English_MS/converted_files/';

# in_file = '/bkpdisk/webapp_backup/hindi_annotation/source_files/rahul_ganydhi_links.txt';
# out_dir = '/bkpdisk/webapp_backup/hindi_annotation/source_files/downloaded_files/';
# conv_dir = '/bkpdisk/webapp_backup/hindi_annotation/source_files/converted_files/';

# if (os.path.exists(out_dir)):
#     shutil.rmtree(out_dir);
# os.makedirs(out_dir);

# if (os.path.exists(conv_dir)):
#     shutil.rmtree(conv_dir);
# os.makedirs(conv_dir);

for line in open(in_file):
    line_conts = line.strip().split();
    out_file_name = out_dir + line_conts[0] + '.mp3';
    conv_file_name = conv_dir + line_conts[0] + '.wav';
    video_url = line_conts[1];
    download_command = "yt-dlp -f 'ba' -x --audio-format mp3 " + video_url + " -o '" + out_file_name + "'";
    conversion_command = 'ffmpeg -i ' + out_file_name + ' -acodec pcm_s16le -ac 1 -ar 48000 ' + conv_file_name;
    print (download_command);
    print ('');
    try:
        os.system(download_command);
        os.system(conversion_command);
    except:
        print ('skipping');

