---
layout: container
name:  "quay.io/biocontainers/kwip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kwip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kwip/container.yaml"
updated_at: "2025-03-05 02:57:51.801107"
latest: "0.2.0--h5b5514e_5"
container_url: "https://biocontainers.pro/tools/kwip"
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
 - "kwip"
 - "kwip-stats"
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
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.2.0--h5b5514e_5"
description: "shpc-registry automated BioContainers addition for kwip"
config: {"url": "https://biocontainers.pro/tools/kwip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kwip", "latest": {"0.2.0--h5b5514e_5": "sha256:6324ef01803096631bafd696c5b31b267a264ef92289d3652abe26d8081661c8"}, "tags": {"0.2.0--h5b5514e_5": "sha256:6324ef01803096631bafd696c5b31b267a264ef92289d3652abe26d8081661c8"}, "docker": "quay.io/biocontainers/kwip", "aliases": {"abundance-dist-single.py": "/usr/local/bin/abundance-dist-single.py", "abundance-dist.py": "/usr/local/bin/abundance-dist.py", "annotate-partitions.py": "/usr/local/bin/annotate-partitions.py", "count-median.py": "/usr/local/bin/count-median.py", "do-partition.py": "/usr/local/bin/do-partition.py", "extract-long-sequences.py": "/usr/local/bin/extract-long-sequences.py", "extract-paired-reads.py": "/usr/local/bin/extract-paired-reads.py", "extract-partitions.py": "/usr/local/bin/extract-partitions.py", "fastq-to-fasta.py": "/usr/local/bin/fastq-to-fasta.py", "filter-abund-single.py": "/usr/local/bin/filter-abund-single.py", "filter-abund.py": "/usr/local/bin/filter-abund.py", "filter-stoptags.py": "/usr/local/bin/filter-stoptags.py", "find-knots.py": "/usr/local/bin/find-knots.py", "interleave-reads.py": "/usr/local/bin/interleave-reads.py", "kwip": "/usr/local/bin/kwip", "kwip-stats": "/usr/local/bin/kwip-stats", "load-graph.py": "/usr/local/bin/load-graph.py", "load-into-counting.py": "/usr/local/bin/load-into-counting.py", "make-initial-stoptags.py": "/usr/local/bin/make-initial-stoptags.py", "merge-partitions.py": "/usr/local/bin/merge-partitions.py", "normalize-by-median.py": "/usr/local/bin/normalize-by-median.py", "partition-graph.py": "/usr/local/bin/partition-graph.py", "readstats.py": "/usr/local/bin/readstats.py", "sample-reads-randomly.py": "/usr/local/bin/sample-reads-randomly.py", "split-paired-reads.py": "/usr/local/bin/split-paired-reads.py", "trim-low-abund.py": "/usr/local/bin/trim-low-abund.py", "unique-kmers.py": "/usr/local/bin/unique-kmers.py", "screed": "/usr/local/bin/screed", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kwip.
shpc-registry automated BioContainers addition for kwip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kwip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kwip:0.2.0--h5b5514e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kwip/0.2.0--h5b5514e_5
$ module help quay.io/biocontainers/kwip/0.2.0--h5b5514e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kwip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kwip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kwip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kwip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kwip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kwip-inspect-deffile:

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


#### kwip

```bash
$ singularity exec <container> /usr/local/bin/kwip
$ podman run --it --rm --entrypoint /usr/local/bin/kwip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kwip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kwip-stats

```bash
$ singularity exec <container> /usr/local/bin/kwip-stats
$ podman run --it --rm --entrypoint /usr/local/bin/kwip-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kwip-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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