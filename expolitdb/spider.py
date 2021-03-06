import random
import requests
import csv


ua_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
           "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 "
           "Safari/536.11",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 "
           "Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
           ]

def spider(spider_url):
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': random.choice(ua_list),
        'X-Requested-With': 'XMLHttpRequest'
        }
    spider_request = requests.get(spider_url, headers=header)
    h1 = spider_request.json()
    if h1['recordsFiltered'] == 0:
        return 0
    else:
        id = h1['data'][0]['id']
        return id

if __name__ == '__main__':
    urlbase = 'https://www.exploit-db.com/exploits/' #??????url
    #cvelist1 = ['2019-0000', '2019-0230']
    b = ''
    with open('cvelist2.txt', 'r', encoding='utf-8') as f:
        b = f.read()
    to_one_line = ' '.join(b.split())
    CVE_LIST = b.split('\n')
    #print(CVE_LIST)
    #b = ['2005-2678', '2005-2089', '2017-7269', '2010-1256', '2008-0074', '2007-1278', '2007-2897', '2001-0500', '2018-11784', '2019-17563', '2019-12418', '2020-1935', '2019-10072', '2019-0221', '2019-0232', '2019-0199', '2018-8014', '2018-8034', '2018-1336', '2018-1305', '2018-1304', '2020-1938', '2020-2572', '2020-2660', '2020-2589', '2020-2574', '2020-2570', '2020-2573', '2020-2579', '2019-2974', '2019-2960', '2019-2948', '2019-2946', '2019-2924', '2019-2923', '2019-2922', '2019-2914', '2019-2911', '2019-2910', '2019-2819', '2019-2805', '2019-2791', '2019-2778', '2019-2774', '2019-2758', '2019-2757', '2019-2755', '2019-2740', '2019-2737', '2019-2731', '2019-2730', '2007-2691', '2019-2683', '2019-2632', '2019-2628', '2019-2627', '2019-2581', '2019-2566', '2019-2532', '2019-2534', '2019-2537', '2019-2528', '2019-2529', '2019-2510', '2019-2507', '2019-2482', '2019-2486', '2019-2481', '2019-2434', '2019-2455', '2019-2420', '2018-3282', '2018-3277', '2018-3278', '2018-3251', '2018-3276', '2018-3200', '2018-3247', '2018-3185', '2018-3187', '2018-3171', '2018-3173', '2018-3161', '2018-3162', '2018-3156', '2018-3155', '2018-3143', '2018-3144', '2018-3133', '2018-3081', '2018-3123', '2018-3077', '2018-3070', '2018-3071', '2018-3066', '2018-3065', '2018-3064', '2018-3061', '2018-3056', '2018-3058', '2018-3060', '2018-3054', '2018-2846', '2018-2819', '2018-2839', '2018-2818', '2018-2817', '2018-2816', '2018-2813', '2018-2812', '2018-2810', '2018-2784', '2018-2786', '2018-2787', '2018-2781', '2018-2782', '2018-2780', '2018-2779', '2018-2778', '2018-2777', '2018-2776', '2018-2775', '2018-2769', '2018-2766', '2018-2761', '2018-2759', '2018-2758', '2018-2696', '2018-2703', '2018-2668', '2018-2667', '2018-2665', '2018-2647', '2018-2646', '2018-2645', '2018-2640', '2018-2622', '2018-2612', '2018-2600', '2018-2591', '2018-2586', '2018-2590', '2018-2583', '2018-2573', '2018-2576', '2018-2565', '2018-2562', '2017-3652', '2017-3650', '2017-3651', '2017-3647', '2017-3648', '2017-3649', '2017-3645', '2017-3646', '2017-3642', '2017-3643', '2017-3644', '2017-3641', '2017-3638', '2017-3639', '2017-3640', '2017-3633', '2017-3634', '2017-10379', '2017-10384', '2017-10365', '2017-10378', '2017-10320', '2017-10314', '2017-10313', '2017-10311', '2017-10296', '2017-10284', '2017-10279', '2017-10276', '2017-10227', '2017-10167', '2017-10165', '2017-10155', '2018-3063', '2018-2805', '2017-3636', '2017-3600', '2017-3464', '2017-3463', '2017-3461', '2017-3456', '2017-3462', '2017-3453', '2017-3309', '2017-3329', '2017-3308', '2017-3305', '2012-3147', '2012-3144', '2012-0496', '2012-0495', '2012-0491', '2012-0490', '2012-0488', '2012-0489', '2012-0486', '2012-0487', '2012-0485', '2008-0075', '2017-3736', '2017-3735', '2016-8610', '2013-6449', '2016-9775', '2016-9774', '2016-5388', '2012-0484', '2012-0119', '2012-0120', '2012-0118', '2012-0116', '2012-0115', '2012-0113', '2011-2262', '2017-3599', '2017-3467', '2017-3465', '2017-3458', '2017-3459', '2017-3460', '2017-3455', '2017-3457', '2017-3454', '2017-3331', '2017-3450', '2018-11218', '2018-12326', '2018-11219', '2016-10517', '2018-12453', '2013-0180', '2015-4335', '2017-3452', '2014-0412', '2014-0401', '2014-0402', '2014-0386', '2013-3839', '2013-3804', '2013-3808', '2013-2392', '2013-3802', '2013-2378', '2013-2389', '2013-2375', '2013-1552', '2013-1555', '2013-1544', '2013-1532', '2013-1531', '2013-1521', '2013-1492', '2013-0386', '2013-0389', '2013-0385', '2013-0383', '2013-0384', '2012-1705', '2013-0375', '2012-0574', '2012-1702', '2012-0553', '2012-0572', '2012-0102', '2012-0101', '2012-0087', '2006-4227', '2012-3166', '2010-3838', '2010-3837', '2010-3836', '2010-3834', '2010-3833', '2010-3682', '2010-3677', '2010-1850', '2010-1849', '2010-1848', '2009-5026', '2009-4028', '2009-4019', '2009-2446', '2008-4098', '2008-3963', '2008-2079', '2007-6304', '2007-3781', '2007-5969', '2007-2692', '2007-3780', '2004-0628', '2004-0627', '2015-8080', '2017-7925', '2013-3612', '2017-7923', '2017-7921', '2019-3948', '2019-0230']
    f = open('result2.csv', 'w+')
    writer = csv.writer(f)
    writer.writerow(('cve', 'result'))
    for s in CVE_LIST:
        url = 'https://www.exploit-db.com/?draw=2&columns[0][data]=date_published&columns[0][name]=date_published&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=download&columns[1][name]=download&columns[1][searchable]=false&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=application_md5&columns[2][name]=application_md5&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=verified&columns[3][name]=verified&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=description&columns[4][name]=description&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=type_id&columns[5][name]=type_id&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=platform_id&columns[6][name]=platform_id&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=author_id&columns[7][name]=author_id&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=code&columns[8][name]=code.code&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=id&columns[9][searchable]=false&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=9&order[0][dir]=desc&start=0&length=15&search[value]=%s&search[regex]=false&author=&port=&type=&tag=&platform=&_=1606893892234'%s
        id = spider(url)
        if id == 0:
            print("cve-%s??????poc"%s)
            writer.writerow(('cve-%s'%s,"no poc"))
        else:
            print("cve-%s???poc"%s)
            writer.writerow(('cve-%s'%s, "poc???"+urlbase+id))


