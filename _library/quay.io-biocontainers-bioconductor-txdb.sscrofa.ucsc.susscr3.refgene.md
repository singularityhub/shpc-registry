---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene/container.yaml"
updated_at: "2025-02-07 03:32:24.987740"
latest: "3.12.0--r44hdfd78af_8"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.4.6--r36_1"
 - "3.12.0--r42hdfd78af_5"
 - "3.11.0--r40_0"
 - "3.10.0--r36_0"
 - "3.12.0--r43hdfd78af_6"
 - "3.12.0--r43hdfd78af_7"
 - "3.12.0--r44hdfd78af_8"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.sscrofa.ucsc.susscr3.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.sscrofa.ucsc.susscr3.refgene", "latest": {"3.12.0--r44hdfd78af_8": "sha256:c15d65c70b5e0735458c183d1f9861e43a02d4aaae954e89d6d7b56024f3122a"}, "tags": {"3.4.6--r36_1": "sha256:f3a3977967d80e17addccde2fe4b5e0f3c074556be6d26956ab33c87794b444f", "3.12.0--r42hdfd78af_5": "sha256:8aed5f665cd0ef1d59fb35c99255d444b8060125570f4ede237b3e155275c533", "3.11.0--r40_0": "sha256:cf41d71291f5b01fdbaa987b6ef04f8aabd043bd5e9b1ae0ec7b9ab7a74806ef", "3.10.0--r36_0": "sha256:3a3710e9c7b090d7d5459a9971d516194f3ce39779c9d36e5965ab306637bbce", "3.12.0--r43hdfd78af_6": "sha256:ed57e0af88fff1cf5b259f52eba5744597ff224c26c96cdedca5aa5b1072098c", "3.12.0--r43hdfd78af_7": "sha256:fd42a792b232d7e90dc8c49192e2fe51fb2dfe951b21101738864563a285d903", "3.12.0--r44hdfd78af_8": "sha256:c15d65c70b5e0735458c183d1f9861e43a02d4aaae954e89d6d7b56024f3122a"}, "docker": "quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.sscrofa.ucsc.susscr3.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene:3.12.0--r44hdfd78af_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene/3.12.0--r44hdfd78af_8
$ module help quay.io/biocontainers/bioconductor-txdb.sscrofa.ucsc.susscr3.refgene/3.12.0--r44hdfd78af_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.sscrofa.ucsc.susscr3.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.sscrofa.ucsc.susscr3.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.sscrofa.ucsc.susscr3.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.sscrofa.ucsc.susscr3.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.sscrofa.ucsc.susscr3.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.sscrofa.ucsc.susscr3.refgene-inspect-deffile:

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