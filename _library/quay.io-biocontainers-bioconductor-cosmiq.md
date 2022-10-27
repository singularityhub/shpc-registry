---
layout: container
name:  "quay.io/biocontainers/bioconductor-cosmiq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cosmiq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cosmiq/container.yaml"
updated_at: "2022-10-27 00:56:41.016636"
latest: "1.28.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-cosmiq"
aliases:
 - ".bioconductor-faahko-post-link.sh"
 - ".bioconductor-faahko-pre-unlink.sh"
versions:
 - "1.28.0--r41hc247a5b_2"
description: "shpc-registry automated BioContainers addition for bioconductor-cosmiq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cosmiq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cosmiq", "latest": {"1.28.0--r41hc247a5b_2": "sha256:58f9831c54d25fa60a651b0706162120035a2eed282d859939b61214045a053c"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:58f9831c54d25fa60a651b0706162120035a2eed282d859939b61214045a053c"}, "docker": "quay.io/biocontainers/bioconductor-cosmiq", "aliases": {".bioconductor-faahko-post-link.sh": "/usr/local/bin/.bioconductor-faahko-post-link.sh", ".bioconductor-faahko-pre-unlink.sh": "/usr/local/bin/.bioconductor-faahko-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cosmiq.
shpc-registry automated BioContainers addition for bioconductor-cosmiq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cosmiq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cosmiq:1.28.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cosmiq/1.28.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-cosmiq/1.28.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cosmiq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosmiq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosmiq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cosmiq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cosmiq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cosmiq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-faahko-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-faahko-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-faahko-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-faahko-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-faahko-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-faahko-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-faahko-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-faahko-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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