from flask import Flask


def not_found(_):
    return "资源不存在", 404


def forbidden(_):
    return "权限不足", 403


def method_not_allow(_):
    return "方法不允许", 405


def unauthorized(_):
    return "未授权", 401


def internal_server_error(_):
    return "服务器端出现一个内部错误啦", 500


def bad_request(_):
    return "请求语法错误", 400


def init_error(app: Flask):
    app.register_error_handler(404, not_found)
    app.register_error_handler(403, forbidden)
    app.register_error_handler(405, method_not_allow)
    app.register_error_handler(401, unauthorized)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(500, internal_server_error)
