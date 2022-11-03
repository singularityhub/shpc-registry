---
layout: container
name:  "quay.io/biocontainers/stellar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stellar/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stellar/container.yaml"
updated_at: "2022-11-03 01:02:54.499306"
latest: "1.4.9--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/stellar"
aliases:
 - "stellar"
versions:
 - "1.4.9--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for stellar"
config: {"url": "https://biocontainers.pro/tools/stellar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stellar", "latest": {"1.4.9--hdfd78af_3": "sha256:6619520061d602a5ed69cdf4d97bee42f58d93c407eb352aabdd0f7fe9126cf3"}, "tags": {"1.4.9--hdfd78af_3": "sha256:6619520061d602a5ed69cdf4d97bee42f58d93c407eb352aabdd0f7fe9126cf3"}, "docker": "quay.io/biocontainers/stellar", "aliases": {"stellar": "/usr/local/bin/stellar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stellar.
shpc-registry automated BioContainers addition for stellar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stellar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stellar:1.4.9--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stellar/1.4.9--hdfd78af_3
$ module help quay.io/biocontainers/stellar/1.4.9--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stellar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stellar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stellar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stellar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stellar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stellar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stellar

```bash
$ singularity exec <container> /usr/local/bin/stellar
$ podman run --it --rm --entrypoint /usr/local/bin/stellar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stellar   -v ${PWD} -w ${PWD} <container> -c " $@"
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