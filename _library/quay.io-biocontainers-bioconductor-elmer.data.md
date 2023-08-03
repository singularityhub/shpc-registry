---
layout: container
name:  "quay.io/biocontainers/bioconductor-elmer.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-elmer.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-elmer.data/container.yaml"
updated_at: "2023-08-03 03:17:01.217938"
latest: "2.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-elmer.data"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.18.0--r41hdfd78af_1"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.12.0--r40_0"
 - "2.10.0--r36_0"
 - "2.22.0--r42hdfd78af_0"
 - "2.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-elmer.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-elmer.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-elmer.data", "latest": {"2.24.0--r43hdfd78af_0": "sha256:2992b3bea8b1a81a5ae14de63bdaae6d1616183f2eeae871ede40cb6865fee09"}, "tags": {"2.8.0--r36_1": "sha256:7b9ea7716d40a1d8062505afc59b1c78f0033dc40212c77bf08a0744079cc5da", "2.18.0--r41hdfd78af_1": "sha256:a774b357770b0065eae1262890a3ab39e05c4999c60d1a0354bf502336fc23cb", "2.16.0--r41hdfd78af_0": "sha256:4f8dcd66c23fa9b1f159c52dbd151d78edc9574aade330aa8dad0588ee580007", "2.14.0--r40hdfd78af_1": "sha256:36acc96a59338b4a09f674e25a1b7e9696057789022ae6115b0be2359fa2db1b", "2.12.0--r40_0": "sha256:bbfe2939dc922aeb47eed84e2859c3e375975a00eb513c6503d723a986b8b20c", "2.10.0--r36_0": "sha256:de4ee4b93ed5da36934b3eeec8672f9f847354f970e6243a6e4f99d69e3a33a3", "2.22.0--r42hdfd78af_0": "sha256:7ea808590ce5a7b4eac2d55b1f9766648c8f189a61a5cedfeaffbd337c426605", "2.24.0--r43hdfd78af_0": "sha256:2992b3bea8b1a81a5ae14de63bdaae6d1616183f2eeae871ede40cb6865fee09"}, "docker": "quay.io/biocontainers/bioconductor-elmer.data", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-elmer.data.
shpc-registry automated BioContainers addition for bioconductor-elmer.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-elmer.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-elmer.data:2.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-elmer.data/2.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-elmer.data/2.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-elmer.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-elmer.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-elmer.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-elmer.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-elmer.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-elmer.data-inspect-deffile:

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