import pysrt

en_file = "d:\youtuber\dongjiang\ep27_白鹭岛到古竹\ep28.1_en.srt"
zh_file = "d:\youtuber\dongjiang\ep27_白鹭岛到古竹\ep28.1_zh-Hans-en.srt"
new_file = "d:\youtuber\dongjiang\ep27_白鹭岛到古竹\ep28.1_en_zh.srt"

subs_en = pysrt.open(en_file)
subs_zh = pysrt.open(zh_file)

for i in range(len(subs_en)):
    subs_en[i].text = subs_en[i].text + "\n" + subs_zh[i].text

subs_en.save(new_file)






