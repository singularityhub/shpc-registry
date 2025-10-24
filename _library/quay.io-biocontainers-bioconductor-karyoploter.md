---
layout: container
name:  "quay.io/biocontainers/bioconductor-karyoploter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-karyoploter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-karyoploter/container.yaml"
updated_at: "2025-10-24 03:11:22.389815"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-karyoploter"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.5--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-karyoploter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-karyoploter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-karyoploter", "latest": {"1.32.0--r44hdfd78af_0": "sha256:4fd360ba05c5355a823480caf4d184e316b6794150e0e8ee0023b91f11cc06f7"}, "tags": {"1.8.5--r351_0": "sha256:8f70dcc11b6f51debd3e19aa751b3323ad6259b7bf60dc1597c94e8dc27a864c", "1.24.0--r42hdfd78af_0": "sha256:047018e8a209cd3517f7005d3e2fe68751f6e92ac1dd81486c3d78407aff67c0", "1.20.0--r41hdfd78af_0": "sha256:e5b286fd0eeee3f6c6432ddc701b6d1d070c2b73b75b5a3ab15be4c29c03411b", "1.18.0--r41hdfd78af_0": "sha256:602b7e2432a33676a8cf3cb894213e84f7fa492b3f534c3b43fc3259a156a89c", "1.16.0--r40hdfd78af_1": "sha256:576ecf98c43719009d7ee6cd9dea93ede99317a0abf05fb43b6ac62f2eb790b6", "1.14.0--r40_0": "sha256:04e1463fc5f978237aef8fb1920547f79fcced20b0a1ea9476dc097bff91c7ee", "1.26.0--r43hdfd78af_0": "sha256:e8ef8f436efadc9b2a4f4769222f2ea97c4eb969583b5960288fadb16774929c", "1.28.0--r43hdfd78af_0": "sha256:c2e7c5bcfd97af3891503afa43bba8bf756a749a1aa1c8238eb63af31e4b2ec2", "1.32.0--r44hdfd78af_0": "sha256:4fd360ba05c5355a823480caf4d184e316b6794150e0e8ee0023b91f11cc06f7"}, "docker": "quay.io/biocontainers/bioconductor-karyoploter", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-karyoploter.
shpc-registry automated BioContainers addition for bioconductor-karyoploter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-karyoploter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-karyoploter:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-karyoploter/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-karyoploter/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-karyoploter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-karyoploter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-karyoploter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-karyoploter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-karyoploter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-karyoploter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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