---
layout: container
name:  "quay.io/biocontainers/strainy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strainy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strainy/container.yaml"
updated_at: "2025-05-12 04:03:39.390190"
latest: "1.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/strainy"
aliases:
 - "community"
 - "gfapy-convert"
 - "gfapy-mergelinear"
 - "gfapy-renumber"
 - "gfapy-validate"
 - "strainy"
 - "flye-modules"
 - "flye-samtools"
 - "flye"
 - "flye-minimap2"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "annot-tsv"
 - "gff2gff.py"
 - "diffimg"
 - "delaunay"
 - "gts-config"
 - "gts2dxf"
 - "gts2oogl"
 - "gts2stl"
 - "gtscheck"
 - "gtscompare"
 - "gtstemplate"
 - "stl2gts"
 - "transform"
 - "guess-ploidy.py"
 - "plot-roh.py"
versions:
 - "1.1--pyh7e72e81_0"
 - "1.1--pyh7e72e81_1"
 - "1.2--pyhdfd78af_1"
description: "singularity registry hpc automated addition for strainy"
config: {"url": "https://biocontainers.pro/tools/strainy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for strainy", "latest": {"1.2--pyhdfd78af_1": "sha256:1e3880dfa9b573b6386f0b5e6d7b188c505c64eafc9dcf85c43ebd6b4a9d781e"}, "tags": {"1.1--pyh7e72e81_0": "sha256:425f31fa4a5ea63b2f84c76d4a02cb84fa2729db1d0435057d0e9a2495aff5d6", "1.1--pyh7e72e81_1": "sha256:33443a8c754fac6b7dcccdb52d3f3fcd14ade96b2508b96697ec91332d967b76", "1.2--pyhdfd78af_1": "sha256:1e3880dfa9b573b6386f0b5e6d7b188c505c64eafc9dcf85c43ebd6b4a9d781e"}, "docker": "quay.io/biocontainers/strainy", "aliases": {"community": "/usr/local/bin/community", "gfapy-convert": "/usr/local/bin/gfapy-convert", "gfapy-mergelinear": "/usr/local/bin/gfapy-mergelinear", "gfapy-renumber": "/usr/local/bin/gfapy-renumber", "gfapy-validate": "/usr/local/bin/gfapy-validate", "strainy": "/usr/local/bin/strainy", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "flye": "/usr/local/bin/flye", "flye-minimap2": "/usr/local/bin/flye-minimap2", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "annot-tsv": "/usr/local/bin/annot-tsv", "gff2gff.py": "/usr/local/bin/gff2gff.py", "diffimg": "/usr/local/bin/diffimg", "delaunay": "/usr/local/bin/delaunay", "gts-config": "/usr/local/bin/gts-config", "gts2dxf": "/usr/local/bin/gts2dxf", "gts2oogl": "/usr/local/bin/gts2oogl", "gts2stl": "/usr/local/bin/gts2stl", "gtscheck": "/usr/local/bin/gtscheck", "gtscompare": "/usr/local/bin/gtscompare", "gtstemplate": "/usr/local/bin/gtstemplate", "stl2gts": "/usr/local/bin/stl2gts", "transform": "/usr/local/bin/transform", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strainy.
singularity registry hpc automated addition for strainy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strainy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strainy:1.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strainy/1.2--pyhdfd78af_1
$ module help quay.io/biocontainers/strainy/1.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strainy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strainy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strainy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strainy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strainy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strainy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### community

```bash
$ singularity exec <container> /usr/local/bin/community
$ podman run --it --rm --entrypoint /usr/local/bin/community   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/community   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-convert

```bash
$ singularity exec <container> /usr/local/bin/gfapy-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-mergelinear

```bash
$ singularity exec <container> /usr/local/bin/gfapy-mergelinear
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-renumber

```bash
$ singularity exec <container> /usr/local/bin/gfapy-renumber
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-validate

```bash
$ singularity exec <container> /usr/local/bin/gfapy-validate
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strainy

```bash
$ singularity exec <container> /usr/local/bin/strainy
$ podman run --it --rm --entrypoint /usr/local/bin/strainy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strainy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye

```bash
$ singularity exec <container> /usr/local/bin/flye
$ podman run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-minimap2

```bash
$ singularity exec <container> /usr/local/bin/flye-minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diffimg

```bash
$ singularity exec <container> /usr/local/bin/diffimg
$ podman run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delaunay

```bash
$ singularity exec <container> /usr/local/bin/delaunay
$ podman run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts-config

```bash
$ singularity exec <container> /usr/local/bin/gts-config
$ podman run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2dxf

```bash
$ singularity exec <container> /usr/local/bin/gts2dxf
$ podman run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2oogl

```bash
$ singularity exec <container> /usr/local/bin/gts2oogl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2stl

```bash
$ singularity exec <container> /usr/local/bin/gts2stl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscheck

```bash
$ singularity exec <container> /usr/local/bin/gtscheck
$ podman run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscompare

```bash
$ singularity exec <container> /usr/local/bin/gtscompare
$ podman run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtstemplate

```bash
$ singularity exec <container> /usr/local/bin/gtstemplate
$ podman run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stl2gts

```bash
$ singularity exec <container> /usr/local/bin/stl2gts
$ podman run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transform

```bash
$ singularity exec <container> /usr/local/bin/transform
$ podman run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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