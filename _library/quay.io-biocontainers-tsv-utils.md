---
layout: container
name:  "quay.io/biocontainers/tsv-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tsv-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tsv-utils/container.yaml"
updated_at: "2023-12-27 02:27:32.001700"
latest: "2.2.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/tsv-utils"
aliases:
 - "csv2tsv"
 - "keep-header"
 - "number-lines"
 - "tsv-append"
 - "tsv-filter"
 - "tsv-join"
 - "tsv-pretty"
 - "tsv-sample"
 - "tsv-select"
 - "tsv-split"
 - "tsv-summarize"
 - "tsv-uniq"
versions:
 - "2.2.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for tsv-utils"
config: {"url": "https://biocontainers.pro/tools/tsv-utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tsv-utils", "latest": {"2.2.0--h9ee0642_0": "sha256:aecdc81d23a00151711286d9cd8cd2c96b0537a44b2184fd21c591a98699dc8e"}, "tags": {"2.2.0--h9ee0642_0": "sha256:aecdc81d23a00151711286d9cd8cd2c96b0537a44b2184fd21c591a98699dc8e"}, "docker": "quay.io/biocontainers/tsv-utils", "aliases": {"csv2tsv": "/usr/local/bin/csv2tsv", "keep-header": "/usr/local/bin/keep-header", "number-lines": "/usr/local/bin/number-lines", "tsv-append": "/usr/local/bin/tsv-append", "tsv-filter": "/usr/local/bin/tsv-filter", "tsv-join": "/usr/local/bin/tsv-join", "tsv-pretty": "/usr/local/bin/tsv-pretty", "tsv-sample": "/usr/local/bin/tsv-sample", "tsv-select": "/usr/local/bin/tsv-select", "tsv-split": "/usr/local/bin/tsv-split", "tsv-summarize": "/usr/local/bin/tsv-summarize", "tsv-uniq": "/usr/local/bin/tsv-uniq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tsv-utils.
shpc-registry automated BioContainers addition for tsv-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tsv-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tsv-utils:2.2.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tsv-utils/2.2.0--h9ee0642_0
$ module help quay.io/biocontainers/tsv-utils/2.2.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tsv-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tsv-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tsv-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tsv-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tsv-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tsv-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csv2tsv

```bash
$ singularity exec <container> /usr/local/bin/csv2tsv
$ podman run --it --rm --entrypoint /usr/local/bin/csv2tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keep-header

```bash
$ singularity exec <container> /usr/local/bin/keep-header
$ podman run --it --rm --entrypoint /usr/local/bin/keep-header   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keep-header   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### number-lines

```bash
$ singularity exec <container> /usr/local/bin/number-lines
$ podman run --it --rm --entrypoint /usr/local/bin/number-lines   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/number-lines   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-append

```bash
$ singularity exec <container> /usr/local/bin/tsv-append
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-append   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-append   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-filter

```bash
$ singularity exec <container> /usr/local/bin/tsv-filter
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-join

```bash
$ singularity exec <container> /usr/local/bin/tsv-join
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-pretty

```bash
$ singularity exec <container> /usr/local/bin/tsv-pretty
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-pretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-pretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-sample

```bash
$ singularity exec <container> /usr/local/bin/tsv-sample
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-select

```bash
$ singularity exec <container> /usr/local/bin/tsv-select
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-select   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-select   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-split

```bash
$ singularity exec <container> /usr/local/bin/tsv-split
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-summarize

```bash
$ singularity exec <container> /usr/local/bin/tsv-summarize
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv-uniq

```bash
$ singularity exec <container> /usr/local/bin/tsv-uniq
$ podman run --it --rm --entrypoint /usr/local/bin/tsv-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
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