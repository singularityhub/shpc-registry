---
layout: container
name:  "quay.io/biocontainers/bioconductor-mousefm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mousefm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mousefm/container.yaml"
updated_at: "2025-11-21 15:43:28.623702"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mousefm"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0.0--r40hdfd78af_2"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mousefm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mousefm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mousefm", "latest": {"1.16.0--r44hdfd78af_0": "sha256:38e0de736e6ebe7089087234e8c69c62119e4238635bd0154e5e6851e0f47515"}, "tags": {"1.0.0--r40hdfd78af_2": "sha256:df2d6893dd3b1542d336aca8d90a72573a655fcb0a4fd32fda5d1e95f9cc002b", "1.8.0--r42hdfd78af_0": "sha256:3c9045946c6d4790af17557d2470fd54c665f4e8e8f981ff0dc6ab1389caef3a", "1.10.0--r43hdfd78af_0": "sha256:128aed2d88d0b5152e19113f7c128a880f5abf60d33b09c7bbdeb531cdf9d9d3", "1.12.0--r43hdfd78af_0": "sha256:a7425251a2e1261f7984e47a4ba9d88ba83ccc20a5bd107721fa412b6464e1bf", "1.16.0--r44hdfd78af_0": "sha256:38e0de736e6ebe7089087234e8c69c62119e4238635bd0154e5e6851e0f47515"}, "docker": "quay.io/biocontainers/bioconductor-mousefm", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mousefm.
shpc-registry automated BioContainers addition for bioconductor-mousefm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mousefm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mousefm:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mousefm/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mousefm/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mousefm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mousefm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mousefm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mousefm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mousefm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mousefm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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