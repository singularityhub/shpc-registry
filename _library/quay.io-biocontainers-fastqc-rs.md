---
layout: container
name:  "quay.io/biocontainers/fastqc-rs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastqc-rs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastqc-rs/container.yaml"
updated_at: "2025-02-01 02:52:53.826524"
latest: "0.3.4--hd2a40b3_1"
container_url: "https://biocontainers.pro/tools/fastqc-rs"
aliases:
 - "fqc"
versions:
 - "0.3.2--he9f29cb_1"
 - "0.3.2--he6968d2_2"
 - "0.3.4--h101ab07_0"
 - "0.3.4--hd2a40b3_1"
description: "shpc-registry automated BioContainers addition for fastqc-rs"
config: {"url": "https://biocontainers.pro/tools/fastqc-rs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastqc-rs", "latest": {"0.3.4--hd2a40b3_1": "sha256:fc512c4aef084bdff061419de6237181cbb5be60460b703b33495591302d3c5e"}, "tags": {"0.3.2--he9f29cb_1": "sha256:f2055f57f051940b57504b49cfddad9e953cf188e381a85f862da23797dae948", "0.3.2--he6968d2_2": "sha256:06922bf4202f66690ff57c2198c9d503d17e2c74da53226f48447f2b91a68d9a", "0.3.4--h101ab07_0": "sha256:538ef5a08a0c619673ca3a6bb6f0d15d0a69d45213300a1d292c42c11cebfbee", "0.3.4--hd2a40b3_1": "sha256:fc512c4aef084bdff061419de6237181cbb5be60460b703b33495591302d3c5e"}, "docker": "quay.io/biocontainers/fastqc-rs", "aliases": {"fqc": "/usr/local/bin/fqc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastqc-rs.
shpc-registry automated BioContainers addition for fastqc-rs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastqc-rs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastqc-rs:0.3.4--hd2a40b3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastqc-rs/0.3.4--hd2a40b3_1
$ module help quay.io/biocontainers/fastqc-rs/0.3.4--hd2a40b3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastqc-rs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastqc-rs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastqc-rs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastqc-rs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastqc-rs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastqc-rs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqc

```bash
$ singularity exec <container> /usr/local/bin/fqc
$ podman run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
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