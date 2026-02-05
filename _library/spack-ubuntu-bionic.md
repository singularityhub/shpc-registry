---
layout: container
name:  "spack/ubuntu-bionic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/spack/ubuntu-bionic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/spack/ubuntu-bionic/container.yaml"
updated_at: "2026-02-05 05:10:35.406825"
latest: "develop-2023-05-14"
container_url: "https://hub.docker.com/r/spack/ubuntu-bionic"
aliases:
 - "sbang"
 - "spack"
 - "spack-python"
versions:
 - "0.16.1"
 - "0.16.2"
 - "0.16.3"
 - "latest"
 - "0.16"
 - "prerelease"
 - "v0.17.2"
 - "v0.18.0"
 - "v0.18.1"
 - "v0.17.3"
 - "v0.19.0"
 - "v0.19.1"
 - "v0.19.2"
 - "develop-2023-05-14"
 - "v0.20.0"
 - "v0.20.1"
 - "v0.20.2"
 - "v0.20.3"
description: "Ubuntu 18.04 with Spack preinstalled."
config: {"docker": "spack/ubuntu-bionic", "url": "https://hub.docker.com/r/spack/ubuntu-bionic", "maintainer": "@vsoch", "description": "Ubuntu 18.04 with Spack preinstalled.", "latest": {"develop-2023-05-14": "crane digest spack/ubuntu-bionic:develop-2023-05-14: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"0.16.1": "crane digest spack/ubuntu-bionic:0.16.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "0.16.2": "crane digest spack/ubuntu-bionic:0.16.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "0.16.3": "crane digest spack/ubuntu-bionic:0.16.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "latest": "crane digest spack/ubuntu-bionic:latest: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "0.16": "crane digest spack/ubuntu-bionic:0.16: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "prerelease": "crane digest spack/ubuntu-bionic:prerelease: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.17.2": "crane digest spack/ubuntu-bionic:v0.17.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.18.0": "crane digest spack/ubuntu-bionic:v0.18.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.18.1": "crane digest spack/ubuntu-bionic:v0.18.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.17.3": "crane digest spack/ubuntu-bionic:v0.17.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.19.0": "crane digest spack/ubuntu-bionic:v0.19.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.19.1": "crane digest spack/ubuntu-bionic:v0.19.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.19.2": "crane digest spack/ubuntu-bionic:v0.19.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "develop-2023-05-14": "crane digest spack/ubuntu-bionic:develop-2023-05-14: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.20.0": "crane digest spack/ubuntu-bionic:v0.20.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.20.1": "crane digest spack/ubuntu-bionic:v0.20.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.20.2": "crane digest spack/ubuntu-bionic:v0.20.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v0.20.3": "crane digest spack/ubuntu-bionic:v0.20.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "aliases": {"sbang": "/opt/spack/bin/sbang", "spack": "/opt/spack/bin/spack", "spack-python": "/opt/spack/bin/spack-python"}}
---

This module is a singularity container wrapper for spack/ubuntu-bionic.
Ubuntu 18.04 with Spack preinstalled.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install spack/ubuntu-bionic
```

Or a specific version:

```bash
$ shpc install spack/ubuntu-bionic:develop-2023-05-14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load spack/ubuntu-bionic/develop-2023-05-14
$ module help spack/ubuntu-bionic/develop-2023-05-14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ubuntu-bionic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ubuntu-bionic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ubuntu-bionic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ubuntu-bionic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ubuntu-bionic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ubuntu-bionic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sbang

```bash
$ singularity exec <container> /opt/spack/bin/sbang
$ podman run --it --rm --entrypoint /opt/spack/bin/sbang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/sbang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spack

```bash
$ singularity exec <container> /opt/spack/bin/spack
$ podman run --it --rm --entrypoint /opt/spack/bin/spack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/spack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spack-python

```bash
$ singularity exec <container> /opt/spack/bin/spack-python
$ podman run --it --rm --entrypoint /opt/spack/bin/spack-python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/spack-python   -v ${PWD} -w ${PWD} <container> -c " $@"
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