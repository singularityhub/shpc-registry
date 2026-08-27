---
layout: container
name:  "quay.io/biocontainers/orthosynassign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orthosynassign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orthosynassign/container.yaml"
updated_at: "2026-08-27 12:42:10.515759"
latest: "1.3.1--py313h9a1e870_0"
container_url: "https://biocontainers.pro/tools/orthosynassign"
aliases:
 - "orthosynassign"
 - "orthosynassign-vis"
 - "pgv-blast"
 - "pgv-download"
 - "pgv-gui"
 - "pgv-mmseqs"
 - "pgv-mummer"
 - "pgv-pmauve"
 - "fc-genconf"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "numpy-config"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
versions:
 - "1.2.0--py314hfa8f182_0"
 - "1.2.0--py310hce5ca29_1"
 - "1.3.1--py313h9a1e870_0"
description: "singularity registry hpc automated addition for orthosynassign"
config: {"url": "https://biocontainers.pro/tools/orthosynassign", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for orthosynassign", "latest": {"1.3.1--py313h9a1e870_0": "sha256:b7f05de9aeff0200d7e5bcaeaecb9cf73831cc35023ef0c1dee9bee87a1fc2e0"}, "tags": {"1.2.0--py314hfa8f182_0": "sha256:602ebea93470852c08cb7056173b48da23ccda5f3ea1c08eb076709ca32623f8", "1.2.0--py310hce5ca29_1": "sha256:4d8d01c5c9b35d667b68dc6d85793da68d9961d88faa8838c34e0ec98448575e", "1.3.1--py313h9a1e870_0": "sha256:b7f05de9aeff0200d7e5bcaeaecb9cf73831cc35023ef0c1dee9bee87a1fc2e0"}, "docker": "quay.io/biocontainers/orthosynassign", "aliases": {"orthosynassign": "/usr/local/bin/orthosynassign", "orthosynassign-vis": "/usr/local/bin/orthosynassign-vis", "pgv-blast": "/usr/local/bin/pgv-blast", "pgv-download": "/usr/local/bin/pgv-download", "pgv-gui": "/usr/local/bin/pgv-gui", "pgv-mmseqs": "/usr/local/bin/pgv-mmseqs", "pgv-mummer": "/usr/local/bin/pgv-mummer", "pgv-pmauve": "/usr/local/bin/pgv-pmauve", "fc-genconf": "/usr/local/bin/fc-genconf", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "numpy-config": "/usr/local/bin/numpy-config", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orthosynassign.
singularity registry hpc automated addition for orthosynassign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orthosynassign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orthosynassign:1.3.1--py313h9a1e870_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orthosynassign/1.3.1--py313h9a1e870_0
$ module help quay.io/biocontainers/orthosynassign/1.3.1--py313h9a1e870_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orthosynassign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orthosynassign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orthosynassign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orthosynassign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orthosynassign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orthosynassign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### orthosynassign

```bash
$ singularity exec <container> /usr/local/bin/orthosynassign
$ podman run --it --rm --entrypoint /usr/local/bin/orthosynassign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthosynassign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthosynassign-vis

```bash
$ singularity exec <container> /usr/local/bin/orthosynassign-vis
$ podman run --it --rm --entrypoint /usr/local/bin/orthosynassign-vis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthosynassign-vis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-blast

```bash
$ singularity exec <container> /usr/local/bin/pgv-blast
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-download

```bash
$ singularity exec <container> /usr/local/bin/pgv-download
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-gui

```bash
$ singularity exec <container> /usr/local/bin/pgv-gui
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-mmseqs

```bash
$ singularity exec <container> /usr/local/bin/pgv-mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-mummer

```bash
$ singularity exec <container> /usr/local/bin/pgv-mummer
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-pmauve

```bash
$ singularity exec <container> /usr/local/bin/pgv-pmauve
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-pmauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-pmauve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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