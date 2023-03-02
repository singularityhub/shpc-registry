---
layout: container
name:  "quay.io/biocontainers/megan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/megan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/megan/container.yaml"
updated_at: "2023-03-02 03:10:30.399215"
latest: "6.21.7--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/megan"
aliases:
 - "MEGAN"
 - "aadder-build"
 - "aadder-run"
 - "blast2lca"
 - "blast2rma"
 - "compute-comparison"
 - "daa-meganizer"
 - "daa2info"
 - "daa2rma"
 - "extract-biome"
 - "gc-assembler"
 - "maf2daa"
 - "megan-server"
 - "read-extractor"
 - "reanalyzer"
 - "references-annotator"
 - "rma2info"
 - "sam2rma"
 - "sort-last-maf"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
versions:
 - "6.21.7--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for megan"
config: {"url": "https://biocontainers.pro/tools/megan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for megan", "latest": {"6.21.7--h9ee0642_0": "sha256:537fb81ee0151a2299ca82649e00f92a8e44f1f6bb3f85a26e9b2e902dbc91b7"}, "tags": {"6.21.7--h9ee0642_0": "sha256:537fb81ee0151a2299ca82649e00f92a8e44f1f6bb3f85a26e9b2e902dbc91b7"}, "docker": "quay.io/biocontainers/megan", "aliases": {"MEGAN": "/usr/local/bin/MEGAN", "aadder-build": "/usr/local/bin/aadder-build", "aadder-run": "/usr/local/bin/aadder-run", "blast2lca": "/usr/local/bin/blast2lca", "blast2rma": "/usr/local/bin/blast2rma", "compute-comparison": "/usr/local/bin/compute-comparison", "daa-meganizer": "/usr/local/bin/daa-meganizer", "daa2info": "/usr/local/bin/daa2info", "daa2rma": "/usr/local/bin/daa2rma", "extract-biome": "/usr/local/bin/extract-biome", "gc-assembler": "/usr/local/bin/gc-assembler", "maf2daa": "/usr/local/bin/maf2daa", "megan-server": "/usr/local/bin/megan-server", "read-extractor": "/usr/local/bin/read-extractor", "reanalyzer": "/usr/local/bin/reanalyzer", "references-annotator": "/usr/local/bin/references-annotator", "rma2info": "/usr/local/bin/rma2info", "sam2rma": "/usr/local/bin/sam2rma", "sort-last-maf": "/usr/local/bin/sort-last-maf", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/megan.
shpc-registry automated BioContainers addition for megan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/megan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/megan:6.21.7--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/megan/6.21.7--h9ee0642_0
$ module help quay.io/biocontainers/megan/6.21.7--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### megan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### megan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### megan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### megan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### megan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### megan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MEGAN

```bash
$ singularity exec <container> /usr/local/bin/MEGAN
$ podman run --it --rm --entrypoint /usr/local/bin/MEGAN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MEGAN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aadder-build

```bash
$ singularity exec <container> /usr/local/bin/aadder-build
$ podman run --it --rm --entrypoint /usr/local/bin/aadder-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aadder-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aadder-run

```bash
$ singularity exec <container> /usr/local/bin/aadder-run
$ podman run --it --rm --entrypoint /usr/local/bin/aadder-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aadder-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2lca

```bash
$ singularity exec <container> /usr/local/bin/blast2lca
$ podman run --it --rm --entrypoint /usr/local/bin/blast2lca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2lca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2rma

```bash
$ singularity exec <container> /usr/local/bin/blast2rma
$ podman run --it --rm --entrypoint /usr/local/bin/blast2rma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2rma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute-comparison

```bash
$ singularity exec <container> /usr/local/bin/compute-comparison
$ podman run --it --rm --entrypoint /usr/local/bin/compute-comparison   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute-comparison   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daa-meganizer

```bash
$ singularity exec <container> /usr/local/bin/daa-meganizer
$ podman run --it --rm --entrypoint /usr/local/bin/daa-meganizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daa-meganizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daa2info

```bash
$ singularity exec <container> /usr/local/bin/daa2info
$ podman run --it --rm --entrypoint /usr/local/bin/daa2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daa2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daa2rma

```bash
$ singularity exec <container> /usr/local/bin/daa2rma
$ podman run --it --rm --entrypoint /usr/local/bin/daa2rma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daa2rma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-biome

```bash
$ singularity exec <container> /usr/local/bin/extract-biome
$ podman run --it --rm --entrypoint /usr/local/bin/extract-biome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-biome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc-assembler

```bash
$ singularity exec <container> /usr/local/bin/gc-assembler
$ podman run --it --rm --entrypoint /usr/local/bin/gc-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf2daa

```bash
$ singularity exec <container> /usr/local/bin/maf2daa
$ podman run --it --rm --entrypoint /usr/local/bin/maf2daa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2daa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megan-server

```bash
$ singularity exec <container> /usr/local/bin/megan-server
$ podman run --it --rm --entrypoint /usr/local/bin/megan-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megan-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read-extractor

```bash
$ singularity exec <container> /usr/local/bin/read-extractor
$ podman run --it --rm --entrypoint /usr/local/bin/read-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reanalyzer

```bash
$ singularity exec <container> /usr/local/bin/reanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/reanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### references-annotator

```bash
$ singularity exec <container> /usr/local/bin/references-annotator
$ podman run --it --rm --entrypoint /usr/local/bin/references-annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/references-annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rma2info

```bash
$ singularity exec <container> /usr/local/bin/rma2info
$ podman run --it --rm --entrypoint /usr/local/bin/rma2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rma2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2rma

```bash
$ singularity exec <container> /usr/local/bin/sam2rma
$ podman run --it --rm --entrypoint /usr/local/bin/sam2rma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2rma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-last-maf

```bash
$ singularity exec <container> /usr/local/bin/sort-last-maf
$ podman run --it --rm --entrypoint /usr/local/bin/sort-last-maf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-last-maf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
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