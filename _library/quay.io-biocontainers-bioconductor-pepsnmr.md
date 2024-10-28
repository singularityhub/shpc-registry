---
layout: container
name:  "quay.io/biocontainers/bioconductor-pepsnmr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pepsnmr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pepsnmr/container.yaml"
updated_at: "2024-10-28 03:34:39.496274"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pepsnmr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.1--r40hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pepsnmr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pepsnmr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pepsnmr", "latest": {"1.20.0--r43hdfd78af_0": "sha256:eadf612098a36dddff07cd8a071e9b1de71d8154728c121c2043b21d2678100a"}, "tags": {"1.8.1--r40hdfd78af_0": "sha256:13d4abb1f5d7723fc898b4dc91e8d00a4ead606cc8e751a6efe5ea1866444651", "1.16.0--r42hdfd78af_0": "sha256:6d3629f1beff352624bf2a907051445566395aabe753a88626b2f2cd2abc0557", "1.12.0--r41hdfd78af_0": "sha256:ea1af7fd320eac8d0e6691fbcf5a0b1797cc81530bd4a87f87ec0a4e8451fc3d", "1.10.0--r41hdfd78af_0": "sha256:0850fb4e7ea0aab6f7f99998c69a2fe67a5edbb3e6276be65a832b821cdc0694", "1.18.0--r43hdfd78af_0": "sha256:420755b5ad77cdb7d3682f142ce311b3130cf0db6eb1e4dfd3c39a1c2e4cfc43", "1.20.0--r43hdfd78af_0": "sha256:eadf612098a36dddff07cd8a071e9b1de71d8154728c121c2043b21d2678100a"}, "docker": "quay.io/biocontainers/bioconductor-pepsnmr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pepsnmr.
shpc-registry automated BioContainers addition for bioconductor-pepsnmr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pepsnmr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pepsnmr:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pepsnmr/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pepsnmr/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pepsnmr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepsnmr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepsnmr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pepsnmr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pepsnmr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pepsnmr-inspect-deffile:

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