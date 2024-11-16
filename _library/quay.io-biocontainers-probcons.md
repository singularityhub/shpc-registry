---
layout: container
name:  "quay.io/biocontainers/probcons"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/probcons/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/probcons/container.yaml"
updated_at: "2024-11-16 03:27:23.606093"
latest: "1.12--h8b12597_1"
container_url: "https://biocontainers.pro/tools/probcons"
aliases:
 - "probcons"
 - "compare"
versions:
 - "1.12--h8b12597_1"
description: "shpc-registry automated BioContainers addition for probcons"
config: {"url": "https://biocontainers.pro/tools/probcons", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for probcons", "latest": {"1.12--h8b12597_1": "sha256:27e2e1eb2b58a10e23554df3c8c38af7f81f11c7992349cbc2802917f088e07d"}, "tags": {"1.12--h8b12597_1": "sha256:27e2e1eb2b58a10e23554df3c8c38af7f81f11c7992349cbc2802917f088e07d"}, "docker": "quay.io/biocontainers/probcons", "aliases": {"probcons": "/usr/local/bin/probcons", "compare": "/usr/local/bin/compare"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/probcons.
shpc-registry automated BioContainers addition for probcons
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/probcons
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/probcons:1.12--h8b12597_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/probcons/1.12--h8b12597_1
$ module help quay.io/biocontainers/probcons/1.12--h8b12597_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### probcons-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### probcons-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### probcons-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### probcons-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### probcons-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### probcons-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### probcons

```bash
$ singularity exec <container> /usr/local/bin/probcons
$ podman run --it --rm --entrypoint /usr/local/bin/probcons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probcons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare

```bash
$ singularity exec <container> /usr/local/bin/compare
$ podman run --it --rm --entrypoint /usr/local/bin/compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare   -v ${PWD} -w ${PWD} <container> -c " $@"
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