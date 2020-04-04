import os
# from oauthenticator.github import GitHubOAuthenticator
# c.JupyterHub.authenticator_class = GitHubOAuthenticator

c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.Authenticator.admin_users = {'admin'}
# c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# c.JupyterHub.hub_ip = os.environ['HUB_IP']
# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
# c.JupyterHub.hub_connect_ip = 'jupyterhub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image = 'jupyter/base-notebook'

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'rt_default'

# delete containers when the stop
c.DockerSpawner.remove = True

# c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
# c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
