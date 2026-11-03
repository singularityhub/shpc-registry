---
layout: container
name:  "quay.io/biocontainers/spatial-continuum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spatial-continuum/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spatial-continuum/container.yaml"
updated_at: "2026-11-03 09:30:21.075604"
latest: "1.0.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/spatial-continuum"
aliases:
 - "cri-calc"
 - "spatial-continuum-audit"
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
versions:
 - "1.0.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for spatial-continuum"
config: {"url": "https://biocontainers.pro/tools/spatial-continuum", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for spatial-continuum", "latest": {"1.0.3--pyhdfd78af_0": "sha256:626c9ecd89e96b49179ad2b4613a3cb0d3d6d8da6c1ad47c0abee6f670e79821"}, "tags": {"1.0.3--pyhdfd78af_0": "sha256:626c9ecd89e96b49179ad2b4613a3cb0d3d6d8da6c1ad47c0abee6f670e79821"}, "docker": "quay.io/biocontainers/spatial-continuum", "aliases": {"cri-calc": "/usr/local/bin/cri-calc", "spatial-continuum-audit": "/usr/local/bin/spatial-continuum-audit", "idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spatial-continuum.
singularity registry hpc automated addition for spatial-continuum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spatial-continuum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spatial-continuum:1.0.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spatial-continuum/1.0.3--pyhdfd78af_0
$ module help quay.io/biocontainers/spatial-continuum/1.0.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spatial-continuum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spatial-continuum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spatial-continuum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spatial-continuum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spatial-continuum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spatial-continuum-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cri-calc

```bash
$ singularity exec <container> /usr/local/bin/cri-calc
$ podman run --it --rm --entrypoint /usr/local/bin/cri-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cri-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spatial-continuum-audit

```bash
$ singularity exec <container> /usr/local/bin/spatial-continuum-audit
$ podman run --it --rm --entrypoint /usr/local/bin/spatial-continuum-audit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spatial-continuum-audit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.15

```bash
$ singularity exec <container> /usr/local/bin/idle3.15
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.15

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.15
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15

```bash
$ singularity exec <container> /usr/local/bin/python3.15
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15-config

```bash
$ singularity exec <container> /usr/local/bin/python3.15-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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