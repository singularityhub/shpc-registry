---
layout: container
name:  "quay.io/biocontainers/plass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plass/container.yaml"
updated_at: "2025-01-21 03:13:58.944971"
latest: "5.cf8933--pl5321h6a68c12_1"
container_url: "https://biocontainers.pro/tools/plass"
aliases:
 - "plass"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "4.687d7--pl5321hf1761c0_3"
 - "4.687d7--pl5321h6a68c12_5"
 - "5.cf8933--pl5321h6a68c12_0"
 - "5.cf8933--pl5321h6a68c12_1"
description: "shpc-registry automated BioContainers addition for plass"
config: {"url": "https://biocontainers.pro/tools/plass", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plass", "latest": {"5.cf8933--pl5321h6a68c12_1": "sha256:5d1022eaca1c22825d88fa641f7cdd21d0209734f915f4cf7c0bd52e3a4de9b9"}, "tags": {"4.687d7--pl5321hf1761c0_3": "sha256:81ff206e4cabdcb4512b9cb5950e9f79ffb8dd038cdfc15d03e2249e80b4f62f", "4.687d7--pl5321h6a68c12_5": "sha256:c14320a99ea06aa7cf4f8d47ee7de453df0207eb5a7e35bc2de073e6c9a5f6b7", "5.cf8933--pl5321h6a68c12_0": "sha256:80fcfeb5b33c9fad81101e5e8e42e555a0d7c8fc0b587434a0128bb7f0644d52", "5.cf8933--pl5321h6a68c12_1": "sha256:5d1022eaca1c22825d88fa641f7cdd21d0209734f915f4cf7c0bd52e3a4de9b9"}, "docker": "quay.io/biocontainers/plass", "aliases": {"plass": "/usr/local/bin/plass", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plass.
shpc-registry automated BioContainers addition for plass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plass:5.cf8933--pl5321h6a68c12_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plass/5.cf8933--pl5321h6a68c12_1
$ module help quay.io/biocontainers/plass/5.cf8933--pl5321h6a68c12_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plass

```bash
$ singularity exec <container> /usr/local/bin/plass
$ podman run --it --rm --entrypoint /usr/local/bin/plass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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