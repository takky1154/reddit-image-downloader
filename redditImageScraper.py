import shutil
from sys import exit
try:
    import requests
except ImportError:
    print('Requests must be installed. PLease run: pip install requests')
    exit()
    

def makeUrl(afterID, subreddit):
        newUrl = subreddit.split('/.json')[0] + "/.json?after={}".format(afterID)
        return newUrl
    

def splitUrl(imageUrl):
        if 'jpg' or 'webm' or 'mp4' or 'gif' or 'gifv' or 'png' in imageUrl:
            return imageUrl.split('/')[-1]  # Returns filename


def downloadImage(imageUrl, imageAmount):  # Function to download the images from
                                # each url passed to it
        filename = splitUrl(imageUrl)
        if filename:
            r = requests.get(imageUrl, stream=True)  # Downloads image
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                print("Successfully downloaded: " + imageUrl)
                imageAmount += 1
        return imageAmount


def run():
    subreddit = input("Please enter subreddit url in the form of \"https://www.reddit.com/r/sub\": ")
    limit = int(input("How many images would you like to download: "))
    subJson = ''
    x = 0
    while x < limit:
        if subJson:
            url = makeUrl(subJson['data']['after'], subreddit)
        else:
            url = makeUrl('', subreddit)
        subJson = requests.get(url, headers={'User-Agent': 'MyRedditScraper'}).json()
        post = subJson['data']['children']
        postCount = range(len(post))
        # Sets postCount equal to the number of posts

        for i in postCount:  # Iterates over the number of posts received the sub
            imageUrl = (post[i]['data']['url'])
            _imageUrls = []
            _imageUrls.append(imageUrl)
            x = downloadImage(_imageUrls[0], x)
            if x == limit:
                break

run()
