import requests
import os
import pandas as pd

def req(load_dt='20120101'):
    # url = gen_url('20240720')
    url = gen_url(load_dt)
    r = requests.get(url)
    code = r.status_code
    # return r.status_code
    data = r.json()    
    # print(data)
    return code, data
    
def gen_url(load_dt='20120101'):
    base_url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={load_dt}"

    return url

def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2df(load_dt):
    _, data = req(load_dt)
    # data.get('').get('')
    l = data['boxOfficeResult']['dailyBoxOfficeList']
#    l = [
#            {'rnum': '1', 'rank': '1'},
#            {'rnum': '2', 'rank': '2'},
#            {'rnum': '3', 'rank': '3'}
#        ]
    df = pd.DataFrame(l)
    return df

def list2df(load_dt='20120101'):
    l = req2list(load_dt)
    df = pd.DataFrame(l)
    return df

def req2list(load_dt)->list:
    _, data = req(load_dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def save2df(load_dt='20120101'):
    df = list2df(load_dt)
    # df에 load_dt 컴럼 추가 (조회 일자 YYMMDD 형식으로)
    # 아래 파일 저장시 load_dt 기본으로 파티셔닝
    df['load_dt'] = load_dt
    print(df.head(5))
    df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])
    return df

def echo(yaho):
    return yaho
