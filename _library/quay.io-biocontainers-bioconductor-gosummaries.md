---
layout: container
name:  "quay.io/biocontainers/bioconductor-gosummaries"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gosummaries/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gosummaries/container.yaml"
updated_at: "2023-09-14 03:42:17.094709"
latest: "2.36.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gosummaries"

versions:
 - "2.30.0--r41hc247a5b_2"
 - "2.34.0--r42hc247a5b_0"
 - "2.34.0--r42hf17093f_1"
 - "2.36.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gosummaries"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gosummaries", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gosummaries", "latest": {"2.36.0--r43hf17093f_0": "sha256:f6b2930e199b3fe6a368542898ddfb5620b7de36379a7ce8daa075120b6402d4"}, "tags": {"2.30.0--r41hc247a5b_2": "sha256:005138f73ce407b7736b9d7963e863a7e5d169133ce2806bc8f40d1598fbe85b", "2.34.0--r42hc247a5b_0": "sha256:4a72988a628d61e390e1af42a0a1f2b08601ff1da1bb2306957198486c23c275", "2.34.0--r42hf17093f_1": "sha256:07c26b1935399f349e8c6073efc37dfa71b8155d0f51e49f064ae2b6044246df", "2.36.0--r43hf17093f_0": "sha256:f6b2930e199b3fe6a368542898ddfb5620b7de36379a7ce8daa075120b6402d4"}, "docker": "quay.io/biocontainers/bioconductor-gosummaries"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gosummaries.
shpc-registry automated BioContainers addition for bioconductor-gosummaries
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gosummaries
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gosummaries:2.36.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gosummaries/2.36.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-gosummaries/2.36.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gosummaries-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gosummaries-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gosummaries-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gosummaries-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gosummaries-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gosummaries-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gosummaries

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