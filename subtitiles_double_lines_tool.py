import pysrt
import pysubs2


ori_file = "d:\youtuber\dongjiang\ep27_白鹭岛到古竹\[English] Why This Fusion Tech May Be a Geothermal Energy Breakthrough [DownSub.com].srt"
new_file = "d:\youtuber\dongjiang\ep27_白鹭岛到古竹\ep28.1_en.srt"

# subs = pysrt.open(ori_file)
subs = pysubs2.load(ori_file, encoding="utf-8")

i = 0
for item in subs:
    # if len(item.text) == 0:
    #     print(item.index)
    item.text = item.text.replace("\\N","")
    # print(item.text)
    # i += 1
    # if i > 5:
    #     break
    # item.text = item.text.replace("\n","")

subs.save(new_file, encoding="utf-8")