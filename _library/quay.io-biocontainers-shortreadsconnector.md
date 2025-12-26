---
layout: container
name:  "quay.io/biocontainers/shortreadsconnector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shortreadsconnector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shortreadsconnector/container.yaml"
updated_at: "2025-12-26 03:57:06.918966"
latest: "1.1.3--0"
container_url: "https://biocontainers.pro/tools/shortreadsconnector"
aliases:
 - "SRC_counter"
 - "SRC_linker_ram"
 - "dsk"
 - "dsk2ascii"
 - "extract_reads_from_bv"
 - "generate_bv"
 - "short_read_connector.sh"
 - "h5dump"
versions:
 - "1.1.3--0"
description: "shpc-registry automated BioContainers addition for shortreadsconnector"
config: {"url": "https://biocontainers.pro/tools/shortreadsconnector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shortreadsconnector", "latest": {"1.1.3--0": "sha256:801fe0edb1118e2d5b6ce3b5e7fe62af66a816d73b8b66845d630b8e7c230e52"}, "tags": {"1.1.3--0": "sha256:801fe0edb1118e2d5b6ce3b5e7fe62af66a816d73b8b66845d630b8e7c230e52"}, "docker": "quay.io/biocontainers/shortreadsconnector", "aliases": {"SRC_counter": "/usr/local/bin/SRC_counter", "SRC_linker_ram": "/usr/local/bin/SRC_linker_ram", "dsk": "/usr/local/bin/dsk", "dsk2ascii": "/usr/local/bin/dsk2ascii", "extract_reads_from_bv": "/usr/local/bin/extract_reads_from_bv", "generate_bv": "/usr/local/bin/generate_bv", "short_read_connector.sh": "/usr/local/bin/short_read_connector.sh", "h5dump": "/usr/local/bin/h5dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shortreadsconnector.
shpc-registry automated BioContainers addition for shortreadsconnector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shortreadsconnector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shortreadsconnector:1.1.3--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shortreadsconnector/1.1.3--0
$ module help quay.io/biocontainers/shortreadsconnector/1.1.3--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shortreadsconnector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shortreadsconnector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shortreadsconnector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shortreadsconnector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shortreadsconnector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shortreadsconnector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SRC_counter

```bash
$ singularity exec <container> /usr/local/bin/SRC_counter
$ podman run --it --rm --entrypoint /usr/local/bin/SRC_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SRC_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SRC_linker_ram

```bash
$ singularity exec <container> /usr/local/bin/SRC_linker_ram
$ podman run --it --rm --entrypoint /usr/local/bin/SRC_linker_ram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SRC_linker_ram   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### short_read_connector.sh

```bash
$ singularity exec <container> /usr/local/bin/short_read_connector.sh
$ podman run --it --rm --entrypoint /usr/local/bin/short_read_connector.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/short_read_connector.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5dump

```bash
$ singularity exec <container> /usr/local/bin/h5dump
$ podman run --it --rm --entrypoint /usr/local/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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