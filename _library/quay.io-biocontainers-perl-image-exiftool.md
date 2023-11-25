---
layout: container
name:  "quay.io/biocontainers/perl-image-exiftool"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-image-exiftool/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-image-exiftool/container.yaml"
updated_at: "2023-11-25 02:44:44.002757"
latest: "12.60--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-image-exiftool"
aliases:
 - "exiftool"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "12.42--pl5321hdfd78af_0"
 - "12.50--pl5321hdfd78af_0"
 - "12.60--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-image-exiftool"
config: {"url": "https://biocontainers.pro/tools/perl-image-exiftool", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-image-exiftool", "latest": {"12.60--pl5321hdfd78af_0": "sha256:9819e264063a4653bf98e306ede7dbc997f294354a8db2b9874e1b891f176e66"}, "tags": {"12.42--pl5321hdfd78af_0": "sha256:22d34da34949fc4ae338ae70d782c0331280173e1f4c20b0e49404e7d3ded2ab", "12.50--pl5321hdfd78af_0": "sha256:83e271dfe7b6fa3881c3ed324b2fba3ff48aaea658709b7fb80c05ea647ea676", "12.60--pl5321hdfd78af_0": "sha256:9819e264063a4653bf98e306ede7dbc997f294354a8db2b9874e1b891f176e66"}, "docker": "quay.io/biocontainers/perl-image-exiftool", "aliases": {"exiftool": "/usr/local/bin/exiftool", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-image-exiftool.
shpc-registry automated BioContainers addition for perl-image-exiftool
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-image-exiftool
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-image-exiftool:12.60--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-image-exiftool/12.60--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-image-exiftool/12.60--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-image-exiftool-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-image-exiftool-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-image-exiftool-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-image-exiftool-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-image-exiftool-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-image-exiftool-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### exiftool

```bash
$ singularity exec <container> /usr/local/bin/exiftool
$ podman run --it --rm --entrypoint /usr/local/bin/exiftool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exiftool   -v ${PWD} -w ${PWD} <container> -c " $@"
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