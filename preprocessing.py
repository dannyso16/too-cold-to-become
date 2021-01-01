import pandas as pd
import re

if __name__ == "__main__":

    """スクレイピングしたcsvデータから個人アカウントを特定できる情報を消して
    `samusugi.csv`として出力
    """

    df = pd.read_csv("data.csv")
    _drop_list = list(set(df.columns) - set(('created_at', 'text')))
    df.drop(columns=_drop_list, inplace=True)

    def _remove_reply(x):
        return re.sub("@.+ ", "", x)

    df.text = df.text.map(_remove_reply)

    df.to_csv("samusugi.csv")
