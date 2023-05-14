---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicdatacommons"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicdatacommons/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicdatacommons/container.yaml"
updated_at: "2023-05-14 03:01:32.087413"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicdatacommons"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicdatacommons"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicdatacommons", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicdatacommons", "latest": {"1.22.0--r42hdfd78af_0": "sha256:917274470ce0934fa4ef67d8ec48a59c88717fdfa03a27bafae478326a50e8f1"}, "tags": {"1.8.0--r36_1": "sha256:79917c059f5e3476fc05277e3e547e3c492f4abba408c19ee482c84f77d35948", "1.22.0--r42hdfd78af_0": "sha256:917274470ce0934fa4ef67d8ec48a59c88717fdfa03a27bafae478326a50e8f1", "1.18.0--r41hdfd78af_0": "sha256:f8cd6a409a9099322bf63607f97c0b163ea4ba39ed78cc39e96e9f0fb7c7ffdd", "1.16.0--r41hdfd78af_0": "sha256:fa481d114a03eb0b05b569e68c398a86dc0bf0e249b909e96568d8be27acf3e5", "1.14.0--r40hdfd78af_1": "sha256:ecaf57e141df50aa1f45fd4738280ced0d8e2a52bfeccd9eaee0be357a7af192", "1.12.0--r40_0": "sha256:834e0bedeaf408bb6d35ccb6181d6e1993e58021256e2dae400cfe728c57207d"}, "docker": "quay.io/biocontainers/bioconductor-genomicdatacommons", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicdatacommons.
shpc-registry automated BioContainers addition for bioconductor-genomicdatacommons
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicdatacommons
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicdatacommons:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicdatacommons/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomicdatacommons/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicdatacommons-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicdatacommons-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicdatacommons-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicdatacommons-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicdatacommons-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicdatacommons-inspect-deffile:

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