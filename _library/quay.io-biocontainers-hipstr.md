---
layout: container
name:  "quay.io/biocontainers/hipstr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hipstr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hipstr/container.yaml"
updated_at: "2026-07-26 05:40:59.726418"
latest: "0.7--hcf09f9e_0"
container_url: "https://biocontainers.pro/tools/hipstr"
aliases:
 - "HipSTR"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "0.7--hcf09f9e_0"
description: "singularity registry hpc automated addition for hipstr"
config: {"url": "https://biocontainers.pro/tools/hipstr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hipstr", "latest": {"0.7--hcf09f9e_0": "sha256:62009960693867d488fec9d10612825e0cace19955fb091d960eab1d7528e2fa"}, "tags": {"0.7--hcf09f9e_0": "sha256:62009960693867d488fec9d10612825e0cace19955fb091d960eab1d7528e2fa"}, "docker": "quay.io/biocontainers/hipstr", "aliases": {"HipSTR": "/usr/local/bin/HipSTR", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hipstr.
singularity registry hpc automated addition for hipstr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hipstr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hipstr:0.7--hcf09f9e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hipstr/0.7--hcf09f9e_0
$ module help quay.io/biocontainers/hipstr/0.7--hcf09f9e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hipstr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hipstr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hipstr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hipstr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hipstr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hipstr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HipSTR

```bash
$ singularity exec <container> /usr/local/bin/HipSTR
$ podman run --it --rm --entrypoint /usr/local/bin/HipSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HipSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
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