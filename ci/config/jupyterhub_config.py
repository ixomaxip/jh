import os
# from oauthenticator.github import GitHubOAuthenticator
# c.JupyterHub.authenticator_class = GitHubOAuthenticator

c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.Authenticator.admin_users = {'admin'}

# c.JupyterHub.hub_ip = os.environ['HUB_IP']
# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]

# c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
