---
layout: container
name:  "quay.io/biocontainers/bioconductor-glimma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-glimma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-glimma/container.yaml"
updated_at: "2025-02-24 03:23:56.113812"
latest: "2.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-glimma"

versions:
 - "2.4.0--r41hdfd78af_0"
 - "2.8.0--r42hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-glimma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-glimma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-glimma", "latest": {"2.16.0--r44hdfd78af_0": "sha256:c08209a0b9bdf1120e6450303e3c9387567d5291e4a5fc74199d95864c4fdaea"}, "tags": {"2.4.0--r41hdfd78af_0": "sha256:623c957cf39a8f1e1c412b38750ff8f2b25027d7ac2008a49829495fb2434356", "2.8.0--r42hdfd78af_0": "sha256:93092409d8d8f210076d873d6ef5614b34dd0f5d27da754208c63517ea892f57", "2.10.0--r43hdfd78af_0": "sha256:7be49f88f8fa212b8ea0810e13ad1eb4d5b1e04d364300f020692c1b7567bf7c", "2.12.0--r43hdfd78af_0": "sha256:9da53d0d6a7a252d5975defd38d0fdba340f51b585f22cacdb8996b912e9490e", "2.16.0--r44hdfd78af_0": "sha256:c08209a0b9bdf1120e6450303e3c9387567d5291e4a5fc74199d95864c4fdaea"}, "docker": "quay.io/biocontainers/bioconductor-glimma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-glimma.
shpc-registry automated BioContainers addition for bioconductor-glimma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-glimma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-glimma:2.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-glimma/2.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-glimma/2.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-glimma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glimma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glimma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-glimma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-glimma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-glimma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-glimma

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