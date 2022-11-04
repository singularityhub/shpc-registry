---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtcga.mrna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtcga.mrna/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtcga.mrna/container.yaml"
updated_at: "2022-11-04 00:16:39.951852"
latest: "1.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtcga.mrna"
aliases:
 - ".bioconductor-rtcga.mrna-post-link.sh"
 - ".bioconductor-rtcga.mrna-pre-unlink.sh"
 - "wget"
versions:
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtcga.mrna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtcga.mrna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtcga.mrna", "latest": {"1.8.0--r351_0": "sha256:e997891a35892b582f188b274aa7367278bbc4050861ea98aab5a0944978d57f"}, "tags": {"1.8.0--r351_0": "sha256:e997891a35892b582f188b274aa7367278bbc4050861ea98aab5a0944978d57f"}, "docker": "quay.io/biocontainers/bioconductor-rtcga.mrna", "aliases": {".bioconductor-rtcga.mrna-post-link.sh": "/usr/local/bin/.bioconductor-rtcga.mrna-post-link.sh", ".bioconductor-rtcga.mrna-pre-unlink.sh": "/usr/local/bin/.bioconductor-rtcga.mrna-pre-unlink.sh", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtcga.mrna.
shpc-registry automated BioContainers addition for bioconductor-rtcga.mrna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga.mrna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga.mrna:1.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtcga.mrna/1.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-rtcga.mrna/1.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtcga.mrna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga.mrna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga.mrna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtcga.mrna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtcga.mrna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtcga.mrna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-rtcga.mrna-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-rtcga.mrna-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-rtcga.mrna-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-rtcga.mrna-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-rtcga.mrna-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-rtcga.mrna-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-rtcga.mrna-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-rtcga.mrna-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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