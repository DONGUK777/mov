from mov.api.call import gen_url, req, get_key, req2df, list2df, save2df
from pandas import DataFrame
import pandas as pd

def test_hidekey():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()
    assert True
    assert "kobis" in url

def test_req():
    code, data = req()
    assert code == 200
    
    code, data = req('20230101')
    assert code == 200
    
# def test_red2df():
#    l = req2df()
#    assert len(l) > 0
#    v = l[0]
#    assert 'rnum' in v.keys()
#    assert v['rnum'] == '1'

def test_red2df():
    l = req2df(load_dt='20120101')
    assert len(l) > 0
    v = l.iloc[0]  # 또는 l['column_name']


def test_list2df():
    df = list2df('20120101')
    print(df)
    assert isinstance(df,DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns
    assert 'salesChange' in df.columns

def test_save2df():
    df = save2df()
    assert isinstance(df, DataFrame)
    assert 'load_dt' in df.columns
