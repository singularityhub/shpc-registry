---
layout: container
name:  "quay.io/biocontainers/trnanalysis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trnanalysis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trnanalysis/container.yaml"
updated_at: "2024-11-22 03:56:46.606483"
latest: "0.1.10--py_1"
container_url: "https://biocontainers.pro/tools/trnanalysis"
aliases:
 - "EukHighConfidenceFilter"
 - "bq"
 - "cgat"
 - "covels-SE"
 - "coves-SE"
 - "detectionCall"
 - "eufindtRNA"
 - "exactSNP"
 - "fasta2gsi"
 - "fastq_screen"
 - "featureCounts"
 - "flattenGTF"
 - "gcloud"
 - "genRandomReads"
 - "propmapped"
 - "qualityScores"
 - "removeDup"
 - "repair"
 - "sstofa"
 - "subindel"
 - "subjunc"
 - "sublong"
 - "subread-align"
 - "subread-buildindex"
 - "subread-fullscan"
 - "tRNAscan-SE"
 - "tRNAscan-SE.conf"
 - "time"
 - "trnanalysis"
 - "trnascan-1.4"
 - "txUnique"
 - "gsutil"
 - "multiqc"
 - "egrep"
 - "fgrep"
 - "grep"
 - "wigToBigWig"
 - "bedGraphToBigWig"
 - "bedToBigBed"
 - "giffilter"
 - "gifsponge"
versions:
 - "0.1.9--py_0"
 - "0.1.10--py_1"
