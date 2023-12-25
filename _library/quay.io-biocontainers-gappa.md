---
layout: container
name:  "quay.io/biocontainers/gappa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gappa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gappa/container.yaml"
updated_at: "2023-12-25 02:43:37.578181"
latest: "0.8.4--hdcf5f25_0"
container_url: "https://biocontainers.pro/tools/gappa"
aliases:
 - "gappa"
versions:
 - "0.8.0--hd03093a_1"
 - "0.8.0--hdcf5f25_3"
 - "0.8.4--hdcf5f25_0"
description: "shpc-registry automated BioContainers addition for gappa"
config: {"url": "https://biocontainers.pro/tools/gappa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gappa", "latest": {"0.8.4--hdcf5f25_0": "sha256:46aa7fbd8bb9e3c4eca381a0faa45e3c8c4fd09e8127364b9c9cde2c65d75467"}, "tags": {"0.8.0--hd03093a_1": "sha256:de63bd594a237f8afd1ec2d0e3c9be70938a03b70491b2ff645a41cebcaed0f6", "0.8.0--hdcf5f25_3": "sha256:c9aaf12447e4c74d5aca027b26cb430842680b7ab3f0cb823fc4e40cbf680088", "0.8.4--hdcf5f25_0": "sha256:46aa7fbd8bb9e3c4eca381a0faa45e3c8c4fd09e8127364b9c9cde2c65d75467"}, "docker": "quay.io/biocontainers/gappa", "aliases": {"gappa": "/usr/local/bin/gappa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gappa.
shpc-registry automated BioContainers addition for gappa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gappa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gappa:0.8.4--hdcf5f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gappa/0.8.4--hdcf5f25_0
$ module help quay.io/biocontainers/gappa/0.8.4--hdcf5f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gappa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gappa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gappa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gappa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gappa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gappa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gappa

```bash
$ singularity exec <container> /usr/local/bin/gappa
$ podman run --it --rm --entrypoint /usr/local/bin/gappa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gappa   -v ${PWD} -w ${PWD} <container> -c " $@"
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