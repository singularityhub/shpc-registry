---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromstardata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromstardata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromstardata/container.yaml"
updated_at: "2025-12-17 03:58:20.925609"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromstardata"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.23.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromstardata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromstardata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromstardata", "latest": {"1.32.0--r44hdfd78af_0": "sha256:3456dc90dc4239ceedd9a0b727af5f86bc57c74b30871199fad9533563b68a2d"}, "tags": {"1.8.0--r351_0": "sha256:0f50633e0469a1169940f69de16cd9f754492ade6d195f9eac883acb87839bfb", "1.24.0--r42hdfd78af_0": "sha256:e17fe4a374682b75f3a25aa43c5f81ff5d3ec21d181c43aabf19cd0f5e41583a", "1.23.0--r42hdfd78af_0": "sha256:4015de1c3e230439c67f16ec5435d76302eec9e4e9fd8883a03dfdf9d07d8245", "1.20.0--r41hdfd78af_1": "sha256:5983aba2b1d0c6b5c43fd395f23dfcd30583f65dd8ef1b39a0522906ac5e9884", "1.18.0--r41hdfd78af_0": "sha256:0b6a4c142212135b331cbf7a2a9acacc55dce18898cbc3ebaf96dac28fce523a", "1.16.0--r40hdfd78af_1": "sha256:6dedfb417158d387d1e6e139ad55848632112e741baf9ae7eb75ad1510ac5082", "1.26.0--r43hdfd78af_0": "sha256:43e29765282a3d75bbe8f4ad8ebffe6175a446e4d84839daa7e0307449a0ac6a", "1.28.0--r43hdfd78af_0": "sha256:903dffab3f71cb914ce36900984fa1d005a57ae845f66e29239fa1fd1bd0bc6d", "1.32.0--r44hdfd78af_0": "sha256:3456dc90dc4239ceedd9a0b727af5f86bc57c74b30871199fad9533563b68a2d"}, "docker": "quay.io/biocontainers/bioconductor-chromstardata", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromstardata.
shpc-registry automated BioContainers addition for bioconductor-chromstardata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromstardata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromstardata:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromstardata/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chromstardata/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromstardata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromstardata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromstardata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromstardata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromstardata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromstardata-inspect-deffile:

```bash
$ singularity inspect -d <container>
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