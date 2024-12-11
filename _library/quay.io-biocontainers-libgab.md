---
layout: container
name:  "quay.io/biocontainers/libgab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libgab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libgab/container.yaml"
updated_at: "2024-12-11 03:22:29.637775"
latest: "1.0.5--h7a259b3_14"
container_url: "https://biocontainers.pro/tools/libgab"
aliases:
 - "bamtools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.5--h5cad929_9"
 - "1.0.5--he40e34d_11"
 - "1.0.5--ha267990_12"
 - "1.0.5--hdc46a4b_13"
 - "1.0.5--h7a259b3_14"
description: "shpc-registry automated BioContainers addition for libgab"
config: {"url": "https://biocontainers.pro/tools/libgab", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libgab", "latest": {"1.0.5--h7a259b3_14": "sha256:d5b0f9e0eac5c976f29da824f720c630fb9b8db9c3905461c8707d6b7c57dc98"}, "tags": {"1.0.5--h5cad929_9": "sha256:aef9e161c577bb10478863a0b0c2b57c622f6befaef97858c22ea46a83f23e23", "1.0.5--he40e34d_11": "sha256:f802c48b5859f31c28bad317d3ce9cb9704210ebdc83c88468c0e9b814cc9ba6", "1.0.5--ha267990_12": "sha256:e4db88a391263f07a84847ef8eccd2cafbd73da57a1474ea4a76694a19b6ae97", "1.0.5--hdc46a4b_13": "sha256:2125e318ce594cf582923d96e4ce47a23cde0b13c391166ea31cb42dee829435", "1.0.5--h7a259b3_14": "sha256:d5b0f9e0eac5c976f29da824f720c630fb9b8db9c3905461c8707d6b7c57dc98"}, "docker": "quay.io/biocontainers/libgab", "aliases": {"bamtools": "/usr/local/bin/bamtools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/libgab.
shpc-registry automated BioContainers addition for libgab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libgab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libgab:1.0.5--h7a259b3_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libgab/1.0.5--h7a259b3_14
$ module help quay.io/biocontainers/libgab/1.0.5--h7a259b3_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libgab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libgab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libgab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libgab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libgab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libgab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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