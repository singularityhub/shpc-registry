---
layout: container
name:  "quay.io/biocontainers/changeo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/changeo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/changeo/container.yaml"
updated_at: "2025-03-19 03:00:38.732099"
latest: "1.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/changeo"
aliases:
 - "AlignRecords.py"
 - "AlignSets.py"
 - "AssemblePairs.py"
 - "AssignGenes.py"
 - "BuildConsensus.py"
 - "BuildTrees.py"
 - "ClusterSets.py"
 - "CollapseSeq.py"
 - "ConvertDb.py"
 - "ConvertHeaders.py"
 - "CreateGermlines.py"
 - "DefineClones.py"
 - "EstimateError.py"
 - "FilterSeq.py"
 - "MakeDb.py"
 - "MaskPrimers.py"
 - "PairSeq.py"
 - "ParseDb.py"
 - "ParseHeaders.py"
 - "ParseLog.py"
 - "SplitSeq.py"
 - "UnifyHeaders.py"
 - "airr-tools"
 - "filter-table"
 - "spdi2prod"
 - "vsearch"
 - "muscle"
 - "align-columns"
 - "blst2tkns"
 - "csv2xml"
 - "disambiguate-nucleotides"
 - "download-ncbi-software"
 - "ecommon.sh"
versions:
 - "1.2.0--pyhdfd78af_0"
 - "1.3.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for changeo"
