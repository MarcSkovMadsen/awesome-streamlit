"""Module of Invoke tasks to be invoked from the command line. Try

invoke --list

from the command line for a list of all available commands.
"""
import subprocess
from dataclasses import dataclass
from typing import List

# pylint: disable=invalid-name
# because Invoke uses 'c' for the Invoke command object
from invoke import task

DOCKER_REGISTRY = "marcskovmadsen"


def _build(  # pylint: disable=too-many-arguments
    c, docker_file: str, image: str, tag: str, context: str, rebuild: bool = False
):
    """Helper function for docker build

    Arguments:
        c {[type]} -- Invoke command object
        docker_file {str} -- The path to the Docker file
        image {str} -- The name of the Docker image
        tag {str} -- The Docker tag
        context {str} -- The context to use for building the Docker image
        rebuild {bool} - If true we rebuild from scratch
    """
    print(
        f"""
Building the '{DOCKER_REGISTRY}/{image}:{tag}' Docker image
===================================
"""
    )
    if rebuild:
        command = (
            f"docker build --no-cache --rm -f {docker_file} "
            f"-t {image}:{tag} -t {image}:latest {context}"
        )
    else:
        command = f"docker build --rm -f {docker_file} -t {image}:{tag} -t {image}:latest {context}"
    c.run(command, echo=True)


@dataclass
class Image:
    """Model of Docker Image. Used to hold settings"""

    name: str
    docker_file: str
    context: str
    dependencies: List
    registry: str = DOCKER_REGISTRY

    @property
    def image(self) -> str:
        """The full name of the image, i.e. registry/name

        Returns:
            str -- [description]
        """

        return f"{self.registry}/{self.name}"


IMAGES = {
    "base": Image(
        docker_file="devops/docker/Dockerfile.base",
        name="awesome-streamlit_base",
        context=".",
        dependencies=[],
        registry=DOCKER_REGISTRY,
    ),
    "prod": Image(
        docker_file="devops/docker/Dockerfile.prod",
        name="awesome-streamlit",
        context=".",
        dependencies=["base"],
        registry=DOCKER_REGISTRY,
    ),
}


@task
def build(c, image="prod", tag="latest", rebuild=False):
    """Build Docker image

    Arguments:
        c {[type]} -- Invoke command

    Keyword Arguments:backend
        image {str} -- Image name: awesome-streamlit (default: {"prod"})
        tag {str} -- Image tag.
            If tag != "latest" then the image will be tagged with both tag and 'latest'
            (default: {"latest"})
        rebuild {bool} -- If set then the image and all dependencies are rebuilt from scratch
            (default: {False})
    """
    image_configuration = IMAGES.get(image, IMAGES["prod"])

    if rebuild:
        for dependent_image in image_configuration.dependencies:
            build(c, image=dependent_image, tag=tag, rebuild=rebuild)

    _build(
        c,
        docker_file=image_configuration.docker_file,
        image=image_configuration.image,
        tag=tag,
        context=image_configuration.context,
        rebuild=False,
    )


@task
def run(c, image="awesome-streamlit", tag="latest"):  # pylint: disable=unused-argument
    """Run the Docker container bash terminal interactively.

    Arguments:
        c {[type]} -- Invoke command object

    Keyword Arguments:
        image {[type]} -- awesome-streamlit (default: {"prod"})
        tag {str} -- Name of tag (default: {"latest"})
    """

    # Invoke cannot run interactive
    print(
        f"""
Running the '{image}:{tag}' Docker image
========================================
"""
    )
    command = (
        f'docker run -it -p 80:80 --entrypoint "/bin/bash" '
        f"{DOCKER_REGISTRY}/{image}:{tag} "
    )
    print(command)
    subprocess.run(command, check=True)


@task
def push(c, image="awesome-streamlit", tag="latest"):
    """Push the Docker container

    Arguments:
        c {[type]} -- Invoke command object

    Keyword Arguments:
        image {[type]} -- awesome-streamlit (default: {"awesome-streamlit"})
        tag {str} -- Name of tag (default: {"latest"})
    """
    command = f"docker push {DOCKER_REGISTRY}/{image}:{tag}"
    c.run(command, echo=True)


@task
def run_server(c):  # pylint: disable=unused-argument
    """Run the Docker image with the Streamlit server.

    Arguments:
        c {[type]} -- Invoke command object

    Keyword Arguments:
        image {[type]} -- awesome-streamlit (default: {"prod"})
        tag {str} -- Name of tag (default: {"latest"})
    """

    # Invoke cannot run interactive
    image = "awesome-streamlit"
    tag = "latest"
    print(
        f"""
Running the '{image}:{tag}' Docker image
========================================
"""
    )
    command = (
        'docker run -it -p 80:80 --entrypoint "streamlit" '
        f"{DOCKER_REGISTRY}/{image}:{tag} "
        "run app.py"
    )

    print(command)
    subprocess.run(command, check=True)


@task
def run_server_with_ping(c):  # pylint: disable=unused-argument
    """Run the docker image with Streamlit server and
    a ping to awesome-streamlit.org every 5 minutes
    to keep it alive

    Arguments:
        c {[type]} -- Invoke command object

    Keyword Arguments:
        image {[type]} -- awesome-streamlit (default: {"prod"})
        tag {str} -- Name of tag (default: {"latest"})
    """

    # Invoke cannot run interactive
    image = "awesome-streamlit"
    tag = "latest"
    print(
        f"""
Running the '{image}:{tag}' Docker image
========================================
"""
    )
    command = (
        'docker run -it -p 80:80 --entrypoint "/bin/bash" '
        f"{DOCKER_REGISTRY}/{image}:{tag} "
        "./scripts/run_awesome_streamlit_with_ping.sh"
    )

    print(command)
    subprocess.run(command, check=True)


@task
def system_prune(c):
    """The docker system prune command will free up space

    It removes all stopped containers, all dangling images, and
    all unused networks to free up space.

    See https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/
    """
    print(
        """Cleaning up the Docker system
================================
"""
    )
    c.run("docker system prune", echo=True)


@task
def remove_unused(command):  # pylint: disable=unused-argument
    """Removes all unused containers to free up space"""
    print("RUN THESE")
    print("docker rmi $(docker images -q)")
    print("docker rm -v $(docker ps -qa)")
