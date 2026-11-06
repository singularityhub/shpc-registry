---
layout: container
name:  "quay.io/biocontainers/panhog"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panhog/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panhog/container.yaml"
updated_at: "2026-11-06 09:09:42.384730"
latest: "0.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/panhog"
aliases:
 - "pangenehog"
 - "panhog"
 - "archive-peptide"
 - "cittest"
 - "combine-uids"
 - "compare-uids"
 - "exclude-uids"
 - "filter-records"
 - "gene2tbl"
 - "gpf2info"
 - "intersect-uids"
 - "rcommon.sh"
 - "split-records"
 - "test-repeat"
 - "uniq-count"
 - "uniq-count-rank"
 - "pal2nal.pl"
 - "ds"
 - "raxml-ng"
 - "raxml-ng-mpi"
 - "gawk-5.4.1"
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "archive-nlmnlp"
 - "archive-pids"
versions:
 - "0.4.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for panhog"
config: {"url": "https://biocontainers.pro/tools/panhog", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for panhog", "latest": {"0.4.1--pyhdfd78af_0": "sha256:fa551dc100b54ddb2fd3e980039d7a1e5009ea5b77d1e137b3df0331dab27dec"}, "tags": {"0.4.1--pyhdfd78af_0": "sha256:fa551dc100b54ddb2fd3e980039d7a1e5009ea5b77d1e137b3df0331dab27dec"}, "docker": "quay.io/biocontainers/panhog", "aliases": {"pangenehog": "/usr/local/bin/pangenehog", "panhog": "/usr/local/bin/panhog", "archive-peptide": "/usr/local/bin/archive-peptide", "cittest": "/usr/local/bin/cittest", "combine-uids": "/usr/local/bin/combine-uids", "compare-uids": "/usr/local/bin/compare-uids", "exclude-uids": "/usr/local/bin/exclude-uids", "filter-records": "/usr/local/bin/filter-records", "gene2tbl": "/usr/local/bin/gene2tbl", "gpf2info": "/usr/local/bin/gpf2info", "intersect-uids": "/usr/local/bin/intersect-uids", "rcommon.sh": "/usr/local/bin/rcommon.sh", "split-records": "/usr/local/bin/split-records", "test-repeat": "/usr/local/bin/test-repeat", "uniq-count": "/usr/local/bin/uniq-count", "uniq-count-rank": "/usr/local/bin/uniq-count-rank", "pal2nal.pl": "/usr/local/bin/pal2nal.pl", "ds": "/usr/local/bin/ds", "raxml-ng": "/usr/local/bin/raxml-ng", "raxml-ng-mpi": "/usr/local/bin/raxml-ng-mpi", "gawk-5.4.1": "/usr/local/bin/gawk-5.4.1", "idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panhog.
singularity registry hpc automated addition for panhog
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panhog
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panhog:0.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panhog/0.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/panhog/0.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panhog-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panhog-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panhog-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panhog-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panhog-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panhog-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pangenehog

```bash
$ singularity exec <container> /usr/local/bin/pangenehog
$ podman run --it --rm --entrypoint /usr/local/bin/pangenehog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pangenehog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panhog

```bash
$ singularity exec <container> /usr/local/bin/panhog
$ podman run --it --rm --entrypoint /usr/local/bin/panhog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panhog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-peptide

```bash
$ singularity exec <container> /usr/local/bin/archive-peptide
$ podman run --it --rm --entrypoint /usr/local/bin/archive-peptide   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-peptide   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cittest

```bash
$ singularity exec <container> /usr/local/bin/cittest
$ podman run --it --rm --entrypoint /usr/local/bin/cittest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cittest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine-uids

```bash
$ singularity exec <container> /usr/local/bin/combine-uids
$ podman run --it --rm --entrypoint /usr/local/bin/combine-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-uids

```bash
$ singularity exec <container> /usr/local/bin/compare-uids
$ podman run --it --rm --entrypoint /usr/local/bin/compare-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exclude-uids

```bash
$ singularity exec <container> /usr/local/bin/exclude-uids
$ podman run --it --rm --entrypoint /usr/local/bin/exclude-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exclude-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-records

```bash
$ singularity exec <container> /usr/local/bin/filter-records
$ podman run --it --rm --entrypoint /usr/local/bin/filter-records   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-records   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2tbl

```bash
$ singularity exec <container> /usr/local/bin/gene2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gene2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpf2info

```bash
$ singularity exec <container> /usr/local/bin/gpf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gpf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersect-uids

```bash
$ singularity exec <container> /usr/local/bin/intersect-uids
$ podman run --it --rm --entrypoint /usr/local/bin/intersect-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersect-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/rcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-records

```bash
$ singularity exec <container> /usr/local/bin/split-records
$ podman run --it --rm --entrypoint /usr/local/bin/split-records   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-records   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-repeat

```bash
$ singularity exec <container> /usr/local/bin/test-repeat
$ podman run --it --rm --entrypoint /usr/local/bin/test-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-count

```bash
$ singularity exec <container> /usr/local/bin/uniq-count
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-count-rank

```bash
$ singularity exec <container> /usr/local/bin/uniq-count-rank
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-count-rank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-count-rank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pal2nal.pl

```bash
$ singularity exec <container> /usr/local/bin/pal2nal.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ds

```bash
$ singularity exec <container> /usr/local/bin/ds
$ podman run --it --rm --entrypoint /usr/local/bin/ds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.15

```bash
$ singularity exec <container> /usr/local/bin/idle3.15
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.15

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.15
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15

```bash
$ singularity exec <container> /usr/local/bin/python3.15
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15-config

```bash
$ singularity exec <container> /usr/local/bin/python3.15-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
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