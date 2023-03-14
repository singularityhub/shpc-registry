---
layout: container
name:  "quay.io/biocontainers/bioconductor-epivizrchart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epivizrchart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epivizrchart/container.yaml"
updated_at: "2023-03-14 03:26:08.354090"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epivizrchart"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epivizrchart"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epivizrchart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epivizrchart", "latest": {"1.20.0--r42hdfd78af_0": "sha256:c4327dee9509606e59c624bae0d4047aeec60e12d0ce3040735c417973b7f197"}, "tags": {"1.8.0--r36_0": "sha256:357732096555a243a49939dc698d49af92476564970fc6fd62f4b617a2f14465", "1.20.0--r42hdfd78af_0": "sha256:c4327dee9509606e59c624bae0d4047aeec60e12d0ce3040735c417973b7f197", "1.16.0--r41hdfd78af_0": "sha256:fcd61033573487f8f9167e989970b883f29bdf2161a53cd336320306c5d11047", "1.14.0--r41hdfd78af_0": "sha256:ccfe607615bc3ca2ef5fb8e350c4d14a5ab5bc1677858cadaa43b9d3cde6eeab", "1.12.0--r40hdfd78af_1": "sha256:e2c7ab74f059c66cbba5a7097a7f63cd17b3c11cbf859546ceb87a38791eb7a7", "1.10.0--r40_0": "sha256:213243b2bd2e448407cbc2ebeff5291a3b532ecf1d4a447b08d84034898c0c78"}, "docker": "quay.io/biocontainers/bioconductor-epivizrchart", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epivizrchart.
shpc-registry automated BioContainers addition for bioconductor-epivizrchart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrchart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrchart:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epivizrchart/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epivizrchart/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epivizrchart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrchart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrchart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epivizrchart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epivizrchart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epivizrchart-inspect-deffile:

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