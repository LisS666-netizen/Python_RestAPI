from time import sleep

from GITHUB import GET_User_Repos


def test_e2e_github():
    GET_User_Repos.test_get_all_repos()
    GET_User_Repos.test_create_new_repo()
    GET_User_Repos.test_get_created_repo()
    GET_User_Repos.test_update_repo()
    GET_User_Repos.test_create_file_in_repo()
    GET_User_Repos.test_update_file_in_repo()
    GET_User_Repos.test_get_content_of_repo()
    GET_User_Repos.test_delete_file_in_repo()
    GET_User_Repos.test_delete_repo()