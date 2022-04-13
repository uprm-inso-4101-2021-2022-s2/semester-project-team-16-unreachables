from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from controller import test
from controller import user
from controller import client
from controller import companies
from controller import employee
from controller import report
from controller import services
from utils.authen import *
from utils import macros

