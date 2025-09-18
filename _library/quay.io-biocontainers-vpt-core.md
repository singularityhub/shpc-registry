---
layout: container
name:  "quay.io/biocontainers/vpt-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vpt-core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vpt-core/container.yaml"
updated_at: "2025-09-18 03:36:23.808873"
latest: "1.2.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/vpt-core"
aliases:
 - "dec265"
 - "gdal_footprint"
 - "gost12-256-hash"
 - "gost12-512-hash"
 - "minigzip"
 - "minizip"
 - "pyproj"
 - "rio"
 - "sozip"
 - "edonr256-hash"
 - "edonr512-hash"
 - "dotenv"
 - "ccmake"
 - "cmake"
 - "cpack"
 - "ctest"
 - "ed2k-link"
 - "has160-hash"
 - "magnet-link"
 - "rhash"
 - "sfv-hash"
 - "tiger-hash"
 - "tth-hash"
 - "whirlpool-hash"
 - "bsdunzip"
 - "genl-ctrl-list"
 - "idiag-socket-details"
 - "nf-ct-add"
 - "nf-ct-events"
 - "nf-ct-list"
 - "nf-exp-add"
 - "nf-exp-delete"
 - "nf-exp-list"
 - "nf-log"
versions:
 - "1.2.0--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_1"
