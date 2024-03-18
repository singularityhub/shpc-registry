---
layout: container
name:  "quay.io/biocontainers/bioconductor-opweight"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-opweight/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-opweight/container.yaml"
updated_at: "2024-03-18 03:01:52.195331"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-opweight"
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
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-opweight"
config: {"url": "https://biocontainers.pro/tools/bioconductor-opweight", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-opweight", "latest": {"1.24.0--r43hdfd78af_0": "sha256:bb69d56852e9e433d58983b0df1328a27268a4f17d0e408d171e6556bb3aabfc"}, "tags": {"1.8.0--r36_0": "sha256:82bbc0f5dc5f807fb0013ed5ba433a63b41b5ae93587f3e27241269da80b8bb6", "1.20.0--r42hdfd78af_0": "sha256:35f4a9fb610c1e725ee35db5c8a18ec50e377328281c33b30a0563b4d7ee94f5", "1.16.0--r41hdfd78af_0": "sha256:4a94202e734e80618a38ccafac75d3f1eaddc7c1075ff244a0a657e2ee354cf1", "1.14.0--r41hdfd78af_0": "sha256:1711ec7dfe809f06ae4bb2aebf5ada976504de0c2054914dc4894391d6866d46", "1.12.0--r40hdfd78af_1": "sha256:414a99cc9c9e289cac6eb0e637e0bb1d5b3c1d08a82530ab72297e55d388eb14", "1.10.0--r40_0": "sha256:0b3b9b915b1c1a88a4255019541e43a15e553f1f4191aa23bbfab3267aa5e8da", "1.22.0--r43hdfd78af_0": "sha256:464d1066020bfa99708f2f5f45323684f870cc0a40906b898f4a90b9671fe6f1", "1.24.0--r43hdfd78af_0": "sha256:bb69d56852e9e433d58983b0df1328a27268a4f17d0e408d171e6556bb3aabfc"}, "docker": "quay.io/biocontainers/bioconductor-opweight", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-opweight.
shpc-registry automated BioContainers addition for bioconductor-opweight
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-opweight
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-opweight:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-opweight/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-opweight/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-opweight-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-opweight-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-opweight-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-opweight-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-opweight-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-opweight-inspect-deffile:

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