

def test_conf(client):
    # sanity check to assert conf.TestConf was used
    assert client.application.config['TESTING'] is True


def test_health(client):
    # ACT
    resp = client.get('/health')

    # ASSERT
    assert resp.json['status'] == 'success'
