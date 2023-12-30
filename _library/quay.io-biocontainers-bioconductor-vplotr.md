---
layout: container
name:  "quay.io/biocontainers/bioconductor-vplotr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vplotr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vplotr/container.yaml"
updated_at: "2023-12-30 02:31:21.196643"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vplotr"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vplotr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vplotr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vplotr", "latest": {"1.10.0--r43hdfd78af_0": "sha256:262533fb491c322b7ffb60a19c18938aa152df049fe225e94489364be495b987"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:eb9697bbd8daba492c48a0f6b16350ca6d1f086e9d674e8c09e7e303f23a02a1", "1.8.0--r42hdfd78af_0": "sha256:cc06929d5245d2d98399539e1279b314c327194e94d1612198170ed653081c3c", "1.10.0--r43hdfd78af_0": "sha256:262533fb491c322b7ffb60a19c18938aa152df049fe225e94489364be495b987"}, "docker": "quay.io/biocontainers/bioconductor-vplotr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vplotr.
shpc-registry automated BioContainers addition for bioconductor-vplotr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vplotr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vplotr:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vplotr/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-vplotr/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vplotr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vplotr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vplotr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vplotr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vplotr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vplotr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vplotr

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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