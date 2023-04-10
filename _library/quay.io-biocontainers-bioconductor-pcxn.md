---
layout: container
name:  "quay.io/biocontainers/bioconductor-pcxn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pcxn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pcxn/container.yaml"
updated_at: "2023-04-10 02:51:01.553959"
latest: "2.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pcxn"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.20.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.0--r40hdfd78af_2"
 - "2.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pcxn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pcxn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pcxn", "latest": {"2.20.0--r42hdfd78af_0": "sha256:ba5a9ff2a618050ffba49b36d96007dcff5a11fc74d838ef24594f868b960a77"}, "tags": {"2.8.0--r36_1": "sha256:4ec2975985a3406d5b78911926fcecd28d0bda45be273c682d286893d88340b3", "2.20.0--r42hdfd78af_0": "sha256:ba5a9ff2a618050ffba49b36d96007dcff5a11fc74d838ef24594f868b960a77", "2.16.0--r41hdfd78af_0": "sha256:ab4a5ccf44fd09a6cdcd2024cc0e03bd94d19e6faf125e9a32ae252a4a6d6796", "2.14.0--r41hdfd78af_0": "sha256:0f8034c2f4ea59b3f4a72a50dbe50cec2b098a259c1c09cd8f6b7a2f10c0442e", "2.12.0--r40hdfd78af_2": "sha256:44d0539c99cbb458fc5b3f495dc82ae3b1949e72559770c73d49948938efc782", "2.10.0--r40_0": "sha256:adffdf5773c4f4aa063e926c0635d67642c27476cbe3b4ab8150f7f966adfda7"}, "docker": "quay.io/biocontainers/bioconductor-pcxn", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pcxn.
shpc-registry automated BioContainers addition for bioconductor-pcxn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pcxn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pcxn:2.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pcxn/2.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pcxn/2.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pcxn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcxn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcxn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pcxn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pcxn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pcxn-inspect-deffile:

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