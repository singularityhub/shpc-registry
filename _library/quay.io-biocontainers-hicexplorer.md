---
layout: container
name:  "quay.io/biocontainers/hicexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hicexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hicexplorer/container.yaml"
updated_at: "2023-01-12 03:04:49.724587"
latest: "2.2--py_1"
container_url: "https://biocontainers.pro/tools/hicexplorer"
aliases:
 - "dask-mpi"
 - "dask-remote"
 - "dask-submit"
 - "findRestSite"
 - "hicAdjustMatrix"
 - "hicAggregateContacts"
 - "hicAverageRegions"
 - "hicBuildMatrix"
 - "hicCompareMatrices"
 - "hicConvertFormat"
 - "hicCorrectMatrix"
 - "hicCorrelate"
 - "hicExport"
 - "hicFindEnrichedContacts"
 - "hicFindTADs"
 - "hicInfo"
 - "hicMergeMatrixBins"
 - "hicNormalize"
 - "hicPCA"
 - "hicPlotAverageRegions"
 - "hicPlotDistVsCounts"
 - "hicPlotMatrix"
 - "hicPlotTADs"
 - "hicPlotViewpoint"
 - "hicQC"
 - "hicSumMatrices"
 - "hicTransform"
 - "hicexplorer"
 - "make_tracks_file"
 - "pgt"
 - "pyGenomeTracks"
 - "cooler"
 - "unidecode"
 - "bam2pairs"
 - "column_remover.pl"
 - "conv-template"
 - "duplicate_header_remover.pl"
 - "fragment_4dnpairs.pl"
 - "from-template"
 - "juicer_shortform2pairs.pl"
 - "merge-pairs.sh"
versions:
 - "2.2beta--py36_0"
 - "2.2--py_1"
