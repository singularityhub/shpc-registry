---
layout: container
name:  "quay.io/biocontainers/bioconductor-ga4ghclient"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ga4ghclient/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ga4ghclient/container.yaml"
updated_at: "2024-07-18 04:17:04.566500"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ga4ghclient"
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
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ga4ghclient"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ga4ghclient", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ga4ghclient", "latest": {"1.26.0--r43hdfd78af_0": "sha256:d4c744f79995d06b7eccb2c0d9818a6faca89c1448f7a35621d6e4b0dc07f197"}, "tags": {"1.8.0--r36_1": "sha256:590d237eb6213a8f175d161731f17b1a800ecd66defb4ed5c52e4ff002642e83", "1.22.0--r42hdfd78af_0": "sha256:2914199482004f1bdd0b370629b61d5585be1418abe2abbb1f9ae714bc2e7ade", "1.18.0--r41hdfd78af_0": "sha256:e5e9e0405701e7eeb8dcd939ce04b90e4916c5a5f97a8ca8dba086776c56e78d", "1.16.0--r41hdfd78af_0": "sha256:60596c867f15aa7c33c2139dc4aaeefd1ba77d94196ee5ea04b3112305e550cf", "1.14.0--r40hdfd78af_1": "sha256:39130b59e6fe43fd75af4c6dc659d9dbd518d993da7d227c5c39d5332733cf25", "1.12.0--r40_0": "sha256:57dcde0c948ecb0311186f5ed0c05f3ae05a95b4c94665a09428b2d06ec84eee", "1.24.0--r43hdfd78af_0": "sha256:9aeca4e08893a13e21c76df5a290fb9f9720a35cc4a898c7433c02c127069a0e", "1.26.0--r43hdfd78af_0": "sha256:d4c744f79995d06b7eccb2c0d9818a6faca89c1448f7a35621d6e4b0dc07f197"}, "docker": "quay.io/biocontainers/bioconductor-ga4ghclient", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ga4ghclient.
shpc-registry automated BioContainers addition for bioconductor-ga4ghclient
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ga4ghclient
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ga4ghclient:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ga4ghclient/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ga4ghclient/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ga4ghclient-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ga4ghclient-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ga4ghclient-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ga4ghclient-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ga4ghclient-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ga4ghclient-inspect-deffile:

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