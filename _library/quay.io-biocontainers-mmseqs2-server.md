---
layout: container
name:  "quay.io/biocontainers/mmseqs2-server"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmseqs2-server/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmseqs2-server/container.yaml"
updated_at: "2026-01-14 04:07:43.293329"
latest: "8.c4b9644--he881be0_0"
container_url: "https://biocontainers.pro/tools/mmseqs2-server"
aliases:
 - "foldseek"
 - "mmseqs-server"
 - "gawk-5.3.0"
 - "gawkbug"
 - "aria2c"
 - "mmseqs"
 - "awk"
 - "gawk"
 - "idn2"
 - "wget"
versions:
 - "8.c4b9644--he881be0_0"
description: "singularity registry hpc automated addition for mmseqs2-server"
config: {"url": "https://biocontainers.pro/tools/mmseqs2-server", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mmseqs2-server", "latest": {"8.c4b9644--he881be0_0": "sha256:522812e279da9c53c196fa282f9971cd780ad0afd4b0a93284250e2fa72e49fa"}, "tags": {"8.c4b9644--he881be0_0": "sha256:522812e279da9c53c196fa282f9971cd780ad0afd4b0a93284250e2fa72e49fa"}, "docker": "quay.io/biocontainers/mmseqs2-server", "aliases": {"foldseek": "/usr/local/bin/foldseek", "mmseqs-server": "/usr/local/bin/mmseqs-server", "gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "gawkbug": "/usr/local/bin/gawkbug", "aria2c": "/usr/local/bin/aria2c", "mmseqs": "/usr/local/bin/mmseqs", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmseqs2-server.
singularity registry hpc automated addition for mmseqs2-server
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmseqs2-server
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmseqs2-server:8.c4b9644--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmseqs2-server/8.c4b9644--he881be0_0
$ module help quay.io/biocontainers/mmseqs2-server/8.c4b9644--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmseqs2-server-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmseqs2-server-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmseqs2-server-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmseqs2-server-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmseqs2-server-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmseqs2-server-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### foldseek

```bash
$ singularity exec <container> /usr/local/bin/foldseek
$ podman run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs-server

```bash
$ singularity exec <container> /usr/local/bin/mmseqs-server
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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