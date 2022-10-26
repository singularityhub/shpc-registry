---
layout: container
name:  "quay.io/biocontainers/abawaca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abawaca/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/abawaca/container.yaml"
updated_at: "2022-10-26 02:47:01.729301"
latest: "1.00--h7d875b9_3"
container_url: "https://biocontainers.pro/tools/abawaca"
aliases:
 - "nuke"
 - "resume"
 - "abawaca"
 - "env-execute"
versions:
 - "1.00--h7d875b9_3"
description: "abawaca (A Binning Algorithm Without A Cool Acronym) is a binning program that can take advantage of different types of information such as differential coverage and DNA signature"
config: {"url": "https://biocontainers.pro/tools/abawaca", "maintainer": "@vsoch", "description": "abawaca (A Binning Algorithm Without A Cool Acronym) is a binning program that can take advantage of different types of information such as differential coverage and DNA signature", "latest": {"1.00--h7d875b9_3": "sha256:e8abcc7c4b3bc204485ef4ba234062a4e4a64f17774bb7303e4102492af44d78"}, "tags": {"1.00--h7d875b9_3": "sha256:e8abcc7c4b3bc204485ef4ba234062a4e4a64f17774bb7303e4102492af44d78"}, "docker": "quay.io/biocontainers/abawaca", "aliases": {"nuke": "/bin/nuke", "resume": "/bin/resume", "abawaca": "/usr/local/bin/abawaca", "env-execute": "/usr/local/env-execute"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abawaca.
abawaca (A Binning Algorithm Without A Cool Acronym) is a binning program that can take advantage of different types of information such as differential coverage and DNA signature
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abawaca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abawaca:1.00--h7d875b9_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abawaca/1.00--h7d875b9_3
$ module help quay.io/biocontainers/abawaca/1.00--h7d875b9_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abawaca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abawaca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abawaca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abawaca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abawaca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abawaca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nuke

```bash
$ singularity exec <container> /bin/nuke
$ podman run --it --rm --entrypoint /bin/nuke   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/nuke   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resume

```bash
$ singularity exec <container> /bin/resume
$ podman run --it --rm --entrypoint /bin/resume   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/resume   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abawaca

```bash
$ singularity exec <container> /usr/local/bin/abawaca
$ podman run --it --rm --entrypoint /usr/local/bin/abawaca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abawaca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env-execute

```bash
$ singularity exec <container> /usr/local/env-execute
$ podman run --it --rm --entrypoint /usr/local/env-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/env-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
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