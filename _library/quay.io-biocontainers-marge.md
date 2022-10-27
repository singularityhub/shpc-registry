---
layout: container
name:  "quay.io/biocontainers/marge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/marge/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/marge/container.yaml"
updated_at: "2022-10-27 01:09:59.438341"
latest: "1.0--py_2"
container_url: "https://biocontainers.pro/tools/marge"
aliases:
 - "bedClip"
 - "bigWigAverageOverBed"
 - "bigWigSummary"
 - "marge"
versions:
 - "1.0--py_2"
description: "shpc-registry automated BioContainers addition for marge"
config: {"url": "https://biocontainers.pro/tools/marge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for marge", "latest": {"1.0--py_2": "sha256:7940ebe4ff8820e19cb1e18b4c36f098eadbd38dc8ad7d157d04d1d0533da105"}, "tags": {"1.0--py_2": "sha256:7940ebe4ff8820e19cb1e18b4c36f098eadbd38dc8ad7d157d04d1d0533da105"}, "docker": "quay.io/biocontainers/marge", "aliases": {"bedClip": "/usr/local/bin/bedClip", "bigWigAverageOverBed": "/usr/local/bin/bigWigAverageOverBed", "bigWigSummary": "/usr/local/bin/bigWigSummary", "marge": "/usr/local/bin/marge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/marge.
shpc-registry automated BioContainers addition for marge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/marge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/marge:1.0--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/marge/1.0--py_2
$ module help quay.io/biocontainers/marge/1.0--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### marge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### marge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### marge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### marge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### marge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### marge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedClip

```bash
$ singularity exec <container> /usr/local/bin/bedClip
$ podman run --it --rm --entrypoint /usr/local/bin/bedClip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedClip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigAverageOverBed

```bash
$ singularity exec <container> /usr/local/bin/bigWigAverageOverBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigSummary

```bash
$ singularity exec <container> /usr/local/bin/bigWigSummary
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### marge

```bash
$ singularity exec <container> /usr/local/bin/marge
$ podman run --it --rm --entrypoint /usr/local/bin/marge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/marge   -v ${PWD} -w ${PWD} <container> -c " $@"
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