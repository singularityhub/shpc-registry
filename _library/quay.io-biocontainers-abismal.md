---
layout: container
name:  "quay.io/biocontainers/abismal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abismal/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/abismal/container.yaml"
updated_at: "2022-10-17 09:57:33.527075"
latest: "1.0.0--h9a82719_0"
container_url: "https://biocontainers.pro/tools/abismal"
aliases:
 - "abismal"
 - "abismalidx"
 - "simreads"
 - "env-execute"
versions:
 - "1.0.0--h9a82719_0"
description: "Abismal tool"
config: {"url": "https://biocontainers.pro/tools/abismal", "maintainer": "@vsoch", "description": "Abismal tool", "latest": {"1.0.0--h9a82719_0": "sha256:45ff3ad0e61a923871ea933a326d24c0e57c41655e79477be67a07d74bd4cd3a"}, "tags": {"1.0.0--h9a82719_0": "sha256:45ff3ad0e61a923871ea933a326d24c0e57c41655e79477be67a07d74bd4cd3a"}, "docker": "quay.io/biocontainers/abismal", "aliases": {"abismal": "/usr/local/bin/abismal", "abismalidx": "/usr/local/bin/abismalidx", "simreads": "/usr/local/bin/simreads", "env-execute": "/usr/local/env-execute"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abismal.
Abismal tool
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abismal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abismal:1.0.0--h9a82719_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abismal/1.0.0--h9a82719_0
$ module help quay.io/biocontainers/abismal/1.0.0--h9a82719_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abismal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abismal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abismal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abismal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abismal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abismal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abismal
       
```bash
$ singularity exec <container> /usr/local/bin/abismal
$ podman run --it --rm --entrypoint /usr/local/bin/abismal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abismal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abismalidx
       
```bash
$ singularity exec <container> /usr/local/bin/abismalidx
$ podman run --it --rm --entrypoint /usr/local/bin/abismalidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abismalidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simreads
       
```bash
$ singularity exec <container> /usr/local/bin/simreads
$ podman run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
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