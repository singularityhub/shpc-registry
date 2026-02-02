---
layout: container
name:  "quay.io/biocontainers/perl-io-compress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-io-compress/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-io-compress/container.yaml"
updated_at: "2026-02-02 12:51:41.441583"
latest: "2.214--pl5321h503566f_0"
container_url: "https://biocontainers.pro/tools/perl-io-compress"

versions:
 - "2.201--pl5321h87f3376_0"
 - "2.201--pl5321hdbdd923_2"
 - "2.201--pl5321hdbdd923_3"
 - "2.201--pl5321h503566f_4"
 - "2.201--pl5321h503566f_5"
 - "2.213--pl5321h503566f_0"
 - "2.214--pl5321h503566f_0"
description: "shpc-registry automated BioContainers addition for perl-io-compress"
config: {"url": "https://biocontainers.pro/tools/perl-io-compress", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-io-compress", "latest": {"2.214--pl5321h503566f_0": "sha256:8a08b6f771c325eb576c3c13c7e37f5cd760c2ce787c3171a70c6d346cfa7ac7"}, "tags": {"2.201--pl5321h87f3376_0": "sha256:0144c44a01c57ac54b86676462335fe12620b7fdb2c25822e43c84a652448e79", "2.201--pl5321hdbdd923_2": "sha256:d3f3d12652640fb994d9e2c0fc875008589297a8c6f3bad7309a881b8e0988c1", "2.201--pl5321hdbdd923_3": "sha256:d680197ec6fa3330032fa9efd1653a40c7f3bc6f9507a22dd30072fbd10be8d4", "2.201--pl5321h503566f_4": "sha256:0a65cc8ec039a4602c70aa9ca671d8cea90462b98c9e81032f18067391db278c", "2.201--pl5321h503566f_5": "sha256:2846dfb45d6e0a4607d5467016cf8efef2317c0efcbfec278e140be4f6f6e7a8", "2.213--pl5321h503566f_0": "sha256:e8d465b0f5f8a2e24f50a40cbc768259408795572b00397882a8ebc7333cb71e", "2.214--pl5321h503566f_0": "sha256:8a08b6f771c325eb576c3c13c7e37f5cd760c2ce787c3171a70c6d346cfa7ac7"}, "docker": "quay.io/biocontainers/perl-io-compress"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-io-compress.
shpc-registry automated BioContainers addition for perl-io-compress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-io-compress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-io-compress:2.214--pl5321h503566f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-io-compress/2.214--pl5321h503566f_0
$ module help quay.io/biocontainers/perl-io-compress/2.214--pl5321h503566f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-io-compress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-io-compress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-io-compress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-io-compress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-io-compress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-io-compress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-io-compress

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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