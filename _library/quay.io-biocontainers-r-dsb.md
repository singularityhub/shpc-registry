---
layout: container
name:  "quay.io/biocontainers/r-dsb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-dsb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-dsb/container.yaml"
updated_at: "2025-10-19 04:00:54.051315"
latest: "2.0.0--r44h3121a25_0"
container_url: "https://biocontainers.pro/tools/r-dsb"
aliases:
 - "pcre2posix_test"
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.3--r43h3121a25_0"
 - "1.0.4--r43h3121a25_0"
 - "2.0.0--r44h3121a25_0"
description: "singularity registry hpc automated addition for r-dsb"
config: {"url": "https://biocontainers.pro/tools/r-dsb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-dsb", "latest": {"2.0.0--r44h3121a25_0": "sha256:6e7fd258f22f5308d8648a8aa1e072b2f26614aa2f47f2a48268f3f35abc05c3"}, "tags": {"1.0.3--r43h3121a25_0": "sha256:e7c6f521bd579f43ef39152cb88de5fbee1205cdd18b32ab81eaddbd73c70d6a", "1.0.4--r43h3121a25_0": "sha256:7eb72959b19e203026d7b24f991ce447ed31e02926f1464f9b1e5deb94996fd9", "2.0.0--r44h3121a25_0": "sha256:6e7fd258f22f5308d8648a8aa1e072b2f26614aa2f47f2a48268f3f35abc05c3"}, "docker": "quay.io/biocontainers/r-dsb", "aliases": {"pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-dsb.
singularity registry hpc automated addition for r-dsb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-dsb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-dsb:2.0.0--r44h3121a25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-dsb/2.0.0--r44h3121a25_0
$ module help quay.io/biocontainers/r-dsb/2.0.0--r44h3121a25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-dsb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-dsb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-dsb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-dsb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-dsb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-dsb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
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