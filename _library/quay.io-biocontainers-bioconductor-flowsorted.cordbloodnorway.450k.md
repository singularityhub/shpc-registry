---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k/container.yaml"
updated_at: "2022-10-29 18:16:08.238635"
latest: "1.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowsorted.cordbloodnorway.450k"
aliases:
 - ".bioconductor-flowsorted.cordbloodnorway.450k-post-link.sh"
 - ".bioconductor-flowsorted.cordbloodnorway.450k-pre-unlink.sh"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowsorted.cordbloodnorway.450k"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowsorted.cordbloodnorway.450k", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowsorted.cordbloodnorway.450k", "latest": {"1.8.0--r351_0": "sha256:8a2f126ebe128eaee70e3b48d42a36e1507593bc5832774883d0ef1654ae143f"}, "tags": {"1.8.0--r351_0": "sha256:8a2f126ebe128eaee70e3b48d42a36e1507593bc5832774883d0ef1654ae143f"}, "docker": "quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k", "aliases": {".bioconductor-flowsorted.cordbloodnorway.450k-post-link.sh": "/usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-post-link.sh", ".bioconductor-flowsorted.cordbloodnorway.450k-pre-unlink.sh": "/usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-pre-unlink.sh", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k.
shpc-registry automated BioContainers addition for bioconductor-flowsorted.cordbloodnorway.450k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k:1.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k/1.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-flowsorted.cordbloodnorway.450k/1.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowsorted.cordbloodnorway.450k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowsorted.cordbloodnorway.450k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowsorted.cordbloodnorway.450k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowsorted.cordbloodnorway.450k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowsorted.cordbloodnorway.450k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowsorted.cordbloodnorway.450k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-flowsorted.cordbloodnorway.450k-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-flowsorted.cordbloodnorway.450k-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowsorted.cordbloodnorway.450k-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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