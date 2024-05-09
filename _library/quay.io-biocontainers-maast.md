---
layout: container
name:  "quay.io/biocontainers/maast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/maast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/maast/container.yaml"
updated_at: "2024-05-09 02:46:35.537276"
latest: "1.0.8--py310hc2b1e32_0"
container_url: "https://biocontainers.pro/tools/maast"
aliases:
 - "lbunzip2"
 - "lbzcat"
 - "lbzip2"
 - "maast"
 - "delta2vcf"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "mash"
 - "FastTreeMP"
 - "FastTree"
 - "fasttree"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
 - "mummerplot"
 - "nucmer"
 - "promer"
 - "repeat-match"
 - "show-aligns"
 - "show-coords"
 - "show-diff"
 - "show-snps"
 - "show-tiling"
 - "pigz"
 - "unpigz"
versions:
 - "1.0.7--py36hffcf100_0"
 - "1.0.7--py38he9326dd_1"
 - "1.0.8--py310hc2b1e32_0"
 - "1.0.8--py38he9326dd_0"
description: "singularity registry hpc automated addition for maast"
config: {"url": "https://biocontainers.pro/tools/maast", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for maast", "latest": {"1.0.8--py310hc2b1e32_0": "sha256:49e502566f444a484238346b9113e51ec0837714869484b9cb6386b052518d80"}, "tags": {"1.0.7--py36hffcf100_0": "sha256:e3b55ff0d4d2ee3b2192bcb1ba3a3d020c52d0826ecfca1509ef5a6a3dddff33", "1.0.7--py38he9326dd_1": "sha256:ed3ecb3074213800c0e6edada799d18246e204c063890d313c57ff902718ff1f", "1.0.8--py310hc2b1e32_0": "sha256:49e502566f444a484238346b9113e51ec0837714869484b9cb6386b052518d80", "1.0.8--py38he9326dd_0": "sha256:c9e4f21e024218f8c11de47cd886944b52f9163db23f4cbec82702b49b997a8f"}, "docker": "quay.io/biocontainers/maast", "aliases": {"lbunzip2": "/usr/local/bin/lbunzip2", "lbzcat": "/usr/local/bin/lbzcat", "lbzip2": "/usr/local/bin/lbzip2", "maast": "/usr/local/bin/maast", "delta2vcf": "/usr/local/bin/delta2vcf", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot", "nucmer": "/usr/local/bin/nucmer", "promer": "/usr/local/bin/promer", "repeat-match": "/usr/local/bin/repeat-match", "show-aligns": "/usr/local/bin/show-aligns", "show-coords": "/usr/local/bin/show-coords", "show-diff": "/usr/local/bin/show-diff", "show-snps": "/usr/local/bin/show-snps", "show-tiling": "/usr/local/bin/show-tiling", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/maast.
singularity registry hpc automated addition for maast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maast:1.0.8--py310hc2b1e32_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maast/1.0.8--py310hc2b1e32_0
$ module help quay.io/biocontainers/maast/1.0.8--py310hc2b1e32_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lbunzip2

```bash
$ singularity exec <container> /usr/local/bin/lbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/lbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lbzcat

```bash
$ singularity exec <container> /usr/local/bin/lbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lbzip2

```bash
$ singularity exec <container> /usr/local/bin/lbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/lbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maast

```bash
$ singularity exec <container> /usr/local/bin/maast
$ podman run --it --rm --entrypoint /usr/local/bin/maast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta2vcf

```bash
$ singularity exec <container> /usr/local/bin/delta2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-c++

```bash
$ singularity exec <container> /usr/local/bin/capnpc-c++
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-capnp

```bash
$ singularity exec <container> /usr/local/bin/capnpc-capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mash

```bash
$ singularity exec <container> /usr/local/bin/mash
$ podman run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /usr/local/bin/mummerplot
$ podman run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucmer

```bash
$ singularity exec <container> /usr/local/bin/nucmer
$ podman run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promer

```bash
$ singularity exec <container> /usr/local/bin/promer
$ podman run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repeat-match

```bash
$ singularity exec <container> /usr/local/bin/repeat-match
$ podman run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-aligns

```bash
$ singularity exec <container> /usr/local/bin/show-aligns
$ podman run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-coords

```bash
$ singularity exec <container> /usr/local/bin/show-coords
$ podman run --it --rm --entrypoint /usr/local/bin/show-coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-diff

```bash
$ singularity exec <container> /usr/local/bin/show-diff
$ podman run --it --rm --entrypoint /usr/local/bin/show-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-snps

```bash
$ singularity exec <container> /usr/local/bin/show-snps
$ podman run --it --rm --entrypoint /usr/local/bin/show-snps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-snps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-tiling

```bash
$ singularity exec <container> /usr/local/bin/show-tiling
$ podman run --it --rm --entrypoint /usr/local/bin/show-tiling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-tiling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
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