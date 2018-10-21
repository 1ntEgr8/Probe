import re

def extract_calendar_events(stri):
    list_of_patterns = [
    r'\d\d(/|-)\d\d(/|-)\d\d',
    r'\d\d(/|-)\m\m(/|-)\d\d\d\d',
    r'\d(/|-)\d(/|-)\d\d',
    r'\d(/|-)\d(/|-)\y\y\y\y',
    r'\d\d?-(Jan|Feb|Mar|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|May|April|July|August|September|October|November|December)-\d\d\d\d',
    r'\d\d\d\d(/|-)\d\d(/|-)\d\d',
    r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tue|Tues|Wed|Thurs|Thu|Fri|Sat|Sun)(\s|\S)+\d\d?(\s|\S)+(Jan|Feb|Mar|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|May|April|July|August|September|October|November|December)(\s|\S)+\d\d\d\d',
    r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tue|Tues|Wed|Thurs|Thu|Fri|Sat|Sun)(\s|\S)+(Jan|Feb|Mar|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|May|April|July|August|September|October|November|December)(\s|\S)+\d\d?(\s|\S)+\d\d\d\d'
    ]

    for pattern in list_of_patterns:
        while True:
            date
