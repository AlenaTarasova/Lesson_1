from main import get_notMe, get_Me
import yaml


with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_1(login):
    res = get_notMe(login)
    lst = res["data"]
    lst_id = [el["id"] for el in lst]
    assert 78249 in lst_id, "тест провален"


def test_create_post(login):
    response = requests.post(data["url_posts"],
                             headers={"X-Auth-Token": login},
                             data={'title': data["title"],
                                   'description': data["description"],
                                   'content': data["content"]})

    lst_description = [el["description"] for el in get_Me(login)["data"]]
    assert data["description"] in lst_description, "тест провален"