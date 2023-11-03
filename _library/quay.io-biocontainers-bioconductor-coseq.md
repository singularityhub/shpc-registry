---
layout: container
name:  "quay.io/biocontainers/bioconductor-coseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-coseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-coseq/container.yaml"
updated_at: "2023-11-03 02:37:46.162847"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-coseq"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-coseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-coseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-coseq", "latest": {"1.24.0--r43hdfd78af_0": "sha256:25e3dc920044827eafa59acae547b60c3340f42a254ae9818c4828f05d129732"}, "tags": {"1.8.0--r36_1": "sha256:9118793b02994c069b9709049d4bc500b87a8319bc88afb23a665903b897c39c", "1.22.0--r42hdfd78af_0": "sha256:152d44d709ec60e7f915c5548ba4ecb2828681d9bebfd878e4c515510439bed5", "1.18.0--r41hdfd78af_0": "sha256:626ba2c320f3c6a575c530d4eb73a2fd05fd0dc05cf5aad1cf0c3a930ded2a67", "1.16.0--r41hdfd78af_0": "sha256:529f2fd2df74165905c3a0c12ef9ebe45135bd05238c53fa3b3ecf36b3a5829f", "1.12.0--r40_0": "sha256:d4d6f67019f8df6b09fbb26ddef361a33c10aa88c97d7517ad99b667ec02075b", "1.10.0--r36_0": "sha256:53b4208420dac921e868687de55c6e10449cb5499fceb3d7c76db0bd9f722051", "1.24.0--r43hdfd78af_0": "sha256:25e3dc920044827eafa59acae547b60c3340f42a254ae9818c4828f05d129732"}, "docker": "quay.io/biocontainers/bioconductor-coseq", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-coseq.
shpc-registry automated BioContainers addition for bioconductor-coseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-coseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-coseq:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-coseq/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-coseq/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-coseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-coseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-coseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-coseq-inspect-deffile:

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