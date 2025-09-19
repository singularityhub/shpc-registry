---
layout: container
name:  "quay.io/biocontainers/pisces"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pisces/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pisces/container.yaml"
updated_at: "2025-09-19 03:19:15.972649"
latest: "5.2.10.49--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/pisces"
aliases:
 - "pisces"
 - "pisces_vqr"
versions:
 - "5.2.9.122--0"
 - "5.2.10.49--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for pisces"
config: {"url": "https://biocontainers.pro/tools/pisces", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pisces", "latest": {"5.2.10.49--hdfd78af_1": "sha256:8bd6fe6f09a4c0acaac06d8058fd1715c1d91a235148028e84fcabfbb9407fbb"}, "tags": {"5.2.9.122--0": "sha256:cb89baea9a1c2ba7a3ac03412b36f64a53fd447592703c5f6dc6994f6876c350", "5.2.10.49--hdfd78af_1": "sha256:8bd6fe6f09a4c0acaac06d8058fd1715c1d91a235148028e84fcabfbb9407fbb"}, "docker": "quay.io/biocontainers/pisces", "aliases": {"pisces": "/usr/local/bin/pisces", "pisces_vqr": "/usr/local/bin/pisces_vqr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pisces.
shpc-registry automated BioContainers addition for pisces
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pisces
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pisces:5.2.10.49--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pisces/5.2.10.49--hdfd78af_1
$ module help quay.io/biocontainers/pisces/5.2.10.49--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pisces-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pisces-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pisces-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pisces-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pisces-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pisces-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pisces

```bash
$ singularity exec <container> /usr/local/bin/pisces
$ podman run --it --rm --entrypoint /usr/local/bin/pisces   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pisces   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pisces_vqr

```bash
$ singularity exec <container> /usr/local/bin/pisces_vqr
$ podman run --it --rm --entrypoint /usr/local/bin/pisces_vqr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pisces_vqr   -v ${PWD} -w ${PWD} <container> -c " $@"
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