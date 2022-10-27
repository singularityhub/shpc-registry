---
layout: container
name:  "quay.io/biocontainers/scanindel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scanindel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scanindel/container.yaml"
updated_at: "2022-10-27 01:15:05.517983"
latest: "1.3--1"
container_url: "https://biocontainers.pro/tools/scanindel"
aliases:
 - "ScanIndel.py"
 - "inchworm"
 - "vcf-combine.py"
versions:
 - "1.3--1"
description: "shpc-registry automated BioContainers addition for scanindel"
config: {"url": "https://biocontainers.pro/tools/scanindel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scanindel", "latest": {"1.3--1": "sha256:c60df4825e351dd87945e687319c5cc6708cc92afb47a2f33e8521c815dfcea0"}, "tags": {"1.3--1": "sha256:c60df4825e351dd87945e687319c5cc6708cc92afb47a2f33e8521c815dfcea0"}, "docker": "quay.io/biocontainers/scanindel", "aliases": {"ScanIndel.py": "/usr/local/bin/ScanIndel.py", "inchworm": "/usr/local/bin/inchworm", "vcf-combine.py": "/usr/local/bin/vcf-combine.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scanindel.
shpc-registry automated BioContainers addition for scanindel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scanindel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scanindel:1.3--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scanindel/1.3--1
$ module help quay.io/biocontainers/scanindel/1.3--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scanindel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scanindel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scanindel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scanindel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scanindel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scanindel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ScanIndel.py

```bash
$ singularity exec <container> /usr/local/bin/ScanIndel.py
$ podman run --it --rm --entrypoint /usr/local/bin/ScanIndel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ScanIndel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inchworm

```bash
$ singularity exec <container> /usr/local/bin/inchworm
$ podman run --it --rm --entrypoint /usr/local/bin/inchworm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inchworm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-combine.py

```bash
$ singularity exec <container> /usr/local/bin/vcf-combine.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-combine.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-combine.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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