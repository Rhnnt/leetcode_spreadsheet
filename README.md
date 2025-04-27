## 概要
Top Interview 150学習管理用スプレッドシートを作成します

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
<img width="747" alt="Screenshot 2025-04-27 at 11 35 15" src="https://github.com/user-attachments/assets/261a8a95-6d57-47dc-83d2-afd5214a6d3c" />
