---
layout: container
name:  "quay.io/biocontainers/bioconductor-pig.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pig.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pig.db0/container.yaml"
updated_at: "2023-12-26 02:24:58.054722"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pig.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pig.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pig.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pig.db0", "latest": {"3.18.0--r43hdfd78af_0": "sha256:52b23107c5f364af94774bc0b6765c9f7c0be785eb11bc9f63d4368d809971da"}, "tags": {"3.8.2--r36_1": "sha256:cfcd3a276bacdb6ace15c0e9c011f874f637b2eb7b7c3baad1269a3647b01b22", "3.16.0--r42hdfd78af_0": "sha256:8e88d2918c3cf367c5a6ad7f1ff898500ab474208fbb0464257bd59d98583ca7", "3.14.0--r41hdfd78af_1": "sha256:62fc8dfa39d305edfc9fb9c340bc13f63f482e2db48c0141536da906e33b6a57", "3.13.0--r41hdfd78af_0": "sha256:6b0b3c643e5bd380008ad14838d3440a1334cb79321dce09336f38ec8a380341", "3.12.0--r40hdfd78af_1": "sha256:cdeca6130f0385f91c360499abd6e2000c497eaa8ce30601cc99e78a052f33d7", "3.11.2--r40_0": "sha256:c8c27909b1f1656fd2f9dd774b8bf9edc593a0c0c519c3efc3e1301d0aa2948e", "3.17.0--r43hdfd78af_0": "sha256:a1cfc372d5c416b631256a78f0fb0732ed2b8bf60249311520ba323f94ac8de3", "3.18.0--r43hdfd78af_0": "sha256:52b23107c5f364af94774bc0b6765c9f7c0be785eb11bc9f63d4368d809971da"}, "docker": "quay.io/biocontainers/bioconductor-pig.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pig.db0.
shpc-registry automated BioContainers addition for bioconductor-pig.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pig.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pig.db0:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pig.db0/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pig.db0/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pig.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pig.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pig.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pig.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pig.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pig.db0-inspect-deffile:

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