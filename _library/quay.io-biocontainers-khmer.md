---
layout: container
name:  "quay.io/biocontainers/khmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/khmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/khmer/container.yaml"
updated_at: "2025-05-10 03:05:59.926103"
latest: "3.0.0a3--py311heabec7a_7"
container_url: "https://biocontainers.pro/tools/khmer"
aliases:
 - "abundance-dist-single.py"
 - "abundance-dist.py"
 - "annotate-partitions.py"
 - "count-median.py"
 - "do-partition.py"
 - "extract-long-sequences.py"
 - "extract-paired-reads.py"
 - "extract-partitions.py"
 - "fastq-to-fasta.py"
 - "filter-abund-single.py"
 - "filter-abund.py"
 - "filter-stoptags.py"
 - "find-knots.py"
 - "interleave-reads.py"
 - "load-graph.py"
 - "load-into-counting.py"
 - "make-initial-stoptags.py"
 - "merge-partitions.py"
 - "normalize-by-median.py"
 - "partition-graph.py"
 - "readstats.py"
 - "sample-reads-randomly.py"
 - "split-paired-reads.py"
 - "trim-low-abund.py"
 - "unique-kmers.py"
 - "screed"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "3.0.0a3--py37h2c368fa_3"
 - "3.0.0a3--py38h94ffb2d_3"
 - "3.0.0a3--py311heabec7a_7"
