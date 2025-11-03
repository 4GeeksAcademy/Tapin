from auth import token_for


def test_create_and_crud_listing(client, create_user):
    user_id = create_user('owner@example.com')
    token = token_for(user_id)
    headers = {'Authorization': f'Bearer {token}'}

    # create
    resp = client.post('/listings', json={'title': 'L1', 'description': 'D1'}, headers=headers)
    assert resp.status_code == 201
    listing = resp.get_json()
    lid = listing['id']

    # read
    r2 = client.get(f'/listings/{lid}')
    assert r2.status_code == 200

    # update
    r3 = client.put(f'/listings/{lid}', json={'title': 'L1-Updated'}, headers=headers)
    assert r3.status_code == 200
    assert r3.get_json()['title'] == 'L1-Updated'

    # delete
    r4 = client.delete(f'/listings/{lid}', headers=headers)
    assert r4.status_code == 200
