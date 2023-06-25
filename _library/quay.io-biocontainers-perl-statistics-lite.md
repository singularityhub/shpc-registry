---
layout: container
name:  "quay.io/biocontainers/perl-statistics-lite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-statistics-lite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-statistics-lite/container.yaml"
updated_at: "2023-06-25 03:58:37.444821"
latest: "3.62--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-statistics-lite"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.62--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-statistics-lite"
config: {"url": "https://biocontainers.pro/tools/perl-statistics-lite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-statistics-lite", "latest": {"3.62--pl5321hdfd78af_2": "sha256:afbb4b8afee2632b1686cd33c5cb4cf8709aab76667896fafb3c47258c9556db"}, "tags": {"3.62--pl5321hdfd78af_2": "sha256:afbb4b8afee2632b1686cd33c5cb4cf8709aab76667896fafb3c47258c9556db"}, "docker": "quay.io/biocontainers/perl-statistics-lite", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-statistics-lite.
shpc-registry automated BioContainers addition for perl-statistics-lite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-statistics-lite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-statistics-lite:3.62--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-statistics-lite/3.62--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-statistics-lite/3.62--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-statistics-lite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-statistics-lite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-statistics-lite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-statistics-lite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-statistics-lite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-statistics-lite-inspect-deffile:

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