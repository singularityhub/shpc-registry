---
layout: container
name:  "quay.io/biocontainers/kobas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kobas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kobas/container.yaml"
updated_at: "2023-02-12 03:17:06.946121"
latest: "3.0.3--py_3"
container_url: "https://biocontainers.pro/tools/kobas"
aliases:
 - "kobas-annotate"
 - "kobas-identify"
 - "kobas-run"
 - "build.sh"
 - "common.go"
 - "rchive.go"
 - "setup-deps.log"
 - "setup.sh"
 - "xtract.go"
 - "metadata_conda_debug.yaml"
 - "bt-context.txt"
 - "bt-link"
 - "bt-load"
versions:
 - "3.0.3--py_3"
description: "shpc-registry automated BioContainers addition for kobas"
config: {"url": "https://biocontainers.pro/tools/kobas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kobas", "latest": {"3.0.3--py_3": "sha256:430b30f6141a51f581f301e8b66bbb8db401d730673acb9eb6ef28ace78a9c66"}, "tags": {"3.0.3--py_3": "sha256:430b30f6141a51f581f301e8b66bbb8db401d730673acb9eb6ef28ace78a9c66"}, "docker": "quay.io/biocontainers/kobas", "aliases": {"kobas-annotate": "/usr/local/bin/kobas-annotate", "kobas-identify": "/usr/local/bin/kobas-identify", "kobas-run": "/usr/local/bin/kobas-run", "build.sh": "/usr/local/bin/build.sh", "common.go": "/usr/local/bin/common.go", "rchive.go": "/usr/local/bin/rchive.go", "setup-deps.log": "/usr/local/bin/setup-deps.log", "setup.sh": "/usr/local/bin/setup.sh", "xtract.go": "/usr/local/bin/xtract.go", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "bt-context.txt": "/usr/local/bin/bt-context.txt", "bt-link": "/usr/local/bin/bt-link", "bt-load": "/usr/local/bin/bt-load"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kobas.
shpc-registry automated BioContainers addition for kobas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kobas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kobas:3.0.3--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kobas/3.0.3--py_3
$ module help quay.io/biocontainers/kobas/3.0.3--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kobas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kobas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kobas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kobas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kobas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kobas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kobas-annotate

```bash
$ singularity exec <container> /usr/local/bin/kobas-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/kobas-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kobas-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kobas-identify

```bash
$ singularity exec <container> /usr/local/bin/kobas-identify
$ podman run --it --rm --entrypoint /usr/local/bin/kobas-identify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kobas-identify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kobas-run

```bash
$ singularity exec <container> /usr/local/bin/kobas-run
$ podman run --it --rm --entrypoint /usr/local/bin/kobas-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kobas-run   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-context.txt

```bash
$ singularity exec <container> /usr/local/bin/bt-context.txt
$ podman run --it --rm --entrypoint /usr/local/bin/bt-context.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-context.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-link

```bash
$ singularity exec <container> /usr/local/bin/bt-link
$ podman run --it --rm --entrypoint /usr/local/bin/bt-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-load

```bash
$ singularity exec <container> /usr/local/bin/bt-load
$ podman run --it --rm --entrypoint /usr/local/bin/bt-load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-load   -v ${PWD} -w ${PWD} <container> -c " $@"
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