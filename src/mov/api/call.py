def req(dt="20120101"):
    base_url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "84c02b6b6453e15a1a3ac31d2a1b59ab"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)


