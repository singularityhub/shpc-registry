---
layout: container
name:  "quay.io/biocontainers/bioconductor-dcgsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dcgsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dcgsa/container.yaml"
updated_at: "2024-04-23 03:04:01.875420"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dcgsa"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dcgsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dcgsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dcgsa", "latest": {"1.30.0--r43hdfd78af_0": "sha256:8d6f7e7ca68d362f2ce3c5dd66cbeff711d9f90b65e0a21ce7287b1d0afcf7fb"}, "tags": {"1.8.0--r351_0": "sha256:09db37fa214f3037777623aef811f5697d5305e15409aaa67c40b6e4769fc42b", "1.26.0--r42hdfd78af_0": "sha256:9ac558605f0f8019eca0d2c71e9f4f1229c28ee465c77746baf814190f6dfa9d", "1.22.0--r41hdfd78af_0": "sha256:c05588f6b4fa1644d7884b84362d8d542766f90290c3a7a9a979f7a3dc5b0b70", "1.20.0--r41hdfd78af_0": "sha256:641e2574acaedf5ab4d4bc1d09d9cc1a6c7252feb14299d59f596b5f7753b841", "1.18.0--r40hdfd78af_1": "sha256:2572b15f0398c423bdf6167cc9a77bff718da299bca9c6e1dbcd5586531be298", "1.16.0--r40_0": "sha256:bb7bfbd55a4fe0084e28f10fd6edc5d35589fed62c1267caa1e341931ea46870", "1.28.0--r43hdfd78af_0": "sha256:103348eb8f9d90b23ab38851a5b998d56690373494e8d57c95e21f610cb2063b", "1.30.0--r43hdfd78af_0": "sha256:8d6f7e7ca68d362f2ce3c5dd66cbeff711d9f90b65e0a21ce7287b1d0afcf7fb"}, "docker": "quay.io/biocontainers/bioconductor-dcgsa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dcgsa.
shpc-registry automated BioContainers addition for bioconductor-dcgsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dcgsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dcgsa:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dcgsa/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dcgsa/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dcgsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dcgsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dcgsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dcgsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dcgsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dcgsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dcgsa

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