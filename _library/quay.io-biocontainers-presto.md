---
layout: container
name:  "quay.io/biocontainers/presto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/presto/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/presto/container.yaml"
updated_at: "2022-10-29 05:38:12.220523"
latest: "0.7.1--pyhdfd78af_0"
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
 - "2to3-3.10"
 - "accn-at-a-time"
 - "align-columns"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asn2xml"
 - "between-two-genes"
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
versions:
 - "0.7.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for presto"
config: {"url": "https://biocontainers.pro/tools/presto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for presto", "latest": {"0.7.1--pyhdfd78af_0": "sha256:2743943d2cb9065b7d19853ad972dcaa6977905e3edf3c0a4cc1fa295691e1c5"}, "tags": {"0.7.1--pyhdfd78af_0": "sha256:2743943d2cb9065b7d19853ad972dcaa6977905e3edf3c0a4cc1fa295691e1c5"}, "docker": "quay.io/biocontainers/presto", "aliases": {"AlignSets.py": "/usr/local/bin/AlignSets.py", "AssemblePairs.py": "/usr/local/bin/AssemblePairs.py", "BuildConsensus.py": "/usr/local/bin/BuildConsensus.py", "ClusterSets.py": "/usr/local/bin/ClusterSets.py", "CollapseSeq.py": "/usr/local/bin/CollapseSeq.py", "ConvertHeaders.py": "/usr/local/bin/ConvertHeaders.py", "EstimateError.py": "/usr/local/bin/EstimateError.py", "FilterSeq.py": "/usr/local/bin/FilterSeq.py", "MaskPrimers.py": "/usr/local/bin/MaskPrimers.py", "PairSeq.py": "/usr/local/bin/PairSeq.py", "ParseHeaders.py": "/usr/local/bin/ParseHeaders.py", "ParseLog.py": "/usr/local/bin/ParseLog.py", "SplitSeq.py": "/usr/local/bin/SplitSeq.py", "UnifyHeaders.py": "/usr/local/bin/UnifyHeaders.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "align-columns": "/usr/local/bin/align-columns", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asn2xml": "/usr/local/bin/asn2xml", "between-two-genes": "/usr/local/bin/between-two-genes", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/presto.
shpc-registry automated BioContainers addition for presto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/presto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/presto:0.7.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/presto/0.7.1--pyhdfd78af_0
$ module help quay.io/biocontainers/presto/0.7.1--pyhdfd78af_0
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


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2xml

```bash
$ singularity exec <container> /usr/local/bin/asn2xml
$ podman run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### between-two-genes

```bash
$ singularity exec <container> /usr/local/bin/between-two-genes
$ podman run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool

```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcheck

```bash
$ singularity exec <container> /usr/local/bin/blastdbcheck
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
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