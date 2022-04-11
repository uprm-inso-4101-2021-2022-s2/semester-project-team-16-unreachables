'''
This script is used to summarize all the macros used throughout the REST API.
'''

#AUNTH0 MACROS
AUTH0_DOMAIN = 'YOUR_DOMAIN'
API_AUDIENCE = 'utilities-tracker.herokuapp.com/'
ALGORITHMS = ["RS256"]

# CRUD operations
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

# CONTROLLER ERROR MESSAES
USR_ERROR = "ERROR FETCHING USERS"
CLIENT_ERROR = "ERROR FETCHING CLIENTS"
EMPLOYEE_ERROR = "ERROR FETCHING EMPLOYEES"
REPORT_ERROR = "ERROR FETCHING REPORTS"
COMPANY_ERROR = "ERROR FETCHING COMPANIES"
SERVICE_ERROR = "ERROR FETCHING SERVICES"

# HTTP ERROR MESSAES
USR_DNE = "USER DOES NOT EXIST"
CLIENT_DNE = "CLIENT DOES NOT EXIST"
EMPLOYEE_DNE = "EMPLOYEE DOES NOT EXIST"
REPORT_DNE = "REPORT DOES NOT EXIST"
COMPANY_DNE = "UTILITY COMPANY DOES NOT EXIST"
SERVICE_DNE = "SERVICE DOES NOT EXIST"
NOT_ALLOWED_TXT = "REQUEST NOT ALLOWED"

# HTTP ERROR CODES
OK = 200
CREATED = 201
ACCEPTED = 202
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
NOT_ALLOWED = 405