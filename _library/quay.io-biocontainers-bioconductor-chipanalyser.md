---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipanalyser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipanalyser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipanalyser/container.yaml"
updated_at: "2024-01-26 02:33:30.962783"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipanalyser"
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
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipanalyser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipanalyser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipanalyser", "latest": {"1.24.0--r43hdfd78af_0": "sha256:23ff1f675bc80a1d24663c53b7284a3d90dc0423c47bee875647787dd18d1dcf"}, "tags": {"1.8.0--r36_0": "sha256:2935eee980d355ceca1583a15a68fd64d2bce60ae405f40bf4416a7e7e1c7cef", "1.20.0--r42hdfd78af_0": "sha256:5b54a29c1b558af0709b9b77622b8288ca2c1433a0ea20de1e04128d10a960d8", "1.16.0--r41hdfd78af_0": "sha256:28ad1f9f1500d36c691ea621ebd5cc759b5a541684437729ad50eb6605a1f9d6", "1.14.0--r41hdfd78af_0": "sha256:591bf55a35286d3e43df4b081255b99d1e76f69002a54cb48a630ca90779b843", "1.12.0--r40hdfd78af_1": "sha256:bcfcc65c7e2884f1911564061abf68e8c093fbaa1ba962fb84abde48e5bb1213", "1.10.0--r40_0": "sha256:5019cba4dca800565d1a13196d15ddaf3e2fe58b67ecd65de24affe717734612", "1.22.0--r43hdfd78af_0": "sha256:f873f2d34ccf18f992f11d6c954bb075d60afab21ce41bdae4dd9d7cbf41ee1d", "1.24.0--r43hdfd78af_0": "sha256:23ff1f675bc80a1d24663c53b7284a3d90dc0423c47bee875647787dd18d1dcf"}, "docker": "quay.io/biocontainers/bioconductor-chipanalyser", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipanalyser.
shpc-registry automated BioContainers addition for bioconductor-chipanalyser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipanalyser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipanalyser:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipanalyser/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipanalyser/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipanalyser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipanalyser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipanalyser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipanalyser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipanalyser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipanalyser-inspect-deffile:

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