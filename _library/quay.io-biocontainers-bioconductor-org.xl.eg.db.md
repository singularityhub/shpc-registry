---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.xl.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.xl.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.xl.eg.db/container.yaml"
updated_at: "2024-02-05 03:27:57.210647"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.xl.eg.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.10.0--r36_0"
 - "3.16.0--r42hdfd78af_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.xl.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.xl.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.xl.eg.db", "latest": {"3.18.0--r43hdfd78af_0": "sha256:c8b3a558861cf69d10a26b9bfea4f73e8dde52600b0e98a2436c6650462109f5"}, "tags": {"3.8.2--r36_1": "sha256:38a746a315dfa1aefea2e8189343418bea94f030a60b1a1fc4184022852634c8", "3.14.0--r41hdfd78af_1": "sha256:c9ccb2f7fbd53614aeabf991085702fa4de277344e7467fca8ee0970a5fb7664", "3.13.0--r41hdfd78af_0": "sha256:71a0b131940f58416717fc2aa8c92a48c032e15eac27c21a110b1d43af792eb5", "3.12.0--r40hdfd78af_1": "sha256:b323fbb2a0bd19bab586b08faf998929f6af1db21fb98303788436ff7711f703", "3.11.1--r40_0": "sha256:66634a67af34a86b90fe2cdf2c767d2ae3310be80d0e4d0d240b2ff0ab513e67", "3.10.0--r36_0": "sha256:bbc2ec80e25717c044c31710d04f9bf1ceb07309ecf79551b5259fe9223f5576", "3.16.0--r42hdfd78af_0": "sha256:b16f17988ba37a2daae17e4a8d2d1595561eb6e7511927e6f7dba271a02bb627", "3.17.0--r43hdfd78af_0": "sha256:b39f2a0f517740c2ac8883ec73870a2f911884ab06ceab766b79a35fee5330d8", "3.18.0--r43hdfd78af_0": "sha256:c8b3a558861cf69d10a26b9bfea4f73e8dde52600b0e98a2436c6650462109f5"}, "docker": "quay.io/biocontainers/bioconductor-org.xl.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.xl.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.xl.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.xl.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.xl.eg.db:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.xl.eg.db/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.xl.eg.db/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.xl.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.xl.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.xl.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.xl.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.xl.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.xl.eg.db-inspect-deffile:

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