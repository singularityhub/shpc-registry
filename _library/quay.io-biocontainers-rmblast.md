---
layout: container
name:  "quay.io/biocontainers/rmblast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rmblast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rmblast/container.yaml"
updated_at: "2025-02-22 03:34:09.938610"
latest: "2.14.1--h91eb8de_1"
container_url: "https://biocontainers.pro/tools/rmblast"
aliases:
 - "rmblastn"
 - "build.sh"
 - "common.go"
 - "rchive.go"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "setup-deps.log"
 - "setup.sh"
 - "xtract.go"
 - "certtool"
versions:
 - "2.9.0--h2d02072_0"
 - "2.11.0--h6200dbe_0"
 - "2.10.0--h2d02072_0"
 - "2.13.0--h5049791_0"
 - "2.13.0--h5709495_1"
 - "2.14.0--h21a3994_1"
 - "2.14.0--h4565617_2"
 - "2.14.1--h4565617_0"
 - "2.14.1--h91eb8de_1"
description: "shpc-registry automated BioContainers addition for rmblast"
config: {"url": "https://biocontainers.pro/tools/rmblast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rmblast", "latest": {"2.14.1--h91eb8de_1": "sha256:538e6cfd5dbf0d493c7b7ba164288c70d154c9a1f13a22ccbb5ed5bad604feef"}, "tags": {"2.9.0--h2d02072_0": "sha256:03d003c2436176bc0a6b803724886cc461d8e3af7c38adcb60913aaa21a536ae", "2.11.0--h6200dbe_0": "sha256:35bfaf4fc9138db97d259e20fd841e11789c2c27e3a21f3ce04f0c9ad6dda69e", "2.10.0--h2d02072_0": "sha256:65dd33a34d3310810b257829b248d53e82b86c74884bf6cbf89a10ee91066f63", "2.13.0--h5049791_0": "sha256:cf57fdef5364bd2700741c1809fdafff0f7faba40f78dbb41e0500c26e5fe7ae", "2.13.0--h5709495_1": "sha256:ed1a9fee1565fb5a0f27c40ea0bfcf432e001351b984eac5c8663f9f5a4e7ea0", "2.14.0--h21a3994_1": "sha256:aebf39e219a69bfc1610c7567762a772e408e7c76ab5bdf90e78d3d57cb7fbc4", "2.14.0--h4565617_2": "sha256:674e3a54898462ed558faabdb0f09d33e27319a7d2eea9ba0cfb74a61de73964", "2.14.1--h4565617_0": "sha256:20818519eebe418663078ab7a7c2e2308f5a8afc598f35d3ec404bd7ae81393b", "2.14.1--h91eb8de_1": "sha256:538e6cfd5dbf0d493c7b7ba164288c70d154c9a1f13a22ccbb5ed5bad604feef"}, "docker": "quay.io/biocontainers/rmblast", "aliases": {"rmblastn": "/usr/local/bin/rmblastn", "build.sh": "/usr/local/bin/build.sh", "common.go": "/usr/local/bin/common.go", "rchive.go": "/usr/local/bin/rchive.go", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "setup-deps.log": "/usr/local/bin/setup-deps.log", "setup.sh": "/usr/local/bin/setup.sh", "xtract.go": "/usr/local/bin/xtract.go", "certtool": "/usr/local/bin/certtool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rmblast.
shpc-registry automated BioContainers addition for rmblast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rmblast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rmblast:2.14.1--h91eb8de_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rmblast/2.14.1--h91eb8de_1
$ module help quay.io/biocontainers/rmblast/2.14.1--h91eb8de_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rmblast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rmblast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rmblast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rmblast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rmblast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rmblast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rmblastn

```bash
$ singularity exec <container> /usr/local/bin/rmblastn
$ podman run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build.sh

```bash
$ singularity exec <container> /usr/local/bin/build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### common.go

```bash
$ singularity exec <container> /usr/local/bin/common.go
$ podman run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rchive.go

```bash
$ singularity exec <container> /usr/local/bin/rchive.go
$ podman run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_report

```bash
$ singularity exec <container> /usr/local/bin/blast_report
$ podman run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_convert

```bash
$ singularity exec <container> /usr/local/bin/blastdb_convert
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_path

```bash
$ singularity exec <container> /usr/local/bin/blastdb_path
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup-deps.log

```bash
$ singularity exec <container> /usr/local/bin/setup-deps.log
$ podman run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.sh

```bash
$ singularity exec <container> /usr/local/bin/setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtract.go

```bash
$ singularity exec <container> /usr/local/bin/xtract.go
$ podman run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
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