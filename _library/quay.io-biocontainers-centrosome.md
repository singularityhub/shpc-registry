---
layout: container
name:  "quay.io/biocontainers/centrosome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/centrosome/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/centrosome/container.yaml"
updated_at: "2022-10-27 00:53:40.739567"
latest: "1.2.1--py39h919a90d_0"
container_url: "https://biocontainers.pro/tools/centrosome"
aliases:
 - "aomdec"
 - "aomenc"
 - "dav1d"
 - "tiff2fsspec"
 - "tiffcomment"
versions:
 - "1.2.1--py39h919a90d_0"
description: "shpc-registry automated BioContainers addition for centrosome"
config: {"url": "https://biocontainers.pro/tools/centrosome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for centrosome", "latest": {"1.2.1--py39h919a90d_0": "sha256:c69100fcbd1f8a78542dccfee785dc7109eb0f80ba82c17e4b5ee7d717bff89d"}, "tags": {"1.2.1--py39h919a90d_0": "sha256:c69100fcbd1f8a78542dccfee785dc7109eb0f80ba82c17e4b5ee7d717bff89d"}, "docker": "quay.io/biocontainers/centrosome", "aliases": {"aomdec": "/usr/local/bin/aomdec", "aomenc": "/usr/local/bin/aomenc", "dav1d": "/usr/local/bin/dav1d", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "tiffcomment": "/usr/local/bin/tiffcomment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/centrosome.
shpc-registry automated BioContainers addition for centrosome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/centrosome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/centrosome:1.2.1--py39h919a90d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/centrosome/1.2.1--py39h919a90d_0
$ module help quay.io/biocontainers/centrosome/1.2.1--py39h919a90d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### centrosome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### centrosome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### centrosome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### centrosome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### centrosome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### centrosome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aomdec

```bash
$ singularity exec <container> /usr/local/bin/aomdec
$ podman run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomenc

```bash
$ singularity exec <container> /usr/local/bin/aomenc
$ podman run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dav1d

```bash
$ singularity exec <container> /usr/local/bin/dav1d
$ podman run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcomment

```bash
$ singularity exec <container> /usr/local/bin/tiffcomment
$ podman run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
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