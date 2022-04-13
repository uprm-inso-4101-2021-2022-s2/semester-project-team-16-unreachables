from utils.app_imports import *

APP = Flask(__name__)
APP.config['JSON_SORT_KEYS'] = False
CORS(APP)

_users = user.UserController()
_clients = client.ClientController()
_companies = companies.CompanyController()
_employees = employee.EmployeeController()
_reports = report.ReportController()
_services = services.ServiceController()


class UtilityRoutes:
    '''
    Help on the Application Handler Object
    TODO: DOCUMENT
    '''

    #APPLICATION ROUTES
    @APP.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    # Does not require authentication
    @APP.route('/')
    @cross_origin(headers=["Content-Type", "Authorization"])
    def home():
        return "Utilities Tracker Homepage"


    # Requires authentication
    @APP.route('/test', methods=(GET, ))
    # @cross_origin(headers=["Content-Type", "Authorization"])
    # @requires_auth
    def test():
        try:
            if request.method == GET:
                return test.TestController().getTest()
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/users', methods=['POST','GET'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def users(): # aka 'register' route
        try:
            if request.method == POST:
                return _users.create(request.json)
            elif request.method == GET:
                return _users.get()
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/users/id/<int:id>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def user_by_id(id):
        try:
            if request.method == GET:
                return _users.get_by_id(id)
            if request.method == PUT:
                request.json["id"] = id
                return _users.update_by_id(request.json)
            elif request.method == DELETE:
                return _users.remove_by_id(id)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/users/username/<string:uname>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def user_by_uname(uname):
        try:
            if request.method == GET:
                return _users.get_by_uname(uname)
            if request.method == PUT:
                request.json["uname"] = uname
                return _users.update_by_uname(request.json)
            elif request.method == DELETE:
                return _users.remove_by_uname(uname)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/users/email/<string:email>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def user_by_email(email):
        try:
            if request.method == GET:
                return _users.get_by_email(email)
            if request.method == PUT:
                request.json["email"] = email
                return _users.update_by_email(request.json)
            elif request.method == DELETE:
                return _users.remove_by_email(email)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/clients', methods=['POST','GET'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def clients(): 
        try:
            if request.method == POST:
                return _clients.create(request.json)
            elif request.method == GET:
                return _clients.get()
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/clients/id/<int:id>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def client_by_id(id):
        try:
            if request.method == GET:
                return _clients.get_by_id(id)
            if request.method == PUT:
                request.json["id"] = id
                return _clients.update_by_id(request.json)
            elif request.method == DELETE:
                return _clients.remove_by_id(id)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/clients/username/<string:uname>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def client_by_uname(uname):
        try:
            if request.method == GET:
                return _clients.get_by_uname(uname)
            if request.method == PUT:
                request.json["uname"] = uname
                return _clients.update_by_uname(request.json)
            elif request.method == DELETE:
                return _clients.remove_by_uname(uname)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/clients/email/<string:email>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def client_by_email(email):
        try:
            if request.method == GET:
                return _clients.get_by_email(email)
            if request.method == PUT:
                request.json["email"] = email
                return _clients.update_by_email(request.json)
            elif request.method == DELETE:
                return _clients.remove_by_email(email)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/companies', methods=['POST','GET'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def companies(): 
        try:
            if request.method == POST:
                return _companies.create(request.json)
            elif request.method == GET:
                return _companies.get()
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/companies/id/<int:id>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def companies_by_id(id):
        try:
            if request.method == GET:
                return _companies.get_by_id(id)
            if request.method == PUT:
                request.json["id"] = id
                return _companies.update_by_id(request.json)
            elif request.method == DELETE:
                return _companies.remove_by_id(id)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/companies/name/<string:cname>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def company_by_cname(cname):
        try:
            if request.method == GET:
                return _companies.get_by_cname(cname)
            if request.method == PUT:
                request.json["company_name"] = cname
                return _companies.update_by_cname(request.json)
            elif request.method == DELETE:
                return _companies.remove_by_cname(cname)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/employees', methods=['POST','GET'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def employees(): 
        try:
            if request.method == POST:
                return _employees.create(request.json)
            elif request.method == GET:
                return _employees.get()
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/employees/id/<int:id>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def employee_by_id(id):
        try:
            if request.method == GET:
                return _employees.get_by_id(id)
            if request.method == PUT:
                request.json["id"] = id
                return _employees.update_by_id(request.json)
            elif request.method == DELETE:
                return _employees.remove_by_id(id)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/employees/username/<string:uname>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def employee_by_uname(uname):
        try:
            if request.method == GET:
                return _employees.get_by_uname(uname)
            if request.method == PUT:
                request.json["uname"] = uname
                return _employees.update_by_uname(request.json)
            elif request.method == DELETE:
                return _employees.remove_by_uname(uname)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/employees/email/<string:email>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def employee_by_email(email):
        try:
            if request.method == GET:
                return _employees.get_by_email(email)
            if request.method == PUT:
                request.json["email"] = email
                return _employees.update_by_email(request.json)
            elif request.method == DELETE:
                return _employees.remove_by_email(email)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/reports', methods=(GET, ))
    @cross_origin(headers=["Content-Type", "Authorization"])
    def reports():
        try:
            return _reports.get()
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/reports/id/<int:id>', methods=['GET'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def report_by_id(id):
        try:
            if request.method == GET:
                return _reports.get_by_id(id)
            if request.method == PUT:
                request.json["id"] = id
                return _reports.update_by_id(request.json)
            elif request.method == DELETE:
                return _reports.remove_by_id(id)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/reports/municipality/<string:municipality>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def report_by_mun(mun):
        try:
            if request.method == GET:
                return _reports.get_by_mun(mun)
            if request.method == PUT:
                request.json["municipality"] = mun
                return _reports.update_by_mun(request.json)
            elif request.method == DELETE:
                return _reports.remove_by_mun(mun)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/services', methods=['POST','GET'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def services(): 
        try:
            if request.method == POST:
                return _services.create(request.json)
            elif request.method == GET:
                return _services.get()
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED
    

    @APP.route('/services/id/<int:id>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def service_by_id(id):
        try:
            if request.method == GET:
                return _services.get_by_id(id)
            if request.method == PUT:
                request.json["id"] = id
                return _services.update_by_id(request.json)
            elif request.method == DELETE:
                return _services.remove_by_id(id)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED
    
        
    @APP.route('/services/companies/name/<string:cname>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def service_by_cname(cname):
        try:
            if request.method == GET:
                return _services.get_by_cname(cname)
            if request.method == PUT:
                request.json["cname"] = cname
                return _services.update_by_cname(request.json)
            elif request.method == DELETE:
                return _services.remove_by_cname(cname)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED


    @APP.route('/services/categories/<string:category>', methods=['GET','PUT','DELETE'])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def service_by_category(category):
        try:
            if request.method == GET:
                return _services.get_by_category(category)
            if request.method == PUT:
                request.json["category"] = category
                return _services.update_by_category(request.json)
            elif request.method == DELETE:
                return _services.remove_by_category(category)
        except:
            return jsonify(NOT_ALLOWED_TXT), NOT_ALLOWED