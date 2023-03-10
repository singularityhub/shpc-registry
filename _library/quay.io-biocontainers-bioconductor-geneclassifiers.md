---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneclassifiers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneclassifiers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneclassifiers/container.yaml"
updated_at: "2023-03-10 03:24:44.957154"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneclassifiers"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneclassifiers"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneclassifiers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneclassifiers", "latest": {"1.22.0--r42hdfd78af_0": "sha256:4628f482639d425380f08b4b5a4fae5cd7aafd7caad1812661adf303144288c7"}, "tags": {"1.8.0--r36_1": "sha256:d4323865fe8e39f5bacb14197c310acdf94f8049437b989726348673132270de", "1.22.0--r42hdfd78af_0": "sha256:4628f482639d425380f08b4b5a4fae5cd7aafd7caad1812661adf303144288c7", "1.18.0--r41hdfd78af_0": "sha256:a1b65c9f38fa0989380d878eb58eca56a00f465b457ae593038970770a05f3fa", "1.16.0--r41hdfd78af_0": "sha256:30c9907fba705f59acdfc9f314733cc89b3076cb7ca6a8a28808c63e23536443", "1.14.0--r40hdfd78af_1": "sha256:208a4041aa77fd65521f06cd0d8f56bb2a896b546a027faea16b48a0dfc44ddd", "1.12.0--r40_0": "sha256:90f2105acaa349610962dd6897a19b0d0cb581c056e1bc71843f29d19544f04f"}, "docker": "quay.io/biocontainers/bioconductor-geneclassifiers", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneclassifiers.
shpc-registry automated BioContainers addition for bioconductor-geneclassifiers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneclassifiers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneclassifiers:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneclassifiers/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geneclassifiers/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneclassifiers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneclassifiers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneclassifiers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneclassifiers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneclassifiers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneclassifiers-inspect-deffile:

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