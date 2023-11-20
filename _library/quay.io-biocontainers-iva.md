---
layout: container
name:  "quay.io/biocontainers/iva"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/iva/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/iva/container.yaml"
updated_at: "2023-11-20 02:50:27.322142"
latest: "1.0.11--py_0"
container_url: "https://biocontainers.pro/tools/iva"
aliases:
 - "basqcol"
 - "fetchseq"
 - "iva"
 - "iva_qc"
 - "iva_qc_make_db"
 - "mixreads"
 - "readstats"
 - "simqual"
 - "simread"
 - "smalt"
 - "splitmates"
 - "splitreads"
 - "trunkreads"
 - "kmc"
 - "kmc_dump"
 - "kmc_tools"
 - "fastaq"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "combineMUMs"
 - "delta-filter"
versions:
 - "1.0.9--py_2"
 - "1.0.11--py_0"
description: "shpc-registry automated BioContainers addition for iva"
config: {"url": "https://biocontainers.pro/tools/iva", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for iva", "latest": {"1.0.11--py_0": "sha256:141db6cbbf8882f044139cedf9262dc78ad9d8d3a552835315d1cf780bcf8dee"}, "tags": {"1.0.9--py_2": "sha256:60681684ef330b1cbd291639c91c013ab3ef157840c0f8d978cbc487e2029be2", "1.0.11--py_0": "sha256:141db6cbbf8882f044139cedf9262dc78ad9d8d3a552835315d1cf780bcf8dee"}, "docker": "quay.io/biocontainers/iva", "aliases": {"basqcol": "/usr/local/bin/basqcol", "fetchseq": "/usr/local/bin/fetchseq", "iva": "/usr/local/bin/iva", "iva_qc": "/usr/local/bin/iva_qc", "iva_qc_make_db": "/usr/local/bin/iva_qc_make_db", "mixreads": "/usr/local/bin/mixreads", "readstats": "/usr/local/bin/readstats", "simqual": "/usr/local/bin/simqual", "simread": "/usr/local/bin/simread", "smalt": "/usr/local/bin/smalt", "splitmates": "/usr/local/bin/splitmates", "splitreads": "/usr/local/bin/splitreads", "trunkreads": "/usr/local/bin/trunkreads", "kmc": "/usr/local/bin/kmc", "kmc_dump": "/usr/local/bin/kmc_dump", "kmc_tools": "/usr/local/bin/kmc_tools", "fastaq": "/usr/local/bin/fastaq", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/iva.
shpc-registry automated BioContainers addition for iva
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/iva
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/iva:1.0.11--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/iva/1.0.11--py_0
$ module help quay.io/biocontainers/iva/1.0.11--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### iva-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### iva-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### iva-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### iva-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### iva-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### iva-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### basqcol

```bash
$ singularity exec <container> /usr/local/bin/basqcol
$ podman run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchseq

```bash
$ singularity exec <container> /usr/local/bin/fetchseq
$ podman run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iva

```bash
$ singularity exec <container> /usr/local/bin/iva
$ podman run --it --rm --entrypoint /usr/local/bin/iva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iva_qc

```bash
$ singularity exec <container> /usr/local/bin/iva_qc
$ podman run --it --rm --entrypoint /usr/local/bin/iva_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iva_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iva_qc_make_db

```bash
$ singularity exec <container> /usr/local/bin/iva_qc_make_db
$ podman run --it --rm --entrypoint /usr/local/bin/iva_qc_make_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iva_qc_make_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mixreads

```bash
$ singularity exec <container> /usr/local/bin/mixreads
$ podman run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readstats

```bash
$ singularity exec <container> /usr/local/bin/readstats
$ podman run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simqual

```bash
$ singularity exec <container> /usr/local/bin/simqual
$ podman run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simread

```bash
$ singularity exec <container> /usr/local/bin/simread
$ podman run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smalt

```bash
$ singularity exec <container> /usr/local/bin/smalt
$ podman run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitmates

```bash
$ singularity exec <container> /usr/local/bin/splitmates
$ podman run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitreads

```bash
$ singularity exec <container> /usr/local/bin/splitreads
$ podman run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trunkreads

```bash
$ singularity exec <container> /usr/local/bin/trunkreads
$ podman run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_dump

```bash
$ singularity exec <container> /usr/local/bin/kmc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
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