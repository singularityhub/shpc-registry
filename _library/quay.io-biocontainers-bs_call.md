---
layout: container
name:  "quay.io/biocontainers/bs_call"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bs_call/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bs_call/container.yaml"
updated_at: "2023-12-28 02:28:26.626559"
latest: "2.02--h2156619_8"
container_url: "https://biocontainers.pro/tools/bs_call"
aliases:
 - "bs_call"
 - "dbSNP_idx"
versions:
 - "2.02--h7c6eca5_6"
 - "2.02--h2156619_8"
description: "shpc-registry automated BioContainers addition for bs_call"
config: {"url": "https://biocontainers.pro/tools/bs_call", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bs_call", "latest": {"2.02--h2156619_8": "sha256:a62b6bbb8234f9c12fb9ad71d5ebf117583677594d32e762238e6223569b99a7"}, "tags": {"2.02--h7c6eca5_6": "sha256:f79a73c5da0181343c500784f89b0c3120a1aaba97decdf4bc18bdf0b87e7fc2", "2.02--h2156619_8": "sha256:a62b6bbb8234f9c12fb9ad71d5ebf117583677594d32e762238e6223569b99a7"}, "docker": "quay.io/biocontainers/bs_call", "aliases": {"bs_call": "/usr/local/bin/bs_call", "dbSNP_idx": "/usr/local/bin/dbSNP_idx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bs_call.
shpc-registry automated BioContainers addition for bs_call
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bs_call
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bs_call:2.02--h2156619_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bs_call/2.02--h2156619_8
$ module help quay.io/biocontainers/bs_call/2.02--h2156619_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bs_call-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bs_call-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bs_call-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bs_call-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bs_call-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bs_call-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bs_call

```bash
$ singularity exec <container> /usr/local/bin/bs_call
$ podman run --it --rm --entrypoint /usr/local/bin/bs_call   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bs_call   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbSNP_idx

```bash
$ singularity exec <container> /usr/local/bin/dbSNP_idx
$ podman run --it --rm --entrypoint /usr/local/bin/dbSNP_idx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbSNP_idx   -v ${PWD} -w ${PWD} <container> -c " $@"
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