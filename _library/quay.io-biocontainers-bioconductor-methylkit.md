---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylkit/container.yaml"
updated_at: "2025-09-18 05:43:33.221174"
latest: "1.32.0--r44h77050f0_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylkit"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351hf484d3e_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.1--r40h399db7b_0"
 - "1.14.1--r40h5f743cb_0"
 - "1.24.0--r42hf17093f_1"
 - "1.26.0--r43hf17093f_0"
 - "1.28.0--r43hf17093f_0"
 - "1.32.0--r44h77050f0_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylkit"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylkit", "latest": {"1.32.0--r44h77050f0_0": "sha256:297ffee2149453173141ccb9dcd10ebb4ed4a2d0b37283a0942eb2a2a4ebb013"}, "tags": {"1.8.1--r351hf484d3e_0": "sha256:c6e8b2f6ac1098afb763a365c428ffd87f8697c76988adb49db5a3b3e74bab97", "1.24.0--r42hc247a5b_0": "sha256:2fafe50bdc5b1c4b395a43252a96e01ff19625f6b1191e1f9e0037a7f9caf7be", "1.20.0--r41hc247a5b_2": "sha256:d79515869b0ed0abc0a10a8a002446cc5c54803b6e203ff76b8faba2a85b07d3", "1.18.0--r41h399db7b_0": "sha256:d07b8d2b40ccc89d3a5aba404c9838896cbbac923f5cba687dc925f5c4fc3550", "1.16.1--r40h399db7b_0": "sha256:6588ac83ebe4805f4d7b561d5db04e8c6ae240fb52659e9cd250ac4c5e326c0a", "1.14.1--r40h5f743cb_0": "sha256:fc3f51fa17884aca1ef397ec56a8c7bdf2a444a7dac398da556afa8fcbc0d8d3", "1.24.0--r42hf17093f_1": "sha256:a41620e457db22d376f2c452e6bf75f84ed2100e1285f12b13ee40562d343a51", "1.26.0--r43hf17093f_0": "sha256:96c91be9687991ef9e415a6a18e2e28856957a34e577ea3abaeb42f24859743e", "1.28.0--r43hf17093f_0": "sha256:40a26dd0292c28c132452b1d434a91ebcbcf8a5d1d2d8203ed2d1b6b67ab8dfc", "1.32.0--r44h77050f0_0": "sha256:297ffee2149453173141ccb9dcd10ebb4ed4a2d0b37283a0942eb2a2a4ebb013"}, "docker": "quay.io/biocontainers/bioconductor-methylkit", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylkit.
shpc-registry automated BioContainers addition for bioconductor-methylkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylkit:1.32.0--r44h77050f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylkit/1.32.0--r44h77050f0_0
$ module help quay.io/biocontainers/bioconductor-methylkit/1.32.0--r44h77050f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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