---
layout: container
name:  "quay.io/biocontainers/pal_finder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pal_finder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pal_finder/container.yaml"
updated_at: "2025-02-13 03:08:04.253916"
latest: "0.02.04--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/pal_finder"
aliases:
 - "long_seq_tm_test"
 - "ntdpal"
 - "oligotm"
 - "pal_finder"
 - "primer3_core"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "0.02.04--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for pal_finder"
config: {"url": "https://biocontainers.pro/tools/pal_finder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pal_finder", "latest": {"0.02.04--hdfd78af_4": "sha256:0b6a16059b57bcba5e0052e0ecf4cbdaaccd9f557abb2f008c397ffbbd7999c4"}, "tags": {"0.02.04--hdfd78af_4": "sha256:0b6a16059b57bcba5e0052e0ecf4cbdaaccd9f557abb2f008c397ffbbd7999c4"}, "docker": "quay.io/biocontainers/pal_finder", "aliases": {"long_seq_tm_test": "/usr/local/bin/long_seq_tm_test", "ntdpal": "/usr/local/bin/ntdpal", "oligotm": "/usr/local/bin/oligotm", "pal_finder": "/usr/local/bin/pal_finder", "primer3_core": "/usr/local/bin/primer3_core", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pal_finder.
shpc-registry automated BioContainers addition for pal_finder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pal_finder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pal_finder:0.02.04--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pal_finder/0.02.04--hdfd78af_4
$ module help quay.io/biocontainers/pal_finder/0.02.04--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pal_finder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pal_finder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pal_finder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pal_finder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pal_finder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pal_finder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### long_seq_tm_test

```bash
$ singularity exec <container> /usr/local/bin/long_seq_tm_test
$ podman run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntdpal

```bash
$ singularity exec <container> /usr/local/bin/ntdpal
$ podman run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oligotm

```bash
$ singularity exec <container> /usr/local/bin/oligotm
$ podman run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pal_finder

```bash
$ singularity exec <container> /usr/local/bin/pal_finder
$ podman run --it --rm --entrypoint /usr/local/bin/pal_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pal_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primer3_core

```bash
$ singularity exec <container> /usr/local/bin/primer3_core
$ podman run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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