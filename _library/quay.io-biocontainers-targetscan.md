---
layout: container
name:  "quay.io/biocontainers/targetscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/targetscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/targetscan/container.yaml"
updated_at: "2025-12-10 03:37:13.952133"
latest: "7.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/targetscan"
aliases:
 - "targetscan_70.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "7.0--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for targetscan"
config: {"url": "https://biocontainers.pro/tools/targetscan", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for targetscan", "latest": {"7.0--pl5321hdfd78af_0": "sha256:766449d7116d75961221a8937ee2687a815992b1ea5d4bff008e98bf5f7e9ac4"}, "tags": {"7.0--pl5321hdfd78af_0": "sha256:766449d7116d75961221a8937ee2687a815992b1ea5d4bff008e98bf5f7e9ac4"}, "docker": "quay.io/biocontainers/targetscan", "aliases": {"targetscan_70.pl": "/usr/local/bin/targetscan_70.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/targetscan.
singularity registry hpc automated addition for targetscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/targetscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/targetscan:7.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/targetscan/7.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/targetscan/7.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### targetscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### targetscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### targetscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### targetscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### targetscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### targetscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### targetscan_70.pl

```bash
$ singularity exec <container> /usr/local/bin/targetscan_70.pl
$ podman run --it --rm --entrypoint /usr/local/bin/targetscan_70.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/targetscan_70.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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