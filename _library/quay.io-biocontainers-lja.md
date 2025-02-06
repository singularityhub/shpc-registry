---
layout: container
name:  "quay.io/biocontainers/lja"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lja/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lja/container.yaml"
updated_at: "2025-02-06 03:10:12.354746"
latest: "0.2--h5b5514e_2"
container_url: "https://biocontainers.pro/tools/lja"
aliases:
 - "jumboDBG"
 - "lja"
 - "run_polishing"
 - "run_tests"
versions:
 - "0.2--h5b5514e_0"
 - "0.2--h5b5514e_2"
description: "singularity registry hpc automated addition for lja"
config: {"url": "https://biocontainers.pro/tools/lja", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lja", "latest": {"0.2--h5b5514e_2": "sha256:c20765a354521d877d329182bd74f2e7a5aad9c364af8bb2371121ca4effd3a4"}, "tags": {"0.2--h5b5514e_0": "sha256:a25602d48f2208b0814fa744e145126467b452de76b48cbffdcf8c4df0bcbdc3", "0.2--h5b5514e_2": "sha256:c20765a354521d877d329182bd74f2e7a5aad9c364af8bb2371121ca4effd3a4"}, "docker": "quay.io/biocontainers/lja", "aliases": {"jumboDBG": "/usr/local/bin/jumboDBG", "lja": "/usr/local/bin/lja", "run_polishing": "/usr/local/bin/run_polishing", "run_tests": "/usr/local/bin/run_tests"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lja.
singularity registry hpc automated addition for lja
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lja
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lja:0.2--h5b5514e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lja/0.2--h5b5514e_2
$ module help quay.io/biocontainers/lja/0.2--h5b5514e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lja-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lja-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lja-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lja-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lja-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lja-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jumboDBG

```bash
$ singularity exec <container> /usr/local/bin/jumboDBG
$ podman run --it --rm --entrypoint /usr/local/bin/jumboDBG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jumboDBG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lja

```bash
$ singularity exec <container> /usr/local/bin/lja
$ podman run --it --rm --entrypoint /usr/local/bin/lja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_polishing

```bash
$ singularity exec <container> /usr/local/bin/run_polishing
$ podman run --it --rm --entrypoint /usr/local/bin/run_polishing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_polishing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_tests

```bash
$ singularity exec <container> /usr/local/bin/run_tests
$ podman run --it --rm --entrypoint /usr/local/bin/run_tests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_tests   -v ${PWD} -w ${PWD} <container> -c " $@"
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