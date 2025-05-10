---
layout: container
name:  "quay.io/biocontainers/cell2cell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cell2cell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cell2cell/container.yaml"
updated_at: "2025-05-10 03:16:55.447365"
latest: "0.7.4--py310h9948957_3"
container_url: "https://biocontainers.pro/tools/cell2cell"
aliases:
 - "gseapy"
 - "runxlrd.py"
 - "h5tools_test_utils"
 - "scanpy"
 - "h5fuse.sh"
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
 - "h5delete"
 - "numba"
 - "natsort"
 - "f2py3.8"
 - "tqdm"
 - "fonttools"
 - "pyftmerge"
versions:
 - "0.7.4--py38h4ac6f70_0"
 - "0.7.4--py39h4ac6f70_1"
 - "0.7.4--py39h9948957_2"
 - "0.7.4--py310h9948957_3"
description: "singularity registry hpc automated addition for cell2cell"
config: {"url": "https://biocontainers.pro/tools/cell2cell", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cell2cell", "latest": {"0.7.4--py310h9948957_3": "sha256:6cbd96d993cf8a015d7263938ab2292f5f7cac90fcd474160c2dbcbabdc6a379"}, "tags": {"0.7.4--py38h4ac6f70_0": "sha256:34cc506e87d9d9ba29917b4f1fadb40ef0c34c29cc9db56b21db48ca914b2b44", "0.7.4--py39h4ac6f70_1": "sha256:6a35ff033f9c70e51469e32c86d45db7bb5390905662d8cc86b0b0b81c6bca6e", "0.7.4--py39h9948957_2": "sha256:76211c9dd801b2cfee75d898706f071b44ab1d765a98aaf4c8be01cf86a7f75e", "0.7.4--py310h9948957_3": "sha256:6cbd96d993cf8a015d7263938ab2292f5f7cac90fcd474160c2dbcbabdc6a379"}, "docker": "quay.io/biocontainers/cell2cell", "aliases": {"gseapy": "/usr/local/bin/gseapy", "runxlrd.py": "/usr/local/bin/runxlrd.py", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "scanpy": "/usr/local/bin/scanpy", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology", "hwloc-info": "/usr/local/bin/hwloc-info", "hwloc-ls": "/usr/local/bin/hwloc-ls", "hwloc-patch": "/usr/local/bin/hwloc-patch", "hwloc-ps": "/usr/local/bin/hwloc-ps", "lstopo": "/usr/local/bin/lstopo", "lstopo-no-graphics": "/usr/local/bin/lstopo-no-graphics", "h5delete": "/usr/local/bin/h5delete", "numba": "/usr/local/bin/numba", "natsort": "/usr/local/bin/natsort", "f2py3.8": "/usr/local/bin/f2py3.8", "tqdm": "/usr/local/bin/tqdm", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cell2cell.
singularity registry hpc automated addition for cell2cell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cell2cell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cell2cell:0.7.4--py310h9948957_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cell2cell/0.7.4--py310h9948957_3
$ module help quay.io/biocontainers/cell2cell/0.7.4--py310h9948957_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cell2cell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cell2cell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cell2cell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cell2cell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cell2cell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cell2cell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gseapy

```bash
$ singularity exec <container> /usr/local/bin/gseapy
$ podman run --it --rm --entrypoint /usr/local/bin/gseapy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gseapy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runxlrd.py

```bash
$ singularity exec <container> /usr/local/bin/runxlrd.py
$ podman run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
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