#用來寫ffmpeg合併檔的filelist
''''
建完filelist後的指令：
ffmpeg -f concat -safe 0 -i filelist.txt -c copy merge.mp4
/* 
1. filelist.txt 當中須以以下格式紀錄要合併的檔案（按順序)
file和檔名之間有空格

file '00M38S_1592452838.mp4'
file '01M38S_1592452898.mp4'

2.merge.mp4 是輸出檔名
*/
''''
for ah in range(1,55):
    s="file \'h{ah}.mp4\'".format(ah=ah)
    print(s)   