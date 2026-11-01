# ANYA ボイスの引き出し

90件すべてのMP3を収録したAndroid向けPWAです。APKではありません。

## 起動
Macで `cd /Users/sekine/Downloads/anya/soundboard/dist && python3 -m http.server 8765` を実行し、http://localhost:8765 を開きます。

## Androidに入れる
`dist` の内容をHTTPSの静的ホスティングに配置し、AndroidのChromeで開いて「ホーム画面に追加」→「インストール」。初回に「全音声をオフライン保存」を押すと通信なしでも再生できます。ローカルMacのHTTP URLではAndroidへのPWAインストールはできません。

分類はファイル名からの推定で、聞き取りや文字起こしによる確定ではありません。「内容確認」は判断できないファイルです。元音声は変更していません。分類一覧.jsonに元パスと分類根拠があります。

検証：90音声の同梱と元ファイルとのSHA256一致、JavaScript構文チェック。Android実機での再生・インストールは未検証。
