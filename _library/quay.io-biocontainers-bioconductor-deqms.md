---
layout: container
name:  "quay.io/biocontainers/bioconductor-deqms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deqms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deqms/container.yaml"
updated_at: "2025-10-29 03:33:25.584628"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-deqms"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.11.1--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-deqms"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deqms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deqms", "latest": {"1.24.0--r44hdfd78af_0": "sha256:882c6317997094561993303d228464f9fa3fcd2086ac88201126dffe48b306f5"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:35eba855e5c3e119319cd27d88a9ded1d6c6d33cecf28faf0bd3b45ddf1c21d9", "1.16.0--r42hdfd78af_0": "sha256:31061354d2a39483077babf7054a547d0a35e3920b5c5522a32b766e52d5ac6d", "1.11.1--r41hdfd78af_0": "sha256:5820795018abd49508cc9c2063c17cbc4a4deaab081205aa59da6e88a6badc20", "1.10.0--r41hdfd78af_0": "sha256:9f2f648f39dea20039775e40096e2f1d0e8dc1588604d80f52e1f4edca2173a2", "1.18.0--r43hdfd78af_0": "sha256:616ba4894b4d62dd8f11af8f57b56c6bec77efd76e5ffc5e158dc6a247ed8ec9", "1.20.0--r43hdfd78af_0": "sha256:7e3b6cdaf850d3d607ae7890d3c533e798e7883fa04bbca9a284d8550a39cae4", "1.24.0--r44hdfd78af_0": "sha256:882c6317997094561993303d228464f9fa3fcd2086ac88201126dffe48b306f5"}, "docker": "quay.io/biocontainers/bioconductor-deqms", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deqms.
shpc-registry automated BioContainers addition for bioconductor-deqms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deqms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deqms:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deqms/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-deqms/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deqms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deqms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deqms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deqms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deqms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deqms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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