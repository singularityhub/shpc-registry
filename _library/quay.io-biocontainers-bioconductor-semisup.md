---
layout: container
name:  "quay.io/biocontainers/bioconductor-semisup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-semisup/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-semisup/container.yaml"
updated_at: "2025-09-28 03:49:33.766874"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-semisup"
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
 - "1.12.3--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-semisup"
config: {"url": "https://biocontainers.pro/tools/bioconductor-semisup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-semisup", "latest": {"1.30.0--r44hdfd78af_0": "sha256:dd6e6eea2fdd4236f8da0bfcecb237a777ae199644cadc737a936f31e2a42f86"}, "tags": {"1.8.0--r36_1": "sha256:908e6aa7d0972558ea83ee5f04484c4bb8407cff3762071d7cd27774a5699a0c", "1.22.0--r42hdfd78af_0": "sha256:93089f6e87aec9f642a7586143e4f1919c8f672fc1cd7cb777cf9d0f7b4ecdbe", "1.18.0--r41hdfd78af_0": "sha256:d565d5890612bad3d1794c03f7664bc64cf77723a6e8a20142565d11e8a91ef9", "1.16.0--r41hdfd78af_0": "sha256:a837313bd5ae0ed3bfbfa37c8b7e268c1a0ad00a12946f871bc03dd65fd1b881", "1.14.0--r40hdfd78af_1": "sha256:b24d6497c902434eb7bb3b4f3a6b5cb076377e7048dcb4affae7b6bebb994cc0", "1.12.3--r40_0": "sha256:418ad264741f624b8d25bcff68314910257b8675801b0118bf1ef3201be4f6f5", "1.24.0--r43hdfd78af_0": "sha256:726e5325942708a3435caa64e2a8e33ec59153f2ccd796d4b0471f1b9cedbfe4", "1.26.0--r43hdfd78af_0": "sha256:2da6265fd89f26d22b66eb3f5426b297286ef5b9728800e4a4f3685caca029c1", "1.30.0--r44hdfd78af_0": "sha256:dd6e6eea2fdd4236f8da0bfcecb237a777ae199644cadc737a936f31e2a42f86"}, "docker": "quay.io/biocontainers/bioconductor-semisup", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-semisup.
shpc-registry automated BioContainers addition for bioconductor-semisup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-semisup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-semisup:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-semisup/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-semisup/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-semisup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-semisup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-semisup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-semisup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-semisup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-semisup-inspect-deffile:

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