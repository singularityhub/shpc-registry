---
layout: container
name:  "quay.io/biocontainers/nanocomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanocomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanocomp/container.yaml"
updated_at: "2025-02-24 02:58:23.344604"
latest: "1.24.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nanocomp"
aliases:
 - "NanoComp"
 - "NanoPlot"
 - "orca-server"
 - "pauvre"
 - "flask"
 - "compile-et.pl"
 - "prerr.properties"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
versions:
 - "1.9.2--py_1"
 - "1.20.0--pyhdfd78af_0"
 - "1.19.3--pyhdfd78af_0"
 - "1.18.0--pyhdfd78af_0"
 - "1.17.0--pyhdfd78af_0"
 - "1.16.1--pyhdfd78af_0"
 - "1.21.0--pyhdfd78af_0"
 - "1.22.0--pyhdfd78af_0"
 - "1.21.2--pyhdfd78af_0"
 - "1.23.1--pyhdfd78af_0"
 - "1.24.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for nanocomp"
config: {"url": "https://biocontainers.pro/tools/nanocomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanocomp", "latest": {"1.24.2--pyhdfd78af_0": "sha256:0276ea4e9e0f12e75b4d40fd3d8b84163a5bd1e54d89960f6ff36140c27e2966"}, "tags": {"1.9.2--py_1": "sha256:2fde57e4bdb7ea7104a036d29753609a3d33aa9950f7eadcc2856ecfbf36f1cc", "1.20.0--pyhdfd78af_0": "sha256:111efe8d500ff547c56d1fe15fc99b689ec47f8329f18a6cf80e06cdfe91b00a", "1.19.3--pyhdfd78af_0": "sha256:1263e702b2974903f99bb3066a1cd2c1ecc3e7508706e353d408a84623e107eb", "1.18.0--pyhdfd78af_0": "sha256:3d7dd3177b55f4dd22c8c2ea2dcb19600d1efea338cb7db231e74ab0516df166", "1.17.0--pyhdfd78af_0": "sha256:f40e0e2b8ad59d72bae8c6b0d4d4776650a7def19ad561bab30490badea1177c", "1.16.1--pyhdfd78af_0": "sha256:d9c51bbfbacd0a09d9e8d66437bb2c0e2525c6e5a5994c53aa97e51344febf32", "1.21.0--pyhdfd78af_0": "sha256:b63e2d6bc17797cdae4361fc25c01533f4418857c44491f112bf18cddb6f71f0", "1.22.0--pyhdfd78af_0": "sha256:0c6a1620a8a790eec4f0ff45429525bc3bfd5012d30235be99e88ef70f3098b9", "1.21.2--pyhdfd78af_0": "sha256:423c260522c1e887d0455508586fd6c060ab2b9f44c772f0d732514110ff2921", "1.23.1--pyhdfd78af_0": "sha256:895808009363967dcf9682329883619550bba9080b2ec2321634e64b275f93e2", "1.24.2--pyhdfd78af_0": "sha256:0276ea4e9e0f12e75b4d40fd3d8b84163a5bd1e54d89960f6ff36140c27e2966"}, "docker": "quay.io/biocontainers/nanocomp", "aliases": {"NanoComp": "/usr/local/bin/NanoComp", "NanoPlot": "/usr/local/bin/NanoPlot", "orca-server": "/usr/local/bin/orca-server", "pauvre": "/usr/local/bin/pauvre", "flask": "/usr/local/bin/flask", "compile-et.pl": "/usr/local/bin/compile-et.pl", "prerr.properties": "/usr/local/bin/prerr.properties", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanocomp.
shpc-registry automated BioContainers addition for nanocomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanocomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanocomp:1.24.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanocomp/1.24.2--pyhdfd78af_0
$ module help quay.io/biocontainers/nanocomp/1.24.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanocomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanocomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanocomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanocomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanocomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanocomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoComp

```bash
$ singularity exec <container> /usr/local/bin/NanoComp
$ podman run --it --rm --entrypoint /usr/local/bin/NanoComp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoComp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NanoPlot

```bash
$ singularity exec <container> /usr/local/bin/NanoPlot
$ podman run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orca-server

```bash
$ singularity exec <container> /usr/local/bin/orca-server
$ podman run --it --rm --entrypoint /usr/local/bin/orca-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orca-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pauvre

```bash
$ singularity exec <container> /usr/local/bin/pauvre
$ podman run --it --rm --entrypoint /usr/local/bin/pauvre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pauvre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerr.properties

```bash
$ singularity exec <container> /usr/local/bin/prerr.properties
$ podman run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlpreview

```bash
$ singularity exec <container> /usr/local/bin/qmlpreview
$ podman run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvkgen

```bash
$ singularity exec <container> /usr/local/bin/qvkgen
$ podman run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
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