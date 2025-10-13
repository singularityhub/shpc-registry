---
layout: container
name:  "rocm/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocm/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocm/tensorflow/container.yaml"
updated_at: "2025-10-13 03:11:53.499436"
latest: "rocm7.0-py3.12-tf2.19-dev"
container_url: "https://hub.docker.com/r/rocm/tensorflow"
aliases:
 - "python"
 - "python3"
versions:
 - "rocm5.5-tf2.11-dev"
 - "gpg"
 - "latest"
 - "rocm5.6-tf2.12-dev"
 - "rocm5.7-tf2.13-dev"
 - "rocm6.0-tf2.14-dev"
 - "rocm6.1-py3.10-tf2.15-dev"
 - "rocm6.2-py3.9-tf2.16-dev"
 - "latest-internal"
 - "rocm6.3-py3.12-tf2.17-dev"
 - "rocm6.4-py3.12-tf2.18-dev"
 - "rocm7.0-py3.12-tf2.19-dev"
description: "Tensorflow with ROCm backend support"
config: {"docker": "rocm/tensorflow", "url": "https://hub.docker.com/r/rocm/tensorflow", "maintainer": "@dipietrantonio", "description": "Tensorflow with ROCm backend support", "latest": {"rocm7.0-py3.12-tf2.19-dev": "crane digest rocm/tensorflow:rocm7.0-py3.12-tf2.19-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"rocm5.5-tf2.11-dev": "crane digest rocm/tensorflow:rocm5.5-tf2.11-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "gpg": "crane digest rocm/tensorflow:gpg: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "latest": "crane digest rocm/tensorflow:latest: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm5.6-tf2.12-dev": "crane digest rocm/tensorflow:rocm5.6-tf2.12-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm5.7-tf2.13-dev": "crane digest rocm/tensorflow:rocm5.7-tf2.13-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm6.0-tf2.14-dev": "crane digest rocm/tensorflow:rocm6.0-tf2.14-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm6.1-py3.10-tf2.15-dev": "crane digest rocm/tensorflow:rocm6.1-py3.10-tf2.15-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm6.2-py3.9-tf2.16-dev": "crane digest rocm/tensorflow:rocm6.2-py3.9-tf2.16-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "latest-internal": "crane digest rocm/tensorflow:latest-internal: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm6.3-py3.12-tf2.17-dev": "crane digest rocm/tensorflow:rocm6.3-py3.12-tf2.17-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm6.4-py3.12-tf2.18-dev": "crane digest rocm/tensorflow:rocm6.4-py3.12-tf2.18-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "rocm7.0-py3.12-tf2.19-dev": "crane digest rocm/tensorflow:rocm7.0-py3.12-tf2.19-dev: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "features": {"gpu": true}, "aliases": {"python": "/usr/bin/python", "python3": "/usr/bin/python3"}}
---

This module is a singularity container wrapper for rocm/tensorflow.
Tensorflow with ROCm backend support
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocm/tensorflow
```

Or a specific version:

```bash
$ shpc install rocm/tensorflow:rocm7.0-py3.12-tf2.19-dev
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocm/tensorflow/rocm7.0-py3.12-tf2.19-dev
$ module help rocm/tensorflow/rocm7.0-py3.12-tf2.19-dev
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tensorflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tensorflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tensorflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tensorflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /usr/bin/python
$ podman run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3

```bash
$ singularity exec <container> /usr/bin/python3
$ podman run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
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