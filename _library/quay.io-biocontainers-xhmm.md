---
layout: container
name:  "quay.io/biocontainers/xhmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xhmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xhmm/container.yaml"
updated_at: "2025-09-24 03:29:59.206855"
latest: "0.0.0.2016_01_04.cc14e52--hc5fcd1e_5"
container_url: "https://biocontainers.pro/tools/xhmm"
aliases:
 - "xhmm"
versions:
 - "0.0.0.2016_01_04.cc14e52--hc5fcd1e_4"
 - "0.0.0.2016_01_04.cc14e52--hc5fcd1e_5"
description: "shpc-registry automated BioContainers addition for xhmm"
config: {"url": "https://biocontainers.pro/tools/xhmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xhmm", "latest": {"0.0.0.2016_01_04.cc14e52--hc5fcd1e_5": "sha256:472b12f42783d2feb63a446bfc17970df04ed5e2ce0f10eee4eece8dec249057"}, "tags": {"0.0.0.2016_01_04.cc14e52--hc5fcd1e_4": "sha256:78fd1ae344727697639f4c200e108a2649a4560b7e82ecbfad26c1e9f35592fc", "0.0.0.2016_01_04.cc14e52--hc5fcd1e_5": "sha256:472b12f42783d2feb63a446bfc17970df04ed5e2ce0f10eee4eece8dec249057"}, "docker": "quay.io/biocontainers/xhmm", "aliases": {"xhmm": "/usr/local/bin/xhmm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xhmm.
shpc-registry automated BioContainers addition for xhmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xhmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xhmm:0.0.0.2016_01_04.cc14e52--hc5fcd1e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xhmm/0.0.0.2016_01_04.cc14e52--hc5fcd1e_5
$ module help quay.io/biocontainers/xhmm/0.0.0.2016_01_04.cc14e52--hc5fcd1e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xhmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xhmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xhmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xhmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xhmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xhmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xhmm

```bash
$ singularity exec <container> /usr/local/bin/xhmm
$ podman run --it --rm --entrypoint /usr/local/bin/xhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xhmm   -v ${PWD} -w ${PWD} <container> -c " $@"
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