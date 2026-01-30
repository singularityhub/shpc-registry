---
layout: container
name:  "quay.io/biocontainers/bioconductor-metaseqr2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metaseqr2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metaseqr2/container.yaml"
updated_at: "2026-01-30 04:39:33.155965"
latest: "1.18.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metaseqr2"
aliases:
 - "pandoc-server"
 - "pandoc"
versions:
 - "1.6.1--r41hc0cfd56_1"
 - "1.10.0--r42hc0cfd56_0"
 - "1.10.0--r42ha9d7317_1"
 - "1.18.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metaseqr2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metaseqr2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metaseqr2", "latest": {"1.18.0--r44h3df3fcb_0": "sha256:dabb658f42fc15d6f78ae882596e96b712a2dfe6958ca055a7a584823f7361b7"}, "tags": {"1.6.1--r41hc0cfd56_1": "sha256:2f6b14e89b698413166d8524afd2ae8f5193db79bbe9d2fa27e63cd8aae9c1e6", "1.10.0--r42hc0cfd56_0": "sha256:45bd486a7fa409b890bb42554bdb931e508b208879517f2ba8f9b0cedf7aa2b3", "1.10.0--r42ha9d7317_1": "sha256:d60964f9ffe305cc094d85a12619bccfe89569abc548c0f34e066019906f5dd2", "1.18.0--r44h3df3fcb_0": "sha256:dabb658f42fc15d6f78ae882596e96b712a2dfe6958ca055a7a584823f7361b7"}, "docker": "quay.io/biocontainers/bioconductor-metaseqr2", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metaseqr2.
shpc-registry automated BioContainers addition for bioconductor-metaseqr2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metaseqr2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metaseqr2:1.18.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metaseqr2/1.18.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-metaseqr2/1.18.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metaseqr2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metaseqr2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metaseqr2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metaseqr2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metaseqr2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metaseqr2-inspect-deffile:

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