description: "shpc-registry automated BioContainers addition for khmer"
config: {"url": "https://biocontainers.pro/tools/khmer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for khmer", "latest": {"3.0.0a3--py311heabec7a_7": "sha256:dadc5f626b089963b527f9a2a65631ccdfd281aebcbabe85fda0bc32372f0405"}, "tags": {"3.0.0a3--py37h2c368fa_3": "sha256:91c918296f50103ee616f9f0832f19298cbbc6c21927b3afe5d89b5ec9f92523", "3.0.0a3--py38h94ffb2d_3": "sha256:a1a77dd003cb43dfe61d69436bb833e60d36edfd83cf40bae0a2298870584e50", "3.0.0a3--py311heabec7a_7": "sha256:dadc5f626b089963b527f9a2a65631ccdfd281aebcbabe85fda0bc32372f0405"}, "docker": "quay.io/biocontainers/khmer", "aliases": {"abundance-dist-single.py": "/usr/local/bin/abundance-dist-single.py", "abundance-dist.py": "/usr/local/bin/abundance-dist.py", "annotate-partitions.py": "/usr/local/bin/annotate-partitions.py", "count-median.py": "/usr/local/bin/count-median.py", "do-partition.py": "/usr/local/bin/do-partition.py", "extract-long-sequences.py": "/usr/local/bin/extract-long-sequences.py", "extract-paired-reads.py": "/usr/local/bin/extract-paired-reads.py", "extract-partitions.py": "/usr/local/bin/extract-partitions.py", "fastq-to-fasta.py": "/usr/local/bin/fastq-to-fasta.py", "filter-abund-single.py": "/usr/local/bin/filter-abund-single.py", "filter-abund.py": "/usr/local/bin/filter-abund.py", "filter-stoptags.py": "/usr/local/bin/filter-stoptags.py", "find-knots.py": "/usr/local/bin/find-knots.py", "interleave-reads.py": "/usr/local/bin/interleave-reads.py", "load-graph.py": "/usr/local/bin/load-graph.py", "load-into-counting.py": "/usr/local/bin/load-into-counting.py", "make-initial-stoptags.py": "/usr/local/bin/make-initial-stoptags.py", "merge-partitions.py": "/usr/local/bin/merge-partitions.py", "normalize-by-median.py": "/usr/local/bin/normalize-by-median.py", "partition-graph.py": "/usr/local/bin/partition-graph.py", "readstats.py": "/usr/local/bin/readstats.py", "sample-reads-randomly.py": "/usr/local/bin/sample-reads-randomly.py", "split-paired-reads.py": "/usr/local/bin/split-paired-reads.py", "trim-low-abund.py": "/usr/local/bin/trim-low-abund.py", "unique-kmers.py": "/usr/local/bin/unique-kmers.py", "screed": "/usr/local/bin/screed", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/khmer.
shpc-registry automated BioContainers addition for khmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/khmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/khmer:3.0.0a3--py311heabec7a_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/khmer/3.0.0a3--py311heabec7a_7
$ module help quay.io/biocontainers/khmer/3.0.0a3--py311heabec7a_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### khmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### khmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### khmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### khmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### khmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### khmer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abundance-dist-single.py

```bash
$ singularity exec <container> /usr/local/bin/abundance-dist-single.py
$ podman run --it --rm --entrypoint /usr/local/bin/abundance-dist-single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abundance-dist-single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abundance-dist.py

```bash
$ singularity exec <container> /usr/local/bin/abundance-dist.py
$ podman run --it --rm --entrypoint /usr/local/bin/abundance-dist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abundance-dist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate-partitions.py

```bash
$ singularity exec <container> /usr/local/bin/annotate-partitions.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count-median.py

```bash
$ singularity exec <container> /usr/local/bin/count-median.py
$ podman run --it --rm --entrypoint /usr/local/bin/count-median.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count-median.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### do-partition.py

```bash
$ singularity exec <container> /usr/local/bin/do-partition.py
$ podman run --it --rm --entrypoint /usr/local/bin/do-partition.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/do-partition.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-long-sequences.py

```bash
$ singularity exec <container> /usr/local/bin/extract-long-sequences.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract-long-sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-long-sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-paired-reads.py

```bash
$ singularity exec <container> /usr/local/bin/extract-paired-reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract-paired-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-paired-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-partitions.py

```bash
$ singularity exec <container> /usr/local/bin/extract-partitions.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-to-fasta.py

```bash
$ singularity exec <container> /usr/local/bin/fastq-to-fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-to-fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-to-fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-abund-single.py

```bash
$ singularity exec <container> /usr/local/bin/filter-abund-single.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter-abund-single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-abund-single.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-abund.py

```bash
$ singularity exec <container> /usr/local/bin/filter-abund.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter-abund.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-abund.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-stoptags.py

```bash
$ singularity exec <container> /usr/local/bin/filter-stoptags.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter-stoptags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-stoptags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-knots.py

```bash
$ singularity exec <container> /usr/local/bin/find-knots.py
$ podman run --it --rm --entrypoint /usr/local/bin/find-knots.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-knots.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interleave-reads.py

```bash
$ singularity exec <container> /usr/local/bin/interleave-reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/interleave-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interleave-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### load-graph.py

```bash
$ singularity exec <container> /usr/local/bin/load-graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/load-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/load-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### load-into-counting.py

```bash
$ singularity exec <container> /usr/local/bin/load-into-counting.py
$ podman run --it --rm --entrypoint /usr/local/bin/load-into-counting.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/load-into-counting.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make-initial-stoptags.py

```bash
$ singularity exec <container> /usr/local/bin/make-initial-stoptags.py
$ podman run --it --rm --entrypoint /usr/local/bin/make-initial-stoptags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make-initial-stoptags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-partitions.py

```bash
$ singularity exec <container> /usr/local/bin/merge-partitions.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize-by-median.py

```bash
$ singularity exec <container> /usr/local/bin/normalize-by-median.py
$ podman run --it --rm --entrypoint /usr/local/bin/normalize-by-median.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize-by-median.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### partition-graph.py

```bash
$ singularity exec <container> /usr/local/bin/partition-graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/partition-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/partition-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readstats.py

```bash
$ singularity exec <container> /usr/local/bin/readstats.py
$ podman run --it --rm --entrypoint /usr/local/bin/readstats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readstats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample-reads-randomly.py

```bash
$ singularity exec <container> /usr/local/bin/sample-reads-randomly.py
$ podman run --it --rm --entrypoint /usr/local/bin/sample-reads-randomly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample-reads-randomly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-paired-reads.py

```bash
$ singularity exec <container> /usr/local/bin/split-paired-reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/split-paired-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-paired-reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim-low-abund.py

```bash
$ singularity exec <container> /usr/local/bin/trim-low-abund.py
$ podman run --it --rm --entrypoint /usr/local/bin/trim-low-abund.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim-low-abund.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unique-kmers.py

```bash
$ singularity exec <container> /usr/local/bin/unique-kmers.py
$ podman run --it --rm --entrypoint /usr/local/bin/unique-kmers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unique-kmers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### screed

```bash
$ singularity exec <container> /usr/local/bin/screed
$ podman run --it --rm --entrypoint /usr/local/bin/screed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/screed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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