description: "shpc-registry automated BioContainers addition for trnanalysis"
config: {"url": "https://biocontainers.pro/tools/trnanalysis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trnanalysis", "latest": {"0.1.10--py_1": "sha256:d24343d938cf048dd68e39e1b70ce6b645b7c11d7a3fa8debeb65775a197316e"}, "tags": {"0.1.9--py_0": "sha256:99860c8f8c87ae8545a37e10d32233a1e65a907382102c1c9c7d67c1541f5d10", "0.1.10--py_1": "sha256:d24343d938cf048dd68e39e1b70ce6b645b7c11d7a3fa8debeb65775a197316e"}, "docker": "quay.io/biocontainers/trnanalysis", "aliases": {"EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "bq": "/usr/local/bin/bq", "cgat": "/usr/local/bin/cgat", "covels-SE": "/usr/local/bin/covels-SE", "coves-SE": "/usr/local/bin/coves-SE", "detectionCall": "/usr/local/bin/detectionCall", "eufindtRNA": "/usr/local/bin/eufindtRNA", "exactSNP": "/usr/local/bin/exactSNP", "fasta2gsi": "/usr/local/bin/fasta2gsi", "fastq_screen": "/usr/local/bin/fastq_screen", "featureCounts": "/usr/local/bin/featureCounts", "flattenGTF": "/usr/local/bin/flattenGTF", "gcloud": "/usr/local/bin/gcloud", "genRandomReads": "/usr/local/bin/genRandomReads", "propmapped": "/usr/local/bin/propmapped", "qualityScores": "/usr/local/bin/qualityScores", "removeDup": "/usr/local/bin/removeDup", "repair": "/usr/local/bin/repair", "sstofa": "/usr/local/bin/sstofa", "subindel": "/usr/local/bin/subindel", "subjunc": "/usr/local/bin/subjunc", "sublong": "/usr/local/bin/sublong", "subread-align": "/usr/local/bin/subread-align", "subread-buildindex": "/usr/local/bin/subread-buildindex", "subread-fullscan": "/usr/local/bin/subread-fullscan", "tRNAscan-SE": "/usr/local/bin/tRNAscan-SE", "tRNAscan-SE.conf": "/usr/local/bin/tRNAscan-SE.conf", "time": "/usr/local/bin/time", "trnanalysis": "/usr/local/bin/trnanalysis", "trnascan-1.4": "/usr/local/bin/trnascan-1.4", "txUnique": "/usr/local/bin/txUnique", "gsutil": "/usr/local/bin/gsutil", "multiqc": "/usr/local/bin/multiqc", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "wigToBigWig": "/usr/local/bin/wigToBigWig", "bedGraphToBigWig": "/usr/local/bin/bedGraphToBigWig", "bedToBigBed": "/usr/local/bin/bedToBigBed", "giffilter": "/usr/local/bin/giffilter", "gifsponge": "/usr/local/bin/gifsponge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trnanalysis.
shpc-registry automated BioContainers addition for trnanalysis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trnanalysis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trnanalysis:0.1.10--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trnanalysis/0.1.10--py_1
$ module help quay.io/biocontainers/trnanalysis/0.1.10--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trnanalysis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trnanalysis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trnanalysis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trnanalysis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trnanalysis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trnanalysis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bq

```bash
$ singularity exec <container> /usr/local/bin/bq
$ podman run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgat

```bash
$ singularity exec <container> /usr/local/bin/cgat
$ podman run --it --rm --entrypoint /usr/local/bin/cgat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covels-SE

```bash
$ singularity exec <container> /usr/local/bin/covels-SE
$ podman run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coves-SE

```bash
$ singularity exec <container> /usr/local/bin/coves-SE
$ podman run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### detectionCall

```bash
$ singularity exec <container> /usr/local/bin/detectionCall
$ podman run --it --rm --entrypoint /usr/local/bin/detectionCall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/detectionCall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eufindtRNA

```bash
$ singularity exec <container> /usr/local/bin/eufindtRNA
$ podman run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exactSNP

```bash
$ singularity exec <container> /usr/local/bin/exactSNP
$ podman run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2gsi

```bash
$ singularity exec <container> /usr/local/bin/fasta2gsi
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2gsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_screen

```bash
$ singularity exec <container> /usr/local/bin/fastq_screen
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_screen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_screen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featureCounts

```bash
$ singularity exec <container> /usr/local/bin/featureCounts
$ podman run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flattenGTF

```bash
$ singularity exec <container> /usr/local/bin/flattenGTF
$ podman run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcloud

```bash
$ singularity exec <container> /usr/local/bin/gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genRandomReads

```bash
$ singularity exec <container> /usr/local/bin/genRandomReads
$ podman run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### propmapped

```bash
$ singularity exec <container> /usr/local/bin/propmapped
$ podman run --it --rm --entrypoint /usr/local/bin/propmapped   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/propmapped   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualityScores

```bash
$ singularity exec <container> /usr/local/bin/qualityScores
$ podman run --it --rm --entrypoint /usr/local/bin/qualityScores   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualityScores   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### removeDup

```bash
$ singularity exec <container> /usr/local/bin/removeDup
$ podman run --it --rm --entrypoint /usr/local/bin/removeDup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/removeDup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repair

```bash
$ singularity exec <container> /usr/local/bin/repair
$ podman run --it --rm --entrypoint /usr/local/bin/repair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sstofa

```bash
$ singularity exec <container> /usr/local/bin/sstofa
$ podman run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sstofa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subindel

```bash
$ singularity exec <container> /usr/local/bin/subindel
$ podman run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subjunc

```bash
$ singularity exec <container> /usr/local/bin/subjunc
$ podman run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sublong

```bash
$ singularity exec <container> /usr/local/bin/sublong
$ podman run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-align

```bash
$ singularity exec <container> /usr/local/bin/subread-align
$ podman run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-buildindex

```bash
$ singularity exec <container> /usr/local/bin/subread-buildindex
$ podman run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-fullscan

```bash
$ singularity exec <container> /usr/local/bin/subread-fullscan
$ podman run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tRNAscan-SE.conf

```bash
$ singularity exec <container> /usr/local/bin/tRNAscan-SE.conf
$ podman run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tRNAscan-SE.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time

```bash
$ singularity exec <container> /usr/local/bin/time
$ podman run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trnanalysis

```bash
$ singularity exec <container> /usr/local/bin/trnanalysis
$ podman run --it --rm --entrypoint /usr/local/bin/trnanalysis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trnanalysis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trnascan-1.4

```bash
$ singularity exec <container> /usr/local/bin/trnascan-1.4
$ podman run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trnascan-1.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### txUnique

```bash
$ singularity exec <container> /usr/local/bin/txUnique
$ podman run --it --rm --entrypoint /usr/local/bin/txUnique   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/txUnique   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsutil

```bash
$ singularity exec <container> /usr/local/bin/gsutil
$ podman run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedGraphToBigWig

```bash
$ singularity exec <container> /usr/local/bin/bedGraphToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBigBed

```bash
$ singularity exec <container> /usr/local/bin/bedToBigBed
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffilter

```bash
$ singularity exec <container> /usr/local/bin/giffilter
$ podman run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifsponge

```bash
$ singularity exec <container> /usr/local/bin/gifsponge
$ podman run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
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