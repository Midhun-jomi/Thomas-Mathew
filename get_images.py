import urllib.request
import json
import re

url = "https://unsplash.com/s/photos/construction"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+', html)
    unique_images = list(set(images))
    for i, img in enumerate(unique_images[:5]):
        print(f"Image {i+1}: {img}?q=80&w=1600")
except Exception as e:
    print(e)
