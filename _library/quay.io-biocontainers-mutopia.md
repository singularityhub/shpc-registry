---
layout: container
name:  "quay.io/biocontainers/mutopia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mutopia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mutopia/container.yaml"
updated_at: "2026-06-17 07:49:52.171899"
latest: "1.0.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mutopia"
aliases:
 - "bigWigAverageOverBed"
 - "gtensor"
 - "luigi"
 - "luigi-deps"
 - "luigi-deps-tree"
 - "luigi-grep"
 - "luigid"
 - "mutopia-sbs"
 - "optuna"
 - "topo-model"
 - "gff2gff"
 - "roh-viz"
 - "vrfs-variances"
 - "nc3tonc4"
 - "nc4tonc3"
 - "ncinfo"
 - "alembic"
 - "mako-render"
 - "h2benchmark"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
 - "rst2pseudoxml"
 - "rst2s5"
 - "rst2xetex"
 - "rst2xml"
 - "checksum-profile"
 - "gff2gff.py"
 - "ref-cache"
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
versions:
 - "1.0.4--pyhdfd78af_0"
 - "1.0.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mutopia"
config: {"url": "https://biocontainers.pro/tools/mutopia", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mutopia", "latest": {"1.0.8--pyhdfd78af_0": "sha256:b75428744e91bfa4447c693bc1451132079386aea2b894d972b3d1c4672e9dd4"}, "tags": {"1.0.4--pyhdfd78af_0": "sha256:c63e342be22076669ee13ba590dfc407bfcd49eb4dd18e567a0606121d507509", "1.0.8--pyhdfd78af_0": "sha256:b75428744e91bfa4447c693bc1451132079386aea2b894d972b3d1c4672e9dd4"}, "docker": "quay.io/biocontainers/mutopia", "aliases": {"bigWigAverageOverBed": "/usr/local/bin/bigWigAverageOverBed", "gtensor": "/usr/local/bin/gtensor", "luigi": "/usr/local/bin/luigi", "luigi-deps": "/usr/local/bin/luigi-deps", "luigi-deps-tree": "/usr/local/bin/luigi-deps-tree", "luigi-grep": "/usr/local/bin/luigi-grep", "luigid": "/usr/local/bin/luigid", "mutopia-sbs": "/usr/local/bin/mutopia-sbs", "optuna": "/usr/local/bin/optuna", "topo-model": "/usr/local/bin/topo-model", "gff2gff": "/usr/local/bin/gff2gff", "roh-viz": "/usr/local/bin/roh-viz", "vrfs-variances": "/usr/local/bin/vrfs-variances", "nc3tonc4": "/usr/local/bin/nc3tonc4", "nc4tonc3": "/usr/local/bin/nc4tonc3", "ncinfo": "/usr/local/bin/ncinfo", "alembic": "/usr/local/bin/alembic", "mako-render": "/usr/local/bin/mako-render", "h2benchmark": "/usr/local/bin/h2benchmark", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt", "rst2pseudoxml": "/usr/local/bin/rst2pseudoxml", "rst2s5": "/usr/local/bin/rst2s5", "rst2xetex": "/usr/local/bin/rst2xetex", "rst2xml": "/usr/local/bin/rst2xml", "checksum-profile": "/usr/local/bin/checksum-profile", "gff2gff.py": "/usr/local/bin/gff2gff.py", "ref-cache": "/usr/local/bin/ref-cache", "zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mutopia.
singularity registry hpc automated addition for mutopia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mutopia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mutopia:1.0.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mutopia/1.0.8--pyhdfd78af_0
$ module help quay.io/biocontainers/mutopia/1.0.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mutopia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mutopia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mutopia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mutopia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mutopia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mutopia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigWigAverageOverBed

```bash
$ singularity exec <container> /usr/local/bin/bigWigAverageOverBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtensor

```bash
$ singularity exec <container> /usr/local/bin/gtensor
$ podman run --it --rm --entrypoint /usr/local/bin/gtensor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtensor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi

```bash
$ singularity exec <container> /usr/local/bin/luigi
$ podman run --it --rm --entrypoint /usr/local/bin/luigi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi-deps

```bash
$ singularity exec <container> /usr/local/bin/luigi-deps
$ podman run --it --rm --entrypoint /usr/local/bin/luigi-deps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi-deps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi-deps-tree

```bash
$ singularity exec <container> /usr/local/bin/luigi-deps-tree
$ podman run --it --rm --entrypoint /usr/local/bin/luigi-deps-tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi-deps-tree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigi-grep

```bash
$ singularity exec <container> /usr/local/bin/luigi-grep
$ podman run --it --rm --entrypoint /usr/local/bin/luigi-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigi-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### luigid

```bash
$ singularity exec <container> /usr/local/bin/luigid
$ podman run --it --rm --entrypoint /usr/local/bin/luigid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/luigid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutopia-sbs

```bash
$ singularity exec <container> /usr/local/bin/mutopia-sbs
$ podman run --it --rm --entrypoint /usr/local/bin/mutopia-sbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutopia-sbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optuna

```bash
$ singularity exec <container> /usr/local/bin/optuna
$ podman run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### topo-model

```bash
$ singularity exec <container> /usr/local/bin/topo-model
$ podman run --it --rm --entrypoint /usr/local/bin/topo-model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/topo-model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff

```bash
$ singularity exec <container> /usr/local/bin/gff2gff
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roh-viz

```bash
$ singularity exec <container> /usr/local/bin/roh-viz
$ podman run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vrfs-variances

```bash
$ singularity exec <container> /usr/local/bin/vrfs-variances
$ podman run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc3tonc4

```bash
$ singularity exec <container> /usr/local/bin/nc3tonc4
$ podman run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc4tonc3

```bash
$ singularity exec <container> /usr/local/bin/nc4tonc3
$ podman run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncinfo

```bash
$ singularity exec <container> /usr/local/bin/ncinfo
$ podman run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alembic

```bash
$ singularity exec <container> /usr/local/bin/alembic
$ podman run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex

```bash
$ singularity exec <container> /usr/local/bin/rst2latex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man

```bash
$ singularity exec <container> /usr/local/bin/rst2man
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt

```bash
$ singularity exec <container> /usr/local/bin/rst2odt
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5

```bash
$ singularity exec <container> /usr/local/bin/rst2s5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml

```bash
$ singularity exec <container> /usr/local/bin/rst2xml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipcmp

```bash
$ singularity exec <container> /usr/local/bin/zipcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipmerge

```bash
$ singularity exec <container> /usr/local/bin/zipmerge
$ podman run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ziptool

```bash
$ singularity exec <container> /usr/local/bin/ziptool
$ podman run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
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