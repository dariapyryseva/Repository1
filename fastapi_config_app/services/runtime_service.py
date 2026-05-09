from config import runtime_config


def get_runtime_config():
    return runtime_config


def update_runtime_config(new_config):
    runtime_config.log_level = new_config.log_level
    runtime_config.feature_flag = new_config.feature_flag
    runtime_config.maintenance_mode = new_config.maintenance_mode
    runtime_config.runtime_message = new_config.runtime_message

    return runtime_config
