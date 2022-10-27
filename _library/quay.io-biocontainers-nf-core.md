---
layout: container
name:  "quay.io/biocontainers/nf-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nf-core/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nf-core/container.yaml"
updated_at: "2022-10-27 01:02:47.008814"
latest: "2.6--pyh7cba7a3_1"
container_url: "https://biocontainers.pro/tools/nf-core"
aliases:
 - "import_igenome"
 - "mulled-hash"
 - "mulled-list"
 - "mulled-update-singularity-containers"
 - "nf-core"
 - "refgenie"
 - "scalar"
versions:
 - "2.6--pyh7cba7a3_1"
description: "shpc-registry automated BioContainers addition for nf-core"
config: {"url": "https://biocontainers.pro/tools/nf-core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nf-core", "latest": {"2.6--pyh7cba7a3_1": "sha256:e93a47ded9e18567f695e8610846f32f935c1db44ac5c5b03ab51ece3e8c5735"}, "tags": {"2.6--pyh7cba7a3_1": "sha256:e93a47ded9e18567f695e8610846f32f935c1db44ac5c5b03ab51ece3e8c5735"}, "docker": "quay.io/biocontainers/nf-core", "aliases": {"import_igenome": "/usr/local/bin/import_igenome", "mulled-hash": "/usr/local/bin/mulled-hash", "mulled-list": "/usr/local/bin/mulled-list", "mulled-update-singularity-containers": "/usr/local/bin/mulled-update-singularity-containers", "nf-core": "/usr/local/bin/nf-core", "refgenie": "/usr/local/bin/refgenie", "scalar": "/usr/local/bin/scalar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nf-core.
shpc-registry automated BioContainers addition for nf-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nf-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nf-core:2.6--pyh7cba7a3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nf-core/2.6--pyh7cba7a3_1
$ module help quay.io/biocontainers/nf-core/2.6--pyh7cba7a3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nf-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nf-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nf-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nf-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nf-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nf-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### import_igenome

```bash
$ singularity exec <container> /usr/local/bin/import_igenome
$ podman run --it --rm --entrypoint /usr/local/bin/import_igenome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_igenome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-hash

```bash
$ singularity exec <container> /usr/local/bin/mulled-hash
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-list

```bash
$ singularity exec <container> /usr/local/bin/mulled-list
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-update-singularity-containers

```bash
$ singularity exec <container> /usr/local/bin/mulled-update-singularity-containers
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-core

```bash
$ singularity exec <container> /usr/local/bin/nf-core
$ podman run --it --rm --entrypoint /usr/local/bin/nf-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refgenie

```bash
$ singularity exec <container> /usr/local/bin/refgenie
$ podman run --it --rm --entrypoint /usr/local/bin/refgenie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refgenie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scalar

```bash
$ singularity exec <container> /usr/local/bin/scalar
$ podman run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
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