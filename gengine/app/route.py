from pyramid_swagger_spec.namespace import create_api_namespace
from pyramid_swagger_spec.swagger import create_swagger_view

api_route = create_api_namespace(namespace="api")

def config_routes(config):
    config.add_route('get_progress', '/progress/{user_id}')
    config.add_route('increase_value', '/increase_value/{variable_name}/{user_id}')
    config.add_route('increase_value_with_key', '/increase_value/{variable_name}/{user_id}/{key}')
    config.add_route('increase_multi_values', '/increase_multi_values')
    config.add_route('add_or_update_user', '/add_or_update_user/{user_id}')
    config.add_route('delete_user', '/delete_user/{user_id}')
    config.add_route('get_achievement_level', '/achievement/{achievement_id}/level/{level}')

    config.add_route('auth_login', '/auth/login')
    config.add_route('change_password', '/auth/change_password')

    config.add_route('register_device', '/register_device/{user_id}')
    config.add_route('get_messages', '/messages/{user_id}')
    config.add_route('read_messages', '/read_messages/{user_id}')

    create_swagger_view(config, namespace="api", title="Admin Api", version="0.1")
