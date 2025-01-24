---
layout: container
name:  "quay.io/biocontainers/bioconductor-treeio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-treeio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-treeio/container.yaml"
updated_at: "2025-01-24 02:49:38.784742"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-treeio"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.1--r41hdfd78af_0"
 - "1.14.3--r40hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.24.1--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_1"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-treeio"
config: {"url": "https://biocontainers.pro/tools/bioconductor-treeio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-treeio", "latest": {"1.30.0--r44hdfd78af_0": "sha256:db5a8d1f350eed28c8d875ab5d5226547dfd49e1eb9e07716361c9a3abc0a030"}, "tags": {"1.8.1--r36_0": "sha256:6a213517007d24f6c70c6b56a22465f48781dbeed848f81cf9166bac71baec72", "1.22.0--r42hdfd78af_0": "sha256:4f8f50aad10962925a8eefdabfccbe53fc78f9151656d0f4b36dc11653b3f0b8", "1.18.0--r41hdfd78af_0": "sha256:7580f1ce01387acd8b9d9721452a577fdabb59ed48210bac0f6e7e2dc1355e15", "1.16.1--r41hdfd78af_0": "sha256:9377ac922392cb895387da17f438897c6cd4b4078f391c24f5c5d9084c411050", "1.14.3--r40hdfd78af_0": "sha256:34f641e313011b3eda91490ede6a113d8bca27469c7ac2325b3109e58f6ae852", "1.12.0--r40_0": "sha256:adcc3c57f0efded0bda7564921d8996bddd4c4919f3430bc5cfd59519b39a7b7", "1.24.1--r43hdfd78af_0": "sha256:976b87b9dd7acd41d41da22c98ba7cc11b548ef280d47726ae8d013657eba186", "1.26.0--r43hdfd78af_1": "sha256:ac9a73d75bab882116881e0acc919e6fa075fa3af03adec1a1eb412165ffe106", "1.30.0--r44hdfd78af_0": "sha256:db5a8d1f350eed28c8d875ab5d5226547dfd49e1eb9e07716361c9a3abc0a030"}, "docker": "quay.io/biocontainers/bioconductor-treeio", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-treeio.
shpc-registry automated BioContainers addition for bioconductor-treeio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-treeio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-treeio:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-treeio/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-treeio/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-treeio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treeio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treeio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-treeio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-treeio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-treeio-inspect-deffile:

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