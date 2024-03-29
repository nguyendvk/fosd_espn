#!/usr/bin/env python3

import sys
import os


raw_extract_path = sys.argv[1] 
dest = sys.argv[2]
os.makedirs(dest, exist_ok=True)
file_prefix = os.path.join(raw_extract_path, "mp3")

# read raw_extract_path
transcript_path = os.path.join(raw_extract_path, "transcriptAll.txt")
transcripts = open(transcript_path, "r").read().split("\n")
list_utt = []

spk2utt_fh = open(os.path.join(dest, "spk2utt"), "w")
text_fh = open(os.path.join(dest, "text"), "w")
utt2spk_fh = open(os.path.join(dest, "utt2spk"), "w")
wavscp_fh = open(os.path.join(dest, "wav.scp"), "w")

for t in transcripts:
  cols = t.split("|")
  filename = cols[0]
  text = cols[1]
  duration = cols[2]

  utt_id = filename[filename.rfind("_", 0,filename.rfind("_")) - 1] + filename[filename.rfind("_") + 1:filename.rfind(".mp3")]
  # list_utt.append((utt_id, text, os.path.join(file_prefix, filename)))

  spk2utt_fh.write(utt_id + " " + utt_id + "\n")
  text_fh.write(utt_id + " " + text + "\n")
  utt2spk_fh.write(utt_id + " " + utt_id + "\n")
  wavscp_fh.write(utt_id + " " + os.path.join(file_prefix, filename) + "\n")

spk2utt_fh.close()
text_fh.close()
utt2spk_fh.close()
wavscp_fh.close()

