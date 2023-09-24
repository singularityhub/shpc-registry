---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellscape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellscape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellscape/container.yaml"
updated_at: "2023-09-24 02:50:14.962579"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellscape"
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
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellscape"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellscape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellscape", "latest": {"1.24.0--r43hdfd78af_0": "sha256:da7f9e540bc102c43f38c156b6005eea0593c1478d806dfc23e8553d95a9a1df"}, "tags": {"1.8.0--r36_1": "sha256:b629ef9c8b5b054ce6d836beb78f0b28ceeabbdec66956e9d457ad540fc1bd92", "1.22.0--r42hdfd78af_0": "sha256:8213f257d2dfb0fd8de8fbf0ddfc1dab3e915312d12d1006e23a869b7b18ce47", "1.18.0--r41hdfd78af_0": "sha256:ea1aee7d8bd5d82bb37578145795b6d6da8d901d123fad38ad4799f015d715f5", "1.16.0--r41hdfd78af_0": "sha256:06a4a17b6ed1f1e89a983a70b62f8cdcda73b5aae012a988eab0eabc7ca8f29d", "1.14.0--r40hdfd78af_1": "sha256:cd91ffbf31f585b55cf7ec3aebc48feca922142f7ee572bd8609e81e1efb8122", "1.12.0--r40_0": "sha256:a4d9b8a14470c1559b5a95be9ef80bab5340c8d62c1979df56496c9cc696140e", "1.24.0--r43hdfd78af_0": "sha256:da7f9e540bc102c43f38c156b6005eea0593c1478d806dfc23e8553d95a9a1df"}, "docker": "quay.io/biocontainers/bioconductor-cellscape", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellscape.
shpc-registry automated BioContainers addition for bioconductor-cellscape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellscape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellscape:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellscape/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellscape/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellscape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellscape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellscape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellscape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellscape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellscape-inspect-deffile:

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