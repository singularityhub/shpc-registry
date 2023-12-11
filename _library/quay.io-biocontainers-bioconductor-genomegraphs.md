---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomegraphs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomegraphs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomegraphs/container.yaml"
updated_at: "2023-12-11 02:30:36.156821"
latest: "1.46.0--r36_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomegraphs"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.46.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomegraphs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomegraphs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomegraphs", "latest": {"1.46.0--r36_0": "sha256:5b2ced05568ef0ce29167fab622ef225fe5cf41ed216d2d27419bba3a31e9b28"}, "tags": {"1.46.0--r36_0": "sha256:5b2ced05568ef0ce29167fab622ef225fe5cf41ed216d2d27419bba3a31e9b28"}, "docker": "quay.io/biocontainers/bioconductor-genomegraphs", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomegraphs.
shpc-registry automated BioContainers addition for bioconductor-genomegraphs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomegraphs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomegraphs:1.46.0--r36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomegraphs/1.46.0--r36_0
$ module help quay.io/biocontainers/bioconductor-genomegraphs/1.46.0--r36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomegraphs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomegraphs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomegraphs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomegraphs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomegraphs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomegraphs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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