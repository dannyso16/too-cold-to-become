import re
import pandas as pd
from collections import Counter


if __name__ == "__main__":

    df = pd.read_csv("samusugi.csv")
    print("{} tweets の分析結果".format(len(df)))
    print("cols: ", df.columns)

    text_list = df.text.tolist()
    date_list = df.created_at.to_list()
    date_list = sorted(date_list)
    _from = date_list[0]
    _to = date_list[-1]
    print("集計期間：{} ～ {}".format(_from, _to))

    matches = []
    pattern = '寒すぎて.+になった'
    prog = re.compile(pattern)
    ignore_chars = [" ", "　", ",", "、"]

    for text in text_list:
        for char in ignore_chars:
            text = text.replace(char, "")
        result = prog.match(text)
        if result:
            matches.append(result.group(0))

    words = [m.replace("寒すぎて", "").replace("になった", "") for m in matches]
    with open("all_words.txt", "w", encoding="utf-8") as f:
        s = "\n".join(set(words))
        f.write(s)

    counter = Counter(words)
    print("「寒すぎて〇になった」の種類：{}".format(len(counter)))
    print("トップ20 !!")
    top10 = counter.most_common(20)
    for i, (name, count) in enumerate(top10):
        print("第{}位：寒すぎて{}になった -> {} tweets".format(i+1, name, count))
