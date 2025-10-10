---
layout: container
name:  "quay.io/biocontainers/bioconductor-intramirexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-intramirexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-intramirexplorer/container.yaml"
updated_at: "2025-10-10 03:12:16.519290"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-intramirexplorer"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-intramirexplorer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-intramirexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-intramirexplorer", "latest": {"1.28.0--r44hdfd78af_0": "sha256:2fe32d115881c044b33eae25df00dc56d1dca7e715cdde2f47464ad40a209005"}, "tags": {"1.8.0--r36_0": "sha256:7b4a19b1754fa80c2cce600c7bb327ea3abe104464eeb0675cf27e2422201adf", "1.20.0--r42hdfd78af_0": "sha256:316129c5429c796e36e4b59de14b29463279ebd2adaf144764631043f5069118", "1.16.0--r41hdfd78af_0": "sha256:cba9a6685eb0e813136ce52d0272b64bdfe945faa278ae48891253e6a3329e8f", "1.12.0--r40hdfd78af_1": "sha256:5ad974bd511f85be5c933ae5a37e0aeff490238187f8585c43af37d68eda1bf9", "1.10.0--r40_0": "sha256:6c535908a8999195222df4c16c0741a67524036be460eef385bd3aba0eca3d67", "1.22.0--r43hdfd78af_0": "sha256:b904f9b49e59399992d6aba3409f64ca90f8f7b884da54cdb6ed8f0b36c49055", "1.24.0--r43hdfd78af_0": "sha256:fa147862169d4901a6cbbb86062336db4a4d9a8e2d638200f1c0a4013d39385b", "1.28.0--r44hdfd78af_0": "sha256:2fe32d115881c044b33eae25df00dc56d1dca7e715cdde2f47464ad40a209005"}, "docker": "quay.io/biocontainers/bioconductor-intramirexplorer", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-intramirexplorer.
shpc-registry automated BioContainers addition for bioconductor-intramirexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-intramirexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-intramirexplorer:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-intramirexplorer/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-intramirexplorer/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-intramirexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-intramirexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-intramirexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-intramirexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-intramirexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-intramirexplorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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