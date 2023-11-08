---
layout: container
name:  "quay.io/biocontainers/bigsi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bigsi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bigsi/container.yaml"
updated_at: "2023-11-08 02:27:24.123701"
latest: "0.3.1--py_0"
container_url: "https://biocontainers.pro/tools/bigsi"
aliases:
 - "bigsi"
 - "falcon-bench"
 - "falcon-print-routes"
 - "hug"
 - "humanfriendly"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "db_archive"
 - "db_checkpoint"
 - "db_deadlock"
 - "db_dump"
 - "db_hotbackup"
 - "db_load"
versions:
 - "0.3.1--py_0"
description: "shpc-registry automated BioContainers addition for bigsi"
config: {"url": "https://biocontainers.pro/tools/bigsi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bigsi", "latest": {"0.3.1--py_0": "sha256:cb03250b3b94c8ad996c8250692df03a4ae9b60fdcfb8770df8833f1172012f5"}, "tags": {"0.3.1--py_0": "sha256:cb03250b3b94c8ad996c8250692df03a4ae9b60fdcfb8770df8833f1172012f5"}, "docker": "quay.io/biocontainers/bigsi", "aliases": {"bigsi": "/usr/local/bin/bigsi", "falcon-bench": "/usr/local/bin/falcon-bench", "falcon-print-routes": "/usr/local/bin/falcon-print-routes", "hug": "/usr/local/bin/hug", "humanfriendly": "/usr/local/bin/humanfriendly", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "db_archive": "/usr/local/bin/db_archive", "db_checkpoint": "/usr/local/bin/db_checkpoint", "db_deadlock": "/usr/local/bin/db_deadlock", "db_dump": "/usr/local/bin/db_dump", "db_hotbackup": "/usr/local/bin/db_hotbackup", "db_load": "/usr/local/bin/db_load"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bigsi.
shpc-registry automated BioContainers addition for bigsi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bigsi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bigsi:0.3.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bigsi/0.3.1--py_0
$ module help quay.io/biocontainers/bigsi/0.3.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bigsi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bigsi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bigsi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bigsi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bigsi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bigsi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigsi

```bash
$ singularity exec <container> /usr/local/bin/bigsi
$ podman run --it --rm --entrypoint /usr/local/bin/bigsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### falcon-bench

```bash
$ singularity exec <container> /usr/local/bin/falcon-bench
$ podman run --it --rm --entrypoint /usr/local/bin/falcon-bench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falcon-bench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### falcon-print-routes

```bash
$ singularity exec <container> /usr/local/bin/falcon-print-routes
$ podman run --it --rm --entrypoint /usr/local/bin/falcon-print-routes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falcon-print-routes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hug

```bash
$ singularity exec <container> /usr/local/bin/hug
$ podman run --it --rm --entrypoint /usr/local/bin/hug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_archive

```bash
$ singularity exec <container> /usr/local/bin/db_archive
$ podman run --it --rm --entrypoint /usr/local/bin/db_archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_checkpoint

```bash
$ singularity exec <container> /usr/local/bin/db_checkpoint
$ podman run --it --rm --entrypoint /usr/local/bin/db_checkpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_checkpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_deadlock

```bash
$ singularity exec <container> /usr/local/bin/db_deadlock
$ podman run --it --rm --entrypoint /usr/local/bin/db_deadlock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_deadlock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_dump

```bash
$ singularity exec <container> /usr/local/bin/db_dump
$ podman run --it --rm --entrypoint /usr/local/bin/db_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_hotbackup

```bash
$ singularity exec <container> /usr/local/bin/db_hotbackup
$ podman run --it --rm --entrypoint /usr/local/bin/db_hotbackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_hotbackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_load

```bash
$ singularity exec <container> /usr/local/bin/db_load
$ podman run --it --rm --entrypoint /usr/local/bin/db_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_load   -v ${PWD} -w ${PWD} <container> -c " $@"
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