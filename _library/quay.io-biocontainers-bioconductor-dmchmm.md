---
layout: container
name:  "quay.io/biocontainers/bioconductor-dmchmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dmchmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dmchmm/container.yaml"
updated_at: "2024-05-24 02:33:38.484694"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dmchmm"
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
description: "shpc-registry automated BioContainers addition for bioconductor-dmchmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dmchmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dmchmm", "latest": {"1.24.0--r43hdfd78af_0": "sha256:59aee73f0f98535ad35e4b904af3572cc0b8a89f3f0fd4d12b4cf3b97abbd0a9"}, "tags": {"1.8.0--r36_0": "sha256:e2bf7f338a9397ea162ebb3a2e2bb3c058b3cefa86bf8e25167d011a8055712f", "1.20.0--r42hdfd78af_0": "sha256:90d8cf3f06148004ece961f8695732e9b339cffad46c709e25579cad2b756841", "1.16.0--r41hdfd78af_0": "sha256:589129c28691440b7eec2e47aeb74e99ccdfeca1fa31b2acb588b04f476f5a0a", "1.14.0--r41hdfd78af_0": "sha256:7cd822eee8e8e2f2283acf9f5c0592cdb638d044f4c4c84a090bc5fea66fddd8", "1.12.0--r40hdfd78af_1": "sha256:24b677e4d588aa3967536e8fb345e7574a2b93ca30b12a8264bd92ddb266b866", "1.10.0--r40_0": "sha256:fc67f892ca3d23892564a7e218f7d20df8b776835090d871ad96a6715ccc9439", "1.22.0--r43hdfd78af_0": "sha256:90ee3342c59d2e1d714a7d33ceaadd6e931219d7046db9555fcfdabebc653d35", "1.24.0--r43hdfd78af_0": "sha256:59aee73f0f98535ad35e4b904af3572cc0b8a89f3f0fd4d12b4cf3b97abbd0a9"}, "docker": "quay.io/biocontainers/bioconductor-dmchmm", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dmchmm.
shpc-registry automated BioContainers addition for bioconductor-dmchmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dmchmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dmchmm:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dmchmm/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dmchmm/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dmchmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmchmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmchmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dmchmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dmchmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dmchmm-inspect-deffile:

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