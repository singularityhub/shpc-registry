---
layout: container
name:  "quay.io/biocontainers/bioconductor-panelcn.mops"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-panelcn.mops/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-panelcn.mops/container.yaml"
updated_at: "2023-06-19 03:09:26.039976"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-panelcn.mops"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-panelcn.mops"
config: {"url": "https://biocontainers.pro/tools/bioconductor-panelcn.mops", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-panelcn.mops", "latest": {"1.20.0--r42hdfd78af_0": "sha256:e887dd632aa76710591ee361202ba32f31bfc8bf3aeb943b9f777ffdda449104"}, "tags": {"1.8.0--r36_0": "sha256:e6b676c9183a94d10c0ccb6c7f3a883f2a81de81fec68a0897c0f8bd4e2d61eb", "1.20.0--r42hdfd78af_0": "sha256:e887dd632aa76710591ee361202ba32f31bfc8bf3aeb943b9f777ffdda449104", "1.16.0--r41hdfd78af_0": "sha256:4087abcd468059b13ffa25e9325599235b7a67554c0b1d76357c852246114b57", "1.14.0--r41hdfd78af_0": "sha256:c47f12e0144875f8a176679cbcb7fde91ea28184ecf88f0c63fb18a6f8ffb377", "1.12.0--r40hdfd78af_1": "sha256:8f43edb364616c9c7b58fb7386b8c6552f1541b5cb280f4d4c12162d184b7405", "1.10.0--r40_0": "sha256:90a2919ba4b423e9a7c5dadce25692da6b699bfe08943aa7f73df7a2a420ba03"}, "docker": "quay.io/biocontainers/bioconductor-panelcn.mops", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-panelcn.mops.
shpc-registry automated BioContainers addition for bioconductor-panelcn.mops
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-panelcn.mops
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-panelcn.mops:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-panelcn.mops/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-panelcn.mops/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-panelcn.mops-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panelcn.mops-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panelcn.mops-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-panelcn.mops-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-panelcn.mops-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-panelcn.mops-inspect-deffile:

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