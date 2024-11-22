---
layout: container
name:  "ghcr.io/autamus/opencv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/opencv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/opencv/container.yaml"
updated_at: "2024-11-22 02:58:31.026120"
latest: "4.6.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/opencv"
aliases:
 - "opencv_version"
 - "setup_vars_opencv4.sh"
versions:
 - "4.5.2"
 - "4.5.3"
 - "latest"
 - "4.6.0"
description: "OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez."
config: {"docker": "ghcr.io/autamus/opencv", "url": "https://github.com/orgs/autamus/packages/container/package/opencv", "maintainer": "@vsoch", "description": "OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez.", "latest": {"4.6.0": "sha256:77d71914da9e8998a0b508f6264511b57f2ba96cd0a9811a9591e43826e4fcd0"}, "tags": {"4.5.2": "sha256:587521b8a8446e22d7997d972449430d86603f2cc8fb52519fe5a8224e1cd43a", "4.5.3": "sha256:5f21e07ad4a6bb1b9e1832c2498fcf308f71a8fab152b6e01eed63ae3f080389", "latest": "sha256:77d71914da9e8998a0b508f6264511b57f2ba96cd0a9811a9591e43826e4fcd0", "4.6.0": "sha256:77d71914da9e8998a0b508f6264511b57f2ba96cd0a9811a9591e43826e4fcd0"}, "aliases": {"opencv_version": "/opt/view/bin/opencv_version", "setup_vars_opencv4.sh": "/opt/view/bin/setup_vars_opencv4.sh"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/opencv.
OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/opencv
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/opencv:4.6.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/opencv/4.6.0
$ module help ghcr.io/autamus/opencv/4.6.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### opencv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### opencv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### opencv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### opencv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### opencv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### opencv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### opencv_version

```bash
$ singularity exec <container> /opt/view/bin/opencv_version
$ podman run --it --rm --entrypoint /opt/view/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup_vars_opencv4.sh

```bash
$ singularity exec <container> /opt/view/bin/setup_vars_opencv4.sh
$ podman run --it --rm --entrypoint /opt/view/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)