# File: resilient_connector.py
#
# Copyright (c) 2022 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

import calendar
import datetime
# Usage of the consts file is recommended
# from resilient_consts import *
import json
import sys
import time

import dateutil.parser
import phantom.app as phantom
from bs4 import UnicodeDammit
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector
from phantom.vault import Vault

import co3


# get string value: return "" if key not in dictionary, otherwise value
# deprecated use dict.get(key, "")
def getsv(dic, key):
    if key in dic:
        return dic[key]
    else:
        return ""


# add key as target_key to target dictionary if key exists in source dictionary
def addifkey(dic, key, tdic, tkey):
    if key in dic:
        tdic[tkey] = dic[key]


class ResilientConnector(BaseConnector):

    def __init__(self):

        # Call the BaseConnectors init first
        super(ResilientConnector, self).__init__()

        self._state = None

        # Variable to hold a base_url in case the app makes REST calls
        # Do note that the app json defines the asset config, so please
        # modify this as you deem fit.
        self._base_url = None

    def get_json_parameter(self, dic, key, action_result):
        if key not in dic:
            return dict()

        value = dic[key]

        action_id = self.get_action_identifier()

        try:
            if not isinstance(value, basestring):  # noqa: F821
                errmsg = "{} failed. {} field is not a string (type={})".format(action_id, key, type(value))
                self.save_progress(errmsg)
                return action_result.set_status(phantom.APP_ERROR, errmsg)
        except:
            if not isinstance(value, str):
                errmsg = "{} failed. {} field is not a string (type={})".format(action_id, key, type(value))
                self.save_progress(errmsg)
                return action_result.set_status(phantom.APP_ERROR, errmsg)

        try:
            payload = json.loads(value)
            return payload
        except Exception as e:
            _, error_msg = self._get_error_message_from_exception(e)
            errmsg = "{} failed. {} field is not valid json, {}".format(action_id, key, error_msg)
            self.save_progress("{0}".format(errmsg))
            return action_result.set_status(phantom.APP_ERROR, errmsg)

    def _get_error_message_from_exception(self, e):
        """ This method is used to get appropriate error message from the exception.
        :param e: Exception object
        :return: error message
        """

        try:
            if hasattr(e, 'args'):
                if len(e.args) > 1:
                    error_code = e.args[0]
                    error_msg = e.args[1]
                elif len(e.args) == 1:
                    error_code = "Error code unavailable"
                    error_msg = e.args[0]
            else:
                error_code = "Error code unavailable"
                error_msg = "Unknown error occurred. Please check the asset configuration and|or action parameters."
        except:
            error_code = "Error code unavailable"
            error_msg = "Unknown error occurred. Please check the asset configuration and|or action parameters."

        try:
            error_msg = self._handle_py_ver_compat_for_input_str(error_msg)
        except TypeError:
            error_msg = "Error occurred while connecting to the server. Please check the asset configuration and|or the action parameters."
        except:
            error_msg = "Unknown error occurred. Please check the asset configuration and|or action parameters."

        return error_code, error_msg

    def _handle_py_ver_compat_for_input_str(self, input_str):
        """
        This method returns the encoded|original string based on the Python version.
        :param sys.version_info[0]: Python major version
        :param input_str: Input string to be processed
        :return: input_str
        """

        try:
            if input_str and sys.version_info[0] < 3:
                input_str = UnicodeDammit(input_str).unicode_markup.encode('utf-8')
        except:
            self.debug_print("Error occurred while handling python 2to3 compatibility for the input string")

        return input_str

    def __handle_exceptions(self, e, action_result):
        action_id = self.get_action_identifier()
        error_code, error_message = self._get_error_message_from_exception(e)
        try:
            if e.response is None:
                return action_result.set_status(phantom.APP_ERROR, "Error code:{} Error message: {}".format(error_code, error_message))

            if e.response.status_code == 400:
                self.save_progress("Bad request.")
                return action_result.set_status(phantom.APP_ERROR, "Error, {} Failed Error code:{} Error message: Bad request."
                                                                   .format(action_id, e.response.status_code))

            elif e.response.status_code == 401:
                self.save_progress("Unauthorized - most commonly, the provided session ID is invalid.")
                error_msg = "Error, {} Failed Error code:{} Error message: Unauthorized - most commonly, " \
                    "the provided session ID is invalid.".format(action_id, e.response.status_code)
                return action_result.set_status(phantom.APP_ERROR, error_msg)

            elif e.response.status_code == 403:
                self.save_progress("Forbidden - most commonly, user authentication failed.")
                error_msg = "Error, {} Failed Error code:{} Error message: Forbidden - most commonly, " \
                    "user authentication failed.".format(action_id, e.response.status_code)
                return action_result.set_status(phantom.APP_ERROR, error_msg)

            elif e.response.status_code == 404:
                self.save_progress("Object not found.")
                return action_result.set_status(phantom.APP_ERROR,
                    "Error, {} Failed Error code:{} Error message: Object not found.".format(action_id, e.response.status_code))

            elif e.response.status_code == 409:
                self.save_progress("Conflicting PUT operation.")
                return action_result.set_status(phantom.APP_ERROR,
                    "Error, {} Failed Error code:{} Error message: Conflicting PUT operation.".format(action_id, e.response.status_code))

            elif e.response.status_code == 500:
                self.save_progress("Internal error.")
                return action_result.set_status(phantom.APP_ERROR,
                    "Error, {} Failed Error code:{} Error message: Internal error.".format(action_id, e.response.status_code))

            elif e.response.status_code == 503:
                self.save_progress("Service unavailable - usually related to LDAP not being accessible.")
                return action_result.set_status(phantom.APP_ERROR, "Service unavailable - usually related to LDAP not being accessible.")

            else:
                self.save_progress("Error: status code {}".format(e.response.status_code))
                return action_result.set_status(phantom.APP_ERROR, "Error: {} failed status code {}".format(action_id, e.response.status_code))
        except:
            pass

        self.save_progress("Error, Action Failed: Error code:{} Error message: {}".format(error_code, error_message))
        return action_result.set_status(phantom.APP_ERROR,
                                        "Error, Action Failed Error code:{} Error message: {}".format(error_code, error_message))

    def _handle_test_connectivity(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()
        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_tickets(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            call = "/incidents?want_closed={}".format(param['want_closed'])

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        itemtype = "incidents"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    # assumes connection already setup
    # return exception on error
    def _get_ticket(self, param):
        action_id = self.get_action_identifier()
        incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
        call = "/incidents/{}".format(incident_id)
        self.save_progress("GET {}".format(call))
        retval = self._client.get(call)
        self.save_progress("{} successful.".format(action_id))
        return retval

    def _handle_get_ticket(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}".format(incident_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "incidents"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_ticket(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            call = "/incidents?want_full_data={}&want_tasks={}".format(param['want_full_data'], param['want_tasks'])
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        fullincidentdatadto = getsv(param, 'fullincidentdatadto')
        if len(fullincidentdatadto) > 1:
            try:
                payload = json.loads(fullincidentdatadto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. fullincidentdatadto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. fullincidentdatadto field is not valid json.".format(action_id))
        else:
            payload = dict()

        if 'name' not in payload:
            addifkey(param, 'incident_name', payload, 'name')
        if 'description' not in payload:
            addifkey(param, 'incident_description', payload, 'description')
        if 'discovered_date' not in payload:
            payload['discovered_date'] = calendar.timegm(time.gmtime()) * 1000

        if 'name' not in payload:
            self.save_progress("json payload does not have required 'name' key")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have required 'name' key")
        if 'description' not in payload:
            self.save_progress("json payload does not have required 'description' key")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have required 'description' key")
        if 'discovered_date' not in payload:
            self.save_progress("json payload does not have required 'discovered_date' key")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have required 'discovered_date' key")

        try:
            self.save_progress("POST {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.post(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "incidents"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_ticket(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        # validate incoming json
        fullincidentdatadto = param['fullincidentdatadto']
        if len(fullincidentdatadto) > 1:
            try:
                payload = json.loads(fullincidentdatadto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. fullincidentdatadto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. fullincidentdatadto field is not valid json.".format(action_id))
        else:
            payload = dict()

        config = self.get_config()

        # setup connection
        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}".format(incident_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        # remove parameter validation code. It just gets in the way
        # if 'name' not in payload:
        #    self.save_progress("json payload does not have 'name' key, payload should be result of get_ticket")
        #    return action_result.set_status(phantom.APP_ERROR, "json payload does not have 'name' key, payload should be result of get_ticket")
        # if 'description' not in payload:
        #    self.save_progress("json payload does not have 'description' key, payload should be result of get_ticket")
        #    return action_result.set_status(
        #        phantom.APP_ERROR, "json payload does not have 'description' key, payload should be result of get_ticket")
        # if 'discovered_date' not in payload:
        #    self.save_progress("json payload does not have 'discovered_date' key, payload should be result of get_ticket")
        #    return action_result.set_status(
        #        phantom.APP_ERROR, "json payload does not have 'discovered_date' key, payload should be result of get_ticket")

        # get ticket first
        # if param.get('get_ticket_and_copy_over', False):
        #    try:
        #        ticket = self._get_ticket(param)
        #    except Exception as e:
        #        return self.__handle_exceptions(e, action_result)

        #    newpayload = payload.copy()
        #    newpayload.update(fullincidentdatadto)
        #    payload = newpayload

        try:
            def apply(arg):
                arg.update(payload)
                return arg

            self.save_progress("GET_PUT {}".format(call))
            self.save_progress("PAYLOAD {}".format(payload))
            retval = self._client.get_put(call, apply)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "incidents"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_search_tickets(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        payload = dict()
        conditions = list()
        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            call = "/incidents/query?return_level=full"
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        querydto = getsv(param, 'querydto')
        if len(querydto) > 1:
            try:
                payload = json.loads(querydto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. querydto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. querydto field is not valid json.".format(action_id))
        else:
            payload = dict()

        if 'filters' in payload:
            filters = payload['filters']
        else:
            filters = list()
            payload['filters'] = filters

        conditions = list()
        if param.get('add_condition_all_active_tickets') is True:
            conditions.append({"field_name": "plan_status", "method": "equals", "value": "A"})
        if param.get('add_condition_created_in_last_24_hours') is True:
            conditions.append({"field_name": "create_date", "method": "gte",
                "value": calendar.timegm((datetime.datetime.utcnow() - datetime.timedelta(days=1)).utctimetuple()) * 1000})
        if param.get('add_condition_closed_in_last_24_hours') is True:
            conditions.append({"field_name": "end_date", "method": "gte",
                "value": calendar.timegm((datetime.datetime.utcnow() - datetime.timedelta(days=1)).utctimetuple()) * 1000})

        for con in ['1st', '2nd', '3rd', '4th', '5th']:
            try:
                name = getsv(param, "{}_condition_field_name".format(con))
                value = getsv(param, "{}_condition_field_value".format(con))
                method = getsv(param, "{}_condition_comparison_method".format(con))
                isdate = param.get("{}_condition_value_is_datetime".format(con))

                ln = len(name)
                lv = len(value)
                lm = len(method)

                # no condition, skip
                if (ln + lv + lm) == 0:
                    self.save_progress("{} condition is not complete".format(con))
                    continue

                if isdate:
                    try:
                        value = calendar.timegm(dateutil.parser.parse(value).utctimetuple()) * 1000
                    except Exception as e:
                        self.save_progress("Warning: {} condition value is not a datetime as expected: {}, skipping".format(con, e))
                        continue

                conditions.append({"field_name": name, "method": method, "value": value})
            except Exception as e:
                self.save_progress("Warning: {} condition not valid, skipping: {}.".format(con, e))

        if len('conditions') == 0:
            self.save_progress("json payload does not have 'conditions' key.")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have 'conditions' key")

        filters.append({ "conditions": conditions })

        try:
            self.save_progress("POST {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.post(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        itemtype = "incidents"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_artifacts(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}/artifacts".format(incident_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        itemtype = "artifacts"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_artifact(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            artifact_id = self._handle_py_ver_compat_for_input_str(param['artifact_id'])
            call = "/incidents/{}/artifacts/{}".format(incident_id, artifact_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "artifacts"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_artifact(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}/artifacts".format(incident_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        incidentartifactdto = getsv(param, 'incidentartifactdto')
        if len(incidentartifactdto) > 1:
            try:
                payload = json.loads(incidentartifactdto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. incidentartifactdto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. incidentartifactdto field is not valid json.".format(action_id))
        else:
            payload = dict()

        if 'description' not in payload:
            description = getsv(param, 'description')
            if len(description) > 0:
                payload['description'] = description
                # addifkey(param, 'incident_description', payload, 'description')
                # payload['description'] = dict()
                # payload['description']['format'] = "text"
                # payload['description']['content'] = getsv(param, 'description')
        if 'type' not in payload:
            type = getsv(param, 'type').lower()
            if type == "url":
                type = 3
            elif type == "domain":
                type = 2
            elif type == "file":
                type = 13
            else:
                try:
                    type = int(type)
                except:
                    self.save_progress("{} failed. Type is not recognized or not an integer".format(action_id))
                    return action_result.set_status(phantom.APP_ERROR, "{} failed. Type is not recognized or not an integer".format(action_id))
            if type > 0:
                payload['type'] = type
        if 'value' not in payload:
            addifkey(param, 'value', payload, 'value')

        if 'type' not in payload:
            self.save_progress("json payload does not have required 'type' key")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have required 'type' key")
        if 'value' not in payload:
            self.save_progress("json payload does not have required 'value' key")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have required 'value' key")
        if 'description' not in payload:
            self.save_progress("json payload does not have required 'description' key")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have required 'description' key")

        try:
            self.save_progress("POST {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.post(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        itemtype = "artifacts"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_artifact(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            artifact_id = self._handle_py_ver_compat_for_input_str(param['artifact_id'])
            call = "/incidents/{}/artifacts/{}".format(incident_id, artifact_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        incidentartifactdto = getsv(param, 'incidentartifactdto')
        if len(incidentartifactdto) > 1:
            try:
                payload = json.loads(incidentartifactdto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. incidentartifactdto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. incidentartifactdto field is not valid json.".format(action_id))
        else:
            payload = dict()

        if 'type' not in payload:
            self.save_progress("json payload does not have 'type' key, payload should be result of get_artifact")
            return action_result.set_status(
                phantom.APP_ERROR, "json payload does not have 'type' key, payload should be result of get_artifact")
        if 'value' not in payload:
            self.save_progress("json payload does not have 'value' key, payload should be result of get_artifact")
            return action_result.set_status(
                phantom.APP_ERROR, "json payload does not have 'value' key, payload should be result of get_artifact")
        if 'description' not in payload:
            self.save_progress("json payload does not have 'description' key, payload should be result of get_artifact")
            return action_result.set_status(
                phantom.APP_ERROR, "json payload does not have 'description' key, payload should be result of get_artifact")

        try:
            self.save_progress("PUT {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.put(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "artifacts"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_comments(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.headers['text_content_output_format'] = "objects_no_convert"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}/comments".format(incident_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        itemtype = "comments"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_comment(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            comment_id = self._handle_py_ver_compat_for_input_str(param['comment_id'])
            call = "/incidents/{}/comments/{}".format(incident_id, comment_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "comments"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_comment(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}/comments".format(incident_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        incidentcommentdto = getsv(param, 'incidentcommentdto')
        if len(incidentcommentdto) > 1:
            try:
                payload = json.loads(incidentcommentdto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. incidentcommentdto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. incidentcommentdto field is not valid json.".format(action_id))
        else:
            payload = dict()

        if 'text' not in payload:
            addifkey(param, 'text', payload, 'text')
        if 'parent_id' not in payload:
            addifkey(param, 'parent_id', payload, 'parent_id')

        if 'text' not in payload:
            self.save_progress("json payload does not have required 'text' key")
            return action_result.set_status(phantom.APP_ERROR, "json payload does not have required 'text' key")

        try:
            self.save_progress("POST {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.post(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "comments"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_comment(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            comment_id = self._handle_py_ver_compat_for_input_str(param['comment_id'])
            call = "/incidents/{}/comments/{}".format(incident_id, comment_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        payload = self.get_json_parameter(param, 'incidentcommentdto', action_result)
        if not isinstance(payload, dict):
            return action_result.set_status(phantom.APP_ERROR, "{} failed. incidentcommentdto field is not valid json.".format(action_id))
        if payload == phantom.APP_ERROR:
            return payload

        # self.debug_print("{} json is {}".format(action_id, payload))

        if 'text' not in payload:
            self.save_progress("json payload does not have required 'text' key, payload should be result of get comment")
            return action_result.set_status(
                phantom.APP_ERROR, "json payload does not have required 'text' key, payload should be result of get comment")

        try:
            self.save_progress("PUT {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.put(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "comments"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_tables(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}/table_data".format(incident_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        itemtype = "tables"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_table(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            table_id = self._handle_py_ver_compat_for_input_str(param['table_id'])
            call = "/incidents/{}/table_data/{}".format(incident_id, table_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "tables"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_table_row(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            table_id = self._handle_py_ver_compat_for_input_str(param['table_id'])
            call = "/incidents/{}/table_data/{}/row_data".format(incident_id, table_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        datatablerowdatadto = param.get('datatablerowdatadto', "")
        if len(datatablerowdatadto) > 1:
            try:
                payload = json.loads(datatablerowdatadto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. datatablerowdatadto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. datatablerowdatadto field is not valid json.".format(action_id))
        else:
            payload = dict()

        for col in ['1st', '2nd', '3rd', '4th', '5th']:
            key = param.get('{}_cell_property'.format(col), "")
            value = param.get('{}_cell_value'.format(col), "")
            if len(key) > 1 and len(value) > 1:
                payload['cells'][key] = value
            elif len(key) > 1 or len(value) > 1:
                self.save_progress("{} cell specification is not complete".format(col))
                continue

        try:
            self.save_progress("POST {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.post(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "table row"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_table_row(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            table_id = self._handle_py_ver_compat_for_input_str(param['table_id'])
            row_id = self._handle_py_ver_compat_for_input_str(param['row_id'])
            call = "/incidents/{}/table_data/{}/row_date/{}".format(incident_id, table_id, row_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        datatablerowdatadto = param.get('datatablerowdatadto', "")
        if len(datatablerowdatadto) > 1:
            try:
                payload = json.loads(datatablerowdatadto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. datatablerowdatadto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. datatablerowdatadto field is not valid json.".format(action_id))
        else:
            payload = dict()

        for col in ['1st', '2nd', '3rd', '4th', '5th']:
            key = param.get('{}_cell_property'.format(col), "")
            value = param.get('{}_cell_value'.format(col), "")
            if len(key) > 1 and len(value) > 1:
                payload['cells'][key] = value
            elif len(key) > 1 or len(value) > 1:
                self.save_progress("{} cell specification is not complete".format(col))
                continue

        try:
            self.save_progress("PUT {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.put(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "table row"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_table_row_with_key(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()
        # all parameters are required so all parameters are len() > 0

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        datatablerowdatadto = param.get('datatablerowdatadto', "")
        if len(datatablerowdatadto) > 1:
            try:
                payload = json.loads(datatablerowdatadto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. datatablerowdatadto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. datatablerowdatadto field is not valid json.".format(action_id))
        else:
            self.save_progress("{} failed. datatablerowdatadto field is empty string.".format(action_id))
            return action_result.set_status(phantom.APP_ERROR, "{} failed. datatablerowdatadto field is empty string.".format(action_id))

        # get table first
        try:
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            table_id = self._handle_py_ver_compat_for_input_str(param['table_id'])
            call = "/incidents/{}/table_data/{}".format(incident_id, table_id)
            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("GET successful")
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        def find_row(table, key, value):
            for row in table['rows']:
                if key in row['cells']:
                    if row['cells'][key] == value:
                        return row['id']
            return None

        key = self._handle_py_ver_compat_for_input_str(param['key'])
        value = self._handle_py_ver_compat_for_input_str(param['value'])
        rowid = find_row(retval, key, value)

        if rowid is None:
            self.save_progress("{} failed. Cannot match {}/{} key/value.".format(action_id, key, value))
            return action_result.set_status(phantom.APP_ERROR, "{} failed. Cannot match {}/{} key/value.".format(action_id, key, value))

        try:
            call = "/incidents/{}/table_data/{}/row_date/{}".format(incident_id, table_id, rowid)
            self.save_progress("PUT {}".format(call))
            self.save_progress("BODY {}".format(payload))
            retval = self._client.put(call, payload)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "table row"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_tasks(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            call = "/tasks"

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = retval
        itemtype = "tasks"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    # assumes connection already setup
    # return exception on error
    def _get_task(self, param):
        action_id = self.get_action_identifier()
        if param.get('handle_format_is_name'):
            self._client.headers['handle_format'] = "names"
        call = "/tasks/{}".format(param['task_id'])
        self.save_progress("GET {}".format(call))
        retval = self._client.get(call)
        self.save_progress("{} successful.".format(action_id))
        return retval

    def _handle_get_task(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            task_id = self._handle_py_ver_compat_for_input_str(param['task_id'])
            call = "/tasks/{}".format(task_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "tasks"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_task(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        taskdto = param.get('taskdto', "")
        if len(taskdto) > 1:
            try:
                payload = json.loads(taskdto)
                if not isinstance(payload, dict):
                    raise Exception
            except Exception:
                self.save_progress("{} failed. taskdto field is not valid json.".format(action_id))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. taskdto field is not valid json.".format(action_id))
        else:
            payload = dict()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            task_id = self._handle_py_ver_compat_for_input_str(param['task_id'])
            call = "/tasks/{}".format(task_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        # get task first
        # if param.get('get_task_and_copy_over', False):
        #    try:
        #        ticket = self._get_task(param)
        #    except Exception as e:
        #        return self.__handle_exceptions(e, action_result)
        #    newpayload = payload.copy()
        #    newpayload.update(taskdto)
        #    payload = newpayload

        try:
            def apply(arg):
                arg.update(payload)
                return arg

            self.save_progress("GET_PUT {}".format(call))
            self.save_progress("PAYLOAD {}".format(payload))
            retval = self._client.get_put(call, apply)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "tasks"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_close_task(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            self._client.connect(config['user'], config['password'])
            task_id = self._handle_py_ver_compat_for_input_str(param['task_id'])
            call = "/tasks/{}".format(task_id)
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        try:
            # self.save_progress("GET {}".format(call))
            # retval = self._client.get(call)
            # payload = retval
            # payload['status'] = "C"
            # self.save_progress("PUT {}".format(call))
            # self.save_progress("BODY {}".format(payload))
            def apply(arg):
                arg['status'] = "C"
                return arg

            retval = self._client.get_put(call, apply)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "tasks"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_attachments(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}/attachments".format(incident_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        itemtype = "attachments"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_attachment(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            attachment_id = self._handle_py_ver_compat_for_input_str(param['attachment_id'])
            call = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)

            self.save_progress("GET {}".format(call))
            retval = self._client.get(call)
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "attachments"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_attachment(self, param):
        action_id = self.get_action_identifier()
        self.save_progress("In action handler for: {0}".format(action_id))
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        try:
            self._client = co3.SimpleClient(org_name=config['org_id'], base_url=config['base_url'], verify=config['verify'])
            if param.get('handle_format_is_name'):
                self._client.headers['handle_format'] = "names"
            self._client.connect(config['user'], config['password'])
            incident_id = self._handle_py_ver_compat_for_input_str(param['incident_id'])
            call = "/incidents/{}/attachments".format(incident_id)

            container_id = self.get_container_id()
            vault_id = self._handle_py_ver_compat_for_input_str(param['vault_id'])
            vault_info = Vault.get_file_info(vault_id=vault_id, container_id=container_id)
            if len(vault_info) == 0:
                self.save_progress("{} failed. {}: vault_id not valid.".format(action_id, param['vault_id']))
                return action_result.set_status(phantom.APP_ERROR, "{} failed. {}: vault_id not valid.".format(action_id, param['vault_id']))
            path = vault_info[0]['path']
            name = vault_info[0]['name']

            retval = self._client.post_attachment(call, path, filename=name)
            # self.save_progress("POST_ATTACHMENT {} path={} name={}".format(call, path, name))
            self.save_progress("{} successful.".format(action_id))
        except Exception as e:
            return self.__handle_exceptions(e, action_result)

        retval = [ retval ]
        itemtype = "attachments"
        for r in retval:
            action_result.add_data(r)
        summary = action_result.update_summary({})
        summary['Number of {}'.format(itemtype)] = len(retval)
        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):

        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", action_id)

        if action_id == 'test_connectivity':
            ret_val = self._handle_test_connectivity(param)

        elif action_id == 'list_tickets':
            ret_val = self._handle_list_tickets(param)

        elif action_id == 'get_ticket':
            ret_val = self._handle_get_ticket(param)

        elif action_id == 'create_ticket':
            ret_val = self._handle_create_ticket(param)

        elif action_id == 'update_ticket':
            ret_val = self._handle_update_ticket(param)

        elif action_id == 'search_tickets':
            ret_val = self._handle_search_tickets(param)

        elif action_id == 'list_artifacts':
            ret_val = self._handle_list_artifacts(param)

        elif action_id == 'get_artifact':
            ret_val = self._handle_get_artifact(param)

        elif action_id == 'create_artifact':
            ret_val = self._handle_create_artifact(param)

        elif action_id == 'update_artifact':
            ret_val = self._handle_update_artifact(param)

        elif action_id == 'list_comments':
            ret_val = self._handle_list_comments(param)

        elif action_id == 'get_comment':
            ret_val = self._handle_get_comment(param)

        elif action_id == 'create_comment':
            ret_val = self._handle_create_comment(param)

        elif action_id == 'update_comment':
            ret_val = self._handle_update_comment(param)

        elif action_id == 'list_tables':
            ret_val = self._handle_list_tables(param)

        elif action_id == 'get_table':
            ret_val = self._handle_get_table(param)

        elif action_id == 'add_table_row':
            ret_val = self._handle_add_table_row(param)

        elif action_id == 'update_table_row':
            ret_val = self._handle_update_table_row(param)

        elif action_id == "update_table_row_with_key":
            ret_val = self._handle_update_table_row_with_key(param)

        elif action_id == 'list_tasks':
            ret_val = self._handle_list_tasks(param)

        elif action_id == 'get_task':
            ret_val = self._handle_get_task(param)

        elif action_id == 'update_task':
            ret_val = self._handle_update_task(param)

        elif action_id == 'close_task':
            ret_val = self._handle_close_task(param)

        elif action_id == 'list_attachments':
            ret_val = self._handle_list_attachments(param)

        elif action_id == 'get_attachment':
            ret_val = self._handle_get_attachment(param)

        elif action_id == 'add_attachment':
            ret_val = self._handle_add_attachment(param)

        return ret_val

    def initialize(self):

        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()

        """
        # get the asset config
        config = self.get_config()

        # Access values in asset config by the name

        # Required values can be accessed directly
        required_config_name = config['required_config_name']

        # Optional values should use the .get() function
        optional_config_name = config.get('optional_config_name')
        """

        return phantom.APP_SUCCESS

    def finalize(self):

        # Save the state, this data is saved accross actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS


if __name__ == '__main__':

    # import pudb
    # pudb.set_trace()

    if (len(sys.argv) < 2):
        print("No test json specified as input")
        sys.exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = ResilientConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    sys.exit(0)
