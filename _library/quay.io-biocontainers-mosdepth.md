---
layout: container
name:  "quay.io/biocontainers/mosdepth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mosdepth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mosdepth/container.yaml"
updated_at: "2023-11-29 03:12:15.807010"
latest: "0.3.5--hd299d5a_0"
container_url: "https://biocontainers.pro/tools/mosdepth"
aliases:
 - "mosdepth"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.3--h37c5b7d_2"
 - "0.3.3--hd299d5a_3"
 - "0.3.4--hd299d5a_0"
 - "0.3.5--hd299d5a_0"
description: "shpc-registry automated BioContainers addition for mosdepth"
config: {"url": "https://biocontainers.pro/tools/mosdepth", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mosdepth", "latest": {"0.3.5--hd299d5a_0": "sha256:3a6d1f534b7d2cf7032fafc6cb84b992e016be84718e9f69157234ec3dfb10bb"}, "tags": {"0.3.3--h37c5b7d_2": "sha256:d550465fce1cbfbe9cfe0facd4aa910b455f9ba93f4f4d701a08a7096e8f7d6e", "0.3.3--hd299d5a_3": "sha256:ef76d433d242983979b72ff2ee03624be59330ea8a5bd7c70004953d265fcced", "0.3.4--hd299d5a_0": "sha256:472e9be8cb302027b0f498bebb8e629cfe36035670ebe1c669dc7fa98f97fc3e", "0.3.5--hd299d5a_0": "sha256:3a6d1f534b7d2cf7032fafc6cb84b992e016be84718e9f69157234ec3dfb10bb"}, "docker": "quay.io/biocontainers/mosdepth", "aliases": {"mosdepth": "/usr/local/bin/mosdepth", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mosdepth.
shpc-registry automated BioContainers addition for mosdepth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mosdepth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mosdepth:0.3.5--hd299d5a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mosdepth/0.3.5--hd299d5a_0
$ module help quay.io/biocontainers/mosdepth/0.3.5--hd299d5a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mosdepth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mosdepth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mosdepth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mosdepth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mosdepth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mosdepth-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
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