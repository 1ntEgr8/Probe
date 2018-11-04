import re

def extract_calendar_events(stri):

    list_of_patterns = [
    r'\d\d?(/|-|. | |.)\d\d?(/|-|. | |.)\d\d\d?\d? ?',
    r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tue|Tues|Wed|Thurs|Thu|Fri|Sat|Sun)?,? +\d\d?(/|-|. | |.)(Jan|Feb|Mar|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|May|April|July|August|September|October|November|December)?(/|-|. | |.)\d\d\d?\d? ?', # you made a change here in the months, added ?; if an error props up , double check that line
    r'\d\d\d\d(/|-|. | |.)\d\d(/|-|. | |.)\d\d? ?',
    r'\d\d\d\d(/|-|. | |.)?(Jan|Feb|Mar|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|May|April|July|August|September|October|November|December)(/|-|. | |.)?\d\d?,? ?(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tue|Tues|Wed|Thurs|Thu|Fri|Sat|Sun)?',
    r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tue|Tues|Wed|Thurs|Thu|Fri|Sat|Sun)?,? (Jan|Feb|Mar|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|May|April|July|August|September|October|November|December)?,? \d\d?, \d\d\d?\d? ?',
    r'\S+ \dth+ \S+ (Jan|Feb|Mar|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|May|April|July|August|September|October|November|December) \d\d\d\d ?'
    ]


s = "Our first general meeting of the semester is coming up soon. It will be next Tuesday, October 23, at 6pm in CoC room 017. Come hear what all of RoboJackets is working on, and see a short presentation by Scott Gilliland about his research. Unfortunately, due to events out of our control, we won't be able to provide pizza for this one. If you can make it, please don't forget to RSVP by clicking this link."

extract_calendar_events(s)
