---
layout: container
name:  "quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx/container.yaml"
updated_at: "2025-12-05 04:02:53.702516"
latest: "1.14.6--h1382715_0"
container_url: "https://biocontainers.pro/tools/esme_hdf5_mvapich_4_0_ucx"
aliases:
 - "chacl"
 - "getfacl"
 - "setfacl"
 - "h5pcc"
 - "h5perf"
 - "h5pfc"
 - "ph5diff"
 - "h5fuse"
 - "attr"
 - "getfattr"
 - "setfattr"
 - "h5delete"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5import"
 - "h5jam"
 - "h5ls"
 - "h5mkgrp"
 - "h5perf_serial"
 - "h5redeploy"
 - "h5repack"
versions:
 - "1.14.6--h1382715_0"
description: "singularity registry hpc automated addition for esme_hdf5_mvapich_4_0_ucx"
config: {"url": "https://biocontainers.pro/tools/esme_hdf5_mvapich_4_0_ucx", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_hdf5_mvapich_4_0_ucx", "latest": {"1.14.6--h1382715_0": "sha256:49604f96b08f4ca69e0f77cc1f3cfdbb11fe3cdf0e44ab636db1e475243ce289"}, "tags": {"1.14.6--h1382715_0": "sha256:49604f96b08f4ca69e0f77cc1f3cfdbb11fe3cdf0e44ab636db1e475243ce289"}, "docker": "quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx", "aliases": {"chacl": "/usr/local/bin/chacl", "getfacl": "/usr/local/bin/getfacl", "setfacl": "/usr/local/bin/setfacl", "h5pcc": "/usr/local/bin/h5pcc", "h5perf": "/usr/local/bin/h5perf", "h5pfc": "/usr/local/bin/h5pfc", "ph5diff": "/usr/local/bin/ph5diff", "h5fuse": "/usr/local/bin/h5fuse", "attr": "/usr/local/bin/attr", "getfattr": "/usr/local/bin/getfattr", "setfattr": "/usr/local/bin/setfattr", "h5delete": "/usr/local/bin/h5delete", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug", "h5diff": "/usr/local/bin/h5diff", "h5import": "/usr/local/bin/h5import", "h5jam": "/usr/local/bin/h5jam", "h5ls": "/usr/local/bin/h5ls", "h5mkgrp": "/usr/local/bin/h5mkgrp", "h5perf_serial": "/usr/local/bin/h5perf_serial", "h5redeploy": "/usr/local/bin/h5redeploy", "h5repack": "/usr/local/bin/h5repack"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx.
singularity registry hpc automated addition for esme_hdf5_mvapich_4_0_ucx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx:1.14.6--h1382715_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx/1.14.6--h1382715_0
$ module help quay.io/biocontainers/esme_hdf5_mvapich_4_0_ucx/1.14.6--h1382715_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_hdf5_mvapich_4_0_ucx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_hdf5_mvapich_4_0_ucx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_hdf5_mvapich_4_0_ucx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_hdf5_mvapich_4_0_ucx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_hdf5_mvapich_4_0_ucx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_hdf5_mvapich_4_0_ucx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chacl

```bash
$ singularity exec <container> /usr/local/bin/chacl
$ podman run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfacl

```bash
$ singularity exec <container> /usr/local/bin/getfacl
$ podman run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setfacl

```bash
$ singularity exec <container> /usr/local/bin/setfacl
$ podman run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pcc

```bash
$ singularity exec <container> /usr/local/bin/h5pcc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf

```bash
$ singularity exec <container> /usr/local/bin/h5perf
$ podman run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pfc

```bash
$ singularity exec <container> /usr/local/bin/h5pfc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ph5diff

```bash
$ singularity exec <container> /usr/local/bin/ph5diff
$ podman run --it --rm --entrypoint /usr/local/bin/ph5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ph5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### attr

```bash
$ singularity exec <container> /usr/local/bin/attr
$ podman run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfattr

```bash
$ singularity exec <container> /usr/local/bin/getfattr
$ podman run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setfattr

```bash
$ singularity exec <container> /usr/local/bin/setfattr
$ podman run --it --rm --entrypoint /usr/local/bin/setfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5diff

```bash
$ singularity exec <container> /usr/local/bin/h5diff
$ podman run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5import

```bash
$ singularity exec <container> /usr/local/bin/h5import
$ podman run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5jam

```bash
$ singularity exec <container> /usr/local/bin/h5jam
$ podman run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5ls

```bash
$ singularity exec <container> /usr/local/bin/h5ls
$ podman run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5mkgrp

```bash
$ singularity exec <container> /usr/local/bin/h5mkgrp
$ podman run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf_serial

```bash
$ singularity exec <container> /usr/local/bin/h5perf_serial
$ podman run --it --rm --entrypoint /usr/local/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5redeploy

```bash
$ singularity exec <container> /usr/local/bin/h5redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5repack

```bash
$ singularity exec <container> /usr/local/bin/h5repack
$ podman run --it --rm --entrypoint /usr/local/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
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