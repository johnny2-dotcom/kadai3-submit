import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(key_word,csv):
    # 検索対象取得
    df=pd.read_csv("./{}".format)
    source=list(df["name"])

    # 検索
    if key_word in source:
        print("『{}』はあります".format(key_word))
        eel.result_disp("『{}』はあります".format(key_word))
    else:
        print("『{}』はありません".format(key_word))
        eel.result_disp("『{}』はありません".format(key_word))
        eel.result_disp("『{}』を追加します".format(key_word))
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(key_word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./{}".format(csv),encoding="utf_8-sig")
    print(source)
