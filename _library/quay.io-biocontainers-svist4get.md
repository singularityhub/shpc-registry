---
layout: container
name:  "quay.io/biocontainers/svist4get"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svist4get/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/svist4get/container.yaml"
updated_at: "2022-10-27 01:08:42.860241"
latest: "1.3.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/svist4get"
aliases:
 - "svist4get"
 - "svist4get_copier"
versions:
 - "1.3.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for svist4get"
config: {"url": "https://biocontainers.pro/tools/svist4get", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svist4get", "latest": {"1.3.1--pyhdfd78af_0": "sha256:e65fe58212741e88b990a9785e532832e301a207bd6841c7d41364d6a4368473"}, "tags": {"1.3.1--pyhdfd78af_0": "sha256:e65fe58212741e88b990a9785e532832e301a207bd6841c7d41364d6a4368473"}, "docker": "quay.io/biocontainers/svist4get", "aliases": {"svist4get": "/usr/local/bin/svist4get", "svist4get_copier": "/usr/local/bin/svist4get_copier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svist4get.
shpc-registry automated BioContainers addition for svist4get
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svist4get
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svist4get:1.3.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svist4get/1.3.1--pyhdfd78af_0
$ module help quay.io/biocontainers/svist4get/1.3.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svist4get-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svist4get-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svist4get-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svist4get-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svist4get-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svist4get-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### svist4get

```bash
$ singularity exec <container> /usr/local/bin/svist4get
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svist4get_copier

```bash
$ singularity exec <container> /usr/local/bin/svist4get_copier
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
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