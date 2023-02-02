---
layout: container
name:  "quay.io/biocontainers/sourmash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sourmash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sourmash/container.yaml"
updated_at: "2023-02-02 03:17:24.041744"
latest: "2.0.0a11--py35hfc679d8_0"
container_url: "https://biocontainers.pro/tools/sourmash"
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
 - "sourmash"
 - "split-paired-reads.py"
 - "trim-low-abund.py"
 - "unique-kmers.py"
 - "screed"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
 - "qhelpconverter"
versions:
 - "2.0.0a9--py35hfc679d8_0"
 - "2.0.0a11--py35hfc679d8_0"
description: "shpc-registry automated BioContainers addition for sourmash"
config: {"url": "https://biocontainers.pro/tools/sourmash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sourmash", "latest": {"2.0.0a11--py35hfc679d8_0": "sha256:61531a5f0f7aabc4bf0807ccd4899d1b66d718e63ae5db378670d68b369f39d0"}, "tags": {"2.0.0a9--py35hfc679d8_0": "sha256:3b1431a5ef4d7a71ecb85bde2147c400dfc89529a8b06fc8e59a8c8073e11874", "2.0.0a11--py35hfc679d8_0": "sha256:61531a5f0f7aabc4bf0807ccd4899d1b66d718e63ae5db378670d68b369f39d0"}, "docker": "quay.io/biocontainers/sourmash", "aliases": {"abundance-dist-single.py": "/usr/local/bin/abundance-dist-single.py", "abundance-dist.py": "/usr/local/bin/abundance-dist.py", "annotate-partitions.py": "/usr/local/bin/annotate-partitions.py", "count-median.py": "/usr/local/bin/count-median.py", "do-partition.py": "/usr/local/bin/do-partition.py", "extract-long-sequences.py": "/usr/local/bin/extract-long-sequences.py", "extract-paired-reads.py": "/usr/local/bin/extract-paired-reads.py", "extract-partitions.py": "/usr/local/bin/extract-partitions.py", "fastq-to-fasta.py": "/usr/local/bin/fastq-to-fasta.py", "filter-abund-single.py": "/usr/local/bin/filter-abund-single.py", "filter-abund.py": "/usr/local/bin/filter-abund.py", "filter-stoptags.py": "/usr/local/bin/filter-stoptags.py", "find-knots.py": "/usr/local/bin/find-knots.py", "interleave-reads.py": "/usr/local/bin/interleave-reads.py", "load-graph.py": "/usr/local/bin/load-graph.py", "load-into-counting.py": "/usr/local/bin/load-into-counting.py", "make-initial-stoptags.py": "/usr/local/bin/make-initial-stoptags.py", "merge-partitions.py": "/usr/local/bin/merge-partitions.py", "normalize-by-median.py": "/usr/local/bin/normalize-by-median.py", "partition-graph.py": "/usr/local/bin/partition-graph.py", "readstats.py": "/usr/local/bin/readstats.py", "sample-reads-randomly.py": "/usr/local/bin/sample-reads-randomly.py", "sourmash": "/usr/local/bin/sourmash", "split-paired-reads.py": "/usr/local/bin/split-paired-reads.py", "trim-low-abund.py": "/usr/local/bin/trim-low-abund.py", "unique-kmers.py": "/usr/local/bin/unique-kmers.py", "screed": "/usr/local/bin/screed", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5", "qhelpconverter": "/usr/local/bin/qhelpconverter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sourmash.
shpc-registry automated BioContainers addition for sourmash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sourmash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sourmash:2.0.0a11--py35hfc679d8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sourmash/2.0.0a11--py35hfc679d8_0
$ module help quay.io/biocontainers/sourmash/2.0.0a11--py35hfc679d8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sourmash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sourmash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sourmash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sourmash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sourmash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sourmash-inspect-deffile:

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


#### sourmash

```bash
$ singularity exec <container> /usr/local/bin/sourmash
$ podman run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m

```bash
$ singularity exec <container> /usr/local/bin/python3.5m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.5

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
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