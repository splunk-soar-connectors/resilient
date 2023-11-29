from dataclasses import dataclass
from resilient import SimpleClient
from typing import Optional


@dataclass
class ResilientClient:
    org_name: str
    base_url: str
    username: Optional[str] = None
    password: Optional[str] = None
    api_key_id: Optional[str] = None
    api_key_secret: Optional[str] = None

    _simple_client = None

    @property
    def simple_client(self):
        if self._simple_client is None:
            self._simple_client = self.get_authenticated_client()
        return self._simple_client

    def list_incidents(self):
        return self.simple_client.get("/incidents")

    def list_artifcats_for_incident(self, incident_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}/artifacts")

    def get_artifact(self, incident_id: str, artifact_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}/artifacts/{artifact_id}")

    def get_incident(self, incident_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}")

    def create_incident(self, payload: dict):
        assert all([k in payload for k in ["name", "description", "discovered_date"]])
        return self.simple_client.post(f"/incidents", payload=payload)

    def get_authenticated_client(self):
        if self.api_key_id and self.api_key_secret:
            return self.get_client_with_api_key()
        elif self.username and self.password:
            return self.get_client_with_credentials()
        else:
            raise NotImplementedError("Can't authenticate without api-key or credentials.")

    # reference auth either with api-key or creds
    # https://github.com/ibmresilient/resilient-python-api/blob/main/resilient/resilient/co3.py#L173-L177

    # https://ibmresilient.github.io/resilient-python-api/pages/resilient/resilient.html#resilient.co3.SimpleClient.get
    # https://www.ibm.com/support/pages/rest-api

    def new_simple_client(self):
        # See resilient/co3.py
        kwargs = {
            "request_max_retries": 1
        }
        return SimpleClient(org_name=self.org_name, base_url=self.base_url, **kwargs)

    def get_client_with_api_key(self):
        client = self.new_simple_client()
        client.set_api_key(self.api_key_id, self.api_key_secret)
        return client

    def get_client_with_credentials(self):
        timeout_seconds = 10
        client = self.new_simple_client()
        client.connect(email=self.username, password=self.password, timeout=timeout_seconds)
        return client
