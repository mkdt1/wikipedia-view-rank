# wikipedia-view-rank

wikipedia-view-rankはWikipedia記事の閲覧数を抽出するプログラムで、アイドルグループのランキング（現在のアイドルグループTOP200）を作成するために開発したものです。

## ランキング指標

本ランキングはWikipedia記事の過去60日分の閲覧数を基準にしております。
[Mediawiki](https://en.wikipedia.org/w/api.php?action=help&modules=main "MediaWiki API help - Wikipedia")の仕様上、60日が閲覧数を取得できる最長期間になります。

## 「現在のアイドルグループTOP200」の集計方法

集計は「[日本のアイドルグループ](https://ja.wikipedia.org/wiki/Category:%E6%97%A5%E6%9C%AC%E3%81%AE%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97 "Category:日本のアイドルグループ - Wikipedia")」カテゴリーに含まれる記事を対象としています。
一部のカテゴリーに含まれる記事は除外しております。
除外対象のカテゴリー一覧は[こちら](https://github.com/mkdt1/wikipedia-view-rank/blob/master/deny_categories.txt)をご参照ください。
なお、「でんぱ組.inc」及び「BABYMETAL」は除外対象カテゴリーに含まれますが、制作者の判断で除外対象から外しております。
また、男性グループ、解散・活動停止中のグループと思われる記事は制作者の判断で除外しています。
除外対象の記事一覧は[こちら](https://github.com/mkdt1/wikipedia-view-rank/blob/master/deny_articles.txt)をご参照ください。
