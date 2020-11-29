# coding: UTF-8
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    #存在しなかった場合
    else:
        print("{}は見つかりませんでした。".format(word))

        #登場人物にいなかった場合登録
        registerconfirm = input("{}を登場人物として登録しますか? y/n >>> ".format(word))
        if registerconfirm=="y":
            source.append(word)
            print("{}を登場人物として登録しました".format(word))
            for w in source:
                print(w)


if __name__ == "__main__":
    search()
