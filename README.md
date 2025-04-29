## 概要
LeetCode Top Interview 150 の学習管理用スプレッドシートを作成します

## 使い方
1.
- Google Cloud Consoleでプロジェクトを作成または選択する
- 以下のAPIを有効化する
  - Google Sheets API
  - Google Drive API
- サービスアカウントを作成し、JSON形式の鍵をダウンロードする
2. `.env`ファイルに、Google Cloudのサービスアカウントキーへのパスを `PATH_TO_CREDENTIAL_JSON` という名前で設定する
3. Googleスプレッドシートで「LeetCode Top Interview 150」という名前のスプレッドシートを作成し、サービスアカウントのメールアドレスを編集権限で追加する
4. ライブラリをインストールする
`pip install gspread gspread-formatting oauth2client selenium beautifulsoup4 python-dotenv`
5. スクリプトを実行する

## こんな感じ
<img width="779" alt="Screenshot 2025-04-29 at 22 37 40" src="https://github.com/user-attachments/assets/63fd835b-a35a-4c2b-a2ba-066ed546fe23" />
