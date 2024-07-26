from mov.api.call import gen_url, req, get_key,req2df

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
    
def test_df():
    l = req2df()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'
