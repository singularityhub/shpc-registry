---
layout: container
name:  "quay.io/biocontainers/perl-sub-exporter-formethods"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-sub-exporter-formethods/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-sub-exporter-formethods/container.yaml"
updated_at: "2023-07-27 05:50:30.111613"
latest: "0.100055--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-sub-exporter-formethods"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.100054--pl5321hdfd78af_0"
 - "0.100055--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-sub-exporter-formethods"
config: {"url": "https://biocontainers.pro/tools/perl-sub-exporter-formethods", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-sub-exporter-formethods", "latest": {"0.100055--pl5321hdfd78af_0": "sha256:408c198f1db074d1811c4f4ac4c6637e5f18ea93229ad67e4bc40feb28fa2d08"}, "tags": {"0.100054--pl5321hdfd78af_0": "sha256:3d33b258588556f7b409fe9154d594503a4a8094e240f616cd2dc9266177054c", "0.100055--pl5321hdfd78af_0": "sha256:408c198f1db074d1811c4f4ac4c6637e5f18ea93229ad67e4bc40feb28fa2d08"}, "docker": "quay.io/biocontainers/perl-sub-exporter-formethods", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-sub-exporter-formethods.
shpc-registry automated BioContainers addition for perl-sub-exporter-formethods
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-sub-exporter-formethods
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-sub-exporter-formethods:0.100055--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-sub-exporter-formethods/0.100055--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-sub-exporter-formethods/0.100055--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-sub-exporter-formethods-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-sub-exporter-formethods-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-sub-exporter-formethods-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-sub-exporter-formethods-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-sub-exporter-formethods-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-sub-exporter-formethods-inspect-deffile:

```bash
$ singularity inspect -d <container>
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