description: "singularity registry hpc automated addition for vpt-core"
config: {"url": "https://biocontainers.pro/tools/vpt-core", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vpt-core", "latest": {"1.2.0--pyhdfd78af_1": "sha256:8d98a5eabcaa055f18400fa90d6467cf88b147826b981d0236ab0bd760b70e8b"}, "tags": {"1.2.0--pyhdfd78af_0": "sha256:b497c9526050d1bb88e6b35e20f767d8c0183632224db1d008bbc5f025552f72", "1.2.0--pyhdfd78af_1": "sha256:8d98a5eabcaa055f18400fa90d6467cf88b147826b981d0236ab0bd760b70e8b"}, "docker": "quay.io/biocontainers/vpt-core", "aliases": {"dec265": "/usr/local/bin/dec265", "gdal_footprint": "/usr/local/bin/gdal_footprint", "gost12-256-hash": "/usr/local/bin/gost12-256-hash", "gost12-512-hash": "/usr/local/bin/gost12-512-hash", "minigzip": "/usr/local/bin/minigzip", "minizip": "/usr/local/bin/minizip", "pyproj": "/usr/local/bin/pyproj", "rio": "/usr/local/bin/rio", "sozip": "/usr/local/bin/sozip", "edonr256-hash": "/usr/local/bin/edonr256-hash", "edonr512-hash": "/usr/local/bin/edonr512-hash", "dotenv": "/usr/local/bin/dotenv", "ccmake": "/usr/local/bin/ccmake", "cmake": "/usr/local/bin/cmake", "cpack": "/usr/local/bin/cpack", "ctest": "/usr/local/bin/ctest", "ed2k-link": "/usr/local/bin/ed2k-link", "has160-hash": "/usr/local/bin/has160-hash", "magnet-link": "/usr/local/bin/magnet-link", "rhash": "/usr/local/bin/rhash", "sfv-hash": "/usr/local/bin/sfv-hash", "tiger-hash": "/usr/local/bin/tiger-hash", "tth-hash": "/usr/local/bin/tth-hash", "whirlpool-hash": "/usr/local/bin/whirlpool-hash", "bsdunzip": "/usr/local/bin/bsdunzip", "genl-ctrl-list": "/usr/local/bin/genl-ctrl-list", "idiag-socket-details": "/usr/local/bin/idiag-socket-details", "nf-ct-add": "/usr/local/bin/nf-ct-add", "nf-ct-events": "/usr/local/bin/nf-ct-events", "nf-ct-list": "/usr/local/bin/nf-ct-list", "nf-exp-add": "/usr/local/bin/nf-exp-add", "nf-exp-delete": "/usr/local/bin/nf-exp-delete", "nf-exp-list": "/usr/local/bin/nf-exp-list", "nf-log": "/usr/local/bin/nf-log"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vpt-core.
singularity registry hpc automated addition for vpt-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vpt-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vpt-core:1.2.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vpt-core/1.2.0--pyhdfd78af_1
$ module help quay.io/biocontainers/vpt-core/1.2.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vpt-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vpt-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vpt-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vpt-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vpt-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vpt-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dec265

```bash
$ singularity exec <container> /usr/local/bin/dec265
$ podman run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_footprint

```bash
$ singularity exec <container> /usr/local/bin/gdal_footprint
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_footprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_footprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-256-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-512-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minigzip

```bash
$ singularity exec <container> /usr/local/bin/minigzip
$ podman run --it --rm --entrypoint /usr/local/bin/minigzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minigzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minizip

```bash
$ singularity exec <container> /usr/local/bin/minizip
$ podman run --it --rm --entrypoint /usr/local/bin/minizip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minizip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyproj

```bash
$ singularity exec <container> /usr/local/bin/pyproj
$ podman run --it --rm --entrypoint /usr/local/bin/pyproj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyproj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rio

```bash
$ singularity exec <container> /usr/local/bin/rio
$ podman run --it --rm --entrypoint /usr/local/bin/rio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sozip

```bash
$ singularity exec <container> /usr/local/bin/sozip
$ podman run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sozip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr256-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr512-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccmake

```bash
$ singularity exec <container> /usr/local/bin/ccmake
$ podman run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmake

```bash
$ singularity exec <container> /usr/local/bin/cmake
$ podman run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpack

```bash
$ singularity exec <container> /usr/local/bin/cpack
$ podman run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctest

```bash
$ singularity exec <container> /usr/local/bin/ctest
$ podman run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ed2k-link

```bash
$ singularity exec <container> /usr/local/bin/ed2k-link
$ podman run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### has160-hash

```bash
$ singularity exec <container> /usr/local/bin/has160-hash
$ podman run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magnet-link

```bash
$ singularity exec <container> /usr/local/bin/magnet-link
$ podman run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rhash

```bash
$ singularity exec <container> /usr/local/bin/rhash
$ podman run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfv-hash

```bash
$ singularity exec <container> /usr/local/bin/sfv-hash
$ podman run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiger-hash

```bash
$ singularity exec <container> /usr/local/bin/tiger-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tth-hash

```bash
$ singularity exec <container> /usr/local/bin/tth-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whirlpool-hash

```bash
$ singularity exec <container> /usr/local/bin/whirlpool-hash
$ podman run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genl-ctrl-list

```bash
$ singularity exec <container> /usr/local/bin/genl-ctrl-list
$ podman run --it --rm --entrypoint /usr/local/bin/genl-ctrl-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genl-ctrl-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idiag-socket-details

```bash
$ singularity exec <container> /usr/local/bin/idiag-socket-details
$ podman run --it --rm --entrypoint /usr/local/bin/idiag-socket-details   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idiag-socket-details   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-ct-add

```bash
$ singularity exec <container> /usr/local/bin/nf-ct-add
$ podman run --it --rm --entrypoint /usr/local/bin/nf-ct-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-ct-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-ct-events

```bash
$ singularity exec <container> /usr/local/bin/nf-ct-events
$ podman run --it --rm --entrypoint /usr/local/bin/nf-ct-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-ct-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-ct-list

```bash
$ singularity exec <container> /usr/local/bin/nf-ct-list
$ podman run --it --rm --entrypoint /usr/local/bin/nf-ct-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-ct-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-exp-add

```bash
$ singularity exec <container> /usr/local/bin/nf-exp-add
$ podman run --it --rm --entrypoint /usr/local/bin/nf-exp-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-exp-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-exp-delete

```bash
$ singularity exec <container> /usr/local/bin/nf-exp-delete
$ podman run --it --rm --entrypoint /usr/local/bin/nf-exp-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-exp-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-exp-list

```bash
$ singularity exec <container> /usr/local/bin/nf-exp-list
$ podman run --it --rm --entrypoint /usr/local/bin/nf-exp-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-exp-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-log

```bash
$ singularity exec <container> /usr/local/bin/nf-log
$ podman run --it --rm --entrypoint /usr/local/bin/nf-log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-log   -v ${PWD} -w ${PWD} <container> -c " $@"
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