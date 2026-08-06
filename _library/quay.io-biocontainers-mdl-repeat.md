---
layout: container
name:  "quay.io/biocontainers/mdl-repeat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mdl-repeat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mdl-repeat/container.yaml"
updated_at: "2026-08-06 06:10:52.478906"
latest: "1.0.1--hab16a5f_0"
container_url: "https://biocontainers.pro/tools/mdl-repeat"
aliases:
 - "mdl-repeat"
versions:
 - "1.0.1--hab16a5f_0"
description: "singularity registry hpc automated addition for mdl-repeat"
config: {"url": "https://biocontainers.pro/tools/mdl-repeat", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mdl-repeat", "latest": {"1.0.1--hab16a5f_0": "sha256:f5749bd2e22d89f018681524bcb57f134ad0d5086130a79b73aeeba271b14359"}, "tags": {"1.0.1--hab16a5f_0": "sha256:f5749bd2e22d89f018681524bcb57f134ad0d5086130a79b73aeeba271b14359"}, "docker": "quay.io/biocontainers/mdl-repeat", "aliases": {"mdl-repeat": "/usr/local/bin/mdl-repeat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mdl-repeat.
singularity registry hpc automated addition for mdl-repeat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mdl-repeat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mdl-repeat:1.0.1--hab16a5f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mdl-repeat/1.0.1--hab16a5f_0
$ module help quay.io/biocontainers/mdl-repeat/1.0.1--hab16a5f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mdl-repeat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mdl-repeat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mdl-repeat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mdl-repeat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mdl-repeat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mdl-repeat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mdl-repeat

```bash
$ singularity exec <container> /usr/local/bin/mdl-repeat
$ podman run --it --rm --entrypoint /usr/local/bin/mdl-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdl-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
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