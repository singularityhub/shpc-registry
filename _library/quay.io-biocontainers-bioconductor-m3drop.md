---
layout: container
name:  "quay.io/biocontainers/bioconductor-m3drop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-m3drop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-m3drop/container.yaml"
updated_at: "2024-12-08 03:38:08.278811"
latest: "1.28.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-m3drop"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-m3drop"
config: {"url": "https://biocontainers.pro/tools/bioconductor-m3drop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-m3drop", "latest": {"1.28.0--r43hdfd78af_1": "sha256:b0383a57f297265f264d321d8fb16d6e2dad6a0f6e25ccceba84ab2843f2eff7"}, "tags": {"1.8.1--r351_0": "sha256:a31efb69b8a66ec7809d14789a05130310d14fb37a71d307bfe526a33a04fa23", "1.24.0--r42hdfd78af_0": "sha256:87d82693a2b4626d9b37f3d90c9b5a807f25396ac2f06cc18c3273e021b12b12", "1.20.0--r41hdfd78af_0": "sha256:70b157334d49a50ee16ea18f99fe35ba38d6250f7bb91152578d8944be441f25", "1.18.0--r41hdfd78af_0": "sha256:b18efacdbcaff3cc0d5e849e4fbf9d44939cb4bc1af59791f48ee7811b43cc1e", "1.16.0--r40hdfd78af_1": "sha256:2dd3b058e1cf615b7e59a269efa164da2ba21268f5776e131a703b08d274bf41", "1.14.0--r40_0": "sha256:0124e008daa2e8ffe21b7da9a7349a4aee05f2b1a3634f136707b02c3280670f", "1.26.0--r43hdfd78af_0": "sha256:d85fb2ea3b4b7ca393a38138c1e462e381d95ce0202c0de8672bc7d0b75e8aff", "1.28.0--r43hdfd78af_1": "sha256:b0383a57f297265f264d321d8fb16d6e2dad6a0f6e25ccceba84ab2843f2eff7"}, "docker": "quay.io/biocontainers/bioconductor-m3drop", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-m3drop.
shpc-registry automated BioContainers addition for bioconductor-m3drop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-m3drop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-m3drop:1.28.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-m3drop/1.28.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-m3drop/1.28.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-m3drop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m3drop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m3drop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-m3drop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-m3drop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-m3drop-inspect-deffile:

```bash
$ singularity inspect -d <container>
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