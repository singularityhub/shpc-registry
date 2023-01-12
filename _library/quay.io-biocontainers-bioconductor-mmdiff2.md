---
layout: container
name:  "quay.io/biocontainers/bioconductor-mmdiff2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mmdiff2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mmdiff2/container.yaml"
updated_at: "2023-01-12 02:57:07.462188"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mmdiff2"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.14.0--r36_0"
 - "1.26.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mmdiff2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mmdiff2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mmdiff2", "latest": {"1.26.0--r42hdfd78af_0": "sha256:99eaef311d2a2a2becce6aa5ba59f74f5f780ab8ced6934141c4b7633c81013e"}, "tags": {"1.8.0--r341_0": "sha256:8d57bafc53fb3cae67e200465edc80b410f6122b746843fc874b15289a3b4a70", "1.22.0--r41hdfd78af_0": "sha256:a024e36ba6a9591c5e7c5885c15055a75cf3c989bd9de5e7c20a0fd218dbd6f6", "1.20.0--r41hdfd78af_0": "sha256:914cdb1d6aa6ca31cbc1dec70a99365de9d1e74bd751b1c46c07860c777bd4cf", "1.18.0--r40hdfd78af_1": "sha256:82f2881232085e6982640214234f9a57011800ffebb29bbeaae4d611e50951ad", "1.16.0--r40_0": "sha256:4ac7b5069ddaf1846ef2a2f1748e7536e633d7f25fa5938262070d636189a18a", "1.14.0--r36_0": "sha256:569d9596d2412bae9fd4787258efa228b0e91f281db482be8ccd93cba0b5b3df", "1.26.0--r42hdfd78af_0": "sha256:99eaef311d2a2a2becce6aa5ba59f74f5f780ab8ced6934141c4b7633c81013e"}, "docker": "quay.io/biocontainers/bioconductor-mmdiff2", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mmdiff2.
shpc-registry automated BioContainers addition for bioconductor-mmdiff2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mmdiff2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mmdiff2:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mmdiff2/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mmdiff2/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mmdiff2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmdiff2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmdiff2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mmdiff2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mmdiff2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mmdiff2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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