---
layout: container
name:  "quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38/container.yaml"
updated_at: "2024-09-02 03:21:05.714001"
latest: "3.10.0--r43hdfd78af_9"
container_url: "https://biocontainers.pro/tools/bioconductor-mafdb.exac.r1.0.nontcga.grch38"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.7.0--r36_2"
 - "3.10.0--r42hdfd78af_7"
 - "3.10.0--r43hdfd78af_8"
 - "3.10.0--r43hdfd78af_9"
description: "shpc-registry automated BioContainers addition for bioconductor-mafdb.exac.r1.0.nontcga.grch38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mafdb.exac.r1.0.nontcga.grch38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mafdb.exac.r1.0.nontcga.grch38", "latest": {"3.10.0--r43hdfd78af_9": "sha256:7db90be97bb29e4ea25730368e144087336c5aaa18c56e7629c7c6ae68ad300e"}, "tags": {"3.7.0--r36_2": "sha256:387a8da0fcce73f4a65bc42adb2511667bd1417f715a81b5eed788622dc78d87", "3.10.0--r42hdfd78af_7": "sha256:106c729efe3b9595f8b98bcb706c4fcf14db3b722ed5317c4178e2bc48c95c04", "3.10.0--r43hdfd78af_8": "sha256:41631b59968fe31c9288e7e7bfa151472c701b50e520c864ad17a7b21a025545", "3.10.0--r43hdfd78af_9": "sha256:7db90be97bb29e4ea25730368e144087336c5aaa18c56e7629c7c6ae68ad300e"}, "docker": "quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38.
shpc-registry automated BioContainers addition for bioconductor-mafdb.exac.r1.0.nontcga.grch38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38:3.10.0--r43hdfd78af_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38/3.10.0--r43hdfd78af_9
$ module help quay.io/biocontainers/bioconductor-mafdb.exac.r1.0.nontcga.grch38/3.10.0--r43hdfd78af_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mafdb.exac.r1.0.nontcga.grch38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.exac.r1.0.nontcga.grch38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.exac.r1.0.nontcga.grch38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mafdb.exac.r1.0.nontcga.grch38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mafdb.exac.r1.0.nontcga.grch38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mafdb.exac.r1.0.nontcga.grch38-inspect-deffile:

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