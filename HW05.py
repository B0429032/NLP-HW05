import csv    # Python standard library中的csv模組。

# 讀取csv檔內容，放到csvDataToRead變數中。
csvFileToRead = open('C:\Users\Kunying\Desktop\冠勳資料\109-2課程\線上校外實習\HW03\HW03A.csv', 'r', encoding='utf-8-sig')
csvDataToRead = csv.reader(csvFileToRead)

# 將csvDataToRead(原csv檔內容)轉為list。
dataList = list(csvDataToRead)
# 注意：必須在轉完list之後才關檔，否則會產生'ValueError: I/O operation on closed file.'
# 　　　的exception。
csvFileToRead.close()
for row_number in range(1, 11400):
    if dataList[row_number][1] = '動作'
        type01=type01+1
    if dataList[row_number][1] = '冒險'
        type02=type02+1
    if dataList[row_number][1] = '科幻'
        type03=type03+1
    if dataList[row_number][1] = '奇幻'
        type04=type04+1
    if dataList[row_number][1] = '劇情'
        type05=type05+1
    if dataList[row_number][1] = '犯罪'
        type06=type06+1
    if dataList[row_number][1] = '恐怖'
        type07=type07+1
    if dataList[row_number][1] = '懸疑/驚悚'
        type08=type08+1
    if dataList[row_number][1] = '喜劇'
        type09=type09+1
    if dataList[row_number][1] = '愛情'
        type10=type10+1
    if dataList[row_number][1] = '溫馨/家庭'
        type11=type11+1
    if dataList[row_number][1] = '動畫'
        type12=type12+1
    if dataList[row_number][1] = '戰爭'
        type13=type13+1
    if dataList[row_number][1] = '音樂/歌舞'
        type14=type14+1
    if dataList[row_number][1] = '歷史/傳記'
        type15=type15+1
    if dataList[row_number][1] = '紀錄片'
        type16=type16+1
    if dataList[row_number][1] = '勵志'
        type17=type17+1
    if dataList[row_number][1] = '武俠'
        type18=type18+1
    if dataList[row_number][1] = '影展'
        type19=type19+1
    if dataList[row_number][1] = '戲劇'
        type20=type20+1
    if dataList[row_number][1] = '影集'
        type21=type21+1
