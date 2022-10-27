---
layout: container
name:  "quay.io/biocontainers/repeatmodeler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/repeatmodeler/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/repeatmodeler/container.yaml"
updated_at: "2022-10-27 00:29:49.675208"
latest: "2.0.3--pl5321h9ee0642_0"
container_url: "https://biocontainers.pro/tools/repeatmodeler"
aliases:
 - "BuildDatabase"
 - "LAI"
 - "LTRPipeline"
 - "LTR_retriever"
 - "Linup"
 - "Ninja"
 - "RM2Bed.py"
 - "Refiner"
 - "RepeatClassifier"
 - "RepeatModeler"
 - "RepeatScout"
 - "alignAndCallConsensus.pl"
 - "buildRMLibFromEMBL.pl"
 - "buildSummary.pl"
 - "build_lmer_table"
 - "compare-out-to-gff.prl"
 - "convert_MGEScan3.0.pl"
 - "convert_ltr_struc.pl"
 - "convert_ltrdetector.pl"
 - "edgeredef"
 - "eledef"
 - "eleredef"
 - "famdef"
 - "filter-stage-1.prl"
 - "filter-stage-2.prl"
 - "generateSeedAlignments.pl"
 - "imagespread"
 - "maskFile.pl"
 - "merge-lmer-tables.prl"
 - "nmerge"
 - "nseg"
 - "viewMSA.pl"
 - "wublastToCrossmatch.pl"
versions:
 - "2.0.3--pl5321h9ee0642_0"
