---
layout: container
name:  "quay.io/biocontainers/bioconductor-mast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mast/container.yaml"
updated_at: "2025-05-27 11:42:20.170097"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mast"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mast"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mast", "latest": {"1.32.0--r44hdfd78af_0": "sha256:4fc4f79cda697bd574b57d951d37ec18c2eb252cec1a2ff01803babb05478241"}, "tags": {"1.8.1--r351_0": "sha256:0f40ff71c5e10189574ae0da8a7ec14d2a534e7fc87451c5247fec738000d52e", "1.24.0--r42hdfd78af_0": "sha256:1ab6863a6d6c741ca936421bb3c6ae90915799dcdc45272127fe38fb5ad39636", "1.20.0--r41hdfd78af_0": "sha256:a8072035539c609cf26c6f3724967887b7f9f782afb58719cef5b1fd24039962", "1.18.0--r41hdfd78af_0": "sha256:d112ea968db06235267bb454a598be9de3ba9f8ffac123d8e9666eccd22854a5", "1.16.0--r40hdfd78af_1": "sha256:f7b1f178d3d4b437dd0cfee7a2c4690fb44cf7128c15fe2ca9ae18eb695f68d1", "1.14.0--r40_0": "sha256:e2e216e45fb15c6582593cef2cec009c77a5af6939d4da4ece879b2481530141", "1.26.0--r43hdfd78af_0": "sha256:db0f7764249f67eac815501f02ce2adbc872c74f506aa728b1918df74b0fb0f9", "1.28.0--r43hdfd78af_0": "sha256:dcc50d8e40111d01f27d5d1aa18e283b116d843852b769b43e91547928191859", "1.32.0--r44hdfd78af_0": "sha256:4fc4f79cda697bd574b57d951d37ec18c2eb252cec1a2ff01803babb05478241"}, "docker": "quay.io/biocontainers/bioconductor-mast", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mast.
shpc-registry automated BioContainers addition for bioconductor-mast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mast:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mast/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mast/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mast-inspect-deffile:

```bash
$ singularity inspect -d <container>
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