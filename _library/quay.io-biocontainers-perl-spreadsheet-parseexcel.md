---
layout: container
name:  "quay.io/biocontainers/perl-spreadsheet-parseexcel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-spreadsheet-parseexcel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-spreadsheet-parseexcel/container.yaml"
updated_at: "2026-01-17 03:33:08.501742"
latest: "0.66--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-spreadsheet-parseexcel"
aliases:
 - "map"
 - "mirrorMappings"
 - "mkCSGB2312"
 - "mkmapfile"
 - "chartex"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.65--pl5321hdfd78af_3"
 - "0.66--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-spreadsheet-parseexcel"
config: {"url": "https://biocontainers.pro/tools/perl-spreadsheet-parseexcel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-spreadsheet-parseexcel", "latest": {"0.66--pl5321hdfd78af_0": "sha256:05801329202578699a99ffb6cb1a5ed72fc0df77426440d606e463644d6ab74d"}, "tags": {"0.65--pl5321hdfd78af_3": "sha256:2670083853ae6844e096a48cac7e57599e82d4a5137adfd57380ab0f05d3ff77", "0.66--pl5321hdfd78af_0": "sha256:05801329202578699a99ffb6cb1a5ed72fc0df77426440d606e463644d6ab74d"}, "docker": "quay.io/biocontainers/perl-spreadsheet-parseexcel", "aliases": {"map": "/usr/local/bin/map", "mirrorMappings": "/usr/local/bin/mirrorMappings", "mkCSGB2312": "/usr/local/bin/mkCSGB2312", "mkmapfile": "/usr/local/bin/mkmapfile", "chartex": "/usr/local/bin/chartex", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-spreadsheet-parseexcel.
shpc-registry automated BioContainers addition for perl-spreadsheet-parseexcel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-spreadsheet-parseexcel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-spreadsheet-parseexcel:0.66--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-spreadsheet-parseexcel/0.66--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-spreadsheet-parseexcel/0.66--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-spreadsheet-parseexcel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-spreadsheet-parseexcel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-spreadsheet-parseexcel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-spreadsheet-parseexcel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-spreadsheet-parseexcel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-spreadsheet-parseexcel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### map

```bash
$ singularity exec <container> /usr/local/bin/map
$ podman run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirrorMappings

```bash
$ singularity exec <container> /usr/local/bin/mirrorMappings
$ podman run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkCSGB2312

```bash
$ singularity exec <container> /usr/local/bin/mkCSGB2312
$ podman run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkmapfile

```bash
$ singularity exec <container> /usr/local/bin/mkmapfile
$ podman run --it --rm --entrypoint /usr/local/bin/mkmapfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkmapfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chartex

```bash
$ singularity exec <container> /usr/local/bin/chartex
$ podman run --it --rm --entrypoint /usr/local/bin/chartex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chartex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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