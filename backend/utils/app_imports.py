from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from controller.test import TestController
from controller.user import UserController
from controller.client import ClientController
from controller.companies import CompanyController
from controller.employee import EmployeeController
from controller.report import ReportController
from controller.services import ServiceController
from utils.authen import *
from utils.macros import *

