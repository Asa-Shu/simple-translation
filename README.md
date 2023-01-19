# simple-translation

## Preview
![example.gif](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1790537/8826f0f8-144e-07ac-eee4-896d0a72bf04.gif)

## Summary

Shortcut key to translate the selected string into English and replace it . The program itself is very simple.

You can find more details [here]().

## Setup

Open Automator.app

![スクリーンショット 2023-01-20 4.14.34.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1790537/93263c9d-27c5-6b6d-8293-99bd4312d5c4.png)

Library > Utilities > Run Shell Scripts
Change shell to Python, write contents of app.py and save as `hoge.workflow`

![スクリーンショット 2023-01-20 4.19.33.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1790537/069f5ca8-315a-1ee7-7795-a0fa571ab650.png)

Open keyboard

![スクリーンショット 2023-01-20 4.20.31.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1790537/3ac2c4fe-b8ac-851d-9766-804b8581f2f5.png)

Shortcut tab > Services

find `hoge` and assign the key combination. Here I assigned `cmd + '` for `translation`. (Recommended)

![スクリーンショット 2023-01-20 4.23.15.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1790537/b9b77d77-6f27-6145-3a32-9db0d7606e09.png)

## Use
Select the part you want to translate into English and press `cmd + '`.

Shortcuts to translate English into Japanese can also be made by simply replacing **'ja'** and **'en'**.
