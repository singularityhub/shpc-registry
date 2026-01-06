---
layout: container
name:  "quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5/container.yaml"
updated_at: "2026-01-06 04:01:43.340749"
latest: "3.10.0--r44hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-mafdb.1kgenomes.phase1.hs37d5"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.7.1--r36_2"
 - "3.10.0--r42hdfd78af_7"
 - "3.10.0--r43hdfd78af_8"
 - "3.10.0--r43hdfd78af_9"
 - "3.10.0--r44hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-mafdb.1kgenomes.phase1.hs37d5"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mafdb.1kgenomes.phase1.hs37d5", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mafdb.1kgenomes.phase1.hs37d5", "latest": {"3.10.0--r44hdfd78af_10": "sha256:5639c1ad5b440c36632fd82070e9bdee2322e24e646fc8c6b4e152c7f166e970"}, "tags": {"3.7.1--r36_2": "sha256:f55e3b851692b2444cf206d6ef01d29beee75a2c620b56d135bb43811de00262", "3.10.0--r42hdfd78af_7": "sha256:543f3a77b8f494f6147c654fe7e3f0bdd0fab390a9498a00c98104c6666bd583", "3.10.0--r43hdfd78af_8": "sha256:a7df6ddede79fb7f80a2fcf7b54d02fe9b7fd8d68aedc10d2a8ec969859fb005", "3.10.0--r43hdfd78af_9": "sha256:2449ff600d11309dbc7b230f376db21333c787f6f2ea8447813917e1dfbac47e", "3.10.0--r44hdfd78af_10": "sha256:5639c1ad5b440c36632fd82070e9bdee2322e24e646fc8c6b4e152c7f166e970"}, "docker": "quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5.
shpc-registry automated BioContainers addition for bioconductor-mafdb.1kgenomes.phase1.hs37d5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5:3.10.0--r44hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5/3.10.0--r44hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-mafdb.1kgenomes.phase1.hs37d5/3.10.0--r44hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mafdb.1kgenomes.phase1.hs37d5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.1kgenomes.phase1.hs37d5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.1kgenomes.phase1.hs37d5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mafdb.1kgenomes.phase1.hs37d5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mafdb.1kgenomes.phase1.hs37d5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mafdb.1kgenomes.phase1.hs37d5-inspect-deffile:

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