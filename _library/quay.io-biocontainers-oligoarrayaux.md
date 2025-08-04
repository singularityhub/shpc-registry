---
layout: container
name:  "quay.io/biocontainers/oligoarrayaux"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oligoarrayaux/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oligoarrayaux/container.yaml"
updated_at: "2025-08-04 04:45:21.117852"
latest: "3.8.1--pl5321h9948957_0"
container_url: "https://biocontainers.pro/tools/oligoarrayaux"
aliases:
 - "ct-energy"
 - "ct2rnaml"
 - "h-num.pl"
 - "hybrid-min"
 - "hybrid-ss-min"
 - "melt.pl"
 - "ss-count.pl"
versions:
 - "3.8--hc9558a2_0"
 - "3.8.1--pl5321h9948957_0"
description: "shpc-registry automated BioContainers addition for oligoarrayaux"
config: {"url": "https://biocontainers.pro/tools/oligoarrayaux", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for oligoarrayaux", "latest": {"3.8.1--pl5321h9948957_0": "sha256:4122e42595e6ef0a8c5f69fae99eb9bdaddfaa770367418e2b609b25398b2d4c"}, "tags": {"3.8--hc9558a2_0": "sha256:a759a3cd0fa5b402031dfa55a23a17a1ec4bd8c739be1005de7a2df668ec889d", "3.8.1--pl5321h9948957_0": "sha256:4122e42595e6ef0a8c5f69fae99eb9bdaddfaa770367418e2b609b25398b2d4c"}, "docker": "quay.io/biocontainers/oligoarrayaux", "aliases": {"ct-energy": "/usr/local/bin/ct-energy", "ct2rnaml": "/usr/local/bin/ct2rnaml", "h-num.pl": "/usr/local/bin/h-num.pl", "hybrid-min": "/usr/local/bin/hybrid-min", "hybrid-ss-min": "/usr/local/bin/hybrid-ss-min", "melt.pl": "/usr/local/bin/melt.pl", "ss-count.pl": "/usr/local/bin/ss-count.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oligoarrayaux.
shpc-registry automated BioContainers addition for oligoarrayaux
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oligoarrayaux
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oligoarrayaux:3.8.1--pl5321h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oligoarrayaux/3.8.1--pl5321h9948957_0
$ module help quay.io/biocontainers/oligoarrayaux/3.8.1--pl5321h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oligoarrayaux-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oligoarrayaux-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oligoarrayaux-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oligoarrayaux-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oligoarrayaux-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oligoarrayaux-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ct-energy

```bash
$ singularity exec <container> /usr/local/bin/ct-energy
$ podman run --it --rm --entrypoint /usr/local/bin/ct-energy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct-energy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2rnaml

```bash
$ singularity exec <container> /usr/local/bin/ct2rnaml
$ podman run --it --rm --entrypoint /usr/local/bin/ct2rnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2rnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h-num.pl

```bash
$ singularity exec <container> /usr/local/bin/h-num.pl
$ podman run --it --rm --entrypoint /usr/local/bin/h-num.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h-num.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hybrid-min

```bash
$ singularity exec <container> /usr/local/bin/hybrid-min
$ podman run --it --rm --entrypoint /usr/local/bin/hybrid-min   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hybrid-min   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hybrid-ss-min

```bash
$ singularity exec <container> /usr/local/bin/hybrid-ss-min
$ podman run --it --rm --entrypoint /usr/local/bin/hybrid-ss-min   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hybrid-ss-min   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### melt.pl

```bash
$ singularity exec <container> /usr/local/bin/melt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/melt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/melt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ss-count.pl

```bash
$ singularity exec <container> /usr/local/bin/ss-count.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ss-count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ss-count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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