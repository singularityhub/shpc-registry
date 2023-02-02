---
layout: container
name:  "quay.io/biocontainers/bioconductor-zebrafish.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-zebrafish.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-zebrafish.db0/container.yaml"
updated_at: "2023-02-02 03:33:13.371618"
latest: "3.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-zebrafish.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-zebrafish.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-zebrafish.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-zebrafish.db0", "latest": {"3.16.0--r42hdfd78af_0": "sha256:45d1c54448a328ec516b02b1c206128b31a96641cc70adf3f517e16c0777785c"}, "tags": {"3.8.2--r36_1": "sha256:1fe40caf61605a6188686a57b18cc47ab629bb0a26fcbdf3bb306139713e91cf", "3.16.0--r42hdfd78af_0": "sha256:45d1c54448a328ec516b02b1c206128b31a96641cc70adf3f517e16c0777785c", "3.14.0--r41hdfd78af_1": "sha256:76dd9b8977334b0f81fa657d6df5d238b55d541d895a9681afc9633a1e8dab55", "3.13.0--r41hdfd78af_0": "sha256:04f1533ed44441dd301475e091132f3cb6d3ea214f8e49363145c0395dfca2e5", "3.12.0--r40hdfd78af_1": "sha256:8d7c73e484c5502d47eae908212b547c308e64ce81199664a1d3264d58e45147", "3.11.2--r40_0": "sha256:f289b732c5a67e83bd0ca5efa411f9c17e1b7b8cb9ac59b8aa82f380de69f1f6"}, "docker": "quay.io/biocontainers/bioconductor-zebrafish.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-zebrafish.db0.
shpc-registry automated BioContainers addition for bioconductor-zebrafish.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-zebrafish.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-zebrafish.db0:3.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-zebrafish.db0/3.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-zebrafish.db0/3.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-zebrafish.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zebrafish.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zebrafish.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-zebrafish.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-zebrafish.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-zebrafish.db0-inspect-deffile:

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