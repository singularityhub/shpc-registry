---
layout: container
name:  "quay.io/biocontainers/zol"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zol/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/zol/container.yaml"
updated_at: "2023-07-19 03:48:54.820274"
latest: "1.2.8--py310h30d9df9_0"
container_url: "https://biocontainers.pro/tools/zol"
aliases:
 - "HYPHYMPI"
 - "ZOL"
 - "axel"
 - "clusterHeatmap.R"
 - "convertMiniprotGffToGbkAndProt.py"
 - "extractBiG-SCAPEclusters.py"
 - "fai"
 - "findOrthologs.py"
 - "gimme_taxa.py"
 - "hyphy"
 - "listAllGenomesInDirectory.py"
 - "ncbi-genome-download"
 - "ngd"
 - "pal2nal.pl"
 - "plotSegments.R"
 - "prepTG"
 - "processNCBIGenBank.py"
 - "pyrodigal"
 - "runProdigalAndMakeProperGenbank.py"
 - "runRBH"
 - "setup_annotation_dbs.py"
 - "skani"
 - "slclust"
 - "splitDiamondResults"
 - "splitDiamondResultsForFai"
 - "zol"
 - "readal"
 - "statal"
 - "trimal"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zmore"
 - "znew"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
versions:
 - "1.2.7--py310h30d9df9_0"
 - "1.2.8--py310h30d9df9_0"
