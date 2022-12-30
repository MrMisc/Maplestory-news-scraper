

@client.command(brief = "<word or phrase to search in the latest news articles from MS website>", description = "You have to type what you are searching for.\n Hint: You can type a vowel in here to just see all the latest news articles")
async def ms_news(ctx, string):
    stock = 'https://maplestory.nexon.net/'
    animalswikia = 'https://maplestory.nexon.net/news/'
    Req = Request(animalswikia)
    uClient = urlopen(Req)
    soup = BeautifulSoup(uClient.read(), 'html5lib')
    listoftitlesandlinks = [(item.find('div', {'class', 'label'}).text, item.a) for item in soup.find_all('div', {'class', 'photo'})]
    thing = string
    listi = []
    for i in listoftitlesandlinks:
        if i[0].lower().__contains__(thing.lower()):
            listi.append(i[1]['href'])
    if len(listi) > 0:
        for j in unique(listi):
            await ctx.send(stock+j)
    else:
        LISTOFDESC = soup.find_all('div', {'class',  'text'})
        ALL = soup.find_all('li', {'class', 'news-item'})
        if len(LISTOFDESC) != len(ALL):
            await ctx.send(f"ERROR! Found {len(LISTOFDESC)} paragraphs but {len(ALL)} links!")
        else:
            matchno = []
            for i in range(len(LISTOFDESC)):
                if LISTOFDESC[i].p.text.lower().__contains__(thing.lower()):
                    matchno.append(i)
            for k in unique([stock+links.a['href'] for links in [ALL[matchnumber] for matchnumber in matchno]]):
                await ctx.send(k)

