---
layout: container
name:  "quay.io/biocontainers/stream_atac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stream_atac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stream_atac/container.yaml"
updated_at: "2024-10-31 03:32:32.850777"
latest: "0.3.5--py_5"
container_url: "https://biocontainers.pro/tools/stream_atac"
aliases:
 - "stream_atac"
 - "zip"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
 - "jupyter-notebook"
 - "jupyter-serverextension"
 - "unzip"
versions:
 - "0.3.5--py_5"
description: "shpc-registry automated BioContainers addition for stream_atac"
config: {"url": "https://biocontainers.pro/tools/stream_atac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stream_atac", "latest": {"0.3.5--py_5": "sha256:5f33f127d097a5d4a3f3bd3492e8dc4b4a53c8757a183e22bbf6f90d9cf9b7c5"}, "tags": {"0.3.5--py_5": "sha256:5f33f127d097a5d4a3f3bd3492e8dc4b4a53c8757a183e22bbf6f90d9cf9b7c5"}, "docker": "quay.io/biocontainers/stream_atac", "aliases": {"stream_atac": "/usr/local/bin/stream_atac", "zip": "/usr/local/bin/zip", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "jupyter-serverextension": "/usr/local/bin/jupyter-serverextension", "unzip": "/usr/local/bin/unzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stream_atac.
shpc-registry automated BioContainers addition for stream_atac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stream_atac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stream_atac:0.3.5--py_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stream_atac/0.3.5--py_5
$ module help quay.io/biocontainers/stream_atac/0.3.5--py_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stream_atac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stream_atac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stream_atac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stream_atac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stream_atac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stream_atac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stream_atac

```bash
$ singularity exec <container> /usr/local/bin/stream_atac
$ podman run --it --rm --entrypoint /usr/local/bin/stream_atac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stream_atac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zip

```bash
$ singularity exec <container> /usr/local/bin/zip
$ podman run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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