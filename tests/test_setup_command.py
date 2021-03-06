from nuke_from_orbit.commands import setup_commands
from nuke_from_orbit.utils import nuke_utils
from pathlib import Path


CONFIG_DIR = Path(__file__).parent.parent.joinpath("configs")
MOCK_USER_CONFIG = {
    "gcp_service_account_file": "mock_sa_file.json",
    "loadtest_dns_domain": "mockdomain.com"
}


def test_main_set_variables(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    mock_config_path = CONFIG_DIR.joinpath("mock_config.yaml")

    setup_commands.main(config_file="mock_config.yaml", external=False, persistence=True)

    nuke_utils.set_variables.assert_called_with(mock_config_path, "v1", False)


def test_main_run_threads_persistence_no_external(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=False, persistence=True)

    nuke_utils.deploy_gke.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_test_container_image.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_persistent_disk.assert_called_with(MOCK_USER_CONFIG)
    # deploy ip shouldn't be called in multithread
    nuke_utils.deploy_ip_address.assert_not_called()


def test_main_run_threads_no_persistence_no_external(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=False, persistence=False)

    nuke_utils.deploy_gke.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_test_container_image.assert_called_with(MOCK_USER_CONFIG)
    # deploy ip and persistent disk shouldn't be called in multithread
    nuke_utils.deploy_ip_address.assert_not_called()
    nuke_utils.deploy_persistent_disk.assert_not_called()


def test_main_run_threads_persistence_external(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=True)

    nuke_utils.deploy_gke.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_test_container_image.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_persistent_disk.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_ip_address.assert_called_with(MOCK_USER_CONFIG)


def test_main_run_threads_no_persistence_external(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    nuke_utils.deploy_gke.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_test_container_image.assert_called_with(MOCK_USER_CONFIG)
    nuke_utils.deploy_ip_address.assert_called_with(MOCK_USER_CONFIG)
    # persistent disk shouldn't be called
    nuke_utils.deploy_persistent_disk.assert_not_called()


def test_main_collect_yaml_templates_call(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    nuke_utils.collect_kube_yaml_templates.assert_called_with(True)


def test_main_collect_yaml_templates_call_no_external(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=False, persistence=False)

    nuke_utils.collect_kube_yaml_templates.assert_called_with(False)


def test_main_render_templates(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates").return_value = ["mock_file_list"]
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    nuke_utils.render_kubernetes_templates.assert_called_with(MOCK_USER_CONFIG, ["mock_file_list"])


def test_main_set_k8s_context(mocker):
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    nuke_utils.set_kubernetes_context.assert_called_with(MOCK_USER_CONFIG)


def test_main_deploy_looker_secret(mocker):

    parent_mock = mocker.Mock()

    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    context_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    deploy_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")

    parent_mock.attach_mock(context_mock, "context_mock")
    parent_mock.attach_mock(deploy_mock, "deploy_mock")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    # determine if context call occurs before deployment
    expected_call_order = [mocker.call.context_mock(MOCK_USER_CONFIG), mocker.call.deploy_mock(MOCK_USER_CONFIG)]
    assert parent_mock.mock_calls == expected_call_order


def test_main_deploy_oauth_secret_external(mocker):

    parent_mock = mocker.Mock()

    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    context_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    deploy_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")

    parent_mock.attach_mock(context_mock, "context_mock")
    parent_mock.attach_mock(deploy_mock, "deploy_mock")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    # determine if context call occurs before deployment
    expected_call_order = [mocker.call.context_mock(MOCK_USER_CONFIG), mocker.call.deploy_mock(MOCK_USER_CONFIG)]
    assert parent_mock.mock_calls == expected_call_order


def test_main_deploy_oauth_secret_no_external(mocker):

    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=False, persistence=False)

    nuke_utils.deploy_oauth_secret.assert_not_called()


def test_main_deploy_external(mocker):

    parent_mock = mocker.Mock()

    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    context_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    deploy_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")

    parent_mock.attach_mock(context_mock, "context_mock")
    parent_mock.attach_mock(deploy_mock, "deploy_mock")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    # determine if context call occurs before deployment
    expected_call_order = [mocker.call.context_mock(MOCK_USER_CONFIG), mocker.call.deploy_mock()]
    assert parent_mock.mock_calls == expected_call_order


def test_main_deploy_external_no_external(mocker):

    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    setup_commands.main(config_file="mock_config.yaml", external=False, persistence=False)

    # determine if context call occurs before deployment
    nuke_utils.deploy_external.assert_not_called()


def test_main_deploy_locust(mocker):

    parent_mock = mocker.Mock()

    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    context_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    deploy_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")

    parent_mock.attach_mock(context_mock, "context_mock")
    parent_mock.attach_mock(deploy_mock, "deploy_mock")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    # determine if context call occurs before deployment
    expected_call_order = [mocker.call.context_mock(MOCK_USER_CONFIG), mocker.call.deploy_mock()]
    assert parent_mock.mock_calls == expected_call_order


def test_main_deploy_secondary(mocker):

    parent_mock = mocker.Mock()

    mocker.patch("nuke_from_orbit.utils.nuke_utils.set_variables").return_value = MOCK_USER_CONFIG
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_gke")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_test_container_image")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_persistent_disk")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.get_ip_address")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.collect_kube_yaml_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.render_kubernetes_templates")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_looker_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_oauth_secret")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_external")
    mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_locust")

    context_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.set_kubernetes_context")
    deploy_mock = mocker.patch("nuke_from_orbit.utils.nuke_utils.deploy_secondary")

    parent_mock.attach_mock(context_mock, "context_mock")
    parent_mock.attach_mock(deploy_mock, "deploy_mock")

    setup_commands.main(config_file="mock_config.yaml", external=True, persistence=False)

    # determine if context call occurs before deployment
    expected_call_order = [mocker.call.context_mock(MOCK_USER_CONFIG), mocker.call.deploy_mock()]
    assert parent_mock.mock_calls == expected_call_order
