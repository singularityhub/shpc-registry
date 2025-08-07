---
layout: container
name:  "quay.io/biocontainers/bioconductor-inpower"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-inpower/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-inpower/container.yaml"
updated_at: "2025-08-07 04:23:36.261562"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-inpower"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-inpower"
config: {"url": "https://biocontainers.pro/tools/bioconductor-inpower", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-inpower", "latest": {"1.42.0--r44hdfd78af_0": "sha256:377ed44a1ef49666efe0ca75796f45449d85755d893893441ff5b692c41359b3"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:94c8addeb3f9ff6c82803f462fd03879c158a0fd43205d7a54262971b9f99c77", "1.34.0--r42hdfd78af_0": "sha256:0010d92c2515e1cda7bf5c849470b515e5b7d2250f71f97de8d07b4b8a7f90a8", "1.36.0--r43hdfd78af_0": "sha256:d3c897afb52f656cda800724685228bbbc6d27fe074d51bc523e6ceb69ac1fa8", "1.38.0--r43hdfd78af_0": "sha256:a25b09a04ce775b227df7b15af378366e6d6a1151bbfc8431b5f5570dbf39aba", "1.42.0--r44hdfd78af_0": "sha256:377ed44a1ef49666efe0ca75796f45449d85755d893893441ff5b692c41359b3"}, "docker": "quay.io/biocontainers/bioconductor-inpower"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-inpower.
shpc-registry automated BioContainers addition for bioconductor-inpower
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-inpower
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-inpower:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-inpower/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-inpower/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-inpower-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-inpower-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-inpower-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-inpower-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-inpower-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-inpower-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-inpower

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