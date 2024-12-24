---
layout: container
name:  "quay.io/biocontainers/bioconductor-moe430bprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moe430bprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moe430bprobe/container.yaml"
updated_at: "2024-12-24 03:31:10.065291"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-moe430bprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-moe430bprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moe430bprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moe430bprobe", "latest": {"2.18.0--r43hdfd78af_13": "sha256:fcebb6d4e0eed1de46fc0b5c5c5382a4885543fa63ec0c6b7a736e46f844ebd2"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:368324a89f4084a395b4379564af09d03d8ed15503bcf58867dbea276801087e", "2.18.0--r41hdfd78af_10": "sha256:d17efe18feaafa12ab7f394cb00bca6f69784e2a3f2a2e36fe7aa3ccc68cd1f8", "2.18.0--r42hdfd78af_11": "sha256:a73008f52ebc70c74a5c561a41493898a95893415d87d70c6a20e6c66c94e180", "2.18.0--r43hdfd78af_12": "sha256:4e065cf6209ad218a4eb17e065ddbd9afcdd7ee8e31aa1822fca243409df310a", "2.18.0--r43hdfd78af_13": "sha256:fcebb6d4e0eed1de46fc0b5c5c5382a4885543fa63ec0c6b7a736e46f844ebd2"}, "docker": "quay.io/biocontainers/bioconductor-moe430bprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moe430bprobe.
shpc-registry automated BioContainers addition for bioconductor-moe430bprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430bprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430bprobe:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moe430bprobe/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-moe430bprobe/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moe430bprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430bprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430bprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moe430bprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moe430bprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moe430bprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moe430bprobe

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