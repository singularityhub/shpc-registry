---
layout: container
name:  "quay.io/biocontainers/short-read-connector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/short-read-connector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/short-read-connector/container.yaml"
updated_at: "2023-09-17 00:23:45.752750"
latest: "1.2.0--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/short-read-connector"
aliases:
 - "SRC_counter"
 - "SRC_linker"
 - "dsk"
 - "dsk2ascii"
 - "extract_reads_from_bv"
 - "generate_bv"
 - "short_read_connector_counter.sh"
 - "short_read_connector_linker.sh"
 - "h5cc"
versions:
 - "1.2.0--h43eeafb_0"
description: "singularity registry hpc automated addition for short-read-connector"
config: {"url": "https://biocontainers.pro/tools/short-read-connector", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for short-read-connector", "latest": {"1.2.0--h43eeafb_0": "sha256:1e61c79989219c12ba9b2423086edef7ca6a9d9ba06c38080d30f9b9558465fb"}, "tags": {"1.2.0--h43eeafb_0": "sha256:1e61c79989219c12ba9b2423086edef7ca6a9d9ba06c38080d30f9b9558465fb"}, "docker": "quay.io/biocontainers/short-read-connector", "aliases": {"SRC_counter": "/usr/local/bin/SRC_counter", "SRC_linker": "/usr/local/bin/SRC_linker", "dsk": "/usr/local/bin/dsk", "dsk2ascii": "/usr/local/bin/dsk2ascii", "extract_reads_from_bv": "/usr/local/bin/extract_reads_from_bv", "generate_bv": "/usr/local/bin/generate_bv", "short_read_connector_counter.sh": "/usr/local/bin/short_read_connector_counter.sh", "short_read_connector_linker.sh": "/usr/local/bin/short_read_connector_linker.sh", "h5cc": "/usr/local/bin/h5cc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/short-read-connector.
singularity registry hpc automated addition for short-read-connector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/short-read-connector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/short-read-connector:1.2.0--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/short-read-connector/1.2.0--h43eeafb_0
$ module help quay.io/biocontainers/short-read-connector/1.2.0--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### short-read-connector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### short-read-connector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### short-read-connector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### short-read-connector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### short-read-connector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### short-read-connector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SRC_counter

```bash
$ singularity exec <container> /usr/local/bin/SRC_counter
$ podman run --it --rm --entrypoint /usr/local/bin/SRC_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SRC_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SRC_linker

```bash
$ singularity exec <container> /usr/local/bin/SRC_linker
$ podman run --it --rm --entrypoint /usr/local/bin/SRC_linker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SRC_linker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsk

```bash
$ singularity exec <container> /usr/local/bin/dsk
$ podman run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsk2ascii

```bash
$ singularity exec <container> /usr/local/bin/dsk2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/dsk2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsk2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_reads_from_bv

```bash
$ singularity exec <container> /usr/local/bin/extract_reads_from_bv
$ podman run --it --rm --entrypoint /usr/local/bin/extract_reads_from_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_reads_from_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_bv

```bash
$ singularity exec <container> /usr/local/bin/generate_bv
$ podman run --it --rm --entrypoint /usr/local/bin/generate_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### short_read_connector_counter.sh

```bash
$ singularity exec <container> /usr/local/bin/short_read_connector_counter.sh
$ podman run --it --rm --entrypoint /usr/local/bin/short_read_connector_counter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/short_read_connector_counter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### short_read_connector_linker.sh

```bash
$ singularity exec <container> /usr/local/bin/short_read_connector_linker.sh
$ podman run --it --rm --entrypoint /usr/local/bin/short_read_connector_linker.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/short_read_connector_linker.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
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