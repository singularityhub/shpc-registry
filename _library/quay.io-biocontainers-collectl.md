---
layout: container
name:  "quay.io/biocontainers/collectl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/collectl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/collectl/container.yaml"
updated_at: "2025-09-08 03:23:06.268551"
latest: "4.0.4--pl5.22.0_3"
container_url: "https://biocontainers.pro/tools/collectl"
aliases:
 - "collectl"
 - "colmux"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "podselect"
versions:
 - "4.0.4--pl5.22.0_3"
description: "shpc-registry automated BioContainers addition for collectl"
config: {"url": "https://biocontainers.pro/tools/collectl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for collectl", "latest": {"4.0.4--pl5.22.0_3": "sha256:8db3314952f1e1c1d75c9e29daa770c0aa1c2ab2b66ac11b79bf3b117db143c0"}, "tags": {"4.0.4--pl5.22.0_3": "sha256:8db3314952f1e1c1d75c9e29daa770c0aa1c2ab2b66ac11b79bf3b117db143c0"}, "docker": "quay.io/biocontainers/collectl", "aliases": {"collectl": "/usr/local/bin/collectl", "colmux": "/usr/local/bin/colmux", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/collectl.
shpc-registry automated BioContainers addition for collectl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/collectl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/collectl:4.0.4--pl5.22.0_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/collectl/4.0.4--pl5.22.0_3
$ module help quay.io/biocontainers/collectl/4.0.4--pl5.22.0_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### collectl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### collectl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### collectl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### collectl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### collectl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### collectl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### collectl

```bash
$ singularity exec <container> /usr/local/bin/collectl
$ podman run --it --rm --entrypoint /usr/local/bin/collectl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/collectl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colmux

```bash
$ singularity exec <container> /usr/local/bin/colmux
$ podman run --it --rm --entrypoint /usr/local/bin/colmux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colmux   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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