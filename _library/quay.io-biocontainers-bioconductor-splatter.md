---
layout: container
name:  "quay.io/biocontainers/bioconductor-splatter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-splatter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-splatter/container.yaml"
updated_at: "2025-10-06 06:44:32.387326"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-splatter"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.1--r41hdfd78af_0"
 - "1.16.1--r41hdfd78af_0"
 - "1.14.1--r40hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-splatter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-splatter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-splatter", "latest": {"1.24.0--r43hdfd78af_0": "sha256:7165a3215c5a637d73cd484ce26ea6b374576522286aeabf3a5a3372037755cc"}, "tags": {"1.8.0--r36_1": "sha256:b7f2a09627e9815febe1f30fd81512d0d9475d2d6308c7d39df99386a05e06ae", "1.22.0--r42hdfd78af_0": "sha256:9e7c59ed99bff73aa15af39c43c68ab624155082ba83987f86d9fcac59becab2", "1.18.1--r41hdfd78af_0": "sha256:1ac4008d34645082187a78c4715463fd82a2313c3cf3ad17ffe55dae0162b1d1", "1.16.1--r41hdfd78af_0": "sha256:29174dee21b4dc3663627e6773c77f2246ebc2e739a88c91398401be8948ad17", "1.14.1--r40hdfd78af_0": "sha256:47c7cfa69dd3b3622195832beb4063373d8d3a9a9accea38706a8a749c4fa844", "1.12.0--r40_0": "sha256:c2c8562618032d9546f5723d51aadf901fd5884523b5556097d3fbd025e7ecdd", "1.24.0--r43hdfd78af_0": "sha256:7165a3215c5a637d73cd484ce26ea6b374576522286aeabf3a5a3372037755cc"}, "docker": "quay.io/biocontainers/bioconductor-splatter", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-splatter.
shpc-registry automated BioContainers addition for bioconductor-splatter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-splatter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-splatter:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-splatter/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-splatter/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-splatter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splatter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splatter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-splatter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-splatter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-splatter-inspect-deffile:

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