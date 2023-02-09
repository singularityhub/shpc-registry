---
layout: container
name:  "quay.io/biocontainers/metalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metalign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metalign/container.yaml"
updated_at: "2023-02-09 03:05:39.056499"
latest: "0.12.5--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/metalign"
aliases:
 - "MakeDNADatabase.py"
 - "MakeNodeGraph.py"
 - "MakeStreamingDNADatabase.py"
 - "MakeStreamingPrefilter.py"
 - "QueryDNADatabase.py"
 - "StreamingQueryDNADatabase.py"
 - "StreamingQueryDNADatabase_queue.py"
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
 - "map_and_profile.py"
 - "merge-partitions.py"
 - "metalign.py"
 - "normalize-by-median.py"
 - "partition-graph.py"
 - "readstats.py"
 - "sample-reads-randomly.py"
 - "select_db.py"
 - "split-paired-reads.py"
 - "trim-low-abund.py"
 - "unique-kmers.py"
 - "screed"
 - "kmc"
 - "kmc_dump"
 - "kmc_tools"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "f2py3.7"
 - "2to3-3.7"
versions:
 - "0.12.5--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for metalign"
config: {"url": "https://biocontainers.pro/tools/metalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metalign", "latest": {"0.12.5--pyh864c0ab_1": "sha256:42c649b328c0d98d8f6436c7d9071fa4a60191fb094afb4c628e19ba01b54a46"}, "tags": {"0.12.5--pyh864c0ab_1": "sha256:42c649b328c0d98d8f6436c7d9071fa4a60191fb094afb4c628e19ba01b54a46"}, "docker": "quay.io/biocontainers/metalign", "aliases": {"MakeDNADatabase.py": "/usr/local/bin/MakeDNADatabase.py", "MakeNodeGraph.py": "/usr/local/bin/MakeNodeGraph.py", "MakeStreamingDNADatabase.py": "/usr/local/bin/MakeStreamingDNADatabase.py", "MakeStreamingPrefilter.py": "/usr/local/bin/MakeStreamingPrefilter.py", "QueryDNADatabase.py": "/usr/local/bin/QueryDNADatabase.py", "StreamingQueryDNADatabase.py": "/usr/local/bin/StreamingQueryDNADatabase.py", "StreamingQueryDNADatabase_queue.py": "/usr/local/bin/StreamingQueryDNADatabase_queue.py", "abundance-dist-single.py": "/usr/local/bin/abundance-dist-single.py", "abundance-dist.py": "/usr/local/bin/abundance-dist.py", "annotate-partitions.py": "/usr/local/bin/annotate-partitions.py", "count-median.py": "/usr/local/bin/count-median.py", "do-partition.py": "/usr/local/bin/do-partition.py", "extract-long-sequences.py": "/usr/local/bin/extract-long-sequences.py", "extract-paired-reads.py": "/usr/local/bin/extract-paired-reads.py", "extract-partitions.py": "/usr/local/bin/extract-partitions.py", "fastq-to-fasta.py": "/usr/local/bin/fastq-to-fasta.py", "filter-abund-single.py": "/usr/local/bin/filter-abund-single.py", "filter-abund.py": "/usr/local/bin/filter-abund.py", "filter-stoptags.py": "/usr/local/bin/filter-stoptags.py", "find-knots.py": "/usr/local/bin/find-knots.py", "interleave-reads.py": "/usr/local/bin/interleave-reads.py", "load-graph.py": "/usr/local/bin/load-graph.py", "load-into-counting.py": "/usr/local/bin/load-into-counting.py", "make-initial-stoptags.py": "/usr/local/bin/make-initial-stoptags.py", "map_and_profile.py": "/usr/local/bin/map_and_profile.py", "merge-partitions.py": "/usr/local/bin/merge-partitions.py", "metalign.py": "/usr/local/bin/metalign.py", "normalize-by-median.py": "/usr/local/bin/normalize-by-median.py", "partition-graph.py": "/usr/local/bin/partition-graph.py", "readstats.py": "/usr/local/bin/readstats.py", "sample-reads-randomly.py": "/usr/local/bin/sample-reads-randomly.py", "select_db.py": "/usr/local/bin/select_db.py", "split-paired-reads.py": "/usr/local/bin/split-paired-reads.py", "trim-low-abund.py": "/usr/local/bin/trim-low-abund.py", "unique-kmers.py": "/usr/local/bin/unique-kmers.py", "screed": "/usr/local/bin/screed", "kmc": "/usr/local/bin/kmc", "kmc_dump": "/usr/local/bin/kmc_dump", "kmc_tools": "/usr/local/bin/kmc_tools", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metalign.
shpc-registry automated BioContainers addition for metalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metalign:0.12.5--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metalign/0.12.5--pyh864c0ab_1
$ module help quay.io/biocontainers/metalign/0.12.5--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MakeDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/MakeDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeNodeGraph.py

```bash
$ singularity exec <container> /usr/local/bin/MakeNodeGraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeNodeGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeNodeGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeStreamingDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/MakeStreamingDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeStreamingDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeStreamingDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeStreamingPrefilter.py

```bash
$ singularity exec <container> /usr/local/bin/MakeStreamingPrefilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeStreamingPrefilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeStreamingPrefilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### QueryDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/QueryDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/QueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/QueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StreamingQueryDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/StreamingQueryDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StreamingQueryDNADatabase_queue.py

```bash
$ singularity exec <container> /usr/local/bin/StreamingQueryDNADatabase_queue.py
$ podman run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase_queue.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase_queue.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### map_and_profile.py

```bash
$ singularity exec <container> /usr/local/bin/map_and_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_and_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_and_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-partitions.py

```bash
$ singularity exec <container> /usr/local/bin/merge-partitions.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-partitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metalign.py

```bash
$ singularity exec <container> /usr/local/bin/metalign.py
$ podman run --it --rm --entrypoint /usr/local/bin/metalign.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metalign.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### select_db.py

```bash
$ singularity exec <container> /usr/local/bin/select_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/select_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_dump

```bash
$ singularity exec <container> /usr/local/bin/kmc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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