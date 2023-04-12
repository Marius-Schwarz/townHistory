import os
import subprocess as sub

def ffmpeg_command(ifile, ofile):
  return ['ffmpeg', '-i', ifile, '-g', '10', ofile]

def filetype_list(suffix, directory='./'):
  return [f for f in os.listdir(directory) if f.endswith(suffix)]

def replace_suffix(filename, replacement='.webm'):
  return filename.split('.')[0] + replacement

sub.call('pwd')

for f in filetype_list('.mp4'):
  print(ffmpeg_command(f, replace_suffix(f)))
  sub.call(ffmpeg_command(f, replace_suffix(f)))


