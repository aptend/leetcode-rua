import requests
import sys


PER_PAGE = 25


def page_url(kind, round, page, region):
    return f"https://leetcode-cn.com/contest/api/ranking/{kind}-{round}/?pagination={page}&region={region}"


def active_users(kind, round, region='local'):
    lo = 0
    hi = total_pages(kind, round, region) // PER_PAGE
    while lo <= hi:
        mid = (lo + hi) // 2
        rank = requests.get(page_url(kind, round, mid, region)).json()[
            'total_rank']
        if rank[0]['score'] == 0:
            hi = mid - 1
        elif rank[-1]['score'] > 0:
            lo = mid + 1
        else:
            for r in rank:
                if r['score'] == 0:
                    return r['rank'] - 1
    return -1


def total_pages(kind, round, region):
    return requests.get(page_url(kind, round, 1, region)).json()['user_num']


def usage():
    print(
    """找出比赛中得分大于0的参赛人数
    Examples: 
    python valid_users_in_contest.py 164              164场周赛中国区
    python valid_users_in_contest.py 164 -g           164场周赛全球
    python valid_users_in_contest.py 11 -b            11场双周赛中国区
    python valid_users_in_contest.py 11 -b -g         11场双周赛全球
    """)


def exit_msg(msg):
    print('眉头一皱，发现事情并不简单: ' + msg)
    usage()
    sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    n = len(argv)
    if n == 1 or n > 4:
        exit_msg('参数数量不对')

    option_flags = set(argv[1:])
    if '-h' in option_flags:
        usage()
        exit(0)

    kind = 'weekly-contest'
    region = 'local'
    try:
        round_num = int(argv[1])
    except TypeError:
        exit_msg('场次要是整数')

    if '-b' in option_flags:
        kind = 'bi' + kind
    if '-g' in option_flags:
        region = 'global'
    err = None
    try:
        ans = active_users(kind, round_num, region)
    except KeyError as e:
        err = e
    if err or ans == -1:
        print("未找到相关场次信息")
    else:
        print(ans)
