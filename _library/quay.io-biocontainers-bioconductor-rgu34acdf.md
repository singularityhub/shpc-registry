---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgu34acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgu34acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgu34acdf/container.yaml"
updated_at: "2025-10-13 03:40:24.016927"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rgu34acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rgu34acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgu34acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgu34acdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:55048803471b09933c26d542835fe5eb0a35a4e5219a5845bba0e5ccbd3f2976"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:a57f0e9e3da0980d11f56daccaa085c531c1267450ff1cace1883934daed6297", "2.18.0--r42hdfd78af_10": "sha256:ec5c89634acd59710eda205dca4cbe9d697b03a76363c937c5b142d01e14ebce", "2.18.0--r43hdfd78af_11": "sha256:ace28946a8680bdacc8d4696dfaedbfaa6d9c7a187fc4d9d2331ccb298244bbd", "2.18.0--r43hdfd78af_12": "sha256:a8fdcd792f13d662ea12c55aa5469eab51d2ce26cdb9ec149dcf71218fb307ec", "2.18.0--r44hdfd78af_13": "sha256:55048803471b09933c26d542835fe5eb0a35a4e5219a5845bba0e5ccbd3f2976"}, "docker": "quay.io/biocontainers/bioconductor-rgu34acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgu34acdf.
shpc-registry automated BioContainers addition for bioconductor-rgu34acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34acdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgu34acdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rgu34acdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgu34acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgu34acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgu34acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgu34acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgu34acdf

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