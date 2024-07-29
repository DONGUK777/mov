from mov.api.call import gen_url, req, get_key,req2df,list2df
from pandas import DataFrame

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
    l = req2df()
    assert len(l) > 0
    v = l.iloc[0]  # 또는 l['column_name']


def test_list2df():
    df = list2df()
    print(df)
    assert isinstance(df,DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns
    assert 'salesChange' in df.columns
