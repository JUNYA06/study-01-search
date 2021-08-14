#課題１を作る上で、処理の流れとしては以下のように考えました。
# リストを生成する処理
# もしCSVが存在する場合は、読み込む処理
# 　リストに追加する処理

# 戻り値を受け取る処理

# 戻り値とリストが一致しているか確認する処理
# 　一致する場合→「見つかった」と出力
# 　一致しない場合→「見つからなかった」と出力

# csvを出力する処理

import csv
csv_path = 'C:/Users/user/python/study-01-search/test.csv'


# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

def export_list_csv(list,csv_path):
    with open(csv_path, 'w', newline='', encoding="utf_8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
        writer.writerows(list)

def import_list_csv(list,csv_path):
    with open(csv_path,'r', encoding="utf_8") as f:
        reader = csv.reader(f, lineterminator='\n')
        
        for row in reader:
            list.extend(row)
            
            print(list)
    return list   

### 検索ツール
def search():
    import_list =[]
    import_list_csv(source,csv_path)

    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    #登場人物の検索
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}が見つかりませんでした".format(word))
        source.append(word)
        print(source)
    export_list_csv(source,r"list.csv")
    

if __name__ == "__main__":
    search()






