---
layout: container
name:  "quay.io/biocontainers/bioconductor-ttmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ttmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ttmap/container.yaml"
updated_at: "2023-02-18 03:04:40.258475"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ttmap"

versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ttmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ttmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ttmap", "latest": {"1.20.0--r42hdfd78af_0": "sha256:bb95f33ad94252c2768abe8f2e3202355459be95fb093616bc3e2ce9da938306"}, "tags": {"1.8.0--r36_0": "sha256:1677c44e98ceb5af5a3bdf0efdefa5bd9b578c395cffa0ff5bfbe3a19267cfd6", "1.20.0--r42hdfd78af_0": "sha256:bb95f33ad94252c2768abe8f2e3202355459be95fb093616bc3e2ce9da938306", "1.16.0--r41hdfd78af_0": "sha256:d69da23f6c8a24517f455c77fb7dc5d4cc141e429e921e0d3feeb545da8b3056", "1.14.0--r41hdfd78af_0": "sha256:2cbff82b2e62c0691547f5f4f5cfbcf34bf3b1fff86465b4216bf36591095856", "1.12.0--r40hdfd78af_1": "sha256:66a398ab41c4f0b179fe6bad4bec91db2d01440556ba875d9235c8b35dc2b093", "1.10.0--r40_0": "sha256:b06bb804479b24039cf61b41c777ee68e0b0c9797712541e5994eacd911d62b4"}, "docker": "quay.io/biocontainers/bioconductor-ttmap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ttmap.
shpc-registry automated BioContainers addition for bioconductor-ttmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ttmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ttmap:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ttmap/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ttmap/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ttmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ttmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ttmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ttmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ttmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ttmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ttmap

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