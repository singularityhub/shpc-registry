---
layout: container
name:  "quay.io/biocontainers/perl-time-local"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-time-local/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-time-local/container.yaml"
updated_at: "2025-05-23 03:35:50.653982"
latest: "1.2300--pl5.22.0_0"
container_url: "https://biocontainers.pro/tools/perl-time-local"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.30--pl5321hdfd78af_0"
 - "1.2300--pl5.22.0_0"
 - "1.35--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-time-local"
config: {"url": "https://biocontainers.pro/tools/perl-time-local", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-time-local", "latest": {"1.2300--pl5.22.0_0": "sha256:0717ce8a2190d83f1135770f7ea6f21bd9bbc833389b23706394fa36724045d8"}, "tags": {"1.30--pl5321hdfd78af_0": "sha256:0eb70a778831c45b2296aa5f46555e7f6bf6cdf0eda52148d4e96c85b0fff2c7", "1.2300--pl5.22.0_0": "sha256:0717ce8a2190d83f1135770f7ea6f21bd9bbc833389b23706394fa36724045d8", "1.35--pl5321hdfd78af_0": "sha256:edfb233a0d9a99e807e9fa37d6c1c4b8783e9e81aaaaa320e31ba041570ddaad"}, "docker": "quay.io/biocontainers/perl-time-local", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-time-local.
shpc-registry automated BioContainers addition for perl-time-local
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-time-local
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-time-local:1.2300--pl5.22.0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-time-local/1.2300--pl5.22.0_0
$ module help quay.io/biocontainers/perl-time-local/1.2300--pl5.22.0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-time-local-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-time-local-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-time-local-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-time-local-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-time-local-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-time-local-inspect-deffile:

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