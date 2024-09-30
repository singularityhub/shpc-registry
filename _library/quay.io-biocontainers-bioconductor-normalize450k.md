---
layout: container
name:  "quay.io/biocontainers/bioconductor-normalize450k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-normalize450k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-normalize450k/container.yaml"
updated_at: "2024-09-30 03:33:38.830962"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-normalize450k"

versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-normalize450k"
config: {"url": "https://biocontainers.pro/tools/bioconductor-normalize450k", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-normalize450k", "latest": {"1.30.0--r43hdfd78af_0": "sha256:5fea10332ff0823a8a6e3dac2330f4b69cd4d3de802d2b13993b5a5e1155eba4"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:d5c9b781ca8f8cf70d51578a4721d347d0c9f4844c0bf97007abea39a651c8e0", "1.26.0--r42hdfd78af_0": "sha256:98df36b98932f3dadf800bc7858b2d1e1c408b09b1a58cd7c7f856839737012e", "1.28.0--r43hdfd78af_0": "sha256:aa5fc87f6301173ae4437024dafcaceb66842660af9f120038324da39b54b0e5", "1.30.0--r43hdfd78af_0": "sha256:5fea10332ff0823a8a6e3dac2330f4b69cd4d3de802d2b13993b5a5e1155eba4"}, "docker": "quay.io/biocontainers/bioconductor-normalize450k"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-normalize450k.
shpc-registry automated BioContainers addition for bioconductor-normalize450k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-normalize450k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-normalize450k:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-normalize450k/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-normalize450k/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-normalize450k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normalize450k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normalize450k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-normalize450k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-normalize450k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-normalize450k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-normalize450k

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