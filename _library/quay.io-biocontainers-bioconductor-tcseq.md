---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcseq/container.yaml"
updated_at: "2025-03-27 03:47:06.871751"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcseq"
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
 - "1.23.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcseq", "latest": {"1.30.0--r44hdfd78af_0": "sha256:ff757842c14e6a41cdad14a49f225c5f8c4054963dc2284398629cb70d0c02ee"}, "tags": {"1.8.0--r36_1": "sha256:dc751aa2c65d5b5a39676cc7e3c4b0d7ef382d5b35ab1659e0c5ef39c0441e62", "1.22.0--r42hdfd78af_0": "sha256:b99984884dbccf7adef94038281fd05474c0dc991a12d2b51aa074815473385e", "1.18.0--r41hdfd78af_0": "sha256:c7e843ce461a02039ba692072fa968ef948fc0ad1e53bf14b4340bcc4aaccdb2", "1.16.0--r41hdfd78af_0": "sha256:2dc91bdd50e7cda72ac857fad49cc6adb6ebaa7ebbb80ac81d55b1b42b04a09d", "1.14.0--r40hdfd78af_1": "sha256:b4bff060a665b3495253831e7a8b8a283541f95b3c225a8082f8b8f01fb9ef38", "1.12.0--r40_0": "sha256:6d17304473324e752bdaa061ee62976e962e66c9b151afadc2e07b1da3b25963", "1.23.0--r43hdfd78af_0": "sha256:5659366fcd96636f549359ac591b235993498f7d7f68166aba76137ace765979", "1.26.0--r43hdfd78af_0": "sha256:c4d0ab6a0c2a9e9df29a0b89f1a394a5938cb6d92d6c21af2d2eec1733becc30", "1.30.0--r44hdfd78af_0": "sha256:ff757842c14e6a41cdad14a49f225c5f8c4054963dc2284398629cb70d0c02ee"}, "docker": "quay.io/biocontainers/bioconductor-tcseq", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcseq.
shpc-registry automated BioContainers addition for bioconductor-tcseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcseq:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcseq/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcseq/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcseq-inspect-deffile:

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