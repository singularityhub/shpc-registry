---
layout: container
name:  "quay.io/biocontainers/r-clustree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-clustree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-clustree/container.yaml"
updated_at: "2024-08-01 03:36:09.208420"
latest: "0.5.1"
container_url: "https://biocontainers.pro/tools/r-clustree"
aliases:
 - "pcre2posix_test"
 - "glpsol"
 - "hb-info"
 - "tjbench"
versions:
 - "0.5.1"
description: "singularity registry hpc automated addition for r-clustree"
config: {"url": "https://biocontainers.pro/tools/r-clustree", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-clustree", "latest": {"0.5.1": "sha256:878416fce524d6288208f2cc59fd10a878df012830f047ac53d39de06cf65e24"}, "tags": {"0.5.1": "sha256:878416fce524d6288208f2cc59fd10a878df012830f047ac53d39de06cf65e24"}, "docker": "quay.io/biocontainers/r-clustree", "aliases": {"pcre2posix_test": "/usr/local/bin/pcre2posix_test", "glpsol": "/usr/local/bin/glpsol", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-clustree.
singularity registry hpc automated addition for r-clustree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-clustree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-clustree:0.5.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-clustree/0.5.1
$ module help quay.io/biocontainers/r-clustree/0.5.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-clustree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-clustree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-clustree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-clustree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-clustree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-clustree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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