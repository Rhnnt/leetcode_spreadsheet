## 概要
Top Interview 150学習管理用スプレッドシートを作成します

## 使い方
1. `.env`ファイルに、Google Cloudのサービスアカウントキーへのパスを `PATH_TO_CREDENTIAL_JSON` という名前で設定する
2. Googleスプレッドシートで「LeetCode Top Interview 150」という名前のスプレッドシートを作成し、サービスアカウントのメールアドレスを編集権限で追加する
3. ライブラリをインストールする
`pip install gspread gspread-formatting oauth2client selenium beautifulsoup4 python-dotenv`
4. スクリプトを実行する