description: "shpc-registry automated BioContainers addition for repeatmodeler"
config: {"url": "https://biocontainers.pro/tools/repeatmodeler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for repeatmodeler", "latest": {"2.0.3--pl5321h9ee0642_0": "sha256:375bee70d308ed528b2ddf525b0c54d731c308a978e9fa67cb4c1f9a43c7722b"}, "tags": {"2.0.3--pl5321h9ee0642_0": "sha256:375bee70d308ed528b2ddf525b0c54d731c308a978e9fa67cb4c1f9a43c7722b"}, "docker": "quay.io/biocontainers/repeatmodeler", "aliases": {"BuildDatabase": "/usr/local/bin/BuildDatabase", "LAI": "/usr/local/bin/LAI", "LTRPipeline": "/usr/local/bin/LTRPipeline", "LTR_retriever": "/usr/local/bin/LTR_retriever", "Linup": "/usr/local/bin/Linup", "Ninja": "/usr/local/bin/Ninja", "RM2Bed.py": "/usr/local/bin/RM2Bed.py", "Refiner": "/usr/local/bin/Refiner", "RepeatClassifier": "/usr/local/bin/RepeatClassifier", "RepeatModeler": "/usr/local/bin/RepeatModeler", "RepeatScout": "/usr/local/bin/RepeatScout", "alignAndCallConsensus.pl": "/usr/local/bin/alignAndCallConsensus.pl", "buildRMLibFromEMBL.pl": "/usr/local/bin/buildRMLibFromEMBL.pl", "buildSummary.pl": "/usr/local/bin/buildSummary.pl", "build_lmer_table": "/usr/local/bin/build_lmer_table", "compare-out-to-gff.prl": "/usr/local/bin/compare-out-to-gff.prl", "convert_MGEScan3.0.pl": "/usr/local/bin/convert_MGEScan3.0.pl", "convert_ltr_struc.pl": "/usr/local/bin/convert_ltr_struc.pl", "convert_ltrdetector.pl": "/usr/local/bin/convert_ltrdetector.pl", "edgeredef": "/usr/local/bin/edgeredef", "eledef": "/usr/local/bin/eledef", "eleredef": "/usr/local/bin/eleredef", "famdef": "/usr/local/bin/famdef", "filter-stage-1.prl": "/usr/local/bin/filter-stage-1.prl", "filter-stage-2.prl": "/usr/local/bin/filter-stage-2.prl", "generateSeedAlignments.pl": "/usr/local/bin/generateSeedAlignments.pl", "imagespread": "/usr/local/bin/imagespread", "maskFile.pl": "/usr/local/bin/maskFile.pl", "merge-lmer-tables.prl": "/usr/local/bin/merge-lmer-tables.prl", "nmerge": "/usr/local/bin/nmerge", "nseg": "/usr/local/bin/nseg", "viewMSA.pl": "/usr/local/bin/viewMSA.pl", "wublastToCrossmatch.pl": "/usr/local/bin/wublastToCrossmatch.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/repeatmodeler.
shpc-registry automated BioContainers addition for repeatmodeler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/repeatmodeler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/repeatmodeler:2.0.3--pl5321h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/repeatmodeler/2.0.3--pl5321h9ee0642_0
$ module help quay.io/biocontainers/repeatmodeler/2.0.3--pl5321h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### repeatmodeler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### repeatmodeler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### repeatmodeler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### repeatmodeler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### repeatmodeler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### repeatmodeler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BuildDatabase

```bash
$ singularity exec <container> /usr/local/bin/BuildDatabase
$ podman run --it --rm --entrypoint /usr/local/bin/BuildDatabase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BuildDatabase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAI

```bash
$ singularity exec <container> /usr/local/bin/LAI
$ podman run --it --rm --entrypoint /usr/local/bin/LAI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LTRPipeline

```bash
$ singularity exec <container> /usr/local/bin/LTRPipeline
$ podman run --it --rm --entrypoint /usr/local/bin/LTRPipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LTRPipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LTR_retriever

```bash
$ singularity exec <container> /usr/local/bin/LTR_retriever
$ podman run --it --rm --entrypoint /usr/local/bin/LTR_retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LTR_retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Linup

```bash
$ singularity exec <container> /usr/local/bin/Linup
$ podman run --it --rm --entrypoint /usr/local/bin/Linup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Linup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Ninja

```bash
$ singularity exec <container> /usr/local/bin/Ninja
$ podman run --it --rm --entrypoint /usr/local/bin/Ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RM2Bed.py

```bash
$ singularity exec <container> /usr/local/bin/RM2Bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RM2Bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Refiner

```bash
$ singularity exec <container> /usr/local/bin/Refiner
$ podman run --it --rm --entrypoint /usr/local/bin/Refiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Refiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatClassifier

```bash
$ singularity exec <container> /usr/local/bin/RepeatClassifier
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatClassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatClassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatModeler

```bash
$ singularity exec <container> /usr/local/bin/RepeatModeler
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatModeler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatModeler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatScout

```bash
$ singularity exec <container> /usr/local/bin/RepeatScout
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatScout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatScout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alignAndCallConsensus.pl

```bash
$ singularity exec <container> /usr/local/bin/alignAndCallConsensus.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alignAndCallConsensus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignAndCallConsensus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildRMLibFromEMBL.pl

```bash
$ singularity exec <container> /usr/local/bin/buildRMLibFromEMBL.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildRMLibFromEMBL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildRMLibFromEMBL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildSummary.pl

```bash
$ singularity exec <container> /usr/local/bin/buildSummary.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildSummary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildSummary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_lmer_table

```bash
$ singularity exec <container> /usr/local/bin/build_lmer_table
$ podman run --it --rm --entrypoint /usr/local/bin/build_lmer_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_lmer_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-out-to-gff.prl

```bash
$ singularity exec <container> /usr/local/bin/compare-out-to-gff.prl
$ podman run --it --rm --entrypoint /usr/local/bin/compare-out-to-gff.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-out-to-gff.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_MGEScan3.0.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_MGEScan3.0.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_MGEScan3.0.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_MGEScan3.0.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_ltr_struc.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_ltr_struc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_ltr_struc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_ltr_struc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_ltrdetector.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_ltrdetector.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_ltrdetector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_ltrdetector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edgeredef

```bash
$ singularity exec <container> /usr/local/bin/edgeredef
$ podman run --it --rm --entrypoint /usr/local/bin/edgeredef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edgeredef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eledef

```bash
$ singularity exec <container> /usr/local/bin/eledef
$ podman run --it --rm --entrypoint /usr/local/bin/eledef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eledef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eleredef

```bash
$ singularity exec <container> /usr/local/bin/eleredef
$ podman run --it --rm --entrypoint /usr/local/bin/eleredef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eleredef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### famdef

```bash
$ singularity exec <container> /usr/local/bin/famdef
$ podman run --it --rm --entrypoint /usr/local/bin/famdef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/famdef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-stage-1.prl

```bash
$ singularity exec <container> /usr/local/bin/filter-stage-1.prl
$ podman run --it --rm --entrypoint /usr/local/bin/filter-stage-1.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-stage-1.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-stage-2.prl

```bash
$ singularity exec <container> /usr/local/bin/filter-stage-2.prl
$ podman run --it --rm --entrypoint /usr/local/bin/filter-stage-2.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-stage-2.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generateSeedAlignments.pl

```bash
$ singularity exec <container> /usr/local/bin/generateSeedAlignments.pl
$ podman run --it --rm --entrypoint /usr/local/bin/generateSeedAlignments.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generateSeedAlignments.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagespread

```bash
$ singularity exec <container> /usr/local/bin/imagespread
$ podman run --it --rm --entrypoint /usr/local/bin/imagespread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagespread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maskFile.pl

```bash
$ singularity exec <container> /usr/local/bin/maskFile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/maskFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maskFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-lmer-tables.prl

```bash
$ singularity exec <container> /usr/local/bin/merge-lmer-tables.prl
$ podman run --it --rm --entrypoint /usr/local/bin/merge-lmer-tables.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-lmer-tables.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nmerge

```bash
$ singularity exec <container> /usr/local/bin/nmerge
$ podman run --it --rm --entrypoint /usr/local/bin/nmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nseg

```bash
$ singularity exec <container> /usr/local/bin/nseg
$ podman run --it --rm --entrypoint /usr/local/bin/nseg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nseg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viewMSA.pl

```bash
$ singularity exec <container> /usr/local/bin/viewMSA.pl
$ podman run --it --rm --entrypoint /usr/local/bin/viewMSA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viewMSA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wublastToCrossmatch.pl

```bash
$ singularity exec <container> /usr/local/bin/wublastToCrossmatch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wublastToCrossmatch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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