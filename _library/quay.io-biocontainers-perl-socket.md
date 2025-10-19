---
layout: container
name:  "quay.io/biocontainers/perl-socket"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-socket/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-socket/container.yaml"
updated_at: "2025-10-19 03:58:49.501881"
latest: "2.027--pl5321h5c03b87_6"
container_url: "https://biocontainers.pro/tools/perl-socket"

versions:
 - "2.027--pl5321hec16e2b_3"
 - "2.027--pl5321h031d066_4"
 - "2.027--pl5321h7b50bb2_5"
 - "2.027--pl5321h5c03b87_6"
description: "shpc-registry automated BioContainers addition for perl-socket"
config: {"url": "https://biocontainers.pro/tools/perl-socket", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-socket", "latest": {"2.027--pl5321h5c03b87_6": "sha256:2f57c319b0c2eb47f02e3949a34f05d2b23a624350e1fee30a5167ff1e2a190d"}, "tags": {"2.027--pl5321hec16e2b_3": "sha256:6258d58b6164744d67b1afa7223265b24789a2295e612ee247cd575221ab6399", "2.027--pl5321h031d066_4": "sha256:6fd2993c0fee09393b9849455f1d6da72b79ea5350bcf366a640d1e8370fff1a", "2.027--pl5321h7b50bb2_5": "sha256:27f50ea48842aa4bc0e3153b4e8bb1e61f7feeeb5a788ea7e9145238fce7bfae", "2.027--pl5321h5c03b87_6": "sha256:2f57c319b0c2eb47f02e3949a34f05d2b23a624350e1fee30a5167ff1e2a190d"}, "docker": "quay.io/biocontainers/perl-socket"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-socket.
shpc-registry automated BioContainers addition for perl-socket
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-socket
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-socket:2.027--pl5321h5c03b87_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-socket/2.027--pl5321h5c03b87_6
$ module help quay.io/biocontainers/perl-socket/2.027--pl5321h5c03b87_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-socket-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-socket-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-socket-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-socket-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-socket-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-socket-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-socket

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