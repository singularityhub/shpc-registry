---
layout: container
name:  "quay.io/biocontainers/sgcocaller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sgcocaller/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sgcocaller/container.yaml"
updated_at: "2024-02-15 03:47:48.730166"
latest: "0.3.9--hda81887_2"
container_url: "https://biocontainers.pro/tools/sgcocaller"
aliases:
 - "sgcocaller"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.9--h0ffbbc5_1"
 - "0.3.9--hda81887_2"
description: "shpc-registry automated BioContainers addition for sgcocaller"
config: {"url": "https://biocontainers.pro/tools/sgcocaller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sgcocaller", "latest": {"0.3.9--hda81887_2": "sha256:0438571fff31d7cd6a6500b2785506dd3dbdde8b2ad25364c87752df621a65d1"}, "tags": {"0.3.9--h0ffbbc5_1": "sha256:ae297be5d6dd8b8e981af6f9ebb350cdaa3caed7f2ffe70ec413752dfdd9cb4b", "0.3.9--hda81887_2": "sha256:0438571fff31d7cd6a6500b2785506dd3dbdde8b2ad25364c87752df621a65d1"}, "docker": "quay.io/biocontainers/sgcocaller", "aliases": {"sgcocaller": "/usr/local/bin/sgcocaller", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sgcocaller.
shpc-registry automated BioContainers addition for sgcocaller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sgcocaller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sgcocaller:0.3.9--hda81887_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sgcocaller/0.3.9--hda81887_2
$ module help quay.io/biocontainers/sgcocaller/0.3.9--hda81887_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sgcocaller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sgcocaller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sgcocaller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sgcocaller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sgcocaller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sgcocaller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sgcocaller

```bash
$ singularity exec <container> /usr/local/bin/sgcocaller
$ podman run --it --rm --entrypoint /usr/local/bin/sgcocaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sgcocaller   -v ${PWD} -w ${PWD} <container> -c " $@"
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