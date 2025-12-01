---
layout: container
name:  "quay.io/biocontainers/cobs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cobs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cobs/container.yaml"
updated_at: "2025-12-01 04:22:33.029903"
latest: "0.3.1--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/cobs"
aliases:
 - "cobs"
 - "xxhsum"
versions:
 - "0.2.0--hd03093a_0"
 - "0.2.1--hd03093a_0"
 - "0.2.1--hdcf5f25_2"
 - "0.3.0--hdcf5f25_1"
 - "0.3.1--hdcf5f25_1"
description: "shpc-registry automated BioContainers addition for cobs"
config: {"url": "https://biocontainers.pro/tools/cobs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cobs", "latest": {"0.3.1--hdcf5f25_1": "sha256:cca2cb7563d7744d965eff228b05f8f88eb5c00cd9ae940e945b8450ded7e906"}, "tags": {"0.2.0--hd03093a_0": "sha256:11fccbca332c0117d09b8b7384d3ea0148d518a8c010b57f95acf0ef9cdffbae", "0.2.1--hd03093a_0": "sha256:ee7815f8322b7f9d5324f91ec905fe0345557810cafae1505ba7f3f9ecc9045d", "0.2.1--hdcf5f25_2": "sha256:6303c417192c413cd1abf7b9dbd8e178dd522ed5a496806d7ce5cd6a265420d3", "0.3.0--hdcf5f25_1": "sha256:be159862779eae8e68a03f7eccd7c13a4d7f30ad8a3b6c248503b2e22cba19d5", "0.3.1--hdcf5f25_1": "sha256:cca2cb7563d7744d965eff228b05f8f88eb5c00cd9ae940e945b8450ded7e906"}, "docker": "quay.io/biocontainers/cobs", "aliases": {"cobs": "/usr/local/bin/cobs", "xxhsum": "/usr/local/bin/xxhsum"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cobs.
shpc-registry automated BioContainers addition for cobs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cobs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cobs:0.3.1--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cobs/0.3.1--hdcf5f25_1
$ module help quay.io/biocontainers/cobs/0.3.1--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cobs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cobs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cobs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cobs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cobs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cobs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cobs

```bash
$ singularity exec <container> /usr/local/bin/cobs
$ podman run --it --rm --entrypoint /usr/local/bin/cobs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cobs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
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