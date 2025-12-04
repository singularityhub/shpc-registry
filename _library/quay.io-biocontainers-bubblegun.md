---
layout: container
name:  "quay.io/biocontainers/bubblegun"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bubblegun/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bubblegun/container.yaml"
updated_at: "2025-12-04 03:44:09.724010"
latest: "1.1.10--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bubblegun"
aliases:
 - "BubbleGun"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "1.1.9--pyhdfd78af_0"
 - "1.1.10--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bubblegun"
config: {"url": "https://biocontainers.pro/tools/bubblegun", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bubblegun", "latest": {"1.1.10--pyhdfd78af_0": "sha256:76b4bb42d54fd8fe1de74e1a3b2489798c7599e922817d8562633f40d68c685a"}, "tags": {"1.1.9--pyhdfd78af_0": "sha256:3569e8c3d13ce376bbfa1358cfc6d20a75649b06f7106c040028b43785fd12c2", "1.1.10--pyhdfd78af_0": "sha256:76b4bb42d54fd8fe1de74e1a3b2489798c7599e922817d8562633f40d68c685a"}, "docker": "quay.io/biocontainers/bubblegun", "aliases": {"BubbleGun": "/usr/local/bin/BubbleGun", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bubblegun.
singularity registry hpc automated addition for bubblegun
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bubblegun
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bubblegun:1.1.10--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bubblegun/1.1.10--pyhdfd78af_0
$ module help quay.io/biocontainers/bubblegun/1.1.10--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bubblegun-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bubblegun-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bubblegun-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bubblegun-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bubblegun-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bubblegun-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BubbleGun

```bash
$ singularity exec <container> /usr/local/bin/BubbleGun
$ podman run --it --rm --entrypoint /usr/local/bin/BubbleGun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BubbleGun   -v ${PWD} -w ${PWD} <container> -c " $@"
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