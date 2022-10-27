---
layout: container
name:  "quay.io/biocontainers/ggcaller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ggcaller/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ggcaller/container.yaml"
updated_at: "2022-10-27 00:30:39.665079"
latest: "1.3.0--py38hee2cf1e_1"
container_url: "https://biocontainers.pro/tools/ggcaller"
aliases:
 - "Bifrost"
 - "ggcaller"
 - "rapidnj"
versions:
 - "1.3.0--py38hee2cf1e_1"
description: "shpc-registry automated BioContainers addition for ggcaller"
config: {"url": "https://biocontainers.pro/tools/ggcaller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ggcaller", "latest": {"1.3.0--py38hee2cf1e_1": "sha256:83f27a9a7b57fa0c0fe140774c18b4992d8678fff7291edd3a7718b931f3b412"}, "tags": {"1.3.0--py38hee2cf1e_1": "sha256:83f27a9a7b57fa0c0fe140774c18b4992d8678fff7291edd3a7718b931f3b412"}, "docker": "quay.io/biocontainers/ggcaller", "aliases": {"Bifrost": "/usr/local/bin/Bifrost", "ggcaller": "/usr/local/bin/ggcaller", "rapidnj": "/usr/local/bin/rapidnj"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ggcaller.
shpc-registry automated BioContainers addition for ggcaller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ggcaller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ggcaller:1.3.0--py38hee2cf1e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ggcaller/1.3.0--py38hee2cf1e_1
$ module help quay.io/biocontainers/ggcaller/1.3.0--py38hee2cf1e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ggcaller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ggcaller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ggcaller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ggcaller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ggcaller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ggcaller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bifrost

```bash
$ singularity exec <container> /usr/local/bin/Bifrost
$ podman run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ggcaller

```bash
$ singularity exec <container> /usr/local/bin/ggcaller
$ podman run --it --rm --entrypoint /usr/local/bin/ggcaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ggcaller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidnj

```bash
$ singularity exec <container> /usr/local/bin/rapidnj
$ podman run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
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