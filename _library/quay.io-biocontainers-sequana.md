---
layout: container
name:  "quay.io/biocontainers/sequana"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sequana/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sequana/container.yaml"
updated_at: "2025-10-29 03:48:33.829402"
latest: "0.19.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sequana"

versions:
 - "0.8.2--py36h4c5857e_1"
 - "0.14.3--pyh7cba7a3_0"
 - "0.13.2--pyh5e36f6f_0"
 - "0.15.1--pyh7cba7a3_0"
 - "0.15.4--pyhdfd78af_0"
 - "0.16.1--pyhdfd78af_0"
 - "0.16.4--pyhdfd78af_0"
 - "0.8.2--py37hf01694f_1"
 - "0.19.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for sequana"
config: {"url": "https://biocontainers.pro/tools/sequana", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sequana", "latest": {"0.19.2--pyhdfd78af_0": "sha256:6635326b9f809c4554c2b673d3bae66a26e9d58c8ee8c6b65cd743fc9baef56c"}, "tags": {"0.8.2--py36h4c5857e_1": "sha256:03bd2313d7dfc05e294f3b5e9d37510fc14c6e5823f657aee0b3146e157f6a28", "0.14.3--pyh7cba7a3_0": "sha256:c684fb31f660c1ab46c990389e1b5ed1f73cfb8d7ce5cffdbf47356a80a1eff9", "0.13.2--pyh5e36f6f_0": "sha256:1e3f43185f9d8f2b5872db976a216a9dbf2731d95662707c8c620d0bf06287b6", "0.15.1--pyh7cba7a3_0": "sha256:2c0b00121993a0ef1ca3cf38f3a6b5249e9cff4a28f316c43bd38278c9c64194", "0.15.4--pyhdfd78af_0": "sha256:319ff3a4bc782a07bec7bc3d604ed2d34831abb6f088ac9686da4eef4b30e501", "0.16.1--pyhdfd78af_0": "sha256:d434a0464b0bea61eac31109bc17fa742429c01cba8fee20878f998927c8103b", "0.16.4--pyhdfd78af_0": "sha256:91d3dfc9ed70f23b1137340cb0f36a1d1683fe24b915f5798b14d2e00159f71f", "0.8.2--py37hf01694f_1": "sha256:3ab260ae4e6857c04d370eff7321de37cc193eec4f371f0ee0d2f3b16c7c030e", "0.19.2--pyhdfd78af_0": "sha256:6635326b9f809c4554c2b673d3bae66a26e9d58c8ee8c6b65cd743fc9baef56c"}, "docker": "quay.io/biocontainers/sequana"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sequana.
shpc-registry automated BioContainers addition for sequana
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sequana
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sequana:0.19.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sequana/0.19.2--pyhdfd78af_0
$ module help quay.io/biocontainers/sequana/0.19.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sequana-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sequana-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sequana-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sequana-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sequana-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sequana-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### sequana

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