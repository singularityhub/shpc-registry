---
layout: container
name:  "quay.io/biocontainers/pedesigner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pedesigner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pedesigner/container.yaml"
updated_at: "2024-12-26 03:13:21.355696"
latest: "0.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pedesigner"
aliases:
 - "cas-offinder"
 - "edonr256-hash"
 - "edonr512-hash"
 - "gost12-256-hash"
 - "gost12-512-hash"
 - "llvm-spirv-15"
 - "pedesigner"
 - "poclcc"
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
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
 - "hwloc-gather-topology"
 - "hwloc-info"
 - "hwloc-ls"
 - "hwloc-patch"
 - "hwloc-ps"
 - "lstopo"
versions:
 - "0.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pedesigner"
config: {"url": "https://biocontainers.pro/tools/pedesigner", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pedesigner", "latest": {"0.2.0--pyhdfd78af_0": "sha256:b8cce844e5647e0019fe53eeeea0ffc7c7d6f85c7295df2fa47cdc2ddbf60fa7"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:b8cce844e5647e0019fe53eeeea0ffc7c7d6f85c7295df2fa47cdc2ddbf60fa7"}, "docker": "quay.io/biocontainers/pedesigner", "aliases": {"cas-offinder": "/usr/local/bin/cas-offinder", "edonr256-hash": "/usr/local/bin/edonr256-hash", "edonr512-hash": "/usr/local/bin/edonr512-hash", "gost12-256-hash": "/usr/local/bin/gost12-256-hash", "gost12-512-hash": "/usr/local/bin/gost12-512-hash", "llvm-spirv-15": "/usr/local/bin/llvm-spirv-15", "pedesigner": "/usr/local/bin/pedesigner", "poclcc": "/usr/local/bin/poclcc", "ccmake": "/usr/local/bin/ccmake", "cmake": "/usr/local/bin/cmake", "cpack": "/usr/local/bin/cpack", "ctest": "/usr/local/bin/ctest", "ed2k-link": "/usr/local/bin/ed2k-link", "has160-hash": "/usr/local/bin/has160-hash", "magnet-link": "/usr/local/bin/magnet-link", "rhash": "/usr/local/bin/rhash", "sfv-hash": "/usr/local/bin/sfv-hash", "tiger-hash": "/usr/local/bin/tiger-hash", "tth-hash": "/usr/local/bin/tth-hash", "whirlpool-hash": "/usr/local/bin/whirlpool-hash", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch", "hwloc-ps": "/usr/local/bin/hwloc-ps", "lstopo": "/usr/local/bin/lstopo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pedesigner.
singularity registry hpc automated addition for pedesigner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pedesigner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pedesigner:0.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pedesigner/0.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/pedesigner/0.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pedesigner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pedesigner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pedesigner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pedesigner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pedesigner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pedesigner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cas-offinder

```bash
$ singularity exec <container> /usr/local/bin/cas-offinder
$ podman run --it --rm --entrypoint /usr/local/bin/cas-offinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cas-offinder   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### llvm-spirv-15

```bash
$ singularity exec <container> /usr/local/bin/llvm-spirv-15
$ podman run --it --rm --entrypoint /usr/local/bin/llvm-spirv-15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llvm-spirv-15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pedesigner

```bash
$ singularity exec <container> /usr/local/bin/pedesigner
$ podman run --it --rm --entrypoint /usr/local/bin/pedesigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pedesigner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poclcc

```bash
$ singularity exec <container> /usr/local/bin/poclcc
$ podman run --it --rm --entrypoint /usr/local/bin/poclcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poclcc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-compress-dir

```bash
$ singularity exec <container> /usr/local/bin/hwloc-compress-dir
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-diff

```bash
$ singularity exec <container> /usr/local/bin/hwloc-diff
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-distrib

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-topology

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-topology
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-info

```bash
$ singularity exec <container> /usr/local/bin/hwloc-info
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-ls

```bash
$ singularity exec <container> /usr/local/bin/hwloc-ls
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-patch

```bash
$ singularity exec <container> /usr/local/bin/hwloc-patch
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-patch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-ps

```bash
$ singularity exec <container> /usr/local/bin/hwloc-ps
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-ps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lstopo

```bash
$ singularity exec <container> /usr/local/bin/lstopo
$ podman run --it --rm --entrypoint /usr/local/bin/lstopo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lstopo   -v ${PWD} -w ${PWD} <container> -c " $@"
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