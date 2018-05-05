modules = ['shutil', 'requests', 'bob', 'bhjb']
def importModules():
    for i in modules:
        try:
            import i
        except ImportError:
                print('{} must be installed. Please run pip install {}'.format(i, i))
            
import shutil
#try:
#    import requests
#except ImportError:
#    print("Requests module required. Please run: pip install requests")
#url = input("Please enter subreddit url: ")

def makeUrl(afterID):
        newUrl = url.split('/.json')[0] + "/.json?after={}".format(afterID)
        return newUrl
    

# subJson just means the json data of the subreddit

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
    
    limit = int(input("How many images would you like to download: "))
    subJson = ''
    x = 0
    while x < limit:
        if subJson:
            url = makeUrl(subJson['data']['after'])
        else:
            url = makeUrl('')
        subJson = requests.get(url, headers={'User-Agent': 'MyRedditScraper'}).json()
        post = subJson['data']['children']
        postCount = range(len(post))
        # Sets postCount equal to the number of posts

        for i in postCount:  # Iterates over the number of posts received the sub
            imageUrl = (post[i]['data']['url'])
            _imageUrls = []
            _imageUrls.append(imageUrl)
            print(x)
            x = downloadImage(_imageUrls[0], x)
            if x == limit:
                break

# Prints the links to the image in the post
importModules()
run()
