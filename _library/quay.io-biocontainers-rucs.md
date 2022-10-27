---
layout: container
name:  "quay.io/biocontainers/rucs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rucs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rucs/container.yaml"
updated_at: "2022-10-27 00:55:23.182217"
latest: "1.0.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/rucs"
aliases:
 - ".rucs-post-link.sh"
 - "install_db.sh"
 - "rucs"
versions:
 - "1.0.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for rucs"
config: {"url": "https://biocontainers.pro/tools/rucs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rucs", "latest": {"1.0.2--hdfd78af_1": "sha256:e31f96e22775f4f161a0a2879cc5c313a8f6fc4044211bb122347f881a920426"}, "tags": {"1.0.2--hdfd78af_1": "sha256:e31f96e22775f4f161a0a2879cc5c313a8f6fc4044211bb122347f881a920426"}, "docker": "quay.io/biocontainers/rucs", "aliases": {".rucs-post-link.sh": "/usr/local/bin/.rucs-post-link.sh", "install_db.sh": "/usr/local/bin/install_db.sh", "rucs": "/usr/local/bin/rucs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rucs.
shpc-registry automated BioContainers addition for rucs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rucs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rucs:1.0.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rucs/1.0.2--hdfd78af_1
$ module help quay.io/biocontainers/rucs/1.0.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rucs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rucs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rucs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rucs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rucs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rucs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .rucs-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.rucs-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.rucs-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.rucs-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_db.sh

```bash
$ singularity exec <container> /usr/local/bin/install_db.sh
$ podman run --it --rm --entrypoint /usr/local/bin/install_db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rucs

```bash
$ singularity exec <container> /usr/local/bin/rucs
$ podman run --it --rm --entrypoint /usr/local/bin/rucs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rucs   -v ${PWD} -w ${PWD} <container> -c " $@"
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