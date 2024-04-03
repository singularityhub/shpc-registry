---
layout: container
name:  "quay.io/biocontainers/bioconductor-bionet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bionet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bionet/container.yaml"
updated_at: "2024-04-03 02:31:13.033372"
latest: "1.62.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bionet"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bionet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bionet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bionet", "latest": {"1.62.0--r43hdfd78af_0": "sha256:a86f54bae32fa2175d3dcb03ffda8c5b431a63991ff12ba2576f502f34383715"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:29fff5cc3f1263df7937776001d008f5e3371669342737abe3feca75902202c1", "1.58.0--r42hdfd78af_0": "sha256:65c756f73ee6238dd2f5681e77a7848e11bd24d1bcacdaf0d07087e22bbb9db1", "1.60.0--r43hdfd78af_0": "sha256:85fc79598bba209decb45f4ed379bb9fee801012d6b4aa54aa94b9b4a62e0c99", "1.62.0--r43hdfd78af_0": "sha256:a86f54bae32fa2175d3dcb03ffda8c5b431a63991ff12ba2576f502f34383715"}, "docker": "quay.io/biocontainers/bioconductor-bionet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bionet.
shpc-registry automated BioContainers addition for bioconductor-bionet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bionet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bionet:1.62.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bionet/1.62.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bionet/1.62.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bionet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bionet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bionet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bionet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bionet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bionet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bionet

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