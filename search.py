### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
csv_path = 'C:/Users/user/python/study-01-search/test.csv'


# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

def export_list_csv(export_list,csv_path):
    with open(csv_path,'w') as f:
        writer =csv.writer(f,lineterminator='\n')

        if isinstance(export_list[0],list):
            writer.writerows(export_list)
        else:
            writer.writerows(export_list)


def import_list_csv(list,csv_path):
    with open(csv_path,'r') as f:
        print(csv_path)
        reader = csv.reader(f)
        for row in reader:
            list.append(row)
            print(list)
    return list   

### 検索ツール
def search():
    import_list =[]
    import_list_csv(import_list,csv_path)
    source.extend(import_list)

    word =input("鬼滅の登場人物の名前を入力してください >>> ")
### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        source.append(word)
        print(source)
    export_list_csv(source,r"list.csv")

if __name__ == "__main__":
    search()

# もしCSVが存在する場合は、読み込み処理
# 　リストに追加する処理

# リストを受け取る処理
# 引数とリストが一致しているか確認する処理
# 　一致する場合
# 　一致しない場合
# csvを出力する処理
