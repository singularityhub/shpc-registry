---
layout: container
name:  "quay.io/biocontainers/bioconductor-transformgampoi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-transformgampoi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-transformgampoi/container.yaml"
updated_at: "2024-03-29 03:02:02.619426"
latest: "1.8.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-transformgampoi"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
 - "1.8.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-transformgampoi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-transformgampoi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-transformgampoi", "latest": {"1.8.0--r43hf17093f_0": "sha256:1fc6be6327fe69e769a46096d4b6bbcf472cf183b16b755dfdb2a0797af46a5b"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:d53aabb903c7d2b4b3acd74998ec3c31fd31fab0ead5c7b854d94db029dcb0e6", "1.4.0--r42hc247a5b_0": "sha256:656e38842e804d60ca0afb310cf90d7216254d5f2156d38bd980bc14c9a6ef4e", "1.4.0--r42hf17093f_1": "sha256:4f10c1a0edddaba3f0dc072fee69c198f073de3d8ae6697e6347d3092521a188", "1.6.0--r43hf17093f_0": "sha256:ee86b9fe25529d47c5083360d61053623d8cd372f511f95e49de2cecb423f3d4", "1.8.0--r43hf17093f_0": "sha256:1fc6be6327fe69e769a46096d4b6bbcf472cf183b16b755dfdb2a0797af46a5b"}, "docker": "quay.io/biocontainers/bioconductor-transformgampoi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-transformgampoi.
shpc-registry automated BioContainers addition for bioconductor-transformgampoi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-transformgampoi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-transformgampoi:1.8.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-transformgampoi/1.8.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-transformgampoi/1.8.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-transformgampoi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transformgampoi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transformgampoi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-transformgampoi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-transformgampoi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-transformgampoi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-transformgampoi

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