description: "shpc-registry automated BioContainers addition for hicexplorer"
config: {"url": "https://biocontainers.pro/tools/hicexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hicexplorer", "latest": {"2.2--py_1": "sha256:96c580bfc06e356a3991e791d58d8ee8d444e9b44cd97d18dfa7e77542359fb5"}, "tags": {"2.2beta--py36_0": "sha256:bacc2db9b335a33d14c1de11d2b0c67b44b4d31d3a6532894595d96c9dbd6815", "2.2--py_1": "sha256:96c580bfc06e356a3991e791d58d8ee8d444e9b44cd97d18dfa7e77542359fb5"}, "docker": "quay.io/biocontainers/hicexplorer", "aliases": {"dask-mpi": "/usr/local/bin/dask-mpi", "dask-remote": "/usr/local/bin/dask-remote", "dask-submit": "/usr/local/bin/dask-submit", "findRestSite": "/usr/local/bin/findRestSite", "hicAdjustMatrix": "/usr/local/bin/hicAdjustMatrix", "hicAggregateContacts": "/usr/local/bin/hicAggregateContacts", "hicAverageRegions": "/usr/local/bin/hicAverageRegions", "hicBuildMatrix": "/usr/local/bin/hicBuildMatrix", "hicCompareMatrices": "/usr/local/bin/hicCompareMatrices", "hicConvertFormat": "/usr/local/bin/hicConvertFormat", "hicCorrectMatrix": "/usr/local/bin/hicCorrectMatrix", "hicCorrelate": "/usr/local/bin/hicCorrelate", "hicExport": "/usr/local/bin/hicExport", "hicFindEnrichedContacts": "/usr/local/bin/hicFindEnrichedContacts", "hicFindTADs": "/usr/local/bin/hicFindTADs", "hicInfo": "/usr/local/bin/hicInfo", "hicMergeMatrixBins": "/usr/local/bin/hicMergeMatrixBins", "hicNormalize": "/usr/local/bin/hicNormalize", "hicPCA": "/usr/local/bin/hicPCA", "hicPlotAverageRegions": "/usr/local/bin/hicPlotAverageRegions", "hicPlotDistVsCounts": "/usr/local/bin/hicPlotDistVsCounts", "hicPlotMatrix": "/usr/local/bin/hicPlotMatrix", "hicPlotTADs": "/usr/local/bin/hicPlotTADs", "hicPlotViewpoint": "/usr/local/bin/hicPlotViewpoint", "hicQC": "/usr/local/bin/hicQC", "hicSumMatrices": "/usr/local/bin/hicSumMatrices", "hicTransform": "/usr/local/bin/hicTransform", "hicexplorer": "/usr/local/bin/hicexplorer", "make_tracks_file": "/usr/local/bin/make_tracks_file", "pgt": "/usr/local/bin/pgt", "pyGenomeTracks": "/usr/local/bin/pyGenomeTracks", "cooler": "/usr/local/bin/cooler", "unidecode": "/usr/local/bin/unidecode", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "conv-template": "/usr/local/bin/conv-template", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "from-template": "/usr/local/bin/from-template", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hicexplorer.
shpc-registry automated BioContainers addition for hicexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hicexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hicexplorer:2.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hicexplorer/2.2--py_1
$ module help quay.io/biocontainers/hicexplorer/2.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hicexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hicexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hicexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hicexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hicexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hicexplorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dask-mpi

```bash
$ singularity exec <container> /usr/local/bin/dask-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/dask-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-remote

```bash
$ singularity exec <container> /usr/local/bin/dask-remote
$ podman run --it --rm --entrypoint /usr/local/bin/dask-remote   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-remote   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-submit

```bash
$ singularity exec <container> /usr/local/bin/dask-submit
$ podman run --it --rm --entrypoint /usr/local/bin/dask-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findRestSite

```bash
$ singularity exec <container> /usr/local/bin/findRestSite
$ podman run --it --rm --entrypoint /usr/local/bin/findRestSite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findRestSite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicAdjustMatrix

```bash
$ singularity exec <container> /usr/local/bin/hicAdjustMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/hicAdjustMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicAdjustMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicAggregateContacts

```bash
$ singularity exec <container> /usr/local/bin/hicAggregateContacts
$ podman run --it --rm --entrypoint /usr/local/bin/hicAggregateContacts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicAggregateContacts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicAverageRegions

```bash
$ singularity exec <container> /usr/local/bin/hicAverageRegions
$ podman run --it --rm --entrypoint /usr/local/bin/hicAverageRegions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicAverageRegions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicBuildMatrix

```bash
$ singularity exec <container> /usr/local/bin/hicBuildMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/hicBuildMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicBuildMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicCompareMatrices

```bash
$ singularity exec <container> /usr/local/bin/hicCompareMatrices
$ podman run --it --rm --entrypoint /usr/local/bin/hicCompareMatrices   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicCompareMatrices   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicConvertFormat

```bash
$ singularity exec <container> /usr/local/bin/hicConvertFormat
$ podman run --it --rm --entrypoint /usr/local/bin/hicConvertFormat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicConvertFormat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicCorrectMatrix

```bash
$ singularity exec <container> /usr/local/bin/hicCorrectMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/hicCorrectMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicCorrectMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicCorrelate

```bash
$ singularity exec <container> /usr/local/bin/hicCorrelate
$ podman run --it --rm --entrypoint /usr/local/bin/hicCorrelate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicCorrelate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicExport

```bash
$ singularity exec <container> /usr/local/bin/hicExport
$ podman run --it --rm --entrypoint /usr/local/bin/hicExport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicExport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicFindEnrichedContacts

```bash
$ singularity exec <container> /usr/local/bin/hicFindEnrichedContacts
$ podman run --it --rm --entrypoint /usr/local/bin/hicFindEnrichedContacts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicFindEnrichedContacts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicFindTADs

```bash
$ singularity exec <container> /usr/local/bin/hicFindTADs
$ podman run --it --rm --entrypoint /usr/local/bin/hicFindTADs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicFindTADs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicInfo

```bash
$ singularity exec <container> /usr/local/bin/hicInfo
$ podman run --it --rm --entrypoint /usr/local/bin/hicInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicMergeMatrixBins

```bash
$ singularity exec <container> /usr/local/bin/hicMergeMatrixBins
$ podman run --it --rm --entrypoint /usr/local/bin/hicMergeMatrixBins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicMergeMatrixBins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicNormalize

```bash
$ singularity exec <container> /usr/local/bin/hicNormalize
$ podman run --it --rm --entrypoint /usr/local/bin/hicNormalize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicNormalize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicPCA

```bash
$ singularity exec <container> /usr/local/bin/hicPCA
$ podman run --it --rm --entrypoint /usr/local/bin/hicPCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicPCA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicPlotAverageRegions

```bash
$ singularity exec <container> /usr/local/bin/hicPlotAverageRegions
$ podman run --it --rm --entrypoint /usr/local/bin/hicPlotAverageRegions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicPlotAverageRegions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicPlotDistVsCounts

```bash
$ singularity exec <container> /usr/local/bin/hicPlotDistVsCounts
$ podman run --it --rm --entrypoint /usr/local/bin/hicPlotDistVsCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicPlotDistVsCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicPlotMatrix

```bash
$ singularity exec <container> /usr/local/bin/hicPlotMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/hicPlotMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicPlotMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicPlotTADs

```bash
$ singularity exec <container> /usr/local/bin/hicPlotTADs
$ podman run --it --rm --entrypoint /usr/local/bin/hicPlotTADs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicPlotTADs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicPlotViewpoint

```bash
$ singularity exec <container> /usr/local/bin/hicPlotViewpoint
$ podman run --it --rm --entrypoint /usr/local/bin/hicPlotViewpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicPlotViewpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicQC

```bash
$ singularity exec <container> /usr/local/bin/hicQC
$ podman run --it --rm --entrypoint /usr/local/bin/hicQC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicQC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicSumMatrices

```bash
$ singularity exec <container> /usr/local/bin/hicSumMatrices
$ podman run --it --rm --entrypoint /usr/local/bin/hicSumMatrices   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicSumMatrices   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicTransform

```bash
$ singularity exec <container> /usr/local/bin/hicTransform
$ podman run --it --rm --entrypoint /usr/local/bin/hicTransform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicTransform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicexplorer

```bash
$ singularity exec <container> /usr/local/bin/hicexplorer
$ podman run --it --rm --entrypoint /usr/local/bin/hicexplorer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicexplorer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_tracks_file

```bash
$ singularity exec <container> /usr/local/bin/make_tracks_file
$ podman run --it --rm --entrypoint /usr/local/bin/make_tracks_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_tracks_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgt

```bash
$ singularity exec <container> /usr/local/bin/pgt
$ podman run --it --rm --entrypoint /usr/local/bin/pgt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGenomeTracks

```bash
$ singularity exec <container> /usr/local/bin/pyGenomeTracks
$ podman run --it --rm --entrypoint /usr/local/bin/pyGenomeTracks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGenomeTracks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooler

```bash
$ singularity exec <container> /usr/local/bin/cooler
$ podman run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-pairs.sh

```bash
$ singularity exec <container> /usr/local/bin/merge-pairs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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