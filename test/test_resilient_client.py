import os
from unittest.mock import patch

import pytest
from resilient import SimpleHTTPException

from resilient_client import ResilientClient


@pytest.fixture
def client_from_env():
    yield ResilientClient(base_url=os.environ["RESILIENT_API_BASE_URL"],
                          org_name=os.environ["RESILIENT_API_ORG_NAME"],
                          api_key_id=os.environ["RESILIENT_API_KEY_ID"],
                          api_key_secret=os.environ["RESILIENT_API_KEY_SECRET"])


def test_client_using_creds_auth():
    username = "user@mail.com"
    password = "pass"

    with pytest.raises(SimpleHTTPException) as e:
        ResilientClient(base_url=os.environ["RESILIENT_API_BASE_URL"],
                        org_name=os.environ["RESILIENT_API_ORG_NAME"],
                        username=username,
                        password=password).get_client_with_credentials()


def test_client_using_api_key_auth():
    c = ResilientClient(base_url=os.environ["RESILIENT_API_BASE_URL"],
                        org_name=os.environ["RESILIENT_API_ORG_NAME"],
                        api_key_id=os.environ["RESILIENT_API_KEY_ID"],
                        api_key_secret=os.environ["RESILIENT_API_KEY_SECRET"]).get_client_with_api_key()
    assert len(c.get("/incidents")) > 0


def test_get_incident(client_from_env):
    resp = client_from_env.get_incident("2098")
    assert resp["id"] == 2098
    assert resp["name"] == "INC03375277 SIEM Malware"


def test_list_incidents_closed(client_from_env):
    resp = client_from_env.list_incidents(closed=True)
    assert len(resp) > 0
    for incident in resp:
        assert all([k in incident for k in ["id", "name", "description", "create_date"]])
        assert incident["properties"]["closed_on"] is not None


def test_list_incidents_not_closed(client_from_env):
    resp = client_from_env.list_incidents(closed=False)
    assert len(resp) > 0
    for incident in resp:
        assert all([k in incident for k in ["id", "name", "description", "create_date"]])
        assert incident["properties"]["closed_on"] is None


def test_list_artifacts(client_from_env):
    resp = client_from_env.list_artifcats_for_incident("2098")
    assert len(resp) > 0
    assert resp[0]['id'] == 2
    assert resp[0]['inc_name'] == 'INC03375277 SIEM Malware'


def test_get_artifact(client_from_env):
    resp = client_from_env.get_artifact(incident_id="2098", artifact_id="2")
    assert resp['id'] == 2
    assert resp['inc_name'] == 'INC03375277 SIEM Malware'


def test_create_incident(client_from_env):
    # API key we have seems to have only read-only access
    resp = client_from_env.create_incident(
        {"name": "Test", "description": "Test", "discovered_date": "2021-01-01T00:00:00.000Z"})
    assert resp
