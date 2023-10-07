---
layout: container
name:  "quay.io/biocontainers/bioconductor-sampleclassifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sampleclassifier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sampleclassifier/container.yaml"
updated_at: "2023-10-07 02:48:28.756494"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sampleclassifier"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.11.0--r40_0"
 - "1.10.0--r36_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sampleclassifier"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sampleclassifier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sampleclassifier", "latest": {"1.24.0--r43hdfd78af_0": "sha256:81b34ae1237d4aa8a2ad8d2a143402f8162ff7b781c04325bdb8ca33ea1f748a"}, "tags": {"1.8.0--r36_1": "sha256:ab1961229dc711f2e71353c1c355d9793411553359a383c39fd180195b6f6c4e", "1.22.0--r42hdfd78af_0": "sha256:a8d7c00b31bbcc1ff69976ba4a6d8579b33df1d4a762af3360fb18153a65e6e5", "1.18.0--r41hdfd78af_0": "sha256:99413830bd0472d9f29ec67bc5c5e1e41781a841d8b769fcccb4ef59daa26529", "1.16.0--r41hdfd78af_0": "sha256:02d2d0d06677d3621b4dc40189afeb326dea717f36edda23efb3e02ca7e4bd09", "1.11.0--r40_0": "sha256:19da9bad68411a2f00f8a8cb2a0eedfb3c9e9dcce021b654eba40824ed450dfd", "1.10.0--r36_0": "sha256:6a35cc8973ee0552bdb736e3e720aa7fd29435079d01f716b831a9dd698625bf", "1.24.0--r43hdfd78af_0": "sha256:81b34ae1237d4aa8a2ad8d2a143402f8162ff7b781c04325bdb8ca33ea1f748a"}, "docker": "quay.io/biocontainers/bioconductor-sampleclassifier", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sampleclassifier.
shpc-registry automated BioContainers addition for bioconductor-sampleclassifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sampleclassifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sampleclassifier:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sampleclassifier/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sampleclassifier/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sampleclassifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sampleclassifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sampleclassifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sampleclassifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sampleclassifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sampleclassifier-inspect-deffile:

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