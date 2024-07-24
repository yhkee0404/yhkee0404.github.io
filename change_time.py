# Save this as ../change_time.py
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def handle(s):
    date_str = s.decode('utf-8')
    [seconds, tzoffset] = date_str.split()
    date = datetime.fromtimestamp(int(seconds), datetime.strptime(tzoffset, '%z').tzinfo)
    kst = date.astimezone(ZoneInfo('Asia/Seoul'))
    print(kst)
    if kst.year != 2024:
        return s
    if kst.month != 3:
        return s
    match kst.day:
        case 27:
            kst = kst.replace(month = 4, day = 14)
        case 18:
            kst = kst.replace(month = 4, day = 13)
        case 17:
            kst = kst.replace(month = 4, day = 10)
        case 16:
            kst = kst.replace(month = 4, day = 7)
        case 15:
            kst = kst.replace(month = 4, day = 6)
        case 14:
            kst = kst.replace(day = 31)
        case 13:
            kst = kst.replace(day = 30)
        case 12:
            kst = kst.replace(day = 24)
        case 11:
            kst = kst.replace(day = 23)
        case 8:
            kst = kst.replace(day = 17)
        case 7:
            kst = kst.replace(day = 16)
        case 6:
            kst = kst.replace(day = 10)
    return f'{int(kst.timestamp())} {tzoffset}'.encode('utf-8')

commit.author_date = handle(commit.author_date)
commit.committer_date = handle(commit.committer_date)