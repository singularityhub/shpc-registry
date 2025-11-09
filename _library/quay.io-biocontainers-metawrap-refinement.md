---
layout: container
name:  "quay.io/biocontainers/metawrap-refinement"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metawrap-refinement/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metawrap-refinement/container.yaml"
updated_at: "2025-11-09 03:49:42.654673"
latest: "1.3.0--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/metawrap-refinement"
aliases:
 - "config-metawrap"
 - "metaWRAP"
 - "metawrap"
 - "checkm"
 - "kraken"
 - "kraken-build"
 - "kraken-filter"
 - "kraken-mpa-report"
 - "kraken-report"
 - "kraken-translate"
 - "ktClassifyHits"
 - "ktImportHits"
 - "ktClassifyBLAST"
 - "ktGetContigMagnitudes"
 - "ktGetLCA"
 - "ktGetLibPath"
 - "ktGetTaxIDFromAcc"
 - "ktGetTaxInfo"
 - "ktImportBLAST"
 - "ktImportDiskUsage"
 - "ktImportEC"
 - "ktImportFCP"
 - "ktImportGalaxy"
 - "ktImportKrona"
 - "ktImportMETAREP-BLAST"
 - "ktImportMETAREP-EC"
 - "ktImportMGRAST"
 - "ktImportPhymmBL"
versions:
 - "1.3.0--hdfd78af_3"
description: "singularity registry hpc automated addition for metawrap-refinement"
config: {"url": "https://biocontainers.pro/tools/metawrap-refinement", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metawrap-refinement", "latest": {"1.3.0--hdfd78af_3": "sha256:39fb041d1ac06f5f6b5683a60add742c916bbcb019e69ef74f4dc2c3835d1823"}, "tags": {"1.3.0--hdfd78af_3": "sha256:39fb041d1ac06f5f6b5683a60add742c916bbcb019e69ef74f4dc2c3835d1823"}, "docker": "quay.io/biocontainers/metawrap-refinement", "aliases": {"config-metawrap": "/usr/local/bin/config-metawrap", "metaWRAP": "/usr/local/bin/metaWRAP", "metawrap": "/usr/local/bin/metawrap", "checkm": "/usr/local/bin/checkm", "kraken": "/usr/local/bin/kraken", "kraken-build": "/usr/local/bin/kraken-build", "kraken-filter": "/usr/local/bin/kraken-filter", "kraken-mpa-report": "/usr/local/bin/kraken-mpa-report", "kraken-report": "/usr/local/bin/kraken-report", "kraken-translate": "/usr/local/bin/kraken-translate", "ktClassifyHits": "/usr/local/bin/ktClassifyHits", "ktImportHits": "/usr/local/bin/ktImportHits", "ktClassifyBLAST": "/usr/local/bin/ktClassifyBLAST", "ktGetContigMagnitudes": "/usr/local/bin/ktGetContigMagnitudes", "ktGetLCA": "/usr/local/bin/ktGetLCA", "ktGetLibPath": "/usr/local/bin/ktGetLibPath", "ktGetTaxIDFromAcc": "/usr/local/bin/ktGetTaxIDFromAcc", "ktGetTaxInfo": "/usr/local/bin/ktGetTaxInfo", "ktImportBLAST": "/usr/local/bin/ktImportBLAST", "ktImportDiskUsage": "/usr/local/bin/ktImportDiskUsage", "ktImportEC": "/usr/local/bin/ktImportEC", "ktImportFCP": "/usr/local/bin/ktImportFCP", "ktImportGalaxy": "/usr/local/bin/ktImportGalaxy", "ktImportKrona": "/usr/local/bin/ktImportKrona", "ktImportMETAREP-BLAST": "/usr/local/bin/ktImportMETAREP-BLAST", "ktImportMETAREP-EC": "/usr/local/bin/ktImportMETAREP-EC", "ktImportMGRAST": "/usr/local/bin/ktImportMGRAST", "ktImportPhymmBL": "/usr/local/bin/ktImportPhymmBL"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metawrap-refinement.
singularity registry hpc automated addition for metawrap-refinement
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metawrap-refinement
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metawrap-refinement:1.3.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metawrap-refinement/1.3.0--hdfd78af_3
$ module help quay.io/biocontainers/metawrap-refinement/1.3.0--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metawrap-refinement-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-refinement-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-refinement-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metawrap-refinement-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metawrap-refinement-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metawrap-refinement-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### config-metawrap

```bash
$ singularity exec <container> /usr/local/bin/config-metawrap
$ podman run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaWRAP

```bash
$ singularity exec <container> /usr/local/bin/metaWRAP
$ podman run --it --rm --entrypoint /usr/local/bin/metaWRAP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaWRAP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metawrap

```bash
$ singularity exec <container> /usr/local/bin/metawrap
$ podman run --it --rm --entrypoint /usr/local/bin/metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken

```bash
$ singularity exec <container> /usr/local/bin/kraken
$ podman run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-build

```bash
$ singularity exec <container> /usr/local/bin/kraken-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-filter

```bash
$ singularity exec <container> /usr/local/bin/kraken-filter
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-translate

```bash
$ singularity exec <container> /usr/local/bin/kraken-translate
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktClassifyHits

```bash
$ singularity exec <container> /usr/local/bin/ktClassifyHits
$ podman run --it --rm --entrypoint /usr/local/bin/ktClassifyHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktClassifyHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportHits

```bash
$ singularity exec <container> /usr/local/bin/ktImportHits
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktClassifyBLAST

```bash
$ singularity exec <container> /usr/local/bin/ktClassifyBLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktClassifyBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktClassifyBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetContigMagnitudes

```bash
$ singularity exec <container> /usr/local/bin/ktGetContigMagnitudes
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetContigMagnitudes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetContigMagnitudes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetLCA

```bash
$ singularity exec <container> /usr/local/bin/ktGetLCA
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetLibPath

```bash
$ singularity exec <container> /usr/local/bin/ktGetLibPath
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetLibPath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetLibPath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetTaxIDFromAcc

```bash
$ singularity exec <container> /usr/local/bin/ktGetTaxIDFromAcc
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetTaxIDFromAcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetTaxIDFromAcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetTaxInfo

```bash
$ singularity exec <container> /usr/local/bin/ktGetTaxInfo
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetTaxInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetTaxInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportBLAST

```bash
$ singularity exec <container> /usr/local/bin/ktImportBLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportDiskUsage

```bash
$ singularity exec <container> /usr/local/bin/ktImportDiskUsage
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportDiskUsage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportDiskUsage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportEC

```bash
$ singularity exec <container> /usr/local/bin/ktImportEC
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportEC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportEC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportFCP

```bash
$ singularity exec <container> /usr/local/bin/ktImportFCP
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportFCP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportFCP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportGalaxy

```bash
$ singularity exec <container> /usr/local/bin/ktImportGalaxy
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportGalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportGalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportKrona

```bash
$ singularity exec <container> /usr/local/bin/ktImportKrona
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportKrona   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportKrona   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportMETAREP-BLAST

```bash
$ singularity exec <container> /usr/local/bin/ktImportMETAREP-BLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-BLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-BLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportMETAREP-EC

```bash
$ singularity exec <container> /usr/local/bin/ktImportMETAREP-EC
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-EC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-EC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportMGRAST

```bash
$ singularity exec <container> /usr/local/bin/ktImportMGRAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportMGRAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportMGRAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportPhymmBL

```bash
$ singularity exec <container> /usr/local/bin/ktImportPhymmBL
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportPhymmBL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportPhymmBL   -v ${PWD} -w ${PWD} <container> -c " $@"
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