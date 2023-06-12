---
layout: container
name:  "quay.io/biocontainers/bioconductor-msstatstmt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msstatstmt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msstatstmt/container.yaml"
updated_at: "2023-06-12 05:10:09.852915"
latest: "2.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msstatstmt"

versions:
 - "2.2.0--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msstatstmt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msstatstmt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msstatstmt", "latest": {"2.6.0--r42hdfd78af_0": "sha256:b5cd05eb8764c37a604d1c6ed6861d85eebec402d64344e20cb114d8ba92e8fe"}, "tags": {"2.2.0--r41hdfd78af_0": "sha256:76e654dc1b9e457c1bc8f5c6c080db6b8f06e710ac5be370dcfbab91d51f0524", "2.6.0--r42hdfd78af_0": "sha256:b5cd05eb8764c37a604d1c6ed6861d85eebec402d64344e20cb114d8ba92e8fe"}, "docker": "quay.io/biocontainers/bioconductor-msstatstmt"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msstatstmt.
shpc-registry automated BioContainers addition for bioconductor-msstatstmt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatstmt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatstmt:2.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msstatstmt/2.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msstatstmt/2.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msstatstmt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatstmt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatstmt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msstatstmt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msstatstmt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msstatstmt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msstatstmt

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