config: {"url": "https://biocontainers.pro/tools/changeo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for changeo", "latest": {"1.3.0--pyhdfd78af_0": "sha256:acd1e9be93a279e4ea03a27d34813636e5354a4dc1c11b1a846862d9b2663220"}, "tags": {"1.2.0--pyhdfd78af_0": "sha256:aa3dc82f13ac8ac5f932b8fa97397bf9138c955196e8c3695b1df5c89ab8d3df", "1.3.0--pyhdfd78af_0": "sha256:acd1e9be93a279e4ea03a27d34813636e5354a4dc1c11b1a846862d9b2663220"}, "docker": "quay.io/biocontainers/changeo", "aliases": {"AlignRecords.py": "/usr/local/bin/AlignRecords.py", "AlignSets.py": "/usr/local/bin/AlignSets.py", "AssemblePairs.py": "/usr/local/bin/AssemblePairs.py", "AssignGenes.py": "/usr/local/bin/AssignGenes.py", "BuildConsensus.py": "/usr/local/bin/BuildConsensus.py", "BuildTrees.py": "/usr/local/bin/BuildTrees.py", "ClusterSets.py": "/usr/local/bin/ClusterSets.py", "CollapseSeq.py": "/usr/local/bin/CollapseSeq.py", "ConvertDb.py": "/usr/local/bin/ConvertDb.py", "ConvertHeaders.py": "/usr/local/bin/ConvertHeaders.py", "CreateGermlines.py": "/usr/local/bin/CreateGermlines.py", "DefineClones.py": "/usr/local/bin/DefineClones.py", "EstimateError.py": "/usr/local/bin/EstimateError.py", "FilterSeq.py": "/usr/local/bin/FilterSeq.py", "MakeDb.py": "/usr/local/bin/MakeDb.py", "MaskPrimers.py": "/usr/local/bin/MaskPrimers.py", "PairSeq.py": "/usr/local/bin/PairSeq.py", "ParseDb.py": "/usr/local/bin/ParseDb.py", "ParseHeaders.py": "/usr/local/bin/ParseHeaders.py", "ParseLog.py": "/usr/local/bin/ParseLog.py", "SplitSeq.py": "/usr/local/bin/SplitSeq.py", "UnifyHeaders.py": "/usr/local/bin/UnifyHeaders.py", "airr-tools": "/usr/local/bin/airr-tools", "filter-table": "/usr/local/bin/filter-table", "spdi2prod": "/usr/local/bin/spdi2prod", "vsearch": "/usr/local/bin/vsearch", "muscle": "/usr/local/bin/muscle", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides", "download-ncbi-software": "/usr/local/bin/download-ncbi-software", "ecommon.sh": "/usr/local/bin/ecommon.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/changeo.
shpc-registry automated BioContainers addition for changeo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/changeo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/changeo:1.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/changeo/1.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/changeo/1.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### changeo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### changeo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### changeo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### changeo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### changeo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### changeo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AlignRecords.py

```bash
$ singularity exec <container> /usr/local/bin/AlignRecords.py
$ podman run --it --rm --entrypoint /usr/local/bin/AlignRecords.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AlignRecords.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AlignSets.py

```bash
$ singularity exec <container> /usr/local/bin/AlignSets.py
$ podman run --it --rm --entrypoint /usr/local/bin/AlignSets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AlignSets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AssemblePairs.py

```bash
$ singularity exec <container> /usr/local/bin/AssemblePairs.py
$ podman run --it --rm --entrypoint /usr/local/bin/AssemblePairs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AssemblePairs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AssignGenes.py

```bash
$ singularity exec <container> /usr/local/bin/AssignGenes.py
$ podman run --it --rm --entrypoint /usr/local/bin/AssignGenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AssignGenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BuildConsensus.py

```bash
$ singularity exec <container> /usr/local/bin/BuildConsensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/BuildConsensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BuildConsensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BuildTrees.py

```bash
$ singularity exec <container> /usr/local/bin/BuildTrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/BuildTrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BuildTrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ClusterSets.py

```bash
$ singularity exec <container> /usr/local/bin/ClusterSets.py
$ podman run --it --rm --entrypoint /usr/local/bin/ClusterSets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ClusterSets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CollapseSeq.py

```bash
$ singularity exec <container> /usr/local/bin/CollapseSeq.py
$ podman run --it --rm --entrypoint /usr/local/bin/CollapseSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CollapseSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ConvertDb.py

```bash
$ singularity exec <container> /usr/local/bin/ConvertDb.py
$ podman run --it --rm --entrypoint /usr/local/bin/ConvertDb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ConvertDb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ConvertHeaders.py

```bash
$ singularity exec <container> /usr/local/bin/ConvertHeaders.py
$ podman run --it --rm --entrypoint /usr/local/bin/ConvertHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ConvertHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateGermlines.py

```bash
$ singularity exec <container> /usr/local/bin/CreateGermlines.py
$ podman run --it --rm --entrypoint /usr/local/bin/CreateGermlines.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CreateGermlines.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DefineClones.py

```bash
$ singularity exec <container> /usr/local/bin/DefineClones.py
$ podman run --it --rm --entrypoint /usr/local/bin/DefineClones.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DefineClones.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EstimateError.py

```bash
$ singularity exec <container> /usr/local/bin/EstimateError.py
$ podman run --it --rm --entrypoint /usr/local/bin/EstimateError.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EstimateError.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FilterSeq.py

```bash
$ singularity exec <container> /usr/local/bin/FilterSeq.py
$ podman run --it --rm --entrypoint /usr/local/bin/FilterSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FilterSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeDb.py

```bash
$ singularity exec <container> /usr/local/bin/MakeDb.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeDb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeDb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaskPrimers.py

```bash
$ singularity exec <container> /usr/local/bin/MaskPrimers.py
$ podman run --it --rm --entrypoint /usr/local/bin/MaskPrimers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaskPrimers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PairSeq.py

```bash
$ singularity exec <container> /usr/local/bin/PairSeq.py
$ podman run --it --rm --entrypoint /usr/local/bin/PairSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PairSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ParseDb.py

```bash
$ singularity exec <container> /usr/local/bin/ParseDb.py
$ podman run --it --rm --entrypoint /usr/local/bin/ParseDb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ParseDb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ParseHeaders.py

```bash
$ singularity exec <container> /usr/local/bin/ParseHeaders.py
$ podman run --it --rm --entrypoint /usr/local/bin/ParseHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ParseHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ParseLog.py

```bash
$ singularity exec <container> /usr/local/bin/ParseLog.py
$ podman run --it --rm --entrypoint /usr/local/bin/ParseLog.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ParseLog.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SplitSeq.py

```bash
$ singularity exec <container> /usr/local/bin/SplitSeq.py
$ podman run --it --rm --entrypoint /usr/local/bin/SplitSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SplitSeq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### UnifyHeaders.py

```bash
$ singularity exec <container> /usr/local/bin/UnifyHeaders.py
$ podman run --it --rm --entrypoint /usr/local/bin/UnifyHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/UnifyHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### airr-tools

```bash
$ singularity exec <container> /usr/local/bin/airr-tools
$ podman run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-table

```bash
$ singularity exec <container> /usr/local/bin/filter-table
$ podman run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2prod

```bash
$ singularity exec <container> /usr/local/bin/spdi2prod
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2tkns

```bash
$ singularity exec <container> /usr/local/bin/blst2tkns
$ podman run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2xml

```bash
$ singularity exec <container> /usr/local/bin/csv2xml
$ podman run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disambiguate-nucleotides

```bash
$ singularity exec <container> /usr/local/bin/disambiguate-nucleotides
$ podman run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-ncbi-software

```bash
$ singularity exec <container> /usr/local/bin/download-ncbi-software
$ podman run --it --rm --entrypoint /usr/local/bin/download-ncbi-software   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-ncbi-software   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecommon.sh

```bash
$ singularity exec <container> /usr/local/bin/ecommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ecommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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