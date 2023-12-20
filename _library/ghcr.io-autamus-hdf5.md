---
layout: container
name:  "ghcr.io/autamus/hdf5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/hdf5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/hdf5/container.yaml"
updated_at: "2023-12-20 02:59:53.525176"
latest: "1.13"
container_url: "https://github.com/orgs/autamus/packages/container/package/hdf5"
aliases:
 - "h5clear"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5dump"
 - "h5format_convert"
 - "h5import"
 - "h5jam"
 - "h5ls"
 - "h5mkgrp"
 - "h5pcc"
 - "h5perf"
 - "h5perf_serial"
 - "h5redeploy"
 - "h5repack"
 - "h5repart"
 - "h5stat"
 - "h5unjam"
versions:
 - "1.12.0"
 - "1.13"
 - "latest"
description: "HDF5 is a unique technology suite that makes possible the management of extremely large and complex data collections."
config: {"docker": "ghcr.io/autamus/hdf5", "url": "https://github.com/orgs/autamus/packages/container/package/hdf5", "maintainer": "@vsoch", "description": "HDF5 is a unique technology suite that makes possible the management of extremely large and complex data collections.", "latest": {"1.13": "sha256:394eaff1aa57a18c403833d66bc88fc180f04f5e22fd49ca9dbef955283aa4a0"}, "tags": {"1.12.0": "sha256:cf708cd850f573a009d3f111f5e7576ba18ccbc7e4c7292ed4d8b233c4f4a99b", "1.13": "sha256:394eaff1aa57a18c403833d66bc88fc180f04f5e22fd49ca9dbef955283aa4a0", "latest": "sha256:394eaff1aa57a18c403833d66bc88fc180f04f5e22fd49ca9dbef955283aa4a0"}, "aliases": {"h5clear": "/opt/view/bin/h5clear", "h5copy": "/opt/view/bin/h5copy", "h5debug": "/opt/view/bin/h5debug", "h5diff": "/opt/view/bin/h5diff", "h5dump": "/opt/view/bin/h5dump", "h5format_convert": "/opt/view/bin/h5format_convert", "h5import": "/opt/view/bin/h5import", "h5jam": "/opt/view/bin/h5jam", "h5ls": "/opt/view/bin/h5ls", "h5mkgrp": "/opt/view/bin/h5mkgrp", "h5pcc": "/opt/view/bin/h5pcc", "h5perf": "/opt/view/bin/h5perf", "h5perf_serial": "/opt/view/bin/h5perf_serial", "h5redeploy": "/opt/view/bin/h5redeploy", "h5repack": "/opt/view/bin/h5repack", "h5repart": "/opt/view/bin/h5repart", "h5stat": "/opt/view/bin/h5stat", "h5unjam": "/opt/view/bin/h5unjam"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/hdf5.
HDF5 is a unique technology suite that makes possible the management of extremely large and complex data collections.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/hdf5
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/hdf5:1.13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hdf5/1.13
$ module help ghcr.io/autamus/hdf5/1.13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hdf5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hdf5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hdf5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hdf5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hdf5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hdf5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### h5clear

```bash
$ singularity exec <container> /opt/view/bin/h5clear
$ podman run --it --rm --entrypoint /opt/view/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /opt/view/bin/h5copy
$ podman run --it --rm --entrypoint /opt/view/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /opt/view/bin/h5debug
$ podman run --it --rm --entrypoint /opt/view/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5diff

```bash
$ singularity exec <container> /opt/view/bin/h5diff
$ podman run --it --rm --entrypoint /opt/view/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5dump

```bash
$ singularity exec <container> /opt/view/bin/h5dump
$ podman run --it --rm --entrypoint /opt/view/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /opt/view/bin/h5format_convert
$ podman run --it --rm --entrypoint /opt/view/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5import

```bash
$ singularity exec <container> /opt/view/bin/h5import
$ podman run --it --rm --entrypoint /opt/view/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5jam

```bash
$ singularity exec <container> /opt/view/bin/h5jam
$ podman run --it --rm --entrypoint /opt/view/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5ls

```bash
$ singularity exec <container> /opt/view/bin/h5ls
$ podman run --it --rm --entrypoint /opt/view/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5mkgrp

```bash
$ singularity exec <container> /opt/view/bin/h5mkgrp
$ podman run --it --rm --entrypoint /opt/view/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pcc

```bash
$ singularity exec <container> /opt/view/bin/h5pcc
$ podman run --it --rm --entrypoint /opt/view/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf

```bash
$ singularity exec <container> /opt/view/bin/h5perf
$ podman run --it --rm --entrypoint /opt/view/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf_serial

```bash
$ singularity exec <container> /opt/view/bin/h5perf_serial
$ podman run --it --rm --entrypoint /opt/view/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5redeploy

```bash
$ singularity exec <container> /opt/view/bin/h5redeploy
$ podman run --it --rm --entrypoint /opt/view/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5repack

```bash
$ singularity exec <container> /opt/view/bin/h5repack
$ podman run --it --rm --entrypoint /opt/view/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5repart

```bash
$ singularity exec <container> /opt/view/bin/h5repart
$ podman run --it --rm --entrypoint /opt/view/bin/h5repart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5repart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5stat

```bash
$ singularity exec <container> /opt/view/bin/h5stat
$ podman run --it --rm --entrypoint /opt/view/bin/h5stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5stat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5unjam

```bash
$ singularity exec <container> /opt/view/bin/h5unjam
$ podman run --it --rm --entrypoint /opt/view/bin/h5unjam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/h5unjam   -v ${PWD} -w ${PWD} <container> -c " $@"
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