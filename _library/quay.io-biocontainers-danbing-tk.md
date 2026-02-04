---
layout: container
name:  "quay.io/biocontainers/danbing-tk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/danbing-tk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/danbing-tk/container.yaml"
updated_at: "2026-02-04 04:24:26.437934"
latest: "1.3.2.5--h9948957_0"
container_url: "https://biocontainers.pro/tools/danbing-tk"
aliases:
 - "danbing-tk"
 - "danbing-tk-pred"
 - "genPanKmers"
 - "ktools"
 - "vntr2kmers_thread"
versions:
 - "1.3.2.5--h9948957_0"
description: "singularity registry hpc automated addition for danbing-tk"
config: {"url": "https://biocontainers.pro/tools/danbing-tk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for danbing-tk", "latest": {"1.3.2.5--h9948957_0": "sha256:abd729a7da90df8c79b94af631fd5127b9ccd25f89a3ad3eb3ef1c731d30aae1"}, "tags": {"1.3.2.5--h9948957_0": "sha256:abd729a7da90df8c79b94af631fd5127b9ccd25f89a3ad3eb3ef1c731d30aae1"}, "docker": "quay.io/biocontainers/danbing-tk", "aliases": {"danbing-tk": "/usr/local/bin/danbing-tk", "danbing-tk-pred": "/usr/local/bin/danbing-tk-pred", "genPanKmers": "/usr/local/bin/genPanKmers", "ktools": "/usr/local/bin/ktools", "vntr2kmers_thread": "/usr/local/bin/vntr2kmers_thread"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/danbing-tk.
singularity registry hpc automated addition for danbing-tk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/danbing-tk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/danbing-tk:1.3.2.5--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/danbing-tk/1.3.2.5--h9948957_0
$ module help quay.io/biocontainers/danbing-tk/1.3.2.5--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### danbing-tk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### danbing-tk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### danbing-tk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### danbing-tk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### danbing-tk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### danbing-tk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### danbing-tk

```bash
$ singularity exec <container> /usr/local/bin/danbing-tk
$ podman run --it --rm --entrypoint /usr/local/bin/danbing-tk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/danbing-tk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### danbing-tk-pred

```bash
$ singularity exec <container> /usr/local/bin/danbing-tk-pred
$ podman run --it --rm --entrypoint /usr/local/bin/danbing-tk-pred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/danbing-tk-pred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genPanKmers

```bash
$ singularity exec <container> /usr/local/bin/genPanKmers
$ podman run --it --rm --entrypoint /usr/local/bin/genPanKmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genPanKmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktools

```bash
$ singularity exec <container> /usr/local/bin/ktools
$ podman run --it --rm --entrypoint /usr/local/bin/ktools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vntr2kmers_thread

```bash
$ singularity exec <container> /usr/local/bin/vntr2kmers_thread
$ podman run --it --rm --entrypoint /usr/local/bin/vntr2kmers_thread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vntr2kmers_thread   -v ${PWD} -w ${PWD} <container> -c " $@"
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