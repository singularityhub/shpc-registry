---
layout: container
name:  "quay.io/biocontainers/bioconductor-bumphunter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bumphunter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bumphunter/container.yaml"
updated_at: "2025-02-07 03:36:57.816378"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bumphunter"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bumphunter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bumphunter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bumphunter", "latest": {"1.44.0--r43hdfd78af_0": "sha256:03c31d595a7710288f8abf43968a62b5d9d5fd579e03aef44f07a4ffe8318863"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:46de4356c9a4fe567b5855c826aa0d2535f5395a8fafc515b62441c6c708142c", "1.40.0--r42hdfd78af_0": "sha256:64c961c02b19e9ff15b56d223dc35c3519518f9a0dc6debdf38b9a6b7077a2f2", "1.42.0--r43hdfd78af_0": "sha256:51a08d62be5a259f6656922d3ef647309c225e697f7ca1b7ba2e3178bba0b24b", "1.44.0--r43hdfd78af_0": "sha256:03c31d595a7710288f8abf43968a62b5d9d5fd579e03aef44f07a4ffe8318863"}, "docker": "quay.io/biocontainers/bioconductor-bumphunter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bumphunter.
shpc-registry automated BioContainers addition for bioconductor-bumphunter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bumphunter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bumphunter:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bumphunter/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bumphunter/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bumphunter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bumphunter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bumphunter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bumphunter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bumphunter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bumphunter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bumphunter

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