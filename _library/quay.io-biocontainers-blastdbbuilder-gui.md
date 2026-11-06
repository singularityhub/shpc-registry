---
layout: container
name:  "quay.io/biocontainers/blastdbbuilder-gui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blastdbbuilder-gui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blastdbbuilder-gui/container.yaml"
updated_at: "2026-11-06 18:11:39.710065"
latest: "1.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/blastdbbuilder-gui"
aliases:
 - "blastdbbuilder"
 - "blastdbbuilder-gui"
 - "blastdbbuilder-gui-desktop"
 - "blastdbbuilder-gui-desktop-uninstall"
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
 - "dataformat"
 - "datasets"
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "seqkit"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
versions:
 - "1.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for blastdbbuilder-gui"
config: {"url": "https://biocontainers.pro/tools/blastdbbuilder-gui", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for blastdbbuilder-gui", "latest": {"1.2.0--pyhdfd78af_0": "sha256:8f2c8d38a0b38efe836e136a0901cbbcbfc3791312e97bc13616161956e0c5e1"}, "tags": {"1.2.0--pyhdfd78af_0": "sha256:8f2c8d38a0b38efe836e136a0901cbbcbfc3791312e97bc13616161956e0c5e1"}, "docker": "quay.io/biocontainers/blastdbbuilder-gui", "aliases": {"blastdbbuilder": "/usr/local/bin/blastdbbuilder", "blastdbbuilder-gui": "/usr/local/bin/blastdbbuilder-gui", "blastdbbuilder-gui-desktop": "/usr/local/bin/blastdbbuilder-gui-desktop", "blastdbbuilder-gui-desktop-uninstall": "/usr/local/bin/blastdbbuilder-gui-desktop-uninstall", "archive-peptide": "/usr/local/bin/archive-peptide", "cittest": "/usr/local/bin/cittest", "combine-uids": "/usr/local/bin/combine-uids", "compare-uids": "/usr/local/bin/compare-uids", "exclude-uids": "/usr/local/bin/exclude-uids", "filter-records": "/usr/local/bin/filter-records", "gene2tbl": "/usr/local/bin/gene2tbl", "gpf2info": "/usr/local/bin/gpf2info", "intersect-uids": "/usr/local/bin/intersect-uids", "rcommon.sh": "/usr/local/bin/rcommon.sh", "split-records": "/usr/local/bin/split-records", "test-repeat": "/usr/local/bin/test-repeat", "uniq-count": "/usr/local/bin/uniq-count", "uniq-count-rank": "/usr/local/bin/uniq-count-rank", "dataformat": "/usr/local/bin/dataformat", "datasets": "/usr/local/bin/datasets", "idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "seqkit": "/usr/local/bin/seqkit", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blastdbbuilder-gui.
singularity registry hpc automated addition for blastdbbuilder-gui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blastdbbuilder-gui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blastdbbuilder-gui:1.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blastdbbuilder-gui/1.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/blastdbbuilder-gui/1.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blastdbbuilder-gui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blastdbbuilder-gui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blastdbbuilder-gui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blastdbbuilder-gui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blastdbbuilder-gui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blastdbbuilder-gui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blastdbbuilder

```bash
$ singularity exec <container> /usr/local/bin/blastdbbuilder
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbbuilder-gui

```bash
$ singularity exec <container> /usr/local/bin/blastdbbuilder-gui
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbbuilder-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbbuilder-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbbuilder-gui-desktop

```bash
$ singularity exec <container> /usr/local/bin/blastdbbuilder-gui-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbbuilder-gui-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbbuilder-gui-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbbuilder-gui-desktop-uninstall

```bash
$ singularity exec <container> /usr/local/bin/blastdbbuilder-gui-desktop-uninstall
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbbuilder-gui-desktop-uninstall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbbuilder-gui-desktop-uninstall   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dataformat

```bash
$ singularity exec <container> /usr/local/bin/dataformat
$ podman run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets

```bash
$ singularity exec <container> /usr/local/bin/datasets
$ podman run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
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