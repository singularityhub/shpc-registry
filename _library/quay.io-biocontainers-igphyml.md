---
layout: container
name:  "quay.io/biocontainers/igphyml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/igphyml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/igphyml/container.yaml"
updated_at: "2025-12-19 05:04:49.765081"
latest: "1.1.5--h7b50bb2_2"
container_url: "https://biocontainers.pro/tools/igphyml"
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
 - "igphyml"
 - "vsearch"
 - "muscle"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
versions:
 - "1.1.4--hec16e2b_0"
 - "1.1.5--hec16e2b_0"
 - "1.1.5--h031d066_1"
 - "1.1.5--h7b50bb2_2"
description: "shpc-registry automated BioContainers addition for igphyml"
config: {"url": "https://biocontainers.pro/tools/igphyml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for igphyml", "latest": {"1.1.5--h7b50bb2_2": "sha256:e186a675b185004075f77bb3881e44d4af4134f047242be24697f042ead5ae56"}, "tags": {"1.1.4--hec16e2b_0": "sha256:5cbeb391e3b542c8048a91a2b089cc294ed65da6a78a2dd079d95524b907028d", "1.1.5--hec16e2b_0": "sha256:acac40085bc503bd2bc599a2a47d9f6708c8156aeda89aa9a7d292bfb948fe5d", "1.1.5--h031d066_1": "sha256:5e0258403e45027165174c0eabdcc8d3bd36ca0f015bf83a5a600ee82f241fa3", "1.1.5--h7b50bb2_2": "sha256:e186a675b185004075f77bb3881e44d4af4134f047242be24697f042ead5ae56"}, "docker": "quay.io/biocontainers/igphyml", "aliases": {"AlignRecords.py": "/usr/local/bin/AlignRecords.py", "AlignSets.py": "/usr/local/bin/AlignSets.py", "AssemblePairs.py": "/usr/local/bin/AssemblePairs.py", "AssignGenes.py": "/usr/local/bin/AssignGenes.py", "BuildConsensus.py": "/usr/local/bin/BuildConsensus.py", "BuildTrees.py": "/usr/local/bin/BuildTrees.py", "ClusterSets.py": "/usr/local/bin/ClusterSets.py", "CollapseSeq.py": "/usr/local/bin/CollapseSeq.py", "ConvertDb.py": "/usr/local/bin/ConvertDb.py", "ConvertHeaders.py": "/usr/local/bin/ConvertHeaders.py", "CreateGermlines.py": "/usr/local/bin/CreateGermlines.py", "DefineClones.py": "/usr/local/bin/DefineClones.py", "EstimateError.py": "/usr/local/bin/EstimateError.py", "FilterSeq.py": "/usr/local/bin/FilterSeq.py", "MakeDb.py": "/usr/local/bin/MakeDb.py", "MaskPrimers.py": "/usr/local/bin/MaskPrimers.py", "PairSeq.py": "/usr/local/bin/PairSeq.py", "ParseDb.py": "/usr/local/bin/ParseDb.py", "ParseHeaders.py": "/usr/local/bin/ParseHeaders.py", "ParseLog.py": "/usr/local/bin/ParseLog.py", "SplitSeq.py": "/usr/local/bin/SplitSeq.py", "UnifyHeaders.py": "/usr/local/bin/UnifyHeaders.py", "airr-tools": "/usr/local/bin/airr-tools", "igphyml": "/usr/local/bin/igphyml", "vsearch": "/usr/local/bin/vsearch", "muscle": "/usr/local/bin/muscle", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/igphyml.
shpc-registry automated BioContainers addition for igphyml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/igphyml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/igphyml:1.1.5--h7b50bb2_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/igphyml/1.1.5--h7b50bb2_2
$ module help quay.io/biocontainers/igphyml/1.1.5--h7b50bb2_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### igphyml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### igphyml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### igphyml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### igphyml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### igphyml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### igphyml-inspect-deffile:

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


#### igphyml

```bash
$ singularity exec <container> /usr/local/bin/igphyml
$ podman run --it --rm --entrypoint /usr/local/bin/igphyml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igphyml   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
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