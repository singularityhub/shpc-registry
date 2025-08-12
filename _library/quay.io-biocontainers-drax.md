---
layout: container
name:  "quay.io/biocontainers/drax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/drax/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/drax/container.yaml"
updated_at: "2025-08-12 03:26:08.723254"
latest: "0.0.0--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/drax"
aliases:
 - "addTaxonNames"
 - "bbmergegapped.sh"
 - "bbqc.sh"
 - "convertNR"
 - "convert_mar_to_kaiju.py"
 - "drax"
 - "gbk2faa.pl"
 - "groot"
 - "kaiju"
 - "kaiju2krona"
 - "kaijuReport"
 - "kaijup"
 - "kaijux"
 - "makeDB.sh"
 - "mergeOutputs"
 - "metacherchant.sh"
 - "mkbwt"
 - "mkfmi"
 - "nextflow"
 - "normandcorrectwrapper.sh"
 - "taxonlist.tsv"
 - "multiqc"
 - "fastp"
 - "ktClassifyBLAST"
 - "ktGetContigMagnitudes"
 - "ktGetLCA"
 - "ktGetLibPath"
 - "ktGetTaxIDFromAcc"
 - "ktGetTaxInfo"
 - "ktImportBLAST"
 - "ktImportDiskUsage"
versions:
 - "0.0.0--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for drax"
config: {"url": "https://biocontainers.pro/tools/drax", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for drax", "latest": {"0.0.0--hdfd78af_4": "sha256:d3e6e39933f1ecf666145f87d4b19a3cddc5dad1e8b7e1a38dc953c919afb364"}, "tags": {"0.0.0--hdfd78af_4": "sha256:d3e6e39933f1ecf666145f87d4b19a3cddc5dad1e8b7e1a38dc953c919afb364"}, "docker": "quay.io/biocontainers/drax", "aliases": {"addTaxonNames": "/usr/local/bin/addTaxonNames", "bbmergegapped.sh": "/usr/local/bin/bbmergegapped.sh", "bbqc.sh": "/usr/local/bin/bbqc.sh", "convertNR": "/usr/local/bin/convertNR", "convert_mar_to_kaiju.py": "/usr/local/bin/convert_mar_to_kaiju.py", "drax": "/usr/local/bin/drax", "gbk2faa.pl": "/usr/local/bin/gbk2faa.pl", "groot": "/usr/local/bin/groot", "kaiju": "/usr/local/bin/kaiju", "kaiju2krona": "/usr/local/bin/kaiju2krona", "kaijuReport": "/usr/local/bin/kaijuReport", "kaijup": "/usr/local/bin/kaijup", "kaijux": "/usr/local/bin/kaijux", "makeDB.sh": "/usr/local/bin/makeDB.sh", "mergeOutputs": "/usr/local/bin/mergeOutputs", "metacherchant.sh": "/usr/local/bin/metacherchant.sh", "mkbwt": "/usr/local/bin/mkbwt", "mkfmi": "/usr/local/bin/mkfmi", "nextflow": "/usr/local/bin/nextflow", "normandcorrectwrapper.sh": "/usr/local/bin/normandcorrectwrapper.sh", "taxonlist.tsv": "/usr/local/bin/taxonlist.tsv", "multiqc": "/usr/local/bin/multiqc", "fastp": "/usr/local/bin/fastp", "ktClassifyBLAST": "/usr/local/bin/ktClassifyBLAST", "ktGetContigMagnitudes": "/usr/local/bin/ktGetContigMagnitudes", "ktGetLCA": "/usr/local/bin/ktGetLCA", "ktGetLibPath": "/usr/local/bin/ktGetLibPath", "ktGetTaxIDFromAcc": "/usr/local/bin/ktGetTaxIDFromAcc", "ktGetTaxInfo": "/usr/local/bin/ktGetTaxInfo", "ktImportBLAST": "/usr/local/bin/ktImportBLAST", "ktImportDiskUsage": "/usr/local/bin/ktImportDiskUsage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/drax.
shpc-registry automated BioContainers addition for drax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/drax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/drax:0.0.0--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/drax/0.0.0--hdfd78af_4
$ module help quay.io/biocontainers/drax/0.0.0--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### drax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### drax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### drax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### drax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### drax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### drax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addTaxonNames

```bash
$ singularity exec <container> /usr/local/bin/addTaxonNames
$ podman run --it --rm --entrypoint /usr/local/bin/addTaxonNames   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addTaxonNames   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbmergegapped.sh

```bash
$ singularity exec <container> /usr/local/bin/bbmergegapped.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbmergegapped.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbmergegapped.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbqc.sh

```bash
$ singularity exec <container> /usr/local/bin/bbqc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbqc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbqc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertNR

```bash
$ singularity exec <container> /usr/local/bin/convertNR
$ podman run --it --rm --entrypoint /usr/local/bin/convertNR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertNR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_mar_to_kaiju.py

```bash
$ singularity exec <container> /usr/local/bin/convert_mar_to_kaiju.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_mar_to_kaiju.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_mar_to_kaiju.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drax

```bash
$ singularity exec <container> /usr/local/bin/drax
$ podman run --it --rm --entrypoint /usr/local/bin/drax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drax   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbk2faa.pl

```bash
$ singularity exec <container> /usr/local/bin/gbk2faa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gbk2faa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbk2faa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groot

```bash
$ singularity exec <container> /usr/local/bin/groot
$ podman run --it --rm --entrypoint /usr/local/bin/groot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju

```bash
$ singularity exec <container> /usr/local/bin/kaiju
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaiju2krona

```bash
$ singularity exec <container> /usr/local/bin/kaiju2krona
$ podman run --it --rm --entrypoint /usr/local/bin/kaiju2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaiju2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaijuReport

```bash
$ singularity exec <container> /usr/local/bin/kaijuReport
$ podman run --it --rm --entrypoint /usr/local/bin/kaijuReport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaijuReport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaijup

```bash
$ singularity exec <container> /usr/local/bin/kaijup
$ podman run --it --rm --entrypoint /usr/local/bin/kaijup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaijup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaijux

```bash
$ singularity exec <container> /usr/local/bin/kaijux
$ podman run --it --rm --entrypoint /usr/local/bin/kaijux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaijux   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeDB.sh

```bash
$ singularity exec <container> /usr/local/bin/makeDB.sh
$ podman run --it --rm --entrypoint /usr/local/bin/makeDB.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeDB.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeOutputs

```bash
$ singularity exec <container> /usr/local/bin/mergeOutputs
$ podman run --it --rm --entrypoint /usr/local/bin/mergeOutputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeOutputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metacherchant.sh

```bash
$ singularity exec <container> /usr/local/bin/metacherchant.sh
$ podman run --it --rm --entrypoint /usr/local/bin/metacherchant.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metacherchant.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkbwt

```bash
$ singularity exec <container> /usr/local/bin/mkbwt
$ podman run --it --rm --entrypoint /usr/local/bin/mkbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkbwt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkfmi

```bash
$ singularity exec <container> /usr/local/bin/mkfmi
$ podman run --it --rm --entrypoint /usr/local/bin/mkfmi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkfmi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow

```bash
$ singularity exec <container> /usr/local/bin/nextflow
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normandcorrectwrapper.sh

```bash
$ singularity exec <container> /usr/local/bin/normandcorrectwrapper.sh
$ podman run --it --rm --entrypoint /usr/local/bin/normandcorrectwrapper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normandcorrectwrapper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonlist.tsv

```bash
$ singularity exec <container> /usr/local/bin/taxonlist.tsv
$ podman run --it --rm --entrypoint /usr/local/bin/taxonlist.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonlist.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
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