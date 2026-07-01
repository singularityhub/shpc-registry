---
layout: container
name:  "quay.io/biocontainers/uqcme-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/uqcme-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/uqcme-cli/container.yaml"
updated_at: "2026-07-01 15:12:59.103338"
latest: "0.9.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/uqcme-cli"
aliases:
 - "uqcme"
 - "uqcme-dashboard"
 - "uqcme-dashboard-smoke"
 - "idna"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
 - "normalizer"
versions:
 - "0.9.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for uqcme-cli"
config: {"url": "https://biocontainers.pro/tools/uqcme-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for uqcme-cli", "latest": {"0.9.2--pyhdfd78af_0": "sha256:e5c7365ceebc7d7016f4bda2238b228b430edc89522309d0cd8434053c069edd"}, "tags": {"0.9.2--pyhdfd78af_0": "sha256:e5c7365ceebc7d7016f4bda2238b228b430edc89522309d0cd8434053c069edd"}, "docker": "quay.io/biocontainers/uqcme-cli", "aliases": {"uqcme": "/usr/local/bin/uqcme", "uqcme-dashboard": "/usr/local/bin/uqcme-dashboard", "uqcme-dashboard-smoke": "/usr/local/bin/uqcme-dashboard-smoke", "idna": "/usr/local/bin/idna", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/uqcme-cli.
singularity registry hpc automated addition for uqcme-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/uqcme-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/uqcme-cli:0.9.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/uqcme-cli/0.9.2--pyhdfd78af_0
$ module help quay.io/biocontainers/uqcme-cli/0.9.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### uqcme-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### uqcme-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### uqcme-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### uqcme-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### uqcme-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uqcme-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### uqcme

```bash
$ singularity exec <container> /usr/local/bin/uqcme
$ podman run --it --rm --entrypoint /usr/local/bin/uqcme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uqcme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uqcme-dashboard

```bash
$ singularity exec <container> /usr/local/bin/uqcme-dashboard
$ podman run --it --rm --entrypoint /usr/local/bin/uqcme-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uqcme-dashboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uqcme-dashboard-smoke

```bash
$ singularity exec <container> /usr/local/bin/uqcme-dashboard-smoke
$ podman run --it --rm --entrypoint /usr/local/bin/uqcme-dashboard-smoke   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uqcme-dashboard-smoke   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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