---
layout: container
name:  "quay.io/biocontainers/cmash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cmash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cmash/container.yaml"
updated_at: "2023-04-18 02:57:23.491633"
latest: "0.5.2--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/cmash"
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
 - "merge-partitions.py"
 - "normalize-by-median.py"
 - "partition-graph.py"
 - "readstats.py"
 - "sample-reads-randomly.py"
 - "split-paired-reads.py"
 - "trim-low-abund.py"
 - "unique-kmers.py"
 - "screed"
 - "f2py3.8"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
versions:
 - "0.5.2--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for cmash"
config: {"url": "https://biocontainers.pro/tools/cmash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cmash", "latest": {"0.5.2--pyh5e36f6f_0": "sha256:106b89f56dd28dc588e54f50fba8018d9c2aff20e534351313d14e2cfbaf07b8"}, "tags": {"0.5.2--pyh5e36f6f_0": "sha256:106b89f56dd28dc588e54f50fba8018d9c2aff20e534351313d14e2cfbaf07b8"}, "docker": "quay.io/biocontainers/cmash", "aliases": {"MakeDNADatabase.py": "/usr/local/bin/MakeDNADatabase.py", "MakeNodeGraph.py": "/usr/local/bin/MakeNodeGraph.py", "MakeStreamingDNADatabase.py": "/usr/local/bin/MakeStreamingDNADatabase.py", "MakeStreamingPrefilter.py": "/usr/local/bin/MakeStreamingPrefilter.py", "QueryDNADatabase.py": "/usr/local/bin/QueryDNADatabase.py", "StreamingQueryDNADatabase.py": "/usr/local/bin/StreamingQueryDNADatabase.py", "StreamingQueryDNADatabase_queue.py": "/usr/local/bin/StreamingQueryDNADatabase_queue.py", "abundance-dist-single.py": "/usr/local/bin/abundance-dist-single.py", "abundance-dist.py": "/usr/local/bin/abundance-dist.py", "annotate-partitions.py": "/usr/local/bin/annotate-partitions.py", "count-median.py": "/usr/local/bin/count-median.py", "do-partition.py": "/usr/local/bin/do-partition.py", "extract-long-sequences.py": "/usr/local/bin/extract-long-sequences.py", "extract-paired-reads.py": "/usr/local/bin/extract-paired-reads.py", "extract-partitions.py": "/usr/local/bin/extract-partitions.py", "fastq-to-fasta.py": "/usr/local/bin/fastq-to-fasta.py", "filter-abund-single.py": "/usr/local/bin/filter-abund-single.py", "filter-abund.py": "/usr/local/bin/filter-abund.py", "filter-stoptags.py": "/usr/local/bin/filter-stoptags.py", "find-knots.py": "/usr/local/bin/find-knots.py", "interleave-reads.py": "/usr/local/bin/interleave-reads.py", "load-graph.py": "/usr/local/bin/load-graph.py", "load-into-counting.py": "/usr/local/bin/load-into-counting.py", "make-initial-stoptags.py": "/usr/local/bin/make-initial-stoptags.py", "merge-partitions.py": "/usr/local/bin/merge-partitions.py", "normalize-by-median.py": "/usr/local/bin/normalize-by-median.py", "partition-graph.py": "/usr/local/bin/partition-graph.py", "readstats.py": "/usr/local/bin/readstats.py", "sample-reads-randomly.py": "/usr/local/bin/sample-reads-randomly.py", "split-paired-reads.py": "/usr/local/bin/split-paired-reads.py", "trim-low-abund.py": "/usr/local/bin/trim-low-abund.py", "unique-kmers.py": "/usr/local/bin/unique-kmers.py", "screed": "/usr/local/bin/screed", "f2py3.8": "/usr/local/bin/f2py3.8", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cmash.
shpc-registry automated BioContainers addition for cmash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cmash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cmash:0.5.2--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cmash/0.5.2--pyh5e36f6f_0
$ module help quay.io/biocontainers/cmash/0.5.2--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cmash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cmash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cmash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cmash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cmash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cmash-inspect-deffile:

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


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
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