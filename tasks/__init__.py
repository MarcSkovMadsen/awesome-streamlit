"""Here we import the different task submodules/ collections"""
from invoke import Collection

from tasks import docker, test

# pylint: disable=invalid-name
# as invoke only recognizes lower case
namespace = Collection()
namespace.add_collection(test)
namespace.add_collection(docker)
