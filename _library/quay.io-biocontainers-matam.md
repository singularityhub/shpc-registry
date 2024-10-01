---
layout: container
name:  "quay.io/biocontainers/matam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/matam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/matam/container.yaml"
updated_at: "2024-10-01 03:04:00.210230"
latest: "1.6.1--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/matam"
aliases:
 - "AbundanceStats"
 - "AlignmentTools"
 - "Clustering"
 - "FrameBot"
 - "KmerFilter"
 - "ProbeMatch"
 - "ReadSeq"
 - "SeqFilters"
 - "SequenceMatch"
 - "classifier"
 - "hmmgs"
 - "index_default_ssu_rrna_db.py"
 - "indexdb_rna"
 - "ktClassifyHits"
 - "ktImportHits"
 - "matam_assembly.py"
 - "matam_compare_samples.py"
 - "matam_db_preprocessing.py"
 - "merge-paired-reads.sh"
 - "sga"
 - "sga-astat.py"
 - "sga-bam2de.pl"
 - "sga-mergeDriver.pl"
 - "sortmerna"
 - "unmerge-paired-reads.sh"
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
versions:
 - "1.6.0--hd03093a_3"
 - "1.6.1--hd03093a_0"
 - "1.6.1--hdcf5f25_1"
description: "shpc-registry automated BioContainers addition for matam"
config: {"url": "https://biocontainers.pro/tools/matam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for matam", "latest": {"1.6.1--hdcf5f25_1": "sha256:3218b2b4e487fca8850240c12b98c66b0ca775e393e527b3afce0429a538e711"}, "tags": {"1.6.0--hd03093a_3": "sha256:4b67c13e4fb04747c427b8fd42f44cf886f9f8e0ed87a715b79ed3c40476e367", "1.6.1--hd03093a_0": "sha256:d8369f9a38449aa4a51ccd1770bb537144622b350bd3b310af06fe70ac3e0b80", "1.6.1--hdcf5f25_1": "sha256:3218b2b4e487fca8850240c12b98c66b0ca775e393e527b3afce0429a538e711"}, "docker": "quay.io/biocontainers/matam", "aliases": {"AbundanceStats": "/usr/local/bin/AbundanceStats", "AlignmentTools": "/usr/local/bin/AlignmentTools", "Clustering": "/usr/local/bin/Clustering", "FrameBot": "/usr/local/bin/FrameBot", "KmerFilter": "/usr/local/bin/KmerFilter", "ProbeMatch": "/usr/local/bin/ProbeMatch", "ReadSeq": "/usr/local/bin/ReadSeq", "SeqFilters": "/usr/local/bin/SeqFilters", "SequenceMatch": "/usr/local/bin/SequenceMatch", "classifier": "/usr/local/bin/classifier", "hmmgs": "/usr/local/bin/hmmgs", "index_default_ssu_rrna_db.py": "/usr/local/bin/index_default_ssu_rrna_db.py", "indexdb_rna": "/usr/local/bin/indexdb_rna", "ktClassifyHits": "/usr/local/bin/ktClassifyHits", "ktImportHits": "/usr/local/bin/ktImportHits", "matam_assembly.py": "/usr/local/bin/matam_assembly.py", "matam_compare_samples.py": "/usr/local/bin/matam_compare_samples.py", "matam_db_preprocessing.py": "/usr/local/bin/matam_db_preprocessing.py", "merge-paired-reads.sh": "/usr/local/bin/merge-paired-reads.sh", "sga": "/usr/local/bin/sga", "sga-astat.py": "/usr/local/bin/sga-astat.py", "sga-bam2de.pl": "/usr/local/bin/sga-bam2de.pl", "sga-mergeDriver.pl": "/usr/local/bin/sga-mergeDriver.pl", "sortmerna": "/usr/local/bin/sortmerna", "unmerge-paired-reads.sh": "/usr/local/bin/unmerge-paired-reads.sh", "ktClassifyBLAST": "/usr/local/bin/ktClassifyBLAST", "ktGetContigMagnitudes": "/usr/local/bin/ktGetContigMagnitudes", "ktGetLCA": "/usr/local/bin/ktGetLCA", "ktGetLibPath": "/usr/local/bin/ktGetLibPath", "ktGetTaxIDFromAcc": "/usr/local/bin/ktGetTaxIDFromAcc", "ktGetTaxInfo": "/usr/local/bin/ktGetTaxInfo", "ktImportBLAST": "/usr/local/bin/ktImportBLAST", "ktImportDiskUsage": "/usr/local/bin/ktImportDiskUsage", "ktImportEC": "/usr/local/bin/ktImportEC", "ktImportFCP": "/usr/local/bin/ktImportFCP"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/matam.
shpc-registry automated BioContainers addition for matam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/matam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/matam:1.6.1--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/matam/1.6.1--hdcf5f25_1
$ module help quay.io/biocontainers/matam/1.6.1--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### matam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### matam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### matam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### matam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### matam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### matam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AbundanceStats

```bash
$ singularity exec <container> /usr/local/bin/AbundanceStats
$ podman run --it --rm --entrypoint /usr/local/bin/AbundanceStats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AbundanceStats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AlignmentTools

```bash
$ singularity exec <container> /usr/local/bin/AlignmentTools
$ podman run --it --rm --entrypoint /usr/local/bin/AlignmentTools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AlignmentTools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Clustering

```bash
$ singularity exec <container> /usr/local/bin/Clustering
$ podman run --it --rm --entrypoint /usr/local/bin/Clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FrameBot

```bash
$ singularity exec <container> /usr/local/bin/FrameBot
$ podman run --it --rm --entrypoint /usr/local/bin/FrameBot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FrameBot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerFilter

```bash
$ singularity exec <container> /usr/local/bin/KmerFilter
$ podman run --it --rm --entrypoint /usr/local/bin/KmerFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ProbeMatch

```bash
$ singularity exec <container> /usr/local/bin/ProbeMatch
$ podman run --it --rm --entrypoint /usr/local/bin/ProbeMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProbeMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ReadSeq

```bash
$ singularity exec <container> /usr/local/bin/ReadSeq
$ podman run --it --rm --entrypoint /usr/local/bin/ReadSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ReadSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SeqFilters

```bash
$ singularity exec <container> /usr/local/bin/SeqFilters
$ podman run --it --rm --entrypoint /usr/local/bin/SeqFilters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SeqFilters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SequenceMatch

```bash
$ singularity exec <container> /usr/local/bin/SequenceMatch
$ podman run --it --rm --entrypoint /usr/local/bin/SequenceMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SequenceMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classifier

```bash
$ singularity exec <container> /usr/local/bin/classifier
$ podman run --it --rm --entrypoint /usr/local/bin/classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmgs

```bash
$ singularity exec <container> /usr/local/bin/hmmgs
$ podman run --it --rm --entrypoint /usr/local/bin/hmmgs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmgs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_default_ssu_rrna_db.py

```bash
$ singularity exec <container> /usr/local/bin/index_default_ssu_rrna_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/index_default_ssu_rrna_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_default_ssu_rrna_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_rna

```bash
$ singularity exec <container> /usr/local/bin/indexdb_rna
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_rna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_rna   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### matam_assembly.py

```bash
$ singularity exec <container> /usr/local/bin/matam_assembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/matam_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matam_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matam_compare_samples.py

```bash
$ singularity exec <container> /usr/local/bin/matam_compare_samples.py
$ podman run --it --rm --entrypoint /usr/local/bin/matam_compare_samples.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matam_compare_samples.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matam_db_preprocessing.py

```bash
$ singularity exec <container> /usr/local/bin/matam_db_preprocessing.py
$ podman run --it --rm --entrypoint /usr/local/bin/matam_db_preprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matam_db_preprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-paired-reads.sh

```bash
$ singularity exec <container> /usr/local/bin/merge-paired-reads.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merge-paired-reads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-paired-reads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga

```bash
$ singularity exec <container> /usr/local/bin/sga
$ podman run --it --rm --entrypoint /usr/local/bin/sga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-astat.py

```bash
$ singularity exec <container> /usr/local/bin/sga-astat.py
$ podman run --it --rm --entrypoint /usr/local/bin/sga-astat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-astat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-bam2de.pl

```bash
$ singularity exec <container> /usr/local/bin/sga-bam2de.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sga-bam2de.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-bam2de.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sga-mergeDriver.pl

```bash
$ singularity exec <container> /usr/local/bin/sga-mergeDriver.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sga-mergeDriver.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sga-mergeDriver.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortmerna

```bash
$ singularity exec <container> /usr/local/bin/sortmerna
$ podman run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unmerge-paired-reads.sh

```bash
$ singularity exec <container> /usr/local/bin/unmerge-paired-reads.sh
$ podman run --it --rm --entrypoint /usr/local/bin/unmerge-paired-reads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unmerge-paired-reads.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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