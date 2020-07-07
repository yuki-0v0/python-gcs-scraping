from bs4 import BeautifulSoup
import requests
import time
import os

targets = ['犬', '猫']

for target in targets:

    # 画像URLを代入する配列を定義
    image_urls = []

    # 画像を保存するディレクトリ名を生成
    save_dir = './{}'.format(target)

    # 画像を保存するディレクトリの存在確認。なければ(False)ならフォルダを作成
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    # 3ページ目までスクレイピングすることを定義
    for num in range(3):

        # yahoo画像検索の簡易版URL
        url = 'https://search.yahoo.co.jp/image/search?p={}&oq=&ei=UTF-8&b={}'.format(target, str(1 + (20 * num)))

        # requestsライブライを使用し指定のURLにGETリクエスト。HTMLを取得
        html = requests.get(url)

        # 外部ライブラリのBeautifulSoup4を使ってHTMLをパース
        # 第1引数はHTML文字列
        # 第2引数はParserライブラリ。今回はPython標準ライブラリのhtml.parserを採用
        # 外部ライブラリもある。例えばlxmlとか。別途インストール（pip install）が必要。標準より高速だが依存性は気になるところ
        soup = BeautifulSoup(html.text,'html.parser')

        # find_allメソッドを使ってalt属性が「{検索キーワード}」の画像検索結果になっているタグを全て取得
        images = soup.find_all(alt='「{}」の画像検索結果'.format(target))
        
        # 取得した要素配列をループしてsrc属性を取得
        for i, image in enumerate(images):
            # 取得した画像URLの数が50以下か確認
            if len(image_urls) < 50:
                # src属性を取得し定義していた配列へ代入
                image_urls.append(image['src']) 

        # 次の処理まで２秒待機（先方側への負荷軽減のため）
        time.sleep(2)

    # 画像をダウンロード
    for i, url in enumerate(image_urls):
        res = requests.get(url, stream=True)
        
        # リクエストが成功した場合にのみ
        if res.status_code == 200:
            # 保存する画像のファイル名を作成。今回は全てjpgにします。
            image_name = save_dir + '/{}.jpg'.format(i)
            # からのファイルを書き込みモード（w）で作成してバイナリ（b）で書き込む準備。バイナリデータにしないとエラーになります
            with open(image_name, 'wb') as f:
                # 画像の中身を書き込む（res.content ＝ 画像の中身）
                f.write(res.content)

        # 次の処理まで２秒待機（先方側への負荷軽減のため）
        time.sleep(2)