description: "singularity registry hpc automated addition for zol"
config: {"url": "https://biocontainers.pro/tools/zol", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for zol", "latest": {"1.2.8--py310h30d9df9_0": "sha256:525638de0d1e583d55a1774922d12f4b93b6bf00b3d193088ee832496c86f256"}, "tags": {"1.2.7--py310h30d9df9_0": "sha256:e6fecbf5fb5bcd06df49b8a06e02f19b49046af79a05d377e66a845834e78258", "1.2.8--py310h30d9df9_0": "sha256:525638de0d1e583d55a1774922d12f4b93b6bf00b3d193088ee832496c86f256"}, "docker": "quay.io/biocontainers/zol", "aliases": {"HYPHYMPI": "/usr/local/bin/HYPHYMPI", "ZOL": "/usr/local/bin/ZOL", "axel": "/usr/local/bin/axel", "clusterHeatmap.R": "/usr/local/bin/clusterHeatmap.R", "convertMiniprotGffToGbkAndProt.py": "/usr/local/bin/convertMiniprotGffToGbkAndProt.py", "extractBiG-SCAPEclusters.py": "/usr/local/bin/extractBiG-SCAPEclusters.py", "fai": "/usr/local/bin/fai", "findOrthologs.py": "/usr/local/bin/findOrthologs.py", "gimme_taxa.py": "/usr/local/bin/gimme_taxa.py", "hyphy": "/usr/local/bin/hyphy", "listAllGenomesInDirectory.py": "/usr/local/bin/listAllGenomesInDirectory.py", "ncbi-genome-download": "/usr/local/bin/ncbi-genome-download", "ngd": "/usr/local/bin/ngd", "pal2nal.pl": "/usr/local/bin/pal2nal.pl", "plotSegments.R": "/usr/local/bin/plotSegments.R", "prepTG": "/usr/local/bin/prepTG", "processNCBIGenBank.py": "/usr/local/bin/processNCBIGenBank.py", "pyrodigal": "/usr/local/bin/pyrodigal", "runProdigalAndMakeProperGenbank.py": "/usr/local/bin/runProdigalAndMakeProperGenbank.py", "runRBH": "/usr/local/bin/runRBH", "setup_annotation_dbs.py": "/usr/local/bin/setup_annotation_dbs.py", "skani": "/usr/local/bin/skani", "slclust": "/usr/local/bin/slclust", "splitDiamondResults": "/usr/local/bin/splitDiamondResults", "splitDiamondResultsForFai": "/usr/local/bin/splitDiamondResultsForFai", "zol": "/usr/local/bin/zol", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal", "trimal": "/usr/local/bin/trimal", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zol.
singularity registry hpc automated addition for zol
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zol
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zol:1.2.8--py310h30d9df9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zol/1.2.8--py310h30d9df9_0
$ module help quay.io/biocontainers/zol/1.2.8--py310h30d9df9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zol-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zol-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zol-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zol-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zol-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zol-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HYPHYMPI

```bash
$ singularity exec <container> /usr/local/bin/HYPHYMPI
$ podman run --it --rm --entrypoint /usr/local/bin/HYPHYMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HYPHYMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ZOL

```bash
$ singularity exec <container> /usr/local/bin/ZOL
$ podman run --it --rm --entrypoint /usr/local/bin/ZOL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ZOL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axel

```bash
$ singularity exec <container> /usr/local/bin/axel
$ podman run --it --rm --entrypoint /usr/local/bin/axel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterHeatmap.R

```bash
$ singularity exec <container> /usr/local/bin/clusterHeatmap.R
$ podman run --it --rm --entrypoint /usr/local/bin/clusterHeatmap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterHeatmap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertMiniprotGffToGbkAndProt.py

```bash
$ singularity exec <container> /usr/local/bin/convertMiniprotGffToGbkAndProt.py
$ podman run --it --rm --entrypoint /usr/local/bin/convertMiniprotGffToGbkAndProt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertMiniprotGffToGbkAndProt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractBiG-SCAPEclusters.py

```bash
$ singularity exec <container> /usr/local/bin/extractBiG-SCAPEclusters.py
$ podman run --it --rm --entrypoint /usr/local/bin/extractBiG-SCAPEclusters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractBiG-SCAPEclusters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fai

```bash
$ singularity exec <container> /usr/local/bin/fai
$ podman run --it --rm --entrypoint /usr/local/bin/fai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findOrthologs.py

```bash
$ singularity exec <container> /usr/local/bin/findOrthologs.py
$ podman run --it --rm --entrypoint /usr/local/bin/findOrthologs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findOrthologs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gimme_taxa.py

```bash
$ singularity exec <container> /usr/local/bin/gimme_taxa.py
$ podman run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hyphy

```bash
$ singularity exec <container> /usr/local/bin/hyphy
$ podman run --it --rm --entrypoint /usr/local/bin/hyphy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hyphy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### listAllGenomesInDirectory.py

```bash
$ singularity exec <container> /usr/local/bin/listAllGenomesInDirectory.py
$ podman run --it --rm --entrypoint /usr/local/bin/listAllGenomesInDirectory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/listAllGenomesInDirectory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-genome-download

```bash
$ singularity exec <container> /usr/local/bin/ncbi-genome-download
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngd

```bash
$ singularity exec <container> /usr/local/bin/ngd
$ podman run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pal2nal.pl

```bash
$ singularity exec <container> /usr/local/bin/pal2nal.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotSegments.R

```bash
$ singularity exec <container> /usr/local/bin/plotSegments.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotSegments.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotSegments.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepTG

```bash
$ singularity exec <container> /usr/local/bin/prepTG
$ podman run --it --rm --entrypoint /usr/local/bin/prepTG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepTG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### processNCBIGenBank.py

```bash
$ singularity exec <container> /usr/local/bin/processNCBIGenBank.py
$ podman run --it --rm --entrypoint /usr/local/bin/processNCBIGenBank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/processNCBIGenBank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runProdigalAndMakeProperGenbank.py

```bash
$ singularity exec <container> /usr/local/bin/runProdigalAndMakeProperGenbank.py
$ podman run --it --rm --entrypoint /usr/local/bin/runProdigalAndMakeProperGenbank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runProdigalAndMakeProperGenbank.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runRBH

```bash
$ singularity exec <container> /usr/local/bin/runRBH
$ podman run --it --rm --entrypoint /usr/local/bin/runRBH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runRBH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup_annotation_dbs.py

```bash
$ singularity exec <container> /usr/local/bin/setup_annotation_dbs.py
$ podman run --it --rm --entrypoint /usr/local/bin/setup_annotation_dbs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup_annotation_dbs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skani

```bash
$ singularity exec <container> /usr/local/bin/skani
$ podman run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slclust

```bash
$ singularity exec <container> /usr/local/bin/slclust
$ podman run --it --rm --entrypoint /usr/local/bin/slclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitDiamondResults

```bash
$ singularity exec <container> /usr/local/bin/splitDiamondResults
$ podman run --it --rm --entrypoint /usr/local/bin/splitDiamondResults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitDiamondResults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitDiamondResultsForFai

```bash
$ singularity exec <container> /usr/local/bin/splitDiamondResultsForFai
$ podman run --it --rm --entrypoint /usr/local/bin/splitDiamondResultsForFai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitDiamondResultsForFai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zol

```bash
$ singularity exec <container> /usr/local/bin/zol
$ podman run --it --rm --entrypoint /usr/local/bin/zol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
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