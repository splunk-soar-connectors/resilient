[comment]: # "Auto-generated SOAR connector documentation"
# Resilient

Publisher: Splunk Community  
Connector Version: 1\.1\.0  
Product Vendor: Resilient  
Product Name: IBM Resilient  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.2\.0  

Resilient Ticket System

[comment]: # " File: README.md"
[comment]: # "Copyright (c) 2022-2024 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
## Port Information

The app uses HTTP/ HTTPS protocol for communicating with the Exabeam server. Below are the default
ports used by Splunk SOAR.

|         Service Name | Transport Protocol | Port |
|----------------------|--------------------|------|
|         http         | tcp                | 80   |
|         https        | tcp                | 443  |


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a IBM Resilient asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | Base URL
**org\_id** |  required  | string | Organization Name
**user** |  required  | string | Service Account
**password** |  required  | password | Service Account Password
**verify** |  optional  | boolean | Verify SSL certificates\. You may need to set REQUESTS\_CA\_BUNDLE to the pem file containing your local CA root certificates

### Supported Actions  
[test connectivity](#action-test-connectivity) - Test connectivity  
[list tickets](#action-list-tickets) - List all incidents  
[get ticket](#action-get-ticket) - Get incident details by id  
[create ticket](#action-create-ticket) - Create new incident  
[update ticket](#action-update-ticket) - Update existing incident\. This action downloads the incident and copies the provided JSON onto the download data, overwriting any existing data elements  
[search tickets](#action-search-tickets) - Submit search query for incidents  
[list artifacts](#action-list-artifacts) - List all artifacts for incident  
[get artifact](#action-get-artifact) - Get artifact details by incident and artifact id  
[create artifact](#action-create-artifact) - Create new artifact  
[update artifact](#action-update-artifact) - Update existing artifact  
[list comments](#action-list-comments) - List all comment for incident  
[get comment](#action-get-comment) - Get comment details by incident and comment id  
[create comment](#action-create-comment) - Create new comment  
[update comment](#action-update-comment) - Update existing comment  
[list tables](#action-list-tables) - List tables  
[get table](#action-get-table) - Get table  
[add table row](#action-add-table-row) - Add table row  
[update table row](#action-update-table-row) - Update table row  
[update table row with key](#action-update-table-row-with-key) - Update table row with key  
[list tasks](#action-list-tasks) - List tasks for user \(defined in asset configuration\)  
[get task](#action-get-task) - Get task details  
[update task](#action-update-task) - Update task\. This action downloads the task and copy the provided json onto the download data, overwriting any existing data elements  
[close task](#action-close-task) - Close task  
[list attachments](#action-list-attachments) - List attachments for incident  
[get attachment](#action-get-attachment) - Get attachment details from incident  
[add attachment](#action-add-attachment) - Add attachment to incident  

## action: 'test connectivity'
Test connectivity

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list tickets'
List all incidents

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**want\_closed** |  optional  | Also returns closed incidents\. Default is true | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.want\_closed | boolean | 
action\_result\.data\.\*\.addr | string | 
action\_result\.data\.\*\.admin\_id | string | 
action\_result\.data\.\*\.assessment | string | 
action\_result\.data\.\*\.city | string | 
action\_result\.data\.\*\.confirmed | boolean | 
action\_result\.data\.\*\.country | string | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.cell | string | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.phone | string | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.crimestatus\_id | numeric | 
action\_result\.data\.\*\.data\_compromised | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.discovered\_date | numeric | 
action\_result\.data\.\*\.draft | boolean | 
action\_result\.data\.\*\.due\_date | string | 
action\_result\.data\.\*\.employee\_involved | string | 
action\_result\.data\.\*\.end\_date | string | 
action\_result\.data\.\*\.exposure | numeric | 
action\_result\.data\.\*\.exposure\_dept\_id | string | 
action\_result\.data\.\*\.exposure\_individual\_name | string | 
action\_result\.data\.\*\.exposure\_type\_id | numeric | 
action\_result\.data\.\*\.exposure\_vendor\_id | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_subsequent\_notification | string | 
action\_result\.data\.\*\.hard\_liability | numeric | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_last\_modified\_date | numeric | 
action\_result\.data\.\*\.inc\_start | string | 
action\_result\.data\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.incident\_type\_ids | numeric | 
action\_result\.data\.\*\.is\_scenario | boolean | 
action\_result\.data\.\*\.jurisdiction\_name | string | 
action\_result\.data\.\*\.jurisdiction\_reg\_id | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.negative\_pr\_likely | string | 
action\_result\.data\.\*\.nist\_attack\_vectors | numeric | 
action\_result\.data\.\*\.org\_handle | numeric | 
action\_result\.data\.\*\.org\_id | numeric | 
action\_result\.data\.\*\.owner\_id | numeric | 
action\_result\.data\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.perms\.change\_workspace | boolean | 
action\_result\.data\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.perms\.create\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.create\_milestones | boolean | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.perms\.list\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.list\_milestones | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.pii\.alberta\_health\_risk\_assessment | string | 
action\_result\.data\.\*\.pii\.assessment | string | 
action\_result\.data\.\*\.pii\.data\_compromised | string | 
action\_result\.data\.\*\.pii\.data\_contained | string | 
action\_result\.data\.\*\.pii\.data\_encrypted | string | 
action\_result\.data\.\*\.pii\.data\_format | string | 
action\_result\.data\.\*\.pii\.determined\_date | numeric | 
action\_result\.data\.\*\.pii\.exposure | numeric | 
action\_result\.data\.\*\.pii\.gdpr\_harm\_risk | string | 
action\_result\.data\.\*\.pii\.harmstatus\_id | numeric | 
action\_result\.data\.\*\.pii\.impact\_likely | string | 
action\_result\.data\.\*\.pii\.ny\_impact\_likely | string | 
action\_result\.data\.\*\.plan\_status | string | 
action\_result\.data\.\*\.reporter | string | 
action\_result\.data\.\*\.resolution\_id | string | 
action\_result\.data\.\*\.resolution\_summary | string | 
action\_result\.data\.\*\.severity\_code | string | 
action\_result\.data\.\*\.start\_date | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.data\.\*\.workspace | numeric | 
action\_result\.data\.\*\.zip | string | 
action\_result\.summary\.Number of incidents | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get ticket'
Get incident details by id

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_id** |  required  | ID of incident to retrieve | string |  `ibm resilient ticketid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.addr | string | 
action\_result\.data\.\*\.admin\_id | string | 
action\_result\.data\.\*\.artifacts | string | 
action\_result\.data\.\*\.assessment | string | 
action\_result\.data\.\*\.city | string | 
action\_result\.data\.\*\.cm\.total | numeric | 
action\_result\.data\.\*\.comments | string | 
action\_result\.data\.\*\.confirmed | boolean | 
action\_result\.data\.\*\.country | string | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.cell | string | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.phone | string | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.crimestatus\_id | numeric | 
action\_result\.data\.\*\.data\_compromised | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.discovered\_date | numeric | 
action\_result\.data\.\*\.draft | boolean | 
action\_result\.data\.\*\.due\_date | string | 
action\_result\.data\.\*\.employee\_involved | string | 
action\_result\.data\.\*\.end\_date | string | 
action\_result\.data\.\*\.exposure | numeric | 
action\_result\.data\.\*\.exposure\_dept\_id | string | 
action\_result\.data\.\*\.exposure\_individual\_name | string | 
action\_result\.data\.\*\.exposure\_type\_id | numeric | 
action\_result\.data\.\*\.exposure\_vendor\_id | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_subsequent\_notification | string | 
action\_result\.data\.\*\.hard\_liability | numeric | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused\_comment | string | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_last\_modified\_date | numeric | 
action\_result\.data\.\*\.inc\_start | string | 
action\_result\.data\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.is\_scenario | boolean | 
action\_result\.data\.\*\.jurisdiction\_name | string | 
action\_result\.data\.\*\.jurisdiction\_reg\_id | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.negative\_pr\_likely | string | 
action\_result\.data\.\*\.org\_handle | numeric | 
action\_result\.data\.\*\.org\_id | numeric | 
action\_result\.data\.\*\.owner\_id | numeric | 
action\_result\.data\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.perms\.change\_workspace | boolean | 
action\_result\.data\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.perms\.create\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.create\_milestones | boolean | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.perms\.list\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.list\_milestones | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.pii\.alberta\_health\_risk\_assessment | string | 
action\_result\.data\.\*\.pii\.assessment | string | 
action\_result\.data\.\*\.pii\.data\_compromised | string | 
action\_result\.data\.\*\.pii\.data\_contained | string | 
action\_result\.data\.\*\.pii\.data\_encrypted | string | 
action\_result\.data\.\*\.pii\.data\_format | string | 
action\_result\.data\.\*\.pii\.determined\_date | numeric | 
action\_result\.data\.\*\.pii\.exposure | numeric | 
action\_result\.data\.\*\.pii\.gdpr\_harm\_risk | string | 
action\_result\.data\.\*\.pii\.harmstatus\_id | numeric | 
action\_result\.data\.\*\.pii\.impact\_likely | string | 
action\_result\.data\.\*\.pii\.ny\_impact\_likely | string | 
action\_result\.data\.\*\.plan\_status | string | 
action\_result\.data\.\*\.reporter | string | 
action\_result\.data\.\*\.resolution\_id | string | 
action\_result\.data\.\*\.resolution\_summary | string | 
action\_result\.data\.\*\.severity\_code | string | 
action\_result\.data\.\*\.start\_date | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.tasks | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.data\.\*\.workspace | numeric | 
action\_result\.data\.\*\.zip | string | 
action\_result\.summary\.Number of incidents | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'create ticket'
Create new incident

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_name** |  required  | Name of incident | string | 
**incident\_description** |  required  | Short description of incident | string | 
**fullincidentdatadto** |  optional  | Incident data as JSON String, format is FullIncidentDataDTO data type from API | string | 
**want\_full\_data** |  optional  | Returns full incident instead of summary\. Default is true | boolean | 
**want\_tasks** |  optional  | Also returns associated tasks\. Default is false | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.fullincidentdatadto | string | 
action\_result\.parameter\.incident\_description | string | 
action\_result\.parameter\.incident\_name | string | 
action\_result\.parameter\.want\_full\_data | boolean | 
action\_result\.parameter\.want\_tasks | boolean | 
action\_result\.data\.\*\.addr | string | 
action\_result\.data\.\*\.admin\_id | string | 
action\_result\.data\.\*\.artifacts | string | 
action\_result\.data\.\*\.assessment | string | 
action\_result\.data\.\*\.city | string | 
action\_result\.data\.\*\.cm\.total | numeric | 
action\_result\.data\.\*\.comments | string | 
action\_result\.data\.\*\.confirmed | boolean | 
action\_result\.data\.\*\.country | string | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.cell | string | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.phone | string | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.crimestatus\_id | numeric | 
action\_result\.data\.\*\.data\_compromised | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.discovered\_date | numeric | 
action\_result\.data\.\*\.draft | boolean | 
action\_result\.data\.\*\.due\_date | string | 
action\_result\.data\.\*\.employee\_involved | string | 
action\_result\.data\.\*\.end\_date | string | 
action\_result\.data\.\*\.exposure | numeric | 
action\_result\.data\.\*\.exposure\_dept\_id | string | 
action\_result\.data\.\*\.exposure\_individual\_name | string | 
action\_result\.data\.\*\.exposure\_type\_id | numeric | 
action\_result\.data\.\*\.exposure\_vendor\_id | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_subsequent\_notification | string | 
action\_result\.data\.\*\.hard\_liability | numeric | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused\_comment | string | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_last\_modified\_date | string | 
action\_result\.data\.\*\.inc\_start | string | 
action\_result\.data\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.is\_scenario | boolean | 
action\_result\.data\.\*\.jurisdiction\_name | string | 
action\_result\.data\.\*\.jurisdiction\_reg\_id | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.negative\_pr\_likely | string | 
action\_result\.data\.\*\.org\_handle | numeric | 
action\_result\.data\.\*\.org\_id | numeric | 
action\_result\.data\.\*\.owner\_id | numeric | 
action\_result\.data\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.perms\.change\_workspace | boolean | 
action\_result\.data\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.perms\.create\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.create\_milestones | boolean | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.perms\.list\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.list\_milestones | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.pii\.alberta\_health\_risk\_assessment | string | 
action\_result\.data\.\*\.pii\.assessment | string | 
action\_result\.data\.\*\.pii\.data\_compromised | string | 
action\_result\.data\.\*\.pii\.data\_contained | string | 
action\_result\.data\.\*\.pii\.data\_encrypted | string | 
action\_result\.data\.\*\.pii\.data\_format | string | 
action\_result\.data\.\*\.pii\.determined\_date | numeric | 
action\_result\.data\.\*\.pii\.exposure | numeric | 
action\_result\.data\.\*\.pii\.gdpr\_harm\_risk | string | 
action\_result\.data\.\*\.pii\.harmstatus\_id | numeric | 
action\_result\.data\.\*\.pii\.impact\_likely | string | 
action\_result\.data\.\*\.pii\.ny\_impact\_likely | string | 
action\_result\.data\.\*\.plan\_status | string | 
action\_result\.data\.\*\.reporter | string | 
action\_result\.data\.\*\.resolution\_id | string | 
action\_result\.data\.\*\.resolution\_summary | string | 
action\_result\.data\.\*\.severity\_code | string | 
action\_result\.data\.\*\.start\_date | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.tasks\.\*\.active | boolean | 
action\_result\.data\.\*\.tasks\.\*\.at\_id | string | 
action\_result\.data\.\*\.tasks\.\*\.attachments\_count | string | 
action\_result\.data\.\*\.tasks\.\*\.auto\_deactivate | boolean | 
action\_result\.data\.\*\.tasks\.\*\.cat\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.category\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.closed\_date | string | 
action\_result\.data\.\*\.tasks\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.tasks\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.tasks\.\*\.custom | boolean | 
action\_result\.data\.\*\.tasks\.\*\.description | string | 
action\_result\.data\.\*\.tasks\.\*\.due\_date | string | 
action\_result\.data\.\*\.tasks\.\*\.form | string | 
action\_result\.data\.\*\.tasks\.\*\.frozen | boolean | 
action\_result\.data\.\*\.tasks\.\*\.id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.inc\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.inc\_owner\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.tasks\.\*\.init\_date | numeric | 
action\_result\.data\.\*\.tasks\.\*\.instr\_text | string | 
action\_result\.data\.\*\.tasks\.\*\.instructions | string | 
action\_result\.data\.\*\.tasks\.\*\.members | string | 
action\_result\.data\.\*\.tasks\.\*\.name | string | 
action\_result\.data\.\*\.tasks\.\*\.notes\_count | string | 
action\_result\.data\.\*\.tasks\.\*\.owner\_fname | string | 
action\_result\.data\.\*\.tasks\.\*\.owner\_id | string | 
action\_result\.data\.\*\.tasks\.\*\.owner\_lname | string | 
action\_result\.data\.\*\.tasks\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.tasks\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.tasks\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.private | string | 
action\_result\.data\.\*\.tasks\.\*\.regs\.88 | string | 
action\_result\.data\.\*\.tasks\.\*\.required | boolean | 
action\_result\.data\.\*\.tasks\.\*\.src\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.status | string | 
action\_result\.data\.\*\.tasks\.\*\.task\_layout | string | 
action\_result\.data\.\*\.tasks\.\*\.user\_notes | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.data\.\*\.workspace | numeric | 
action\_result\.data\.\*\.zip | string | 
action\_result\.summary\.Number of incidents | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update ticket'
Update existing incident\. This action downloads the incident and copies the provided JSON onto the download data, overwriting any existing data elements

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_id** |  required  | ID of incident to update | string |  `ibm resilient ticketid` 
**fullincidentdatadto** |  required  | Incident data as JSON String, the format is FullIncidentDataDTO data type from API\. This data should first be retrieved from Resilient and then modified with the desired changes | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.fullincidentdatadto | string | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.addr | string | 
action\_result\.data\.\*\.admin\_id | string | 
action\_result\.data\.\*\.artifacts | string | 
action\_result\.data\.\*\.assessment | string | 
action\_result\.data\.\*\.city | string | 
action\_result\.data\.\*\.cm\.total | numeric | 
action\_result\.data\.\*\.comments | string | 
action\_result\.data\.\*\.confirmed | boolean | 
action\_result\.data\.\*\.country | string | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.cell | string | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.phone | string | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.crimestatus\_id | numeric | 
action\_result\.data\.\*\.data\_compromised | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.discovered\_date | numeric | 
action\_result\.data\.\*\.draft | boolean | 
action\_result\.data\.\*\.due\_date | string | 
action\_result\.data\.\*\.employee\_involved | string | 
action\_result\.data\.\*\.end\_date | string | 
action\_result\.data\.\*\.exposure | numeric | 
action\_result\.data\.\*\.exposure\_dept\_id | string | 
action\_result\.data\.\*\.exposure\_individual\_name | string | 
action\_result\.data\.\*\.exposure\_type\_id | numeric | 
action\_result\.data\.\*\.exposure\_vendor\_id | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_subsequent\_notification | string | 
action\_result\.data\.\*\.hard\_liability | numeric | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused\_comment | string | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_last\_modified\_date | numeric | 
action\_result\.data\.\*\.inc\_start | string | 
action\_result\.data\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.is\_scenario | boolean | 
action\_result\.data\.\*\.jurisdiction\_name | string | 
action\_result\.data\.\*\.jurisdiction\_reg\_id | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.negative\_pr\_likely | string | 
action\_result\.data\.\*\.org\_handle | numeric | 
action\_result\.data\.\*\.org\_id | numeric | 
action\_result\.data\.\*\.owner\_id | numeric | 
action\_result\.data\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.perms\.change\_workspace | boolean | 
action\_result\.data\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.perms\.create\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.create\_milestones | boolean | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.perms\.list\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.list\_milestones | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.pii\.alberta\_health\_risk\_assessment | string | 
action\_result\.data\.\*\.pii\.assessment | string | 
action\_result\.data\.\*\.pii\.data\_compromised | string | 
action\_result\.data\.\*\.pii\.data\_contained | string | 
action\_result\.data\.\*\.pii\.data\_encrypted | string | 
action\_result\.data\.\*\.pii\.data\_format | string | 
action\_result\.data\.\*\.pii\.determined\_date | numeric | 
action\_result\.data\.\*\.pii\.exposure | numeric | 
action\_result\.data\.\*\.pii\.gdpr\_harm\_risk | string | 
action\_result\.data\.\*\.pii\.harmstatus\_id | numeric | 
action\_result\.data\.\*\.pii\.impact\_likely | string | 
action\_result\.data\.\*\.pii\.ny\_impact\_likely | string | 
action\_result\.data\.\*\.plan\_status | string | 
action\_result\.data\.\*\.reporter | string | 
action\_result\.data\.\*\.resolution\_id | string | 
action\_result\.data\.\*\.resolution\_summary | string | 
action\_result\.data\.\*\.severity\_code | string | 
action\_result\.data\.\*\.start\_date | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.tasks | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.data\.\*\.workspace | numeric | 
action\_result\.data\.\*\.zip | string | 
action\_result\.summary\.Number of incidents | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'search tickets'
Submit search query for incidents

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**querydto** |  optional  | Query data as JSON String, the format is QueryDTO data type from API | string | 
**add\_condition\_all\_active\_tickets** |  optional  | Filters for active tickets | boolean | 
**add\_condition\_closed\_in\_last\_24\_hours** |  optional  | Filters for tickets closed in last 24 hours | boolean | 
**add\_condition\_created\_in\_last\_24\_hours** |  optional  | Filters for tickets created in last 24 hours | boolean | 
**1st\_condition\_field\_name** |  optional  | The field name in the condition | string | 
**1st\_condition\_field\_value** |  optional  | The value used for comparison | string | 
**1st\_condition\_value\_is\_datetime** |  optional  | The value is a datetime; convert to Resilient internal representation | boolean | 
**1st\_condition\_comparison\_method** |  optional  | The method used to compare the value, \[equals, gt, lte\]\. Look up MethodName datatype in the API | string | 
**2nd\_condition\_field\_name** |  optional  | The field name in the condition | string | 
**2nd\_condition\_field\_value** |  optional  | The value used for comparison | string | 
**2nd\_condition\_value\_is\_datetime** |  optional  | The value is a datetime | boolean | 
**2nd\_condition\_comparison\_method** |  optional  | The method used to compare the value | string | 
**3rd\_condition\_field\_name** |  optional  | The field name in the condition | string | 
**3rd\_condition\_field\_value** |  optional  | The value used for comparison | string | 
**3rd\_condition\_value\_is\_datetime** |  optional  | The value is a datetime | boolean | 
**3rd\_condition\_comparison\_method** |  optional  | The method used to compare the value | string | 
**4th\_condition\_field\_name** |  optional  | The field name in the condition | string | 
**4th\_condition\_field\_value** |  optional  | The value used for comparison | string | 
**4th\_condition\_value\_is\_datetime** |  optional  | The value is a datetime | boolean | 
**4th\_condition\_comparison\_method** |  optional  | The method used to compare the value | string | 
**5th\_condition\_field\_name** |  optional  | The field name in the condition | string | 
**5th\_condition\_field\_value** |  optional  | The value used for comparison | string | 
**5th\_condition\_value\_is\_datetime** |  optional  | The value is a datetime | boolean | 
**5th\_condition\_comparison\_method** |  optional  | The method used to compare the value | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.1st\_condition\_comparison\_method | string | 
action\_result\.parameter\.1st\_condition\_field\_name | string | 
action\_result\.parameter\.1st\_condition\_field\_value | string | 
action\_result\.parameter\.1st\_condition\_value\_is\_datetime | boolean | 
action\_result\.parameter\.2nd\_condition\_comparison\_method | string | 
action\_result\.parameter\.2nd\_condition\_field\_name | string | 
action\_result\.parameter\.2nd\_condition\_field\_value | string | 
action\_result\.parameter\.2nd\_condition\_value\_is\_datetime | boolean | 
action\_result\.parameter\.3rd\_condition\_comparison\_method | string | 
action\_result\.parameter\.3rd\_condition\_field\_name | string | 
action\_result\.parameter\.3rd\_condition\_field\_value | string | 
action\_result\.parameter\.3rd\_condition\_value\_is\_datetime | boolean | 
action\_result\.parameter\.4th\_condition\_comparison\_method | string | 
action\_result\.parameter\.4th\_condition\_field\_name | string | 
action\_result\.parameter\.4th\_condition\_field\_value | string | 
action\_result\.parameter\.4th\_condition\_value\_is\_datetime | boolean | 
action\_result\.parameter\.5th\_condition\_comparison\_method | string | 
action\_result\.parameter\.5th\_condition\_field\_name | string | 
action\_result\.parameter\.5th\_condition\_field\_value | string | 
action\_result\.parameter\.5th\_condition\_value\_is\_datetime | boolean | 
action\_result\.parameter\.add\_condition\_all\_active\_tickets | boolean | 
action\_result\.parameter\.add\_condition\_closed\_in\_last\_24\_hours | boolean | 
action\_result\.parameter\.add\_condition\_created\_in\_last\_24\_hours | boolean | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.querydto | string | 
action\_result\.data\.\*\.addr | string | 
action\_result\.data\.\*\.admin\_id | string | 
action\_result\.data\.\*\.artifacts | string | 
action\_result\.data\.\*\.assessment | string | 
action\_result\.data\.\*\.city | string | 
action\_result\.data\.\*\.cm\.total | numeric | 
action\_result\.data\.\*\.cm\.unassigneds\.\*\.count | numeric | 
action\_result\.data\.\*\.cm\.unassigneds\.\*\.geo | numeric | 
action\_result\.data\.\*\.comments | string | 
action\_result\.data\.\*\.confirmed | boolean | 
action\_result\.data\.\*\.country | string | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.crimestatus\_id | numeric | 
action\_result\.data\.\*\.data\_compromised | boolean | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.discovered\_date | numeric | 
action\_result\.data\.\*\.draft | boolean | 
action\_result\.data\.\*\.due\_date | string | 
action\_result\.data\.\*\.employee\_involved | string | 
action\_result\.data\.\*\.end\_date | string | 
action\_result\.data\.\*\.exposure | numeric | 
action\_result\.data\.\*\.exposure\_dept\_id | string | 
action\_result\.data\.\*\.exposure\_individual\_name | string | 
action\_result\.data\.\*\.exposure\_type\_id | numeric | 
action\_result\.data\.\*\.exposure\_vendor\_id | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_breach\_type\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_consequences\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_final\_assessment\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_identification\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_personal\_data\_comment | string | 
action\_result\.data\.\*\.gdpr\.gdpr\_subsequent\_notification | string | 
action\_result\.data\.\*\.hard\_liability | numeric | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_acquired\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_additional\_misuse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_adverse\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_breach\_comment | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused | string | 
action\_result\.data\.\*\.hipaa\.hipaa\_misused\_comment | string | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_last\_modified\_date | numeric | 
action\_result\.data\.\*\.inc\_start | string | 
action\_result\.data\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.incident\_type\_ids | numeric | 
action\_result\.data\.\*\.is\_scenario | boolean | 
action\_result\.data\.\*\.jurisdiction\_name | string | 
action\_result\.data\.\*\.jurisdiction\_reg\_id | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.negative\_pr\_likely | string | 
action\_result\.data\.\*\.nist\_attack\_vectors | numeric | 
action\_result\.data\.\*\.org\_handle | numeric | 
action\_result\.data\.\*\.org\_id | numeric | 
action\_result\.data\.\*\.owner\_id | numeric | 
action\_result\.data\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.perms\.change\_workspace | boolean | 
action\_result\.data\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.perms\.create\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.create\_milestones | boolean | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.perms\.list\_artifacts | boolean | 
action\_result\.data\.\*\.perms\.list\_milestones | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.pii\.alberta\_health\_risk\_assessment | string | 
action\_result\.data\.\*\.pii\.assessment | string | 
action\_result\.data\.\*\.pii\.data\_compromised | boolean | 
action\_result\.data\.\*\.pii\.data\_contained | string | 
action\_result\.data\.\*\.pii\.data\_encrypted | string | 
action\_result\.data\.\*\.pii\.data\_format | numeric | 
action\_result\.data\.\*\.pii\.determined\_date | numeric | 
action\_result\.data\.\*\.pii\.exposure | numeric | 
action\_result\.data\.\*\.pii\.gdpr\_harm\_risk | string | 
action\_result\.data\.\*\.pii\.harmstatus\_id | numeric | 
action\_result\.data\.\*\.pii\.impact\_likely | string | 
action\_result\.data\.\*\.pii\.ny\_impact\_likely | string | 
action\_result\.data\.\*\.plan\_status | string | 
action\_result\.data\.\*\.regulators\.ids | numeric | 
action\_result\.data\.\*\.reporter | string | 
action\_result\.data\.\*\.resolution\_id | string | 
action\_result\.data\.\*\.resolution\_summary | string | 
action\_result\.data\.\*\.severity\_code | numeric | 
action\_result\.data\.\*\.severity\_code\.name | string | 
action\_result\.data\.\*\.start\_date | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.tasks | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.data\.\*\.workspace | numeric | 
action\_result\.data\.\*\.zip | string | 
action\_result\.summary\.Number of incidents | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list artifacts'
List all artifacts for incident

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.attachment | string | 
action\_result\.data\.\*\.created | numeric | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.hash | string |  `sha256` 
action\_result\.data\.\*\.id | numeric |  `artifactid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.ip\.destination | string | 
action\_result\.data\.\*\.ip\.source | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.properties | string | 
action\_result\.data\.\*\.relating | string | 
action\_result\.data\.\*\.type | numeric | 
action\_result\.data\.\*\.value | string |  `url` 
action\_result\.summary\.Number of artifacts | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get artifact'
Get artifact details by incident and artifact id

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**artifact\_id** |  required  | ID of artifact to retrieve | string |  `artifactid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.artifact\_id | string | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.attachment | string | 
action\_result\.data\.\*\.created | numeric | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.hash | string |  `sha256` 
action\_result\.data\.\*\.id | numeric |  `artifactid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.ip\.destination | string | 
action\_result\.data\.\*\.ip\.source | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.properties | string | 
action\_result\.data\.\*\.relating | string | 
action\_result\.data\.\*\.type | numeric | 
action\_result\.data\.\*\.value | string |  `url` 
action\_result\.summary\.Number of artifacts | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'create artifact'
Create new artifact

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**incidentartifactdto** |  optional  | Artifact data as JSON String, format is IncidentArtifactDTO data type from API | string | 
**type** |  optional  | Type of artifact | string | 
**value** |  optional  | Artifact value field | string | 
**description** |  optional  | Short description of artifact | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.description | string | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.parameter\.incidentartifactdto | string | 
action\_result\.parameter\.type | string | 
action\_result\.parameter\.value | string |  `url` 
action\_result\.data\.\*\.attachment | string | 
action\_result\.data\.\*\.created | numeric | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.hash | string |  `sha256` 
action\_result\.data\.\*\.id | numeric |  `artifactid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.ip\.destination | string | 
action\_result\.data\.\*\.ip\.source | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.pending\_sources | numeric | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.properties | string | 
action\_result\.data\.\*\.relating | string | 
action\_result\.data\.\*\.type | numeric | 
action\_result\.data\.\*\.value | string |  `url` 
action\_result\.summary\.Number of artifacts | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update artifact'
Update existing artifact

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**artifact\_id** |  required  | ID of artifact to update | string |  `artifactid` 
**incidentartifactdto** |  required  | Artifact data as JSON String, format is IncidentArtifactDTO data type from API | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.artifact\_id | string | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.parameter\.incidentartifactdto | string | 
action\_result\.data\.\*\.attachment | string | 
action\_result\.data\.\*\.created | numeric | 
action\_result\.data\.\*\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.creator\.display\_name | string | 
action\_result\.data\.\*\.creator\.email | string |  `email` 
action\_result\.data\.\*\.creator\.fname | string | 
action\_result\.data\.\*\.creator\.id | numeric | 
action\_result\.data\.\*\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.creator\.lname | string | 
action\_result\.data\.\*\.creator\.locked | boolean | 
action\_result\.data\.\*\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.creator\.status | string | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.hash | string |  `sha256` 
action\_result\.data\.\*\.id | numeric |  `artifactid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.ip\.destination | string | 
action\_result\.data\.\*\.ip\.source | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.properties | string | 
action\_result\.data\.\*\.relating | string | 
action\_result\.data\.\*\.type | numeric | 
action\_result\.data\.\*\.value | string |  `url` 
action\_result\.summary\.Number of artifacts | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list comments'
List all comment for incident

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.comment\_perms\.delete | boolean | 
action\_result\.data\.\*\.comment\_perms\.update | boolean | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient commentid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.is\_deleted | boolean | 
action\_result\.data\.\*\.modify\_date | numeric | 
action\_result\.data\.\*\.modify\_principal\.display\_name | string | 
action\_result\.data\.\*\.modify\_principal\.id | numeric | 
action\_result\.data\.\*\.modify\_principal\.name | string |  `email` 
action\_result\.data\.\*\.modify\_principal\.type | string | 
action\_result\.data\.\*\.modify\_user\.first\_name | string | 
action\_result\.data\.\*\.modify\_user\.id | numeric | 
action\_result\.data\.\*\.modify\_user\.last\_name | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.task\_custom | string | 
action\_result\.data\.\*\.task\_id | string | 
action\_result\.data\.\*\.task\_members | string | 
action\_result\.data\.\*\.task\_name | string | 
action\_result\.data\.\*\.text | string | 
action\_result\.data\.\*\.text\.content | string | 
action\_result\.data\.\*\.text\.format | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.user\_fname | string | 
action\_result\.data\.\*\.user\_id | numeric | 
action\_result\.data\.\*\.user\_lname | string | 
action\_result\.data\.\*\.user\_name | string | 
action\_result\.summary\.Number of comments | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get comment'
Get comment details by incident and comment id

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**comment\_id** |  required  | ID of comment to retrieve | string |  `ibm resilient commentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.comment\_id | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.children\.\*\.comment\_perms\.delete | boolean | 
action\_result\.data\.\*\.children\.\*\.comment\_perms\.update | boolean | 
action\_result\.data\.\*\.children\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.children\.\*\.id | numeric | 
action\_result\.data\.\*\.children\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.children\.\*\.inc\_name | string | 
action\_result\.data\.\*\.children\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.children\.\*\.is\_deleted | boolean | 
action\_result\.data\.\*\.children\.\*\.modify\_date | numeric | 
action\_result\.data\.\*\.children\.\*\.modify\_principal\.display\_name | string | 
action\_result\.data\.\*\.children\.\*\.modify\_principal\.id | numeric | 
action\_result\.data\.\*\.children\.\*\.modify\_principal\.name | string |  `email` 
action\_result\.data\.\*\.children\.\*\.modify\_principal\.type | string | 
action\_result\.data\.\*\.children\.\*\.modify\_user\.first\_name | string | 
action\_result\.data\.\*\.children\.\*\.modify\_user\.id | numeric | 
action\_result\.data\.\*\.children\.\*\.modify\_user\.last\_name | string | 
action\_result\.data\.\*\.children\.\*\.parent\_id | numeric | 
action\_result\.data\.\*\.children\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.children\.\*\.task\_custom | string | 
action\_result\.data\.\*\.children\.\*\.task\_id | string | 
action\_result\.data\.\*\.children\.\*\.task\_members | string | 
action\_result\.data\.\*\.children\.\*\.task\_name | string | 
action\_result\.data\.\*\.children\.\*\.text | string | 
action\_result\.data\.\*\.children\.\*\.type | string | 
action\_result\.data\.\*\.children\.\*\.user\_fname | string | 
action\_result\.data\.\*\.children\.\*\.user\_id | numeric | 
action\_result\.data\.\*\.children\.\*\.user\_lname | string | 
action\_result\.data\.\*\.children\.\*\.user\_name | string | 
action\_result\.data\.\*\.comment\_perms\.delete | boolean | 
action\_result\.data\.\*\.comment\_perms\.update | boolean | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient commentid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.is\_deleted | boolean | 
action\_result\.data\.\*\.modify\_date | numeric | 
action\_result\.data\.\*\.modify\_principal\.display\_name | string | 
action\_result\.data\.\*\.modify\_principal\.id | numeric | 
action\_result\.data\.\*\.modify\_principal\.name | string |  `email` 
action\_result\.data\.\*\.modify\_principal\.type | string | 
action\_result\.data\.\*\.modify\_user\.first\_name | string | 
action\_result\.data\.\*\.modify\_user\.id | numeric | 
action\_result\.data\.\*\.modify\_user\.last\_name | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.task\_custom | string | 
action\_result\.data\.\*\.task\_id | string | 
action\_result\.data\.\*\.task\_members | string | 
action\_result\.data\.\*\.task\_name | string | 
action\_result\.data\.\*\.text | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.user\_fname | string | 
action\_result\.data\.\*\.user\_id | numeric | 
action\_result\.data\.\*\.user\_lname | string | 
action\_result\.data\.\*\.user\_name | string | 
action\_result\.summary\.Number of comments | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'create comment'
Create new comment

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**parent\_id** |  optional  | The ID of the initial comment if posting a reply | string |  `ibm resilient commentid` 
**text** |  optional  | Comment as text | string | 
**incidentcommentdto** |  optional  | Comment data as JSON String, format is IncidentCommentDTO data type from API | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.parameter\.incidentcommentdto | string | 
action\_result\.parameter\.parent\_id | string |  `ibm resilient commentid` 
action\_result\.parameter\.text | string | 
action\_result\.data\.\*\.comment\_perms\.delete | boolean | 
action\_result\.data\.\*\.comment\_perms\.update | boolean | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient commentid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.is\_deleted | boolean | 
action\_result\.data\.\*\.modify\_date | numeric | 
action\_result\.data\.\*\.modify\_principal\.display\_name | string | 
action\_result\.data\.\*\.modify\_principal\.id | numeric | 
action\_result\.data\.\*\.modify\_principal\.name | string |  `email` 
action\_result\.data\.\*\.modify\_principal\.type | string | 
action\_result\.data\.\*\.modify\_user\.first\_name | string | 
action\_result\.data\.\*\.modify\_user\.id | numeric | 
action\_result\.data\.\*\.modify\_user\.last\_name | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.task\_custom | string | 
action\_result\.data\.\*\.task\_id | string | 
action\_result\.data\.\*\.task\_members | string | 
action\_result\.data\.\*\.task\_name | string | 
action\_result\.data\.\*\.text | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.user\_fname | string | 
action\_result\.data\.\*\.user\_id | numeric | 
action\_result\.data\.\*\.user\_lname | string | 
action\_result\.data\.\*\.user\_name | string | 
action\_result\.summary\.Number of comments | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update comment'
Update existing comment

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**comment\_id** |  required  | ID of comment to retrieve | string |  `ibm resilient commentid` 
**incidentcommentdto** |  required  | Comment data as JSON String, format is IncidentCommentDTO data type from API | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.comment\_id | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.parameter\.incidentcommentdto | string | 
action\_result\.data\.\*\.comment\_perms\.delete | boolean | 
action\_result\.data\.\*\.comment\_perms\.update | boolean | 
action\_result\.data\.\*\.create\_date | numeric | 
action\_result\.data\.\*\.id | numeric |  `ibm resilient commentid` 
action\_result\.data\.\*\.inc\_id | numeric |  `ibm resilient ticketid` 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.is\_deleted | boolean | 
action\_result\.data\.\*\.modify\_date | numeric | 
action\_result\.data\.\*\.modify\_principal\.display\_name | string | 
action\_result\.data\.\*\.modify\_principal\.id | numeric | 
action\_result\.data\.\*\.modify\_principal\.name | string |  `email` 
action\_result\.data\.\*\.modify\_principal\.type | string | 
action\_result\.data\.\*\.modify\_user\.first\_name | string | 
action\_result\.data\.\*\.modify\_user\.id | numeric | 
action\_result\.data\.\*\.modify\_user\.last\_name | string | 
action\_result\.data\.\*\.parent\_id | string | 
action\_result\.data\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.task\_custom | string | 
action\_result\.data\.\*\.task\_id | string | 
action\_result\.data\.\*\.task\_members | string | 
action\_result\.data\.\*\.task\_name | string | 
action\_result\.data\.\*\.text | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.user\_fname | string | 
action\_result\.data\.\*\.user\_id | numeric | 
action\_result\.data\.\*\.user\_lname | string | 
action\_result\.data\.\*\.user\_name | string | 
action\_result\.summary\.Number of comments | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list tables'
List tables

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data | string | 
action\_result\.summary\.Number of tables | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get table'
Get table

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**table\_id** |  required  | ID of table | string |  `ibm resilient ticketid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string |  `ibm resilient ticketid` 
action\_result\.parameter\.table\_id | string |  `ibm resilient ticketid` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.perms\.update | boolean | 
action\_result\.data\.\*\.perms\.delete | boolean | 
action\_result\.data\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.rows\.\*\.type\_id | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.180\.row\_id | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.180\.id | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.180\.value | string | 
action\_result\.data\.\*\.rows\.\*\.cells\.181\.row\_id | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.181\.id | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.181\.value | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.179\.row\_id | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.179\.id | numeric | 
action\_result\.data\.\*\.rows\.\*\.cells\.179\.value | numeric | 
action\_result\.data\.\*\.rows\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.rows\.\*\.version | numeric | 
action\_result\.data\.\*\.rows\.\*\.table\_name | string | 
action\_result\.data\.\*\.rows\.\*\.inc\_name | string | 
action\_result\.data\.\*\.rows\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.rows\.\*\.id | numeric | 
action\_result\.data\.\*\.id | numeric | 
action\_result\.summary\.Number of tables | numeric |   

## action: 'add table row'
Add table row

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**table\_id** |  required  | ID of table | string |  `tableid` 
**datatablerowdatadto** |  required  | Table row as JSON String, format is DataTableRowDataDTO data type from API | string | 
**1st\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**1st\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**2nd\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**2nd\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**3rd\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**3rd\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**4th\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**4th\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**5th\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**5th\_condition\_cell\_value** |  optional  | The value of the cell | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.1st\_condition\_cell\_property | string | 
action\_result\.parameter\.1st\_condition\_cell\_value | string | 
action\_result\.parameter\.2nd\_condition\_cell\_property | string | 
action\_result\.parameter\.2nd\_condition\_cell\_value | string | 
action\_result\.parameter\.3rd\_condition\_cell\_property | string | 
action\_result\.parameter\.3rd\_condition\_cell\_value | string | 
action\_result\.parameter\.4th\_condition\_cell\_property | string | 
action\_result\.parameter\.4th\_condition\_cell\_value | string | 
action\_result\.parameter\.5th\_condition\_cell\_property | string | 
action\_result\.parameter\.5th\_condition\_cell\_value | string | 
action\_result\.parameter\.datatablerowdatadto | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.parameter\.table\_id | string | 
action\_result\.data\.\*\.cells\.179\.id | numeric | 
action\_result\.data\.\*\.cells\.179\.row\_id | numeric | 
action\_result\.data\.\*\.cells\.179\.value | string | 
action\_result\.data\.\*\.cells\.180\.id | numeric | 
action\_result\.data\.\*\.cells\.180\.row\_id | numeric | 
action\_result\.data\.\*\.cells\.180\.value | string | 
action\_result\.data\.\*\.cells\.181\.id | numeric | 
action\_result\.data\.\*\.cells\.181\.row\_id | numeric | 
action\_result\.data\.\*\.cells\.181\.value | numeric | 
action\_result\.data\.\*\.id | numeric | 
action\_result\.data\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.table\_name | string | 
action\_result\.data\.\*\.type\_id | numeric | 
action\_result\.data\.\*\.version | numeric | 
action\_result\.summary\.Number of table row | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update table row'
Update table row

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**table\_id** |  required  | ID of table | string |  `tableid` 
**row\_id** |  required  | ID of row in table | string |  `rowid` 
**datatablerowdatadto** |  required  | Table row as JSON String, format is DataTableRowDataDTO data type from API | string | 
**1st\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**1st\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**2nd\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**2nd\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**3rd\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**3rd\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**4th\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**4th\_condition\_cell\_value** |  optional  | The value of the cell | string | 
**5th\_condition\_cell\_property** |  optional  | The property name of the cell | string | 
**5th\_condition\_cell\_value** |  optional  | The value of the cell | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.1st\_condition\_cell\_property | string | 
action\_result\.parameter\.1st\_condition\_cell\_value | string | 
action\_result\.parameter\.2nd\_condition\_cell\_property | string | 
action\_result\.parameter\.2nd\_condition\_cell\_value | string | 
action\_result\.parameter\.3rd\_condition\_cell\_property | string | 
action\_result\.parameter\.3rd\_condition\_cell\_value | string | 
action\_result\.parameter\.4th\_condition\_cell\_property | string | 
action\_result\.parameter\.4th\_condition\_cell\_value | string | 
action\_result\.parameter\.5th\_condition\_cell\_property | string | 
action\_result\.parameter\.5th\_condition\_cell\_value | string | 
action\_result\.parameter\.datatablerowdatadto | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string |  `ibm resilient ticketid` 
action\_result\.parameter\.row\_id | string |  `rowid` 
action\_result\.parameter\.table\_id | string |  `tableid` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update table row with key'
Update table row with key

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**table\_id** |  required  | ID of table | string |  `tableid` 
**key** |  required  | Property name in row to find | string |  `ibm resilient keyid` 
**value** |  required  | Property value in row to find | string | 
**datatablerowdatadto** |  required  | Table row as JSON String, format is DataTableRowDataDTO data type from API | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.datatablerowdatadto | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string |  `ibm resilient ticketid` 
action\_result\.parameter\.key | string |  `ibm resilient keyid` 
action\_result\.parameter\.table\_id | string |  `tableid` 
action\_result\.parameter\.value | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list tasks'
List tasks for user \(defined in asset configuration\)

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.data\.\*\.inc\.addr | string | 
action\_result\.data\.\*\.inc\.admin\_id | string | 
action\_result\.data\.\*\.inc\.assessment | string | 
action\_result\.data\.\*\.inc\.city | string | 
action\_result\.data\.\*\.inc\.confirmed | boolean | 
action\_result\.data\.\*\.inc\.country | string | 
action\_result\.data\.\*\.inc\.create\_date | numeric | 
action\_result\.data\.\*\.inc\.creator\.create\_date | numeric | 
action\_result\.data\.\*\.inc\.creator\.display\_name | string | 
action\_result\.data\.\*\.inc\.creator\.email | string |  `email` 
action\_result\.data\.\*\.inc\.creator\.fname | string | 
action\_result\.data\.\*\.inc\.creator\.id | numeric | 
action\_result\.data\.\*\.inc\.creator\.is\_external | boolean | 
action\_result\.data\.\*\.inc\.creator\.last\_login | numeric | 
action\_result\.data\.\*\.inc\.creator\.last\_modified\_time | numeric | 
action\_result\.data\.\*\.inc\.creator\.lname | string | 
action\_result\.data\.\*\.inc\.creator\.locked | boolean | 
action\_result\.data\.\*\.inc\.creator\.password\_changed | boolean | 
action\_result\.data\.\*\.inc\.creator\.status | string | 
action\_result\.data\.\*\.inc\.creator\_id | numeric | 
action\_result\.data\.\*\.inc\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.inc\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.inc\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.inc\.creator\_principal\.type | string | 
action\_result\.data\.\*\.inc\.crimestatus\_id | numeric | 
action\_result\.data\.\*\.inc\.data\_compromised | string | 
action\_result\.data\.\*\.inc\.description | string | 
action\_result\.data\.\*\.inc\.discovered\_date | numeric | 
action\_result\.data\.\*\.inc\.draft | boolean | 
action\_result\.data\.\*\.inc\.due\_date | string | 
action\_result\.data\.\*\.inc\.employee\_involved | string | 
action\_result\.data\.\*\.inc\.end\_date | string | 
action\_result\.data\.\*\.inc\.exposure | numeric | 
action\_result\.data\.\*\.inc\.exposure\_dept\_id | string | 
action\_result\.data\.\*\.inc\.exposure\_individual\_name | string | 
action\_result\.data\.\*\.inc\.exposure\_type\_id | numeric | 
action\_result\.data\.\*\.inc\.exposure\_vendor\_id | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_breach\_type | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_breach\_type\_comment | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_consequences | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_consequences\_comment | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_final\_assessment | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_final\_assessment\_comment | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_identification | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_identification\_comment | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_personal\_data | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_personal\_data\_comment | string | 
action\_result\.data\.\*\.inc\.gdpr\.gdpr\_subsequent\_notification | string | 
action\_result\.data\.\*\.inc\.hard\_liability | numeric | 
action\_result\.data\.\*\.inc\.id | numeric | 
action\_result\.data\.\*\.inc\.inc\_last\_modified\_date | numeric | 
action\_result\.data\.\*\.inc\.inc\_start | string | 
action\_result\.data\.\*\.inc\.inc\_training | boolean | 
action\_result\.data\.\*\.inc\.is\_scenario | boolean | 
action\_result\.data\.\*\.inc\.jurisdiction\_name | string | 
action\_result\.data\.\*\.inc\.jurisdiction\_reg\_id | string | 
action\_result\.data\.\*\.inc\.name | string | 
action\_result\.data\.\*\.inc\.negative\_pr\_likely | string | 
action\_result\.data\.\*\.inc\.org\_handle | numeric | 
action\_result\.data\.\*\.inc\.org\_id | numeric | 
action\_result\.data\.\*\.inc\.owner\_id | numeric | 
action\_result\.data\.\*\.inc\.perms\.assign | boolean | 
action\_result\.data\.\*\.inc\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.inc\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.inc\.perms\.change\_workspace | boolean | 
action\_result\.data\.\*\.inc\.perms\.close | boolean | 
action\_result\.data\.\*\.inc\.perms\.comment | boolean | 
action\_result\.data\.\*\.inc\.perms\.create\_artifacts | boolean | 
action\_result\.data\.\*\.inc\.perms\.create\_milestones | boolean | 
action\_result\.data\.\*\.inc\.perms\.delete | boolean | 
action\_result\.data\.\*\.inc\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.inc\.perms\.list\_artifacts | boolean | 
action\_result\.data\.\*\.inc\.perms\.list\_milestones | boolean | 
action\_result\.data\.\*\.inc\.perms\.read | boolean | 
action\_result\.data\.\*\.inc\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.inc\.perms\.write | boolean | 
action\_result\.data\.\*\.inc\.phase\_id | numeric | 
action\_result\.data\.\*\.inc\.pii\.alberta\_health\_risk\_assessment | string | 
action\_result\.data\.\*\.inc\.pii\.assessment | string | 
action\_result\.data\.\*\.inc\.pii\.data\_compromised | string | 
action\_result\.data\.\*\.inc\.pii\.data\_contained | string | 
action\_result\.data\.\*\.inc\.pii\.data\_encrypted | string | 
action\_result\.data\.\*\.inc\.pii\.data\_format | string | 
action\_result\.data\.\*\.inc\.pii\.determined\_date | numeric | 
action\_result\.data\.\*\.inc\.pii\.exposure | numeric | 
action\_result\.data\.\*\.inc\.pii\.gdpr\_harm\_risk | string | 
action\_result\.data\.\*\.inc\.pii\.harmstatus\_id | numeric | 
action\_result\.data\.\*\.inc\.pii\.impact\_likely | string | 
action\_result\.data\.\*\.inc\.pii\.ny\_impact\_likely | string | 
action\_result\.data\.\*\.inc\.plan\_status | string | 
action\_result\.data\.\*\.inc\.reporter | string | 
action\_result\.data\.\*\.inc\.resolution\_id | string | 
action\_result\.data\.\*\.inc\.resolution\_summary | string | 
action\_result\.data\.\*\.inc\.severity\_code | string | 
action\_result\.data\.\*\.inc\.start\_date | string | 
action\_result\.data\.\*\.inc\.state | string | 
action\_result\.data\.\*\.inc\.vers | numeric | 
action\_result\.data\.\*\.inc\.workspace | numeric | 
action\_result\.data\.\*\.inc\.zip | string | 
action\_result\.data\.\*\.tasks\.\*\.category\_id | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.active | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.at\_id | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.attachments\_count | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.auto\_deactivate | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.cat\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.category\_id | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.closed\_date | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.custom | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.description | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.due\_date | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.form | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.frozen | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.inc\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.inc\_owner\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.init\_date | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.instr\_text | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.instructions | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.members | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.name | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.notes\_count | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.owner\_fname | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.owner\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.owner\_lname | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.private | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.required | boolean | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.src\_name | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.status | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.task\_layout | string | 
action\_result\.data\.\*\.tasks\.\*\.child\_tasks\.\*\.user\_notes | string | 
action\_result\.data\.\*\.tasks\.\*\.id | string | 
action\_result\.data\.\*\.tasks\.\*\.name | string | 
action\_result\.data\.\*\.tasks\.\*\.parent\_id | string | 
action\_result\.data\.\*\.tasks\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.tasks\.\*\.status | string | 
action\_result\.summary\.Number of tasks | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get task'
Get task details

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**task\_id** |  required  | ID of incident | string |  `ibm resilient taskid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.task\_id | string | 
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.at\_id | string | 
action\_result\.data\.\*\.attachments\_count | numeric | 
action\_result\.data\.\*\.auto\_deactivate | boolean | 
action\_result\.data\.\*\.cat\_name | string | 
action\_result\.data\.\*\.category\_id | numeric | 
action\_result\.data\.\*\.closed\_date | string | 
action\_result\.data\.\*\.creator\_principal\.display\_name | string | 
action\_result\.data\.\*\.creator\_principal\.id | numeric | 
action\_result\.data\.\*\.creator\_principal\.name | string |  `email` 
action\_result\.data\.\*\.creator\_principal\.type | string | 
action\_result\.data\.\*\.custom | boolean | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.due\_date | string | 
action\_result\.data\.\*\.form | string | 
action\_result\.data\.\*\.frozen | boolean | 
action\_result\.data\.\*\.id | numeric | 
action\_result\.data\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner\_id | numeric | 
action\_result\.data\.\*\.inc\_training | boolean | 
action\_result\.data\.\*\.init\_date | numeric | 
action\_result\.data\.\*\.instr\_text | string | 
action\_result\.data\.\*\.instructions | string | 
action\_result\.data\.\*\.members | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.notes\_count | numeric | 
action\_result\.data\.\*\.owner\_fname | string | 
action\_result\.data\.\*\.owner\_id | string | 
action\_result\.data\.\*\.owner\_lname | string | 
action\_result\.data\.\*\.perms\.assign | boolean | 
action\_result\.data\.\*\.perms\.attach\_file | boolean | 
action\_result\.data\.\*\.perms\.change\_members | boolean | 
action\_result\.data\.\*\.perms\.close | boolean | 
action\_result\.data\.\*\.perms\.comment | boolean | 
action\_result\.data\.\*\.perms\.delete\_attachments | boolean | 
action\_result\.data\.\*\.perms\.read | boolean | 
action\_result\.data\.\*\.perms\.read\_attachments | boolean | 
action\_result\.data\.\*\.perms\.write | boolean | 
action\_result\.data\.\*\.phase\_id | numeric | 
action\_result\.data\.\*\.private | string | 
action\_result\.data\.\*\.regs\.88 | string | 
action\_result\.data\.\*\.required | boolean | 
action\_result\.data\.\*\.src\_name | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.user\_notes | string | 
action\_result\.summary\.Number of tasks | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update task'
Update task\. This action downloads the task and copy the provided json onto the download data, overwriting any existing data elements

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**task\_id** |  required  | ID of incident | string |  `ibm resilient taskid` 
**taskdto** |  required  | Table row as JSON String, format is TaskDTO data type from API | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.task\_id | string | 
action\_result\.parameter\.taskdto | string | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.success | boolean | 
action\_result\.data\.\*\.title | string | 
action\_result\.summary\.Number of tasks | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'close task'
Close task

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**task\_id** |  required  | ID of incident | string |  `ibm resilient taskid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.task\_id | string | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.success | boolean | 
action\_result\.data\.\*\.title | string | 
action\_result\.summary\.Number of tasks | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list attachments'
List attachments for incident

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.content\_type | string | 
action\_result\.data\.\*\.created | numeric | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.id | numeric | 
action\_result\.data\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.size | numeric | 
action\_result\.data\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.task\_custom | string | 
action\_result\.data\.\*\.task\_id | string | 
action\_result\.data\.\*\.task\_members | string | 
action\_result\.data\.\*\.task\_name | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.uuid | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.summary\.Number of attachments | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get attachment'
Get attachment details from incident

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**attachment\_id** |  required  | ID of attachment | string |  `ibm resilient attachmentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.attachment\_id | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.data\.\*\.content\_type | string | 
action\_result\.data\.\*\.created | numeric | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.id | numeric | 
action\_result\.data\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.size | numeric | 
action\_result\.data\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.task\_custom | string | 
action\_result\.data\.\*\.task\_id | string | 
action\_result\.data\.\*\.task\_members | string | 
action\_result\.data\.\*\.task\_name | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.uuid | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.summary\.Number of attachments | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add attachment'
Add attachment to incident

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**handle\_format\_is\_name** |  optional  | Treat handles as a name\. Default is true | boolean | 
**incident\_id** |  required  | ID of incident | string |  `ibm resilient ticketid` 
**vault\_id** |  required  | Vault ID of file | string |  `vaultid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.handle\_format\_is\_name | boolean | 
action\_result\.parameter\.incident\_id | string | 
action\_result\.parameter\.vault\_id | string |  `sha1`  `vault id` 
action\_result\.data\.\*\.content\_type | string | 
action\_result\.data\.\*\.created | numeric | 
action\_result\.data\.\*\.creator\_id | numeric | 
action\_result\.data\.\*\.id | numeric | 
action\_result\.data\.\*\.inc\_id | numeric | 
action\_result\.data\.\*\.inc\_name | string | 
action\_result\.data\.\*\.inc\_owner | numeric | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.size | numeric | 
action\_result\.data\.\*\.task\_at\_id | string | 
action\_result\.data\.\*\.task\_custom | string | 
action\_result\.data\.\*\.task\_id | string | 
action\_result\.data\.\*\.task\_members | string | 
action\_result\.data\.\*\.task\_name | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.uuid | string | 
action\_result\.data\.\*\.vers | numeric | 
action\_result\.summary\.Number of attachments | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 