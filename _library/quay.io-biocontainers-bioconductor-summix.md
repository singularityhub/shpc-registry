---
layout: container
name:  "quay.io/biocontainers/bioconductor-summix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-summix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-summix/container.yaml"
updated_at: "2024-12-06 03:19:51.816596"
latest: "2.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-summix"

versions:
 - "2.0.0--r41hdfd78af_0"
 - "2.4.0--r42hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-summix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-summix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-summix", "latest": {"2.8.0--r43hdfd78af_0": "sha256:db57433b6fc6432e9dc5a284225b54d5d2213dff1fc15f94b52bda2703e92f7b"}, "tags": {"2.0.0--r41hdfd78af_0": "sha256:844d4ee7d116b840d25b44faedbd0b01a1b521afb3a0f91cca883e0c57cd03eb", "2.4.0--r42hdfd78af_0": "sha256:85207fc4485dc569602e014b427e18d5c4f56f2534497f2e8aea0bf2b8191412", "2.6.0--r43hdfd78af_0": "sha256:13eed9f3049936971c1bc05fcd36d308ae24fb008f93f5ab99b8c25d8464fd49", "2.8.0--r43hdfd78af_0": "sha256:db57433b6fc6432e9dc5a284225b54d5d2213dff1fc15f94b52bda2703e92f7b"}, "docker": "quay.io/biocontainers/bioconductor-summix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-summix.
shpc-registry automated BioContainers addition for bioconductor-summix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-summix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-summix:2.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-summix/2.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-summix/2.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-summix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-summix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-summix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-summix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-summix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-summix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-summix

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