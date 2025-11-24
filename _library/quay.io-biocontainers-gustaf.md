---
layout: container
name:  "quay.io/biocontainers/gustaf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gustaf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gustaf/container.yaml"
updated_at: "2025-11-24 03:34:56.786098"
latest: "1.0.10--h8ecad89_1"
container_url: "https://biocontainers.pro/tools/gustaf"
aliases:
 - "gustaf"
 - "gustaf_mate_joining"
versions:
 - "1.0.8--h9ee0642_2"
 - "1.0.10--h9948957_0"
 - "1.0.10--h8ecad89_1"
description: "shpc-registry automated BioContainers addition for gustaf"
config: {"url": "https://biocontainers.pro/tools/gustaf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gustaf", "latest": {"1.0.10--h8ecad89_1": "sha256:61126fba9c19c24981cf6c03de7c7ca8808e42edf2051e37bc499e75ce959459"}, "tags": {"1.0.8--h9ee0642_2": "sha256:6fb3a15cfce7d2dee26544322b825794bc21979c76d10295f4816059863e0bc0", "1.0.10--h9948957_0": "sha256:493b7db866bafe4ff5b5b42f5a07aa1246b11afc015d0b0af03bfe0f2298d792", "1.0.10--h8ecad89_1": "sha256:61126fba9c19c24981cf6c03de7c7ca8808e42edf2051e37bc499e75ce959459"}, "docker": "quay.io/biocontainers/gustaf", "aliases": {"gustaf": "/usr/local/bin/gustaf", "gustaf_mate_joining": "/usr/local/bin/gustaf_mate_joining"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gustaf.
shpc-registry automated BioContainers addition for gustaf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gustaf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gustaf:1.0.10--h8ecad89_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gustaf/1.0.10--h8ecad89_1
$ module help quay.io/biocontainers/gustaf/1.0.10--h8ecad89_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gustaf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gustaf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gustaf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gustaf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gustaf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gustaf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gustaf

```bash
$ singularity exec <container> /usr/local/bin/gustaf
$ podman run --it --rm --entrypoint /usr/local/bin/gustaf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gustaf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gustaf_mate_joining

```bash
$ singularity exec <container> /usr/local/bin/gustaf_mate_joining
$ podman run --it --rm --entrypoint /usr/local/bin/gustaf_mate_joining   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gustaf_mate_joining   -v ${PWD} -w ${PWD} <container> -c " $@"
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