---
layout: container
name:  "quay.io/biocontainers/galaxy-job-config-init"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/galaxy-job-config-init/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/galaxy-job-config-init/container.yaml"
updated_at: "2025-10-13 03:42:51.677488"
latest: "0.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/galaxy-job-config-init"
aliases:
 - "galaxy-job-config-init"
 - "galaxy-job-config-init-summary"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for galaxy-job-config-init"
config: {"url": "https://biocontainers.pro/tools/galaxy-job-config-init", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for galaxy-job-config-init", "latest": {"0.1.3--pyhdfd78af_0": "sha256:20c438a8d4e9b5f6e74a498df95c3a6ca7afcffa05af8e23b84d69e7564d0554"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:20c438a8d4e9b5f6e74a498df95c3a6ca7afcffa05af8e23b84d69e7564d0554"}, "docker": "quay.io/biocontainers/galaxy-job-config-init", "aliases": {"galaxy-job-config-init": "/usr/local/bin/galaxy-job-config-init", "galaxy-job-config-init-summary": "/usr/local/bin/galaxy-job-config-init-summary", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/galaxy-job-config-init.
singularity registry hpc automated addition for galaxy-job-config-init
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/galaxy-job-config-init
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/galaxy-job-config-init:0.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/galaxy-job-config-init/0.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/galaxy-job-config-init/0.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### galaxy-job-config-init-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-job-config-init-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-job-config-init-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### galaxy-job-config-init-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### galaxy-job-config-init-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### galaxy-job-config-init-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### galaxy-job-config-init

```bash
$ singularity exec <container> /usr/local/bin/galaxy-job-config-init
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-job-config-init   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-job-config-init   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-job-config-init-summary

```bash
$ singularity exec <container> /usr/local/bin/galaxy-job-config-init-summary
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-job-config-init-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-job-config-init-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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