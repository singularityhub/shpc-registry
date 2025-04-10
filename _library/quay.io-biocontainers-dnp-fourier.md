---
layout: container
name:  "quay.io/biocontainers/dnp-fourier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnp-fourier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnp-fourier/container.yaml"
updated_at: "2025-04-10 03:40:08.017105"
latest: "1.0--h503566f_6"
container_url: "https://biocontainers.pro/tools/dnp-fourier"
aliases:
 - "dnp-fourier"
versions:
 - "1.0--h87f3376_3"
 - "1.0--h87f3376_4"
 - "1.0--hdbdd923_5"
 - "1.0--h503566f_6"
description: "shpc-registry automated BioContainers addition for dnp-fourier"
config: {"url": "https://biocontainers.pro/tools/dnp-fourier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnp-fourier", "latest": {"1.0--h503566f_6": "sha256:f7d46b1b6305419ded2c2ef4a8f7efb02f5f29dad9293b0d534e93604ed63ca3"}, "tags": {"1.0--h87f3376_3": "sha256:5876b3d64a4e0efc23a01378557fcd6cf0c3178bab69c3ada307d6ffb3fc3407", "1.0--h87f3376_4": "sha256:945e437e9f0dc5069f3b88d537be1eb567f7d869afbaabb426d8dfb9bb2493e7", "1.0--hdbdd923_5": "sha256:98f1de2e4131260ebcb614e9c74389c922c603eaafc6067165eb46232cac31f5", "1.0--h503566f_6": "sha256:f7d46b1b6305419ded2c2ef4a8f7efb02f5f29dad9293b0d534e93604ed63ca3"}, "docker": "quay.io/biocontainers/dnp-fourier", "aliases": {"dnp-fourier": "/usr/local/bin/dnp-fourier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnp-fourier.
shpc-registry automated BioContainers addition for dnp-fourier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnp-fourier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnp-fourier:1.0--h503566f_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnp-fourier/1.0--h503566f_6
$ module help quay.io/biocontainers/dnp-fourier/1.0--h503566f_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnp-fourier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnp-fourier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnp-fourier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnp-fourier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnp-fourier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnp-fourier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnp-fourier

```bash
$ singularity exec <container> /usr/local/bin/dnp-fourier
$ podman run --it --rm --entrypoint /usr/local/bin/dnp-fourier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnp-fourier   -v ${PWD} -w ${PWD} <container> -c " $@"
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