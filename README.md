# alt_browser_acc

atcoder_cli (acc) を使用した AtCoder への提出結果を取得して CLI 上に表示するための Web スクレイピングスクリプトです。
[termux](https://github.com/termux/termux-app) を使用して作成したコーディング環境で自分で使用するために作成したものです。

## インストール手順

termux 内で使用することを前提とします。

1. このリポジトリを clone します。

```bash
git clone https://github.com/DaisukeTK/alt_browser_acc
```

2. プロジェクトのディレクトリに移動します

```bash
cd alt_browser_acc
```

3. make を叩いてビルド後、インストールします(pyinstaller が必要です)

```bash
make && make install
```

## Usage

BROWSER 環境変数に適用して acc コマンドを実行します。

```bash
$ BROWSER=alt_blowser_acc acc
```
