# coding: UTF-8
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
source = []
#CSVからキャラクターリストを読み込む
with open("./charactors.csv") as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for line in reader:
        for word in line:
            source.append(word)
            
### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    #存在しなかった場合
    else:
        print("{}は見つかりませんでした。".format(word))

        #登場人物にいなかった場合登録,CSVに書き込み
        registerconfirm = input("{}を登場人物として登録しますか? y/n >>> ".format(word))
        if registerconfirm=="y":
            with open("./charactors.csv", mode="a") as f:
                writercsv = csv.writer(f, lineterminator=',')
                writercsv.writerow([word])
            


if __name__ == "__main__":
    search()
