---
layout: container
name:  "quay.io/biocontainers/bioconductor-tscr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tscr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tscr/container.yaml"
updated_at: "2024-11-14 03:16:56.102550"
latest: "1.11.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tscr"
aliases:
 - "pandoc-server"
 - "pandoc"
versions:
 - "1.6.1--r41hc0cfd56_1"
 - "1.10.0--r42hc0cfd56_0"
 - "1.10.0--r42ha9d7317_1"
 - "1.11.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tscr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tscr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tscr", "latest": {"1.11.0--r43ha9d7317_0": "sha256:2f1e926b26dfd2b1d27baaef25949a606e5582f2764dbf0636a9ad9a24ef0229"}, "tags": {"1.6.1--r41hc0cfd56_1": "sha256:c3214aa9061a874eba035a392d418a9534232d45d30c3597d6985cebd6be48a3", "1.10.0--r42hc0cfd56_0": "sha256:bc5cbaaf4772d6d0be2cf1340ca286514158816b5b8049980b1be1e1ff34c70c", "1.10.0--r42ha9d7317_1": "sha256:9b7efe3299a56876b64672e0bd0f7b86f728fd155e18bfaa0fa51e2753450e9b", "1.11.0--r43ha9d7317_0": "sha256:2f1e926b26dfd2b1d27baaef25949a606e5582f2764dbf0636a9ad9a24ef0229"}, "docker": "quay.io/biocontainers/bioconductor-tscr", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tscr.
shpc-registry automated BioContainers addition for bioconductor-tscr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tscr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tscr:1.11.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tscr/1.11.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-tscr/1.11.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tscr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tscr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tscr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tscr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tscr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tscr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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