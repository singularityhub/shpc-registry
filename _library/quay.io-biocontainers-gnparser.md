---
layout: container
name:  "quay.io/biocontainers/gnparser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gnparser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gnparser/container.yaml"
updated_at: "2025-12-08 05:34:44.667241"
latest: "1.11.9--he881be0_0"
container_url: "https://biocontainers.pro/tools/gnparser"
aliases:
 - "gnparser"
versions:
 - "1.7.3--he881be0_0"
 - "1.7.4--he881be0_0"
 - "1.9.0--he881be0_0"
 - "1.8.0--he881be0_0"
 - "1.7.5--he881be0_0"
 - "1.9.1--he881be0_0"
 - "1.9.2--he881be0_0"
 - "1.10.1--he881be0_0"
 - "1.10.3--he881be0_1"
 - "1.11.1--he881be0_0"
 - "1.10.4--he881be0_0"
 - "1.11.4--he881be0_0"
 - "1.11.6--he881be0_0"
 - "1.11.7--he881be0_0"
 - "1.11.8--he881be0_0"
 - "1.11.9--he881be0_0"
description: "singularity registry hpc automated addition for gnparser"
config: {"url": "https://biocontainers.pro/tools/gnparser", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gnparser", "latest": {"1.11.9--he881be0_0": "sha256:5e07c0147421f66d709fc2ef0eb911bd870c456e5bb8508e99eafbd589cf63e4"}, "tags": {"1.7.3--he881be0_0": "sha256:0a904113afb449aa067dd164c0fe2bb2294858d482880d21b07ca4bd40b2bfe9", "1.7.4--he881be0_0": "sha256:c353d0e337b6941ef2141a2db804a1597a9a811f24516c261e9d342d0c6901ce", "1.9.0--he881be0_0": "sha256:ea4ac2cfb9baa31d7d5fa5285ab182a4d482917b03a92a864c3ec7dfad04bf36", "1.8.0--he881be0_0": "sha256:a1b3c473c2ca713382646a9107e33080290eb462798b9dd4ab6e3552f39b086f", "1.7.5--he881be0_0": "sha256:2903bdc646a012513cd46bf23a4d516637521f3bd80d9570b09bbdbc04ac7af4", "1.9.1--he881be0_0": "sha256:334ed6869f84d661350ddb7b5479674390281559cabe5436884811378a5e12f9", "1.9.2--he881be0_0": "sha256:47ecc44bf099ec71a0be689be8f69f000755a13f04e3f507224935204ad015b3", "1.10.1--he881be0_0": "sha256:9d370d4b3b5cf29e07f2c30d52926304e8b88f23fcefa8654d5ad5adff569186", "1.10.3--he881be0_1": "sha256:ddf6d184fc2edd202c41b8a94ebb22821483a08deb94b7b4734b2a661a89773e", "1.11.1--he881be0_0": "sha256:3d48afbf417153949ead3b03b7850697db7f3724f4228953f298e5c0fa73e158", "1.10.4--he881be0_0": "sha256:5fa668dbfb17b7e3680ab6e356f1cd2f136ed790bb056f8eb8a4aaf32f8ab1b4", "1.11.4--he881be0_0": "sha256:81f452aa8526da67413ed825ba9c193f50bcc64e8f09572b761bc5df3b515789", "1.11.6--he881be0_0": "sha256:b533e9b835474a9c9bdf68b9b4006c72233fb73c1388526171cdd34f6b4d3d15", "1.11.7--he881be0_0": "sha256:1ff8103eb4a6a24d242f8d2641a05bd3dd91a872f55f788467c7124fd0cacc52", "1.11.8--he881be0_0": "sha256:b6ddb94f5cdef4786c1fb98cdcb9572d6b8e08d3aa22bc3e3b6b945c5b8034ea", "1.11.9--he881be0_0": "sha256:5e07c0147421f66d709fc2ef0eb911bd870c456e5bb8508e99eafbd589cf63e4"}, "docker": "quay.io/biocontainers/gnparser", "aliases": {"gnparser": "/usr/local/bin/gnparser"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gnparser.
singularity registry hpc automated addition for gnparser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gnparser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gnparser:1.11.9--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gnparser/1.11.9--he881be0_0
$ module help quay.io/biocontainers/gnparser/1.11.9--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gnparser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gnparser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gnparser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gnparser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gnparser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gnparser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gnparser

```bash
$ singularity exec <container> /usr/local/bin/gnparser
$ podman run --it --rm --entrypoint /usr/local/bin/gnparser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnparser   -v ${PWD} -w ${PWD} <container> -c " $@"
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