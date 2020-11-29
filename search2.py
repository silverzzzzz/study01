# coding: UTF-8
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    ### ここに検索ロジックを書く
    flag = word in source
    if flag == 1:
        print("{}が見つかりました".format(word))
    #存在しなかった場合
    else:
        print("{}は見つかりませんでした".format(word))

if __name__ == "__main__":
    search()
