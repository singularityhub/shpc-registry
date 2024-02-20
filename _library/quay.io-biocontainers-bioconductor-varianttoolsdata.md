---
layout: container
name:  "quay.io/biocontainers/bioconductor-varianttoolsdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-varianttoolsdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-varianttoolsdata/container.yaml"
updated_at: "2024-02-20 02:47:10.196520"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-varianttoolsdata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_1"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-varianttoolsdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-varianttoolsdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-varianttoolsdata", "latest": {"1.26.0--r43hdfd78af_0": "sha256:f4cfda74a27e7361e344cdfd4a338451a1b316e21ffb57436102e0165a1c47ea"}, "tags": {"1.8.0--r36_1": "sha256:cc5b0da1cddb5df9031ede5bef86ef5be44d7e7fba6269842fdb87a77cddffca", "1.22.0--r42hdfd78af_0": "sha256:c2ee128e6b209aea057b9b9225f312f81ca94e682ea89bc0f98e8b1ff39f67d4", "1.18.0--r41hdfd78af_1": "sha256:69e0fcb66f771698c89f36e965b23e7084f49984a30315598b8a46036bfbf363", "1.16.0--r41hdfd78af_0": "sha256:ff3d2eb8f5deaf83f4a3c75204fec59b84f438ee425a66873d1449f0fb023067", "1.14.0--r40hdfd78af_1": "sha256:abf048534da6a237a0ab1e59b5afeb7fd0e3ed90a8fedb67f7793ce2ad171b74", "1.12.0--r40_0": "sha256:49093644aeb599b423f227f0f60c8d5c97eea6df9c05748fc3808a5e005132b6", "1.24.0--r43hdfd78af_0": "sha256:7b00b230c71ee45fd0b7ffba84c02eaf8638afce1ab4b894545583f8735715d0", "1.26.0--r43hdfd78af_0": "sha256:f4cfda74a27e7361e344cdfd4a338451a1b316e21ffb57436102e0165a1c47ea"}, "docker": "quay.io/biocontainers/bioconductor-varianttoolsdata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-varianttoolsdata.
shpc-registry automated BioContainers addition for bioconductor-varianttoolsdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-varianttoolsdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-varianttoolsdata:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-varianttoolsdata/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-varianttoolsdata/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-varianttoolsdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varianttoolsdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varianttoolsdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-varianttoolsdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-varianttoolsdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-varianttoolsdata-inspect-deffile:

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