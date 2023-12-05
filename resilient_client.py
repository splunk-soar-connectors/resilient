import logging
from dataclasses import dataclass
from typing import Dict, Optional, Union
from urllib.parse import urlencode

from resilient import SimpleClient

logger = logging.getLogger(__name__)


@dataclass
class ResilientClient:
    org_name: str
    base_url: str
    username: Optional[str] = None
    password: Optional[str] = None
    api_key_id: Optional[str] = None
    api_key_secret: Optional[str] = None
    verify: Union[bool, str] = None

    _simple_client = None

    @property
    def simple_client(self):
        if self._simple_client is None:
            self._simple_client = self.authenticate()
        return self._simple_client

    # TODO: may not need this func
    def get(self, path: str, query_params: Dict = None):
        query_params = query_params or {}
        query_string = urlencode(query_params)
        uri = f"{path}?{query_string}"
        logger.info(f"GET {uri}")
        return self.simple_client.get(uri)

    def list_incidents(self, closed: bool = False):
        condition = {
            "field_name": "properties.closed_on",
            "method": "not_equals" if closed else "equals",
            "value": None
        }

        return self.simple_client.post("/incidents/query", params={
            "return_level": "normal"
        }, payload={
            "filters": [
                {
                    "conditions": [condition]
                }
            ],
            "sorts": [
                {
                    "field_name": "create_date",
                    "type": "desc"
                }
            ]
        })

    def list_artifcats_for_incident(self, incident_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}/artifacts")

    def get_artifact(self, incident_id: str, artifact_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}/artifacts/{artifact_id}")

    def get_comment(self, incident_id: str, comment_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}/comments/{comment_id}")

    def list_comments_for_incident(self, incident_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}/comments")

    def list_attachments_for_incident(self, incident_id: str, use_handle_format_names: bool = False):
        if use_handle_format_names:
            self.simple_client.headers["handle_format"] = "names"
        return self.simple_client.get(f"/incidents/{incident_id}/attachments")

    def get_attachment(self, incident_id: str, attachment_id: str, use_handle_format_names: bool = False):
        if use_handle_format_names:
            self.simple_client.headers["handle_format"] = "names"
        return self.simple_client.get(f"/incidents/{incident_id}/attachments/{attachment_id}")

    def post_attachment(self, incident_id: str, filepath: str, filename: str, use_handle_format_names: bool = False):
        if use_handle_format_names:
            self.simple_client.headers["handle_format"] = "names"
        self.simple_client.post_attachment(f"/incidents/{incident_id}/attachments", filepath, filename=filename)

    def list_tables_for_incident(self, incident_id: str, use_handle_format_names: bool = False):
        if use_handle_format_names:
            self.simple_client.headers["handle_format"] = "names"
        return self.simple_client.get(f"/incidents/{incident_id}/table_data")

    def get_table(self, incident_id: str, table_id: str, use_handle_format_names: bool = False):
        if use_handle_format_names:
            self.simple_client.headers["handle_format"] = "names"
        return self.simple_client.get(f"/incidents/{incident_id}/table_data/{table_id}")

    def get_incident(self, incident_id: str):
        return self.simple_client.get(f"/incidents/{incident_id}")

    def create_incident(self, payload: dict):
        assert all([k in payload for k in ["name", "description", "discovered_date"]])
        return self.simple_client.post(f"/incidents", payload=payload)

    def authenticate(self) -> SimpleClient:
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
        return SimpleClient(org_name=self.org_name, base_url=self.base_url, verify=self.verify, **kwargs)

    def get_client_with_api_key(self):
        client = self.new_simple_client()
        client.set_api_key(self.api_key_id, self.api_key_secret)
        return client

    def get_client_with_credentials(self):
        timeout_seconds = 10
        client = self.new_simple_client()
        client.connect(email=self.username, password=self.password, timeout=timeout_seconds)
        return client
