---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedtcgadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedtcgadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedtcgadata/container.yaml"
updated_at: "2023-08-11 03:05:58.487565"
latest: "1.22.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedtcgadata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_1"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.22.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedtcgadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedtcgadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedtcgadata", "latest": {"1.22.2--r43hdfd78af_0": "sha256:41456a6767a4ba446026f6f7cbf319ea7421ed2c05ec2fdf024726c040ab8a1e"}, "tags": {"1.8.0--r36_0": "sha256:975d911f99fdae54b6b79d4fe5344d6a06d369f7c0745fbd72068f12f99274a6", "1.16.0--r41hdfd78af_1": "sha256:9af61b0dc3c452433a7c9a008f4637a351dd128560264c5686426d4f113c1be3", "1.14.0--r41hdfd78af_0": "sha256:05924190ec8385093a1b73edf89eefd8c0c8f58209b5a8cca4865d3598c9675d", "1.12.0--r40hdfd78af_1": "sha256:81e30aac57c442960b544e3f9a500cff5be026ad8f460cfcb23ecb304c94927a", "1.10.0--r40_0": "sha256:e6932b6812e39d9709c3cd7374250a0a5a2c89d3736ffcaa40d447895308bf89", "1.20.0--r42hdfd78af_0": "sha256:6ea17b204551c6cc7c981ad782dabd45e8b4b1d435b3cdefcbb3d6926bcefc74", "1.22.2--r43hdfd78af_0": "sha256:41456a6767a4ba446026f6f7cbf319ea7421ed2c05ec2fdf024726c040ab8a1e"}, "docker": "quay.io/biocontainers/bioconductor-curatedtcgadata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedtcgadata.
shpc-registry automated BioContainers addition for bioconductor-curatedtcgadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedtcgadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedtcgadata:1.22.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedtcgadata/1.22.2--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedtcgadata/1.22.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedtcgadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedtcgadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedtcgadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedtcgadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedtcgadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedtcgadata-inspect-deffile:

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