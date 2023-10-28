#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import glob
import re
from moviepy.editor import *

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

if __name__ == '__main__':

    file_list = glob.glob(r'*.png')
    file_list.sort(key=natural_keys)

    time = 0.333
    fade = 0.167

    file_fx_list = []
    video = ImageClip(file_list[0]).set_duration(time)
    file_fx_list.append(video.set_start(time - fade).crossfadein(fade))        

    for idx, image in enumerate(file_list[1:]):
        idx += 2
        video = ImageClip(image).set_duration(time)
        file_fx_list.append(video.set_start(time*idx - fade*idx).crossfadein(fade))        

    concat_clip = CompositeVideoClip(file_fx_list)
    # concat_clip.write_videofile(r"outputpy1.mp4",
    concat_clip.write_videofile("outputpy_time" + str(time) + "_fade" + str(fade) + ".mp4",
                                threads=16,
                                fps=24,
                                write_logfile=False,
                                )

    # print(file_list)
    # print(len(file_list))
    # print(file_list[0])

    # time = '00:00:01.00'
    # fade = '00:00:00.50'

# https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
# https://stackoverflow.com/questions/72285020/how-to-add-transitions-between-clips-in-moviepy
# https://qiita.com/showchan33/items/968a07c078bf0a7f9e46
# https://nonbiri3.com/?p=6393