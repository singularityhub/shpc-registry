---
layout: container
name:  "quay.io/biocontainers/snver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snver/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/snver/container.yaml"
updated_at: "2022-10-27 01:13:24.927582"
latest: "0.5.3--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/snver"
aliases:
 - "snver"
 - "snver-pool"
versions:
 - "0.5.3--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for snver"
config: {"url": "https://biocontainers.pro/tools/snver", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snver", "latest": {"0.5.3--hdfd78af_1": "sha256:0e85cfc9cd3b22796a18374a2ceff2d94feab778ac4f76f5c51b3cb45350a158"}, "tags": {"0.5.3--hdfd78af_1": "sha256:0e85cfc9cd3b22796a18374a2ceff2d94feab778ac4f76f5c51b3cb45350a158"}, "docker": "quay.io/biocontainers/snver", "aliases": {"snver": "/usr/local/bin/snver", "snver-pool": "/usr/local/bin/snver-pool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snver.
shpc-registry automated BioContainers addition for snver
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snver
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snver:0.5.3--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snver/0.5.3--hdfd78af_1
$ module help quay.io/biocontainers/snver/0.5.3--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snver

```bash
$ singularity exec <container> /usr/local/bin/snver
$ podman run --it --rm --entrypoint /usr/local/bin/snver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snver-pool

```bash
$ singularity exec <container> /usr/local/bin/snver-pool
$ podman run --it --rm --entrypoint /usr/local/bin/snver-pool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snver-pool   -v ${PWD} -w ${PWD} <container> -c " $@"
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