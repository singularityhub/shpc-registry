---
layout: container
name:  "quay.io/biocontainers/pairsnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pairsnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pairsnp/container.yaml"
updated_at: "2026-01-27 04:27:14.258228"
latest: "0.3.1--hdcf5f25_2"
container_url: "https://biocontainers.pro/tools/pairsnp"
aliases:
 - "pairsnp"
versions:
 - "0.3.1--hd03093a_0"
 - "0.3.1--hdcf5f25_2"
description: "shpc-registry automated BioContainers addition for pairsnp"
config: {"url": "https://biocontainers.pro/tools/pairsnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pairsnp", "latest": {"0.3.1--hdcf5f25_2": "sha256:48d2bd55544c9c7bfa2b01a51999a74eabe40206686537ead86c01951171571c"}, "tags": {"0.3.1--hd03093a_0": "sha256:e40980cdccd3c1c2eb98f6a0f20cdbe76a5b2327cab8d7816587750809d3e306", "0.3.1--hdcf5f25_2": "sha256:48d2bd55544c9c7bfa2b01a51999a74eabe40206686537ead86c01951171571c"}, "docker": "quay.io/biocontainers/pairsnp", "aliases": {"pairsnp": "/usr/local/bin/pairsnp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pairsnp.
shpc-registry automated BioContainers addition for pairsnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pairsnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pairsnp:0.3.1--hdcf5f25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pairsnp/0.3.1--hdcf5f25_2
$ module help quay.io/biocontainers/pairsnp/0.3.1--hdcf5f25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pairsnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pairsnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pairsnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pairsnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pairsnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pairsnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pairsnp

```bash
$ singularity exec <container> /usr/local/bin/pairsnp
$ podman run --it --rm --entrypoint /usr/local/bin/pairsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
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