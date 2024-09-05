---
layout: container
name:  "quay.io/biocontainers/bioconductor-dupradar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dupradar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dupradar/container.yaml"
updated_at: "2024-09-05 04:46:54.687322"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dupradar"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_1"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_1"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dupradar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dupradar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dupradar", "latest": {"1.32.0--r43hdfd78af_0": "sha256:74448027f03ccd5a6b04ed5a073499a660ec3076401e2d03bbaf7e86f5b34dd3"}, "tags": {"1.8.0--r3.4.1_1": "sha256:b8f7fe99d93b1d9c1570b3298fbf078fb03bdd78211c08bd2aec121d28237e0b", "1.28.0--r42hdfd78af_0": "sha256:5b28ed9c23f94916d707a8378ae81784a02389ef937f31f28b672aaff264b7bd", "1.24.0--r41hdfd78af_0": "sha256:e1c3b900d8e2f6c006a083e32ef6598d8a22a2419eb1a5a623df3831863ac85e", "1.22.0--r41hdfd78af_0": "sha256:05c84eb552473d9fbeca0ff3465229207238e77ac15ee5710aa9885f5c0b38b0", "1.20.0--r40hdfd78af_1": "sha256:d15305aae8ab25b523580272bb6a8630f6c872a6b60421c6a8ffe5684b350b80", "1.18.0--r40_1": "sha256:7258496709eb73e9e4e339d10f6b912ef598fedb79d8ccfd31ca35044cfbc86e", "1.30.0--r43hdfd78af_0": "sha256:71fd4a59618bb6a82bae7d14035052e91fbe8d268a3cc408f039b9d8866a7434", "1.32.0--r43hdfd78af_0": "sha256:74448027f03ccd5a6b04ed5a073499a660ec3076401e2d03bbaf7e86f5b34dd3"}, "docker": "quay.io/biocontainers/bioconductor-dupradar", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dupradar.
shpc-registry automated BioContainers addition for bioconductor-dupradar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dupradar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dupradar:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dupradar/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dupradar/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dupradar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dupradar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dupradar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dupradar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dupradar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dupradar-inspect-deffile:

```bash
$ singularity inspect -d <container>
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