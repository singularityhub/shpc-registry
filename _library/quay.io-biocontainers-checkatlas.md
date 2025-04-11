---
layout: container
name:  "quay.io/biocontainers/checkatlas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/checkatlas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/checkatlas/container.yaml"
updated_at: "2025-04-11 03:16:24.696646"
latest: "0.4.17--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/checkatlas"
aliases:
 - "checkatlas"
 - "checkatlas-workflow"
 - "dul-receive-pack"
 - "dul-upload-pack"
 - "dulwich"
 - "h5fuse.sh"
 - "keyring"
 - "pkginfo"
 - "poetry"
 - "pyproject-build"
 - "python-build"
 - "rocm-smi"
 - "virtualenv"
 - "h5delete"
 - "scanpy"
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
 - "lstopo-no-graphics"
 - "doesitcache"
 - "aec"
 - "pycc"
 - "hb-info"
 - "numba"
 - "natsort"
 - "tjbench"
 - "jsonschema"
 - "dbus-cleanup-sockets"
versions:
 - "0.4.2--pyhdfd78af_0"
 - "0.4.17--pyhdfd78af_0"
description: "singularity registry hpc automated addition for checkatlas"
config: {"url": "https://biocontainers.pro/tools/checkatlas", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for checkatlas", "latest": {"0.4.17--pyhdfd78af_0": "sha256:dc1937c4b26f162b0c175a5564445b534b24ad7db7d0b2a17459d32ff2f88588"}, "tags": {"0.4.2--pyhdfd78af_0": "sha256:36e53f3615f7a959d69f702f1bee3e73a1d6566df1f103590bc2fab82c9861ee", "0.4.17--pyhdfd78af_0": "sha256:dc1937c4b26f162b0c175a5564445b534b24ad7db7d0b2a17459d32ff2f88588"}, "docker": "quay.io/biocontainers/checkatlas", "aliases": {"checkatlas": "/usr/local/bin/checkatlas", "checkatlas-workflow": "/usr/local/bin/checkatlas-workflow", "dul-receive-pack": "/usr/local/bin/dul-receive-pack", "dul-upload-pack": "/usr/local/bin/dul-upload-pack", "dulwich": "/usr/local/bin/dulwich", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "keyring": "/usr/local/bin/keyring", "pkginfo": "/usr/local/bin/pkginfo", "poetry": "/usr/local/bin/poetry", "pyproject-build": "/usr/local/bin/pyproject-build", "python-build": "/usr/local/bin/python-build", "rocm-smi": "/usr/local/bin/rocm-smi", "virtualenv": "/usr/local/bin/virtualenv", "h5delete": "/usr/local/bin/h5delete", "scanpy": "/usr/local/bin/scanpy", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch", "hwloc-ps": "/usr/local/bin/hwloc-ps", "lstopo": "/usr/local/bin/lstopo", "lstopo-no-graphics": "/usr/local/bin/lstopo-no-graphics", "doesitcache": "/usr/local/bin/doesitcache", "aec": "/usr/local/bin/aec", "pycc": "/usr/local/bin/pycc", "hb-info": "/usr/local/bin/hb-info", "numba": "/usr/local/bin/numba", "natsort": "/usr/local/bin/natsort", "tjbench": "/usr/local/bin/tjbench", "jsonschema": "/usr/local/bin/jsonschema", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/checkatlas.
singularity registry hpc automated addition for checkatlas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/checkatlas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/checkatlas:0.4.17--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/checkatlas/0.4.17--pyhdfd78af_0
$ module help quay.io/biocontainers/checkatlas/0.4.17--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### checkatlas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### checkatlas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### checkatlas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### checkatlas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### checkatlas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### checkatlas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### checkatlas

```bash
$ singularity exec <container> /usr/local/bin/checkatlas
$ podman run --it --rm --entrypoint /usr/local/bin/checkatlas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkatlas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkatlas-workflow

```bash
$ singularity exec <container> /usr/local/bin/checkatlas-workflow
$ podman run --it --rm --entrypoint /usr/local/bin/checkatlas-workflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkatlas-workflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dul-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/dul-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/dul-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dul-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dul-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/dul-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/dul-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dul-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dulwich

```bash
$ singularity exec <container> /usr/local/bin/dulwich
$ podman run --it --rm --entrypoint /usr/local/bin/dulwich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dulwich   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkginfo

```bash
$ singularity exec <container> /usr/local/bin/pkginfo
$ podman run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poetry

```bash
$ singularity exec <container> /usr/local/bin/poetry
$ podman run --it --rm --entrypoint /usr/local/bin/poetry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poetry   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyproject-build

```bash
$ singularity exec <container> /usr/local/bin/pyproject-build
$ podman run --it --rm --entrypoint /usr/local/bin/pyproject-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyproject-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-build

```bash
$ singularity exec <container> /usr/local/bin/python-build
$ podman run --it --rm --entrypoint /usr/local/bin/python-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rocm-smi

```bash
$ singularity exec <container> /usr/local/bin/rocm-smi
$ podman run --it --rm --entrypoint /usr/local/bin/rocm-smi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rocm-smi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv

```bash
$ singularity exec <container> /usr/local/bin/virtualenv
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### lstopo-no-graphics

```bash
$ singularity exec <container> /usr/local/bin/lstopo-no-graphics
$ podman run --it --rm --entrypoint /usr/local/bin/lstopo-no-graphics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lstopo-no-graphics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aec

```bash
$ singularity exec <container> /usr/local/bin/aec
$ podman run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-cleanup-sockets

```bash
$ singularity exec <container> /usr/local/bin/dbus-cleanup-sockets
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
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