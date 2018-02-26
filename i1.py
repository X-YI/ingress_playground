import requests

url = 'https://www.ingress.com/r/getPlexts'

headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9',
           'content-length': '182',
           'content-type': 'application/json; charset=UTF-8',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/64.0.3282.186 Safari/537.36',
           'x-csrftoken': 'C2Qz6EVGwgwiDDxe7FIQdO6Z4TwBL6Tr',
           'x-requested-with': 'XMLHttpRequest'}

payload = {'maxLatE6': '39997506',
           'maxLngE6': '116344614',
           'maxTimestampMs': '-1',
           'minLatE6': '39946134',
           'minLngE6': '116266851',
           'minTimestampMs': '-1',
           'tab': '"all"',
           'v': '"e74fb9b169e5aeb2cd88d3084471609d78885526"'}

cookies = {'csrftoken': 'C2Qz6EVGwgwiDDxe7FIQdO6Z4TwBL6Tr',
          'G_ENABLED_IDPS':'google',
          '__utmz=24037858.1519082033.9.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr':'https://www.ingress.com/intel',
          '__utmc':'24037858',
          '__utma':'24037858.490347001.1515911990.1519597248.1519641561.17',
          '__utmt':'1',
          'SACSID':'~AJKiYcEPQd96Lro6l5xiDIeP1'
                   '-Y_SEMkAMOYsAJgZDJCNhyWl4s2DivBVUBcqKHUXjniSeIRY4YBTz4kQSGnFLhjPV93uzqsYz6LZhV7zXME85GS7YSEvL'
                   '-L6gDBgqY7sQJuDyxq2cYcZAb2TZVG_U1-u9EMc6XndiSsik7i_WFGtJlijAmJwzzDCBv7iGnswfcN0qZG-M-W_cSDXZZZZm'
                   '-Y9GsG8AC5JlJ4grIdtoHCjtMTCEyj3VH_7yvBw0oL7PJwDxbp4QRdfx0gKMZPc2g64ab-cC'
                   '-xjfCJY5ImOqF22eJDAXMJBPJsRv2RyqMW-rWH4g-6tvOH',
           'ingress.intelmap.zoom':'14',
           '__utmb':'24037858.6.9.1519641973525',
           'ingress.intelmap.lat':'39.971825235411806',
           'ingress.intelmap.lng':'116.30573272705077'}

r = requests.post(url, params=payload, headers=headers, cookies=cookies)
print(r)
