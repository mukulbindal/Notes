import requests
import urllib3
from bs4 import BeautifulSoup
from collections import defaultdict
import threading
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = 'https://www.fishbowlapp.com/bowl/'
result = defaultdict(set)
old_result = defaultdict(set)

def print_relavant_posts(bowl):
    response = requests.get(base_url + bowls[0], headers={'User-Agent': 'PostmanRuntime/7.26.10'}, verify=False)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')

    posts_divs = soup.find_all(class_='post-text')

    if posts_divs:
        for posts in posts_divs:
            post = posts.text 
            
            result[bowl].add(post)

bowls = ['tech-india', 'job-referrals-and-openings', 'job-referrals', 'interview-experience']
def compare(a: dict, b: dict):
    for key in a.keys():
        l1 = a[key]
        l2 = b[key]
        if len(l1) != len(l2):
            return False
        for x, y in zip(l1, l2):
            if x != y:
                return False
    return True 

def start_threads():
    threads = []
    for bowl in bowls:
        thread = threading.Thread(target=print_relavant_posts, args=(bowl,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    if compare(result, old_result) == False:
        print(result)

while True:
    start_threads()
    print('sleeping for 300 seconds...')
    time.sleep(300)
    print('woke up..')
    old_result = result
    

