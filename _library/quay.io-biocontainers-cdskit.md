---
layout: container
name:  "quay.io/biocontainers/cdskit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cdskit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cdskit/container.yaml"
updated_at: "2026-01-06 04:16:29.348060"
latest: "0.14.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cdskit"
aliases:
 - "cdskit"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.14.2--pyhdfd78af_0"
 - "0.14.4--pyh7e72e81_0"
 - "0.14.4--pyhdfd78af_1"
 - "0.14.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for cdskit"
config: {"url": "https://biocontainers.pro/tools/cdskit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cdskit", "latest": {"0.14.5--pyhdfd78af_0": "sha256:bc3836579906c2aa0800280f108bbbbb67cdd6533100cfa9eb40a95f2c837956"}, "tags": {"0.14.2--pyhdfd78af_0": "sha256:be2898469a9f232235b899c529861bfb34633506e14207d2528e85bc1afc97ea", "0.14.4--pyh7e72e81_0": "sha256:2dc05d61a0e56a12f273858fb0596d5d55fd0f56ffde474fad4d6bdc235db395", "0.14.4--pyhdfd78af_1": "sha256:3fb47cad304697f26fbc83fb5b64d89b65afa7c572feca47cae436fb40939bd1", "0.14.5--pyhdfd78af_0": "sha256:bc3836579906c2aa0800280f108bbbbb67cdd6533100cfa9eb40a95f2c837956"}, "docker": "quay.io/biocontainers/cdskit", "aliases": {"cdskit": "/usr/local/bin/cdskit", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cdskit.
singularity registry hpc automated addition for cdskit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cdskit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cdskit:0.14.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cdskit/0.14.5--pyhdfd78af_0
$ module help quay.io/biocontainers/cdskit/0.14.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cdskit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cdskit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cdskit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cdskit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cdskit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cdskit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cdskit

```bash
$ singularity exec <container> /usr/local/bin/cdskit
$ podman run --it --rm --entrypoint /usr/local/bin/cdskit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdskit   -v ${PWD} -w ${PWD} <container> -c " $@"
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