---
layout: container
name:  "quay.io/biocontainers/sscocaller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sscocaller/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sscocaller/container.yaml"
updated_at: "2023-04-29 03:03:01.698483"
latest: "0.2.2--hda81887_4"
container_url: "https://biocontainers.pro/tools/sscocaller"
aliases:
 - "sscocaller"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.2.2--h0ffbbc5_3"
 - "0.2.2--hda81887_4"
description: "shpc-registry automated BioContainers addition for sscocaller"
config: {"url": "https://biocontainers.pro/tools/sscocaller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sscocaller", "latest": {"0.2.2--hda81887_4": "sha256:c3a7033e01d6e4546f31e1b984ef4264f1e098b571299181cb56814a5cc21770"}, "tags": {"0.2.2--h0ffbbc5_3": "sha256:becafe137af9922b3cb2f3594322b7ab6ebe8e3df2d7aea4bd3f427d222678ef", "0.2.2--hda81887_4": "sha256:c3a7033e01d6e4546f31e1b984ef4264f1e098b571299181cb56814a5cc21770"}, "docker": "quay.io/biocontainers/sscocaller", "aliases": {"sscocaller": "/usr/local/bin/sscocaller", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sscocaller.
shpc-registry automated BioContainers addition for sscocaller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sscocaller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sscocaller:0.2.2--hda81887_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sscocaller/0.2.2--hda81887_4
$ module help quay.io/biocontainers/sscocaller/0.2.2--hda81887_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sscocaller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sscocaller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sscocaller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sscocaller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sscocaller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sscocaller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sscocaller

```bash
$ singularity exec <container> /usr/local/bin/sscocaller
$ podman run --it --rm --entrypoint /usr/local/bin/sscocaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sscocaller   -v ${PWD} -w ${PWD} <container> -c " $@"
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