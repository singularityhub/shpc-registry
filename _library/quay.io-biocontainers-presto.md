---
layout: container
name:  "quay.io/biocontainers/presto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/presto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/presto/container.yaml"
updated_at: "2026-02-04 04:44:06.375918"
latest: "0.7.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/presto"
aliases:
 - "AlignSets.py"
 - "AssemblePairs.py"
 - "BuildConsensus.py"
 - "ClusterSets.py"
 - "CollapseSeq.py"
 - "ConvertHeaders.py"
 - "EstimateError.py"
 - "FilterSeq.py"
 - "MaskPrimers.py"
 - "PairSeq.py"
 - "ParseHeaders.py"
 - "ParseLog.py"
 - "SplitSeq.py"
 - "UnifyHeaders.py"
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
 - "0.7.1--pyhdfd78af_0"
 - "0.7.2--pyhdfd78af_0"
 - "0.7.4--pyhdfd78af_0"
 - "0.7.5--pyhdfd78af_0"
 - "0.7.6--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for presto"
config: {"url": "https://biocontainers.pro/tools/presto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for presto", "latest": {"0.7.6--pyhdfd78af_0": "sha256:5caeaf5a8674f622d5be94ce16f1ce64638690c5adc4e8416a9f485a2fd06ec6"}, "tags": {"0.7.1--pyhdfd78af_0": "sha256:2743943d2cb9065b7d19853ad972dcaa6977905e3edf3c0a4cc1fa295691e1c5", "0.7.2--pyhdfd78af_0": "sha256:8d5a941bb135b548c6657cbf5905af08cc5b86775049d3c6cae8263a090be1c4", "0.7.4--pyhdfd78af_0": "sha256:e62ce5a6b59d31dae19fcb34807d79f64f6924737f6adbc6ad0ced1f4152c803", "0.7.5--pyhdfd78af_0": "sha256:c50dc5bb86be281b99eaab5bdbe2f5899b7da07a6231daece3cf14d3ea9bfd07", "0.7.6--pyhdfd78af_0": "sha256:5caeaf5a8674f622d5be94ce16f1ce64638690c5adc4e8416a9f485a2fd06ec6"}, "docker": "quay.io/biocontainers/presto", "aliases": {"AlignSets.py": "/usr/local/bin/AlignSets.py", "AssemblePairs.py": "/usr/local/bin/AssemblePairs.py", "BuildConsensus.py": "/usr/local/bin/BuildConsensus.py", "ClusterSets.py": "/usr/local/bin/ClusterSets.py", "CollapseSeq.py": "/usr/local/bin/CollapseSeq.py", "ConvertHeaders.py": "/usr/local/bin/ConvertHeaders.py", "EstimateError.py": "/usr/local/bin/EstimateError.py", "FilterSeq.py": "/usr/local/bin/FilterSeq.py", "MaskPrimers.py": "/usr/local/bin/MaskPrimers.py", "PairSeq.py": "/usr/local/bin/PairSeq.py", "ParseHeaders.py": "/usr/local/bin/ParseHeaders.py", "ParseLog.py": "/usr/local/bin/ParseLog.py", "SplitSeq.py": "/usr/local/bin/SplitSeq.py", "UnifyHeaders.py": "/usr/local/bin/UnifyHeaders.py", "vsearch": "/usr/local/bin/vsearch", "muscle": "/usr/local/bin/muscle", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/presto.
shpc-registry automated BioContainers addition for presto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/presto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/presto:0.7.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/presto/0.7.6--pyhdfd78af_0
$ module help quay.io/biocontainers/presto/0.7.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### presto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### presto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### presto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### presto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### presto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### presto-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### BuildConsensus.py

```bash
$ singularity exec <container> /usr/local/bin/BuildConsensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/BuildConsensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BuildConsensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ConvertHeaders.py

```bash
$ singularity exec <container> /usr/local/bin/ConvertHeaders.py
$ podman run --it --rm --entrypoint /usr/local/bin/ConvertHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ConvertHeaders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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