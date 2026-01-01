---
layout: container
name:  "quay.io/biocontainers/obitools4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/obitools4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/obitools4/container.yaml"
updated_at: "2026-01-01 04:23:00.903695"
latest: "4.4.0--h6e5cb0d_0"
container_url: "https://biocontainers.pro/tools/obitools4"
aliases:
 - "obiannotate"
 - "obiclean"
 - "obicleandb"
 - "obicomplement"
 - "obiconsensus"
 - "obiconvert"
 - "obicount"
 - "obicsv"
 - "obidemerge"
 - "obidistribute"
 - "obigrep"
 - "obijoin"
 - "obikmermatch"
 - "obikmersimcount"
 - "obilandmark"
 - "obimatrix"
 - "obimicrosat"
 - "obimultiplex"
 - "obipairing"
 - "obipcr"
 - "obireffamidx"
 - "obirefidx"
 - "obiscript"
 - "obisplit"
 - "obisummary"
 - "obitag"
 - "obitagpcr"
 - "obitaxonomy"
 - "obiuniq"
versions:
 - "4.4.0--h6e5cb0d_0"
description: "singularity registry hpc automated addition for obitools4"
config: {"url": "https://biocontainers.pro/tools/obitools4", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for obitools4", "latest": {"4.4.0--h6e5cb0d_0": "sha256:d5eba1ae26193ac84eb53db23d1b5cd495a633b00ff3f4405d399e860ea3159a"}, "tags": {"4.4.0--h6e5cb0d_0": "sha256:d5eba1ae26193ac84eb53db23d1b5cd495a633b00ff3f4405d399e860ea3159a"}, "docker": "quay.io/biocontainers/obitools4", "aliases": {"obiannotate": "/usr/local/bin/obiannotate", "obiclean": "/usr/local/bin/obiclean", "obicleandb": "/usr/local/bin/obicleandb", "obicomplement": "/usr/local/bin/obicomplement", "obiconsensus": "/usr/local/bin/obiconsensus", "obiconvert": "/usr/local/bin/obiconvert", "obicount": "/usr/local/bin/obicount", "obicsv": "/usr/local/bin/obicsv", "obidemerge": "/usr/local/bin/obidemerge", "obidistribute": "/usr/local/bin/obidistribute", "obigrep": "/usr/local/bin/obigrep", "obijoin": "/usr/local/bin/obijoin", "obikmermatch": "/usr/local/bin/obikmermatch", "obikmersimcount": "/usr/local/bin/obikmersimcount", "obilandmark": "/usr/local/bin/obilandmark", "obimatrix": "/usr/local/bin/obimatrix", "obimicrosat": "/usr/local/bin/obimicrosat", "obimultiplex": "/usr/local/bin/obimultiplex", "obipairing": "/usr/local/bin/obipairing", "obipcr": "/usr/local/bin/obipcr", "obireffamidx": "/usr/local/bin/obireffamidx", "obirefidx": "/usr/local/bin/obirefidx", "obiscript": "/usr/local/bin/obiscript", "obisplit": "/usr/local/bin/obisplit", "obisummary": "/usr/local/bin/obisummary", "obitag": "/usr/local/bin/obitag", "obitagpcr": "/usr/local/bin/obitagpcr", "obitaxonomy": "/usr/local/bin/obitaxonomy", "obiuniq": "/usr/local/bin/obiuniq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/obitools4.
singularity registry hpc automated addition for obitools4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/obitools4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/obitools4:4.4.0--h6e5cb0d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/obitools4/4.4.0--h6e5cb0d_0
$ module help quay.io/biocontainers/obitools4/4.4.0--h6e5cb0d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### obitools4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### obitools4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### obitools4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### obitools4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### obitools4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### obitools4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### obiannotate

```bash
$ singularity exec <container> /usr/local/bin/obiannotate
$ podman run --it --rm --entrypoint /usr/local/bin/obiannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiclean

```bash
$ singularity exec <container> /usr/local/bin/obiclean
$ podman run --it --rm --entrypoint /usr/local/bin/obiclean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiclean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obicleandb

```bash
$ singularity exec <container> /usr/local/bin/obicleandb
$ podman run --it --rm --entrypoint /usr/local/bin/obicleandb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obicleandb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obicomplement

```bash
$ singularity exec <container> /usr/local/bin/obicomplement
$ podman run --it --rm --entrypoint /usr/local/bin/obicomplement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obicomplement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiconsensus

```bash
$ singularity exec <container> /usr/local/bin/obiconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/obiconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiconvert

```bash
$ singularity exec <container> /usr/local/bin/obiconvert
$ podman run --it --rm --entrypoint /usr/local/bin/obiconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obicount

```bash
$ singularity exec <container> /usr/local/bin/obicount
$ podman run --it --rm --entrypoint /usr/local/bin/obicount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obicount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obicsv

```bash
$ singularity exec <container> /usr/local/bin/obicsv
$ podman run --it --rm --entrypoint /usr/local/bin/obicsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obicsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obidemerge

```bash
$ singularity exec <container> /usr/local/bin/obidemerge
$ podman run --it --rm --entrypoint /usr/local/bin/obidemerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obidemerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obidistribute

```bash
$ singularity exec <container> /usr/local/bin/obidistribute
$ podman run --it --rm --entrypoint /usr/local/bin/obidistribute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obidistribute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obigrep

```bash
$ singularity exec <container> /usr/local/bin/obigrep
$ podman run --it --rm --entrypoint /usr/local/bin/obigrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obigrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obijoin

```bash
$ singularity exec <container> /usr/local/bin/obijoin
$ podman run --it --rm --entrypoint /usr/local/bin/obijoin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obijoin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obikmermatch

```bash
$ singularity exec <container> /usr/local/bin/obikmermatch
$ podman run --it --rm --entrypoint /usr/local/bin/obikmermatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obikmermatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obikmersimcount

```bash
$ singularity exec <container> /usr/local/bin/obikmersimcount
$ podman run --it --rm --entrypoint /usr/local/bin/obikmersimcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obikmersimcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obilandmark

```bash
$ singularity exec <container> /usr/local/bin/obilandmark
$ podman run --it --rm --entrypoint /usr/local/bin/obilandmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obilandmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obimatrix

```bash
$ singularity exec <container> /usr/local/bin/obimatrix
$ podman run --it --rm --entrypoint /usr/local/bin/obimatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obimatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obimicrosat

```bash
$ singularity exec <container> /usr/local/bin/obimicrosat
$ podman run --it --rm --entrypoint /usr/local/bin/obimicrosat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obimicrosat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obimultiplex

```bash
$ singularity exec <container> /usr/local/bin/obimultiplex
$ podman run --it --rm --entrypoint /usr/local/bin/obimultiplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obimultiplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obipairing

```bash
$ singularity exec <container> /usr/local/bin/obipairing
$ podman run --it --rm --entrypoint /usr/local/bin/obipairing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obipairing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obipcr

```bash
$ singularity exec <container> /usr/local/bin/obipcr
$ podman run --it --rm --entrypoint /usr/local/bin/obipcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obipcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obireffamidx

```bash
$ singularity exec <container> /usr/local/bin/obireffamidx
$ podman run --it --rm --entrypoint /usr/local/bin/obireffamidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obireffamidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obirefidx

```bash
$ singularity exec <container> /usr/local/bin/obirefidx
$ podman run --it --rm --entrypoint /usr/local/bin/obirefidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obirefidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiscript

```bash
$ singularity exec <container> /usr/local/bin/obiscript
$ podman run --it --rm --entrypoint /usr/local/bin/obiscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obisplit

```bash
$ singularity exec <container> /usr/local/bin/obisplit
$ podman run --it --rm --entrypoint /usr/local/bin/obisplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obisplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obisummary

```bash
$ singularity exec <container> /usr/local/bin/obisummary
$ podman run --it --rm --entrypoint /usr/local/bin/obisummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obisummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obitag

```bash
$ singularity exec <container> /usr/local/bin/obitag
$ podman run --it --rm --entrypoint /usr/local/bin/obitag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obitag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obitagpcr

```bash
$ singularity exec <container> /usr/local/bin/obitagpcr
$ podman run --it --rm --entrypoint /usr/local/bin/obitagpcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obitagpcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obitaxonomy

```bash
$ singularity exec <container> /usr/local/bin/obitaxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/obitaxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obitaxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obiuniq

```bash
$ singularity exec <container> /usr/local/bin/obiuniq
$ podman run --it --rm --entrypoint /usr/local/bin/obiuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obiuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
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