import searchengine
pagelist = ["http://kiwitobes.com/wiki.html"]
crawler = searchengine.crawler("")
crawler.crawl(pagelist)

crawler = searchengine.crawler("searchindex.db")
crawler.createindextables()

crawler = searchengine.crawler("seachindex.db")
pages = ["http://kiwitobes.com/wiki.html"]
crawler.crawl(pages)