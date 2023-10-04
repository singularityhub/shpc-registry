---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocversion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocversion/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocversion/container.yaml"
updated_at: "2023-10-04 05:07:23.960723"
latest: "3.17.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocversion"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.9.0--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_0"
 - "3.13.1--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.17.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocversion"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocversion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocversion", "latest": {"3.17.1--r43hdfd78af_0": "sha256:8b5f05d8a7d8f1a3796bb7746639ec70457b530c43e9fd857c94aa492047c02c"}, "tags": {"3.9.0--r36_1": "sha256:fdcaa0698da552cbbd9b00b5e0919489f2d56353609bb8802a8604646fbf0c61", "3.16.0--r42hdfd78af_0": "sha256:9325edeadeeb99f5e8f8104273279187754f140798a8af9faa38bba3c7013c7a", "3.14.0--r41hdfd78af_0": "sha256:f251340bb1c87565f3be082a92c0c488f08e406186c668a4299547ba666f921b", "3.13.1--r41hdfd78af_0": "sha256:70c18d41b951f9627789d7a4f84688103ec207781978091eab7c62f311bc5ee6", "3.12.0--r40hdfd78af_1": "sha256:e4463ec58d876e8080f5760d03d2870f724031cb4956fea54e35bc525dd298fb", "3.11.1--r40_0": "sha256:c901a6d40cc5afbb4f9b4e40878ba084b582e95b637968452d04556cf62419f7", "3.17.1--r43hdfd78af_0": "sha256:8b5f05d8a7d8f1a3796bb7746639ec70457b530c43e9fd857c94aa492047c02c"}, "docker": "quay.io/biocontainers/bioconductor-biocversion", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocversion.
shpc-registry automated BioContainers addition for bioconductor-biocversion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocversion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocversion:3.17.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocversion/3.17.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocversion/3.17.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocversion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocversion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocversion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocversion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocversion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocversion-inspect-deffile:

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