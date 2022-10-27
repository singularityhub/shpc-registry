---
layout: container
name:  "quay.io/biocontainers/deepaccess"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepaccess/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepaccess/container.yaml"
updated_at: "2022-10-27 01:09:47.318952"
latest: "0.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/deepaccess"
aliases:
 - "deepaccess"
versions:
 - "0.1.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for deepaccess"
config: {"url": "https://biocontainers.pro/tools/deepaccess", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepaccess", "latest": {"0.1.3--pyhdfd78af_0": "sha256:be1fee28598fea542546c856828b03fe2aed9b82281fe484a0eefa9a2b576e14"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:be1fee28598fea542546c856828b03fe2aed9b82281fe484a0eefa9a2b576e14"}, "docker": "quay.io/biocontainers/deepaccess", "aliases": {"deepaccess": "/usr/local/bin/deepaccess"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepaccess.
shpc-registry automated BioContainers addition for deepaccess
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepaccess
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepaccess:0.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepaccess/0.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/deepaccess/0.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepaccess-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepaccess-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepaccess-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepaccess-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepaccess-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepaccess-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepaccess

```bash
$ singularity exec <container> /usr/local/bin/deepaccess
$ podman run --it --rm --entrypoint /usr/local/bin/deepaccess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepaccess   -v ${PWD} -w ${PWD} <container> -c " $@"
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