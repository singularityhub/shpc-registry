---
layout: container
name:  "quay.io/biocontainers/selscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/selscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/selscan/container.yaml"
updated_at: "2023-05-05 03:17:07.650688"
latest: "1.2.0a--h0fdf51a_4"
container_url: "https://biocontainers.pro/tools/selscan"
aliases:
 - "norm"
 - "selscan"
versions:
 - "1.2.0a--h0fdf51a_4"
description: "shpc-registry automated BioContainers addition for selscan"
config: {"url": "https://biocontainers.pro/tools/selscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for selscan", "latest": {"1.2.0a--h0fdf51a_4": "sha256:9aecb16dd630cfc483aea257e45608250e388861730e5220ed7a2ccd3750c21e"}, "tags": {"1.2.0a--h0fdf51a_4": "sha256:9aecb16dd630cfc483aea257e45608250e388861730e5220ed7a2ccd3750c21e"}, "docker": "quay.io/biocontainers/selscan", "aliases": {"norm": "/usr/local/bin/norm", "selscan": "/usr/local/bin/selscan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/selscan.
shpc-registry automated BioContainers addition for selscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/selscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/selscan:1.2.0a--h0fdf51a_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/selscan/1.2.0a--h0fdf51a_4
$ module help quay.io/biocontainers/selscan/1.2.0a--h0fdf51a_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### selscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### selscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### selscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### selscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### selscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### selscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### norm

```bash
$ singularity exec <container> /usr/local/bin/norm
$ podman run --it --rm --entrypoint /usr/local/bin/norm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/norm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### selscan

```bash
$ singularity exec <container> /usr/local/bin/selscan
$ podman run --it --rm --entrypoint /usr/local/bin/selscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selscan   -v ${PWD} -w ${PWD} <container> -c " $@"
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