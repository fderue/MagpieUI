from pyramid.view import view_config
import requests
import json
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPOk,
    HTTPTemporaryRedirect,
    HTTPBadRequest,
    HTTPConflict,
    HTTPCreated,
    HTTPNotFound
)

from pyramid.httpexceptions import exception_response

import logging
logger = logging.getLogger(__name__)


def check_res(response):
    if response.status_code >= 400:
        raise exception_response(response.status_code, body=response.text)


def includeme(config):

    logger.info('Adding management ...')
    config.add_route('group_manager', '/group_manager')
    config.add_route('user_manager', '/user_manager')
    config.add_route('service_manager', '/service_manager')
    config.scan()
