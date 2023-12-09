---
layout: container
name:  "quay.io/biocontainers/bioconductor-scbn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scbn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scbn/container.yaml"
updated_at: "2023-12-09 03:06:32.669668"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scbn"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scbn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scbn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scbn", "latest": {"1.18.0--r43hdfd78af_0": "sha256:7f0c3b13f8dea194af8a585b645c2edc8509240ced8c994041e8c7121bb8547e"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:9040066586c7db50bb765db2ecf63f2028a13a95d7587c06ee61acd0db15629b", "1.16.0--r42hdfd78af_0": "sha256:c6787060db4f1686296e1783ad287a5a938904a2a3241f047dbcd82dd0bd0bf9", "1.12.0--r41hdfd78af_0": "sha256:442ed5b0f161397beed42323442e9056cd39b7dffe9abdcc1be688fbfafbc651", "1.10.0--r41hdfd78af_0": "sha256:85597e47cdbe5f36677cae520b9ec0785d5445e6554f924d9b9433ab632f13c9", "1.18.0--r43hdfd78af_0": "sha256:7f0c3b13f8dea194af8a585b645c2edc8509240ced8c994041e8c7121bb8547e"}, "docker": "quay.io/biocontainers/bioconductor-scbn", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scbn.
shpc-registry automated BioContainers addition for bioconductor-scbn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scbn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scbn:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scbn/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scbn/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scbn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scbn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scbn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scbn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scbn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scbn-inspect-deffile:

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