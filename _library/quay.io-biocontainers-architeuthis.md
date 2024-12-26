---
layout: container
name:  "quay.io/biocontainers/architeuthis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/architeuthis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/architeuthis/container.yaml"
updated_at: "2024-12-26 03:28:41.969700"
latest: "0.3.1--he881be0_0"
container_url: "https://biocontainers.pro/tools/architeuthis"
aliases:
 - "architeuthis"
 - "taxonkit"
versions:
 - "0.2.1--he881be0_0"
 - "0.3.0--he881be0_1"
 - "0.3.1--he881be0_0"
description: "singularity registry hpc automated addition for architeuthis"
config: {"url": "https://biocontainers.pro/tools/architeuthis", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for architeuthis", "latest": {"0.3.1--he881be0_0": "sha256:31aff5200d149e713d2a809b788b6f31f62b70beea5b2177b9a8fa357a97d15c"}, "tags": {"0.2.1--he881be0_0": "sha256:72ef08355e8d61b8b08835872e66971b7502900a204b9f52e314b3694436b1d0", "0.3.0--he881be0_1": "sha256:fa39abe7e8ee48a52ec90f127ae8f34e6cc05624ab7b103d5b978e5c84345ff0", "0.3.1--he881be0_0": "sha256:31aff5200d149e713d2a809b788b6f31f62b70beea5b2177b9a8fa357a97d15c"}, "docker": "quay.io/biocontainers/architeuthis", "aliases": {"architeuthis": "/usr/local/bin/architeuthis", "taxonkit": "/usr/local/bin/taxonkit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/architeuthis.
singularity registry hpc automated addition for architeuthis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/architeuthis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/architeuthis:0.3.1--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/architeuthis/0.3.1--he881be0_0
$ module help quay.io/biocontainers/architeuthis/0.3.1--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### architeuthis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### architeuthis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### architeuthis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### architeuthis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### architeuthis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### architeuthis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### architeuthis

```bash
$ singularity exec <container> /usr/local/bin/architeuthis
$ podman run --it --rm --entrypoint /usr/local/bin/architeuthis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/architeuthis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
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