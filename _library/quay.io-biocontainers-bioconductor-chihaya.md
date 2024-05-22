---
layout: container
name:  "quay.io/biocontainers/bioconductor-chihaya"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chihaya/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chihaya/container.yaml"
updated_at: "2024-05-22 02:45:19.477157"
latest: "1.2.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chihaya"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.0--r43hf17093f_0"
 - "1.2.0--r43hf17093f_0"
description: "singularity registry hpc automated addition for bioconductor-chihaya"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chihaya", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-chihaya", "latest": {"1.2.0--r43hf17093f_0": "sha256:3bfbe245ae6e04979ef83016f7cbe0cd81dfa48fcdfb230dc71eaaf8e783e115"}, "tags": {"1.0.0--r43hf17093f_0": "sha256:02e3de6626bf00c71a7dd5412ebacaeb662bbeb77110e02728c8e343297e3c14", "1.2.0--r43hf17093f_0": "sha256:3bfbe245ae6e04979ef83016f7cbe0cd81dfa48fcdfb230dc71eaaf8e783e115"}, "docker": "quay.io/biocontainers/bioconductor-chihaya", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chihaya.
singularity registry hpc automated addition for bioconductor-chihaya
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chihaya
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chihaya:1.2.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chihaya/1.2.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-chihaya/1.2.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chihaya-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chihaya-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chihaya-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chihaya-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chihaya-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chihaya-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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