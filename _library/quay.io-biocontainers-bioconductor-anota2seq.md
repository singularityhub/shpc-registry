---
layout: container
name:  "quay.io/biocontainers/bioconductor-anota2seq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anota2seq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anota2seq/container.yaml"
updated_at: "2025-05-10 03:45:26.680385"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-anota2seq"
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
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-anota2seq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anota2seq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-anota2seq", "latest": {"1.28.0--r44hdfd78af_0": "sha256:e0410b322bcb79edb306d3d6009a39b4e9c6457d7f201071a6ac1571218894e4"}, "tags": {"1.8.0--r36_0": "sha256:b616416e92a6fdea6eed3f543621afdcab63d4360bd897626b498a9ba5ec87d6", "1.20.0--r42hdfd78af_0": "sha256:6e8b5ceab1175a811d7b84c2f6cb62714846626327de4c52f56d4d35257e888c", "1.16.0--r41hdfd78af_0": "sha256:f8ee4ea46aaa32d430cf9ee1e4cc56f383a749b47691f6df4b394cc1ee376d2e", "1.14.0--r41hdfd78af_0": "sha256:86f5b1e3b29f2d0ff4c4178d2e94f03ecc5564b7b14483129ec95030e843d435", "1.12.0--r40hdfd78af_1": "sha256:1b8d9c352fad764c252686880808770fbae0e7d1dcb0374106a57565504dd417", "1.10.0--r40_0": "sha256:f3e655a0f987b394ec2f6827e60bf50d27a25c7e96955e0a0f7cd082e16f062a", "1.22.0--r43hdfd78af_0": "sha256:aa42114419602a0bcdba9698bd415dd08cb75698e6993054c6a0b06e93325d93", "1.24.0--r43hdfd78af_0": "sha256:c0cf9ae3fb0b091c86cc42a4606281b2ef1f737919c1c07036986f53224ef967", "1.28.0--r44hdfd78af_0": "sha256:e0410b322bcb79edb306d3d6009a39b4e9c6457d7f201071a6ac1571218894e4"}, "docker": "quay.io/biocontainers/bioconductor-anota2seq", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anota2seq.
shpc-registry automated BioContainers addition for bioconductor-anota2seq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anota2seq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anota2seq:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anota2seq/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-anota2seq/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anota2seq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anota2seq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anota2seq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anota2seq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anota2seq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anota2seq-inspect-deffile:

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