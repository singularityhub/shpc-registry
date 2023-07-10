---
layout: container
name:  "quay.io/biocontainers/coils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/coils/container.yaml"
updated_at: "2023-07-10 04:15:20.047706"
latest: "2.2.1--h031d066_4"
container_url: "https://biocontainers.pro/tools/coils"
aliases:
 - "coils-svr.pl"
 - "coils-wrap.pl"
 - "ncoils"
versions:
 - "2.2.1--hec16e2b_2"
 - "2.2.1--h031d066_4"
description: "shpc-registry automated BioContainers addition for coils"
config: {"url": "https://biocontainers.pro/tools/coils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for coils", "latest": {"2.2.1--h031d066_4": "sha256:41d210195b2ef4de535ad7d546458eba7c52ba1c8136bf9d4e0437ce37d6ae4c"}, "tags": {"2.2.1--hec16e2b_2": "sha256:bb6b9ae2ac65d8cdcb0eb51beadeceaa94d43b5441406df33fc4958ee7fc26ee", "2.2.1--h031d066_4": "sha256:41d210195b2ef4de535ad7d546458eba7c52ba1c8136bf9d4e0437ce37d6ae4c"}, "docker": "quay.io/biocontainers/coils", "aliases": {"coils-svr.pl": "/usr/local/bin/coils-svr.pl", "coils-wrap.pl": "/usr/local/bin/coils-wrap.pl", "ncoils": "/usr/local/bin/ncoils"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coils.
shpc-registry automated BioContainers addition for coils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coils:2.2.1--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coils/2.2.1--h031d066_4
$ module help quay.io/biocontainers/coils/2.2.1--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coils-svr.pl

```bash
$ singularity exec <container> /usr/local/bin/coils-svr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/coils-svr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coils-svr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coils-wrap.pl

```bash
$ singularity exec <container> /usr/local/bin/coils-wrap.pl
$ podman run --it --rm --entrypoint /usr/local/bin/coils-wrap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coils-wrap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncoils

```bash
$ singularity exec <container> /usr/local/bin/ncoils
$ podman run --it --rm --entrypoint /usr/local/bin/ncoils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncoils   -v ${PWD} -w ${PWD} <container> -c " $@"
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