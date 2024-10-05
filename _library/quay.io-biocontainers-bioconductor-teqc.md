---
layout: container
name:  "quay.io/biocontainers/bioconductor-teqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-teqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-teqc/container.yaml"
updated_at: "2024-10-05 03:16:45.473811"
latest: "4.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-teqc"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "4.8.0--r36_0"
 - "4.20.0--r42hdfd78af_0"
 - "4.16.0--r41hdfd78af_0"
 - "4.14.0--r41hdfd78af_0"
 - "4.12.0--r40hdfd78af_1"
 - "4.10.0--r40_0"
 - "4.22.0--r43hdfd78af_0"
 - "4.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-teqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-teqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-teqc", "latest": {"4.24.0--r43hdfd78af_0": "sha256:171a018d7d08a325342bbb05b51db12fa4c7b65469ffac9cedbe87e194ed232a"}, "tags": {"4.8.0--r36_0": "sha256:9ab0f48e2b3279e636ac2cd9990921370a369ce89cc72a2fd9951c0bb929f2ea", "4.20.0--r42hdfd78af_0": "sha256:1388b85fb0c1baa831214c4797bd3c17805a386a157c2711480d140a769a2202", "4.16.0--r41hdfd78af_0": "sha256:1415170191251d485caa66c91577b62b7d828834fa21c6cbc914b5e8d7507647", "4.14.0--r41hdfd78af_0": "sha256:bc25be51702e17de145eb786539f9ac253f11d7623f6f8a118fd267d589b9c26", "4.12.0--r40hdfd78af_1": "sha256:7aca099f19e296d56867bc5ac7831c0958d6a5fd8156a4350ace657299890f69", "4.10.0--r40_0": "sha256:ae3a565bc7311c94c959ad1534fa5b3c9cf8c88117ea017d933706cadb868888", "4.22.0--r43hdfd78af_0": "sha256:2d359c88999ceb241345ffcfb674545c6bd303af8bcdc18ab439a284e9677dbe", "4.24.0--r43hdfd78af_0": "sha256:171a018d7d08a325342bbb05b51db12fa4c7b65469ffac9cedbe87e194ed232a"}, "docker": "quay.io/biocontainers/bioconductor-teqc", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-teqc.
shpc-registry automated BioContainers addition for bioconductor-teqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-teqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-teqc:4.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-teqc/4.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-teqc/4.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-teqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-teqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-teqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-teqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-teqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-teqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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