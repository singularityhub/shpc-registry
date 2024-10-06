---
layout: container
name:  "quay.io/biocontainers/pcaone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pcaone/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pcaone/container.yaml"
updated_at: "2024-10-06 03:31:47.784574"
latest: "0.4.4--h2bf1ecc_1"
container_url: "https://biocontainers.pro/tools/pcaone"
aliases:
 - "PCAone"
 - "PCAone.avx2"
 - "PCAone.x64"
versions:
 - "0.3.1--h761a8d5_0"
 - "0.3.2--h761a8d5_0"
 - "0.3.2--hf73f384_2"
 - "0.3.4--hf73f384_0"
 - "0.3.5--hf73f384_0"
 - "0.4.0--hf73f384_0"
 - "0.3.9--hf73f384_0"
 - "0.4.1--hf73f384_0"
 - "0.4.3--hf73f384_0"
 - "0.4.4--hf73f384_0"
 - "0.4.4--h2bf1ecc_1"
description: "singularity registry hpc automated addition for pcaone"
config: {"url": "https://biocontainers.pro/tools/pcaone", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pcaone", "latest": {"0.4.4--h2bf1ecc_1": "sha256:b37261af9bc8d441b5e9f129224346f3f3fe9eb5e07e3f061b1a55fa19b140bb"}, "tags": {"0.3.1--h761a8d5_0": "sha256:d99c680eaf58f9aa301d77a4addae9b092eef9bc7c5e5f34cbde5de681277366", "0.3.2--h761a8d5_0": "sha256:0d73402b7ad65f453c1493ad33400dcb54a23e027cbbc8658feea27f21ab3794", "0.3.2--hf73f384_2": "sha256:1f5135499db289a991268b131890fb958b9d0e2a7d34854cf67f74b80b4a958f", "0.3.4--hf73f384_0": "sha256:768fce3f66843ba0d45cee84a6f913d8cfc3ab850645951557063ff259a7bdb3", "0.3.5--hf73f384_0": "sha256:535846a6d87098f47e89c0f658e97d9bb6f4e4cfbc91872ac96e479d0695aa5c", "0.4.0--hf73f384_0": "sha256:7c6e62ff0f4ca66b4bc8f47c50d6cf0b69dced589d1c6da12dcbb38bd38c917c", "0.3.9--hf73f384_0": "sha256:b2264d0929f49473041c5b1af2d117912043830ef256b0e32b016806028e44e3", "0.4.1--hf73f384_0": "sha256:be4d5958bfbca0684d0dd85b4b16d770a9a6ecc2027ef4fd2546f2f79095073c", "0.4.3--hf73f384_0": "sha256:a6f96a159a8836f278473fe173999c63ba6edf5ad3c9a29ddfcff667bb7523e2", "0.4.4--hf73f384_0": "sha256:f2672399cbb605a3bb00b91f8f1638cf01135693be21e602c79d20d74d026b1f", "0.4.4--h2bf1ecc_1": "sha256:b37261af9bc8d441b5e9f129224346f3f3fe9eb5e07e3f061b1a55fa19b140bb"}, "docker": "quay.io/biocontainers/pcaone", "aliases": {"PCAone": "/usr/local/bin/PCAone", "PCAone.avx2": "/usr/local/bin/PCAone.avx2", "PCAone.x64": "/usr/local/bin/PCAone.x64"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pcaone.
singularity registry hpc automated addition for pcaone
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pcaone
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pcaone:0.4.4--h2bf1ecc_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pcaone/0.4.4--h2bf1ecc_1
$ module help quay.io/biocontainers/pcaone/0.4.4--h2bf1ecc_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pcaone-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pcaone-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pcaone-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pcaone-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pcaone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pcaone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PCAone

```bash
$ singularity exec <container> /usr/local/bin/PCAone
$ podman run --it --rm --entrypoint /usr/local/bin/PCAone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PCAone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PCAone.avx2

```bash
$ singularity exec <container> /usr/local/bin/PCAone.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/PCAone.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PCAone.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PCAone.x64

```bash
$ singularity exec <container> /usr/local/bin/PCAone.x64
$ podman run --it --rm --entrypoint /usr/local/bin/PCAone.x64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PCAone.x64   -v ${PWD} -w ${PWD} <container> -c " $@"
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