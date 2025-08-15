---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtu34cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtu34cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtu34cdf/container.yaml"
updated_at: "2025-08-15 04:14:12.253506"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rtu34cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rtu34cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtu34cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtu34cdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:91d5016cc502efa322f935a9ce39f59e1155588e81d9b9db8986d9cf86f790f0"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:aa8524a5d81b84f9e609cd329e6cfc0b22cd5958f1612bea4cd973f7d351e0be", "2.18.0--r42hdfd78af_10": "sha256:4ee6656a7419978e1f28f12e97909830c861acb88203e1cfbed978ec39341f6b", "2.18.0--r43hdfd78af_11": "sha256:50e4e8b8c131baa882e8b8a78643ec9bab9dd2b92923cc4bdce2c66a2a38ff4c", "2.18.0--r43hdfd78af_12": "sha256:f08a140d2fdcb2c524875e05936db3d416e5ec6195b2ba75efb4a8117454a4e9", "2.18.0--r44hdfd78af_13": "sha256:91d5016cc502efa322f935a9ce39f59e1155588e81d9b9db8986d9cf86f790f0"}, "docker": "quay.io/biocontainers/bioconductor-rtu34cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtu34cdf.
shpc-registry automated BioContainers addition for bioconductor-rtu34cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtu34cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtu34cdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtu34cdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rtu34cdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtu34cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtu34cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtu34cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtu34cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtu34cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtu34cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtu34cdf

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