---
layout: container
name:  "quay.io/biocontainers/nirvana"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nirvana/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nirvana/container.yaml"
updated_at: "2026-03-11 04:13:55.236280"
latest: "3.18.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/nirvana"
aliases:
 - "Downloader"
 - "Nirvana"
 - "dotnet"
 - "lttng-gen-tp"
versions:
 - "3.18.1--hdfd78af_1"
description: "singularity registry hpc automated addition for nirvana"
config: {"url": "https://biocontainers.pro/tools/nirvana", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nirvana", "latest": {"3.18.1--hdfd78af_1": "sha256:00e9b4d403e0c64e61aa5a2e376b0b9ec5ac444b4cb8cf91c7e05a406ee537c0"}, "tags": {"3.18.1--hdfd78af_1": "sha256:00e9b4d403e0c64e61aa5a2e376b0b9ec5ac444b4cb8cf91c7e05a406ee537c0"}, "docker": "quay.io/biocontainers/nirvana", "aliases": {"Downloader": "/usr/local/bin/Downloader", "Nirvana": "/usr/local/bin/Nirvana", "dotnet": "/usr/local/bin/dotnet", "lttng-gen-tp": "/usr/local/bin/lttng-gen-tp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nirvana.
singularity registry hpc automated addition for nirvana
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nirvana
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nirvana:3.18.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nirvana/3.18.1--hdfd78af_1
$ module help quay.io/biocontainers/nirvana/3.18.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nirvana-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nirvana-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nirvana-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nirvana-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nirvana-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nirvana-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Downloader

```bash
$ singularity exec <container> /usr/local/bin/Downloader
$ podman run --it --rm --entrypoint /usr/local/bin/Downloader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Downloader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Nirvana

```bash
$ singularity exec <container> /usr/local/bin/Nirvana
$ podman run --it --rm --entrypoint /usr/local/bin/Nirvana   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Nirvana   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotnet

```bash
$ singularity exec <container> /usr/local/bin/dotnet
$ podman run --it --rm --entrypoint /usr/local/bin/dotnet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotnet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
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