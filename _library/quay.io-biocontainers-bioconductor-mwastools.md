---
layout: container
name:  "quay.io/biocontainers/bioconductor-mwastools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mwastools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mwastools/container.yaml"
updated_at: "2023-04-19 02:57:21.746168"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mwastools"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.22.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mwastools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mwastools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mwastools", "latest": {"1.22.0--r42hdfd78af_0": "sha256:3b19a6f7172e626355c9718bf63926f413b546324f267c8cf4b421afebcd611f"}, "tags": {"1.8.0--r36_1": "sha256:91431b41a094dbe342475014287c208e6ee4fe05874ccae6ca085809dc2b1366", "1.18.0--r41hdfd78af_0": "sha256:7a2484439ac904045eac8aad915dffb7d7e99546f8fb054527dc0b03ab08aedb", "1.16.0--r41hdfd78af_0": "sha256:d0c14d65b7373ce2cdb76028d82e4406a747d5ccc2a9dfd5519bd31f18fedc98", "1.14.0--r40hdfd78af_1": "sha256:f348f9de5dcdd69974d25e60c35fddd73f587ebc32f6abbd6774b73d31f629b0", "1.12.0--r40_0": "sha256:2e5555287d9594819f32c35ea582f4de61dbae47f989e5954c761963eff757c7", "1.10.0--r36_0": "sha256:aaea3670618eae8d6929b6d97ce731a1617cdc2e030c70fc0fa4d454b985ec3c", "1.22.0--r42hdfd78af_0": "sha256:3b19a6f7172e626355c9718bf63926f413b546324f267c8cf4b421afebcd611f"}, "docker": "quay.io/biocontainers/bioconductor-mwastools", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mwastools.
shpc-registry automated BioContainers addition for bioconductor-mwastools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mwastools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mwastools:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mwastools/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mwastools/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mwastools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mwastools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mwastools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mwastools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mwastools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mwastools-inspect-deffile:

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