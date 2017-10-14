import requests

url = "https://ja.wikipedia.org/w/api.php"

### 集計ルールの読み込み

RULES = [
    "target_categories",
    "deny_categories",
    "target_articles",
    "deny_articles",
]

rules = {}

for rule in RULES:
    tmp = []

    with open("./rules/{}.txt".format(rule)) as f:
        for line in [x.strip() for x in f.readlines()]:
            if line != "" and line[0] != "#":
                tmp.append(line)

    rules[rule] = tmp


### 対象カテゴリーに含まれる記事の取得

p = {
    "format": "json",
    "action": "query",
    "utf8": "",
    "list": "categorymembers",
    "cmlimit": "500",
}

articles = set()

for category in rules["target_categories"]:
    next_page = None
    p["cmtitle"] = "Category:{}".format(category)

    if "cmcontinue" in p:
        p.pop("cmcontinue")

    while True:
        if next_page is not None:
            p["cmcontinue"] = next_page

        r = requests.get(url, params=p)
        j = r.json()

        for article in j["query"]["categorymembers"]:
            articles.add(article["title"])
    
        if "continue" not in j:
            break
    
        next_page = j["continue"]["cmcontinue"]


### 閲覧数の取得と禁止条件に一致する記事の除外

p = {"format": "json",
     "action": "query",
     "utf8": "",
     "cllimit": 500,
     "prop": "pageviews|categories|pageprops"}

outputs = []

for article in articles:
    if ":" in article or article in rules["deny_articles"]:
        continue

    p["titles"] = article
    r = requests.get(url, params=p)
    j = r.json()

    page = list(j["query"]["pages"].values())[0]
    deny_flag = False

    if article in rules["target_articles"]:
        categories = []
    else:
        categories = [x["title"].split(":")[-1] for x in page["categories"]] 
        
    for category in categories:
        for deny_category in rules["deny_categories"]:
            if category == deny_category:
                deny_flag = True
                break

    if deny_flag:
        continue

    if "pageprops" not in page or "displaytitle" not in page["pageprops"]:
        title = article
    else:
        title = page["pageprops"]["displaytitle"]

    view_count = 0
    views = page["pageviews"]

    for v in views.values():
        if v is not None:
            view_count += v

    output = {
        "title": title,
        "view_count": view_count,
    }

    outputs.append(output)


### 結果のソートと表示

outputs.sort(key=lambda x: x["view_count"], reverse=True)

for i, output in enumerate(outputs):
    print('{},"{}",{}'.format(i + 1, output["title"], output["view_count"]))
