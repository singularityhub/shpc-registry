---
layout: container
name:  "quay.io/biocontainers/instanexus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/instanexus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/instanexus/container.yaml"
updated_at: "2026-06-27 05:59:55.579705"
latest: "0.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/instanexus"
aliases:
 - "hatch"
 - "hatchling"
 - "httpx2"
 - "instanexus"
 - "instanexus-optimize"
 - "trove-classifiers"
 - "userpath"
 - "uv"
 - "uvx"
 - "gawk-5.4.0"
 - "distro"
 - "fc-genconf"
 - "keyring"
 - "virtualenv"
 - "idna"
 - "plotly_get_chrome"
 - "clustalo"
 - "aria2c"
 - "mmseqs"
 - "hb-raster"
 - "hb-vector"
 - "gawkbug"
 - "gawk"
 - "awk"
 - "markdown-it"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
versions:
 - "0.2.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for instanexus"
config: {"url": "https://biocontainers.pro/tools/instanexus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for instanexus", "latest": {"0.2.1--pyhdfd78af_0": "sha256:69adc0fecd6b74a754cd4799039ed516ad2ef9676c5f8575efa2d9abf5944f6c"}, "tags": {"0.2.1--pyhdfd78af_0": "sha256:69adc0fecd6b74a754cd4799039ed516ad2ef9676c5f8575efa2d9abf5944f6c"}, "docker": "quay.io/biocontainers/instanexus", "aliases": {"hatch": "/usr/local/bin/hatch", "hatchling": "/usr/local/bin/hatchling", "httpx2": "/usr/local/bin/httpx2", "instanexus": "/usr/local/bin/instanexus", "instanexus-optimize": "/usr/local/bin/instanexus-optimize", "trove-classifiers": "/usr/local/bin/trove-classifiers", "userpath": "/usr/local/bin/userpath", "uv": "/usr/local/bin/uv", "uvx": "/usr/local/bin/uvx", "gawk-5.4.0": "/usr/local/bin/gawk-5.4.0", "distro": "/usr/local/bin/distro", "fc-genconf": "/usr/local/bin/fc-genconf", "keyring": "/usr/local/bin/keyring", "virtualenv": "/usr/local/bin/virtualenv", "idna": "/usr/local/bin/idna", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "clustalo": "/usr/local/bin/clustalo", "aria2c": "/usr/local/bin/aria2c", "mmseqs": "/usr/local/bin/mmseqs", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "gawkbug": "/usr/local/bin/gawkbug", "gawk": "/usr/local/bin/gawk", "awk": "/usr/local/bin/awk", "markdown-it": "/usr/local/bin/markdown-it", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/instanexus.
singularity registry hpc automated addition for instanexus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/instanexus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/instanexus:0.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/instanexus/0.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/instanexus/0.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### instanexus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### instanexus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### instanexus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### instanexus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### instanexus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### instanexus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hatch

```bash
$ singularity exec <container> /usr/local/bin/hatch
$ podman run --it --rm --entrypoint /usr/local/bin/hatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hatchling

```bash
$ singularity exec <container> /usr/local/bin/hatchling
$ podman run --it --rm --entrypoint /usr/local/bin/hatchling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hatchling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx2

```bash
$ singularity exec <container> /usr/local/bin/httpx2
$ podman run --it --rm --entrypoint /usr/local/bin/httpx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### instanexus

```bash
$ singularity exec <container> /usr/local/bin/instanexus
$ podman run --it --rm --entrypoint /usr/local/bin/instanexus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/instanexus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### instanexus-optimize

```bash
$ singularity exec <container> /usr/local/bin/instanexus-optimize
$ podman run --it --rm --entrypoint /usr/local/bin/instanexus-optimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/instanexus-optimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trove-classifiers

```bash
$ singularity exec <container> /usr/local/bin/trove-classifiers
$ podman run --it --rm --entrypoint /usr/local/bin/trove-classifiers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trove-classifiers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### userpath

```bash
$ singularity exec <container> /usr/local/bin/userpath
$ podman run --it --rm --entrypoint /usr/local/bin/userpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/userpath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uv

```bash
$ singularity exec <container> /usr/local/bin/uv
$ podman run --it --rm --entrypoint /usr/local/bin/uv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvx

```bash
$ singularity exec <container> /usr/local/bin/uvx
$ podman run --it --rm --entrypoint /usr/local/bin/uvx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distro

```bash
$ singularity exec <container> /usr/local/bin/distro
$ podman run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv

```bash
$ singularity exec <container> /usr/local/bin/virtualenv
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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