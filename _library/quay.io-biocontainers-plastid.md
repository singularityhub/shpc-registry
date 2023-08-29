---
layout: container
name:  "quay.io/biocontainers/plastid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plastid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plastid/container.yaml"
updated_at: "2023-08-29 03:48:48.127568"
latest: "0.6.1--py39had3e4b6_2"
container_url: "https://biocontainers.pro/tools/plastid"
aliases:
 - "counts_in_region"
 - "crossmap"
 - "cs"
 - "fasta_clipping_histogram.pl"
 - "fasta_formatter"
 - "fasta_nucleotide_changer"
 - "fastq_masker"
 - "fastq_quality_boxplot_graph.sh"
 - "fastq_quality_converter"
 - "fastq_quality_filter"
 - "fastq_quality_trimmer"
 - "fastq_to_fasta"
 - "fastx_artifacts_filter"
 - "fastx_barcode_splitter.pl"
 - "fastx_clipper"
 - "fastx_collapser"
 - "fastx_nucleotide_distribution_graph.sh"
 - "fastx_nucleotide_distribution_line_graph.sh"
 - "fastx_quality_stats"
 - "fastx_renamer"
 - "fastx_reverse_complement"
 - "fastx_trimmer"
 - "fastx_uncollapser"
 - "findjuncs"
 - "get_count_vectors"
 - "gff_parent_types"
 - "make_wiggle"
 - "metagene"
 - "phase_by_size"
 - "psite"
 - "reformat_transcripts"
 - "slidejuncs"
 - "test_table_equality"
 - "nosetests-3.9"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
 - "nosetests"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "fonttools"
 - "pyftmerge"
versions:
 - "0.6.1--py37ha26db04_0"
 - "0.6.1--py39h1b88516_1"
 - "0.6.1--py39had3e4b6_2"
description: "shpc-registry automated BioContainers addition for plastid"
config: {"url": "https://biocontainers.pro/tools/plastid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plastid", "latest": {"0.6.1--py39had3e4b6_2": "sha256:fa75c9a285863669b1d964a75c9d5900f57dd38d33ec584b18b65b48222be0aa"}, "tags": {"0.6.1--py37ha26db04_0": "sha256:2a3d98e213e3387fc81cc30c25f25c8824266c9738be2e1dc3f075daefe867a4", "0.6.1--py39h1b88516_1": "sha256:b1ca9e620e29006699101e06a874ed52823eab2435d7729cfc7312389e8b3398", "0.6.1--py39had3e4b6_2": "sha256:fa75c9a285863669b1d964a75c9d5900f57dd38d33ec584b18b65b48222be0aa"}, "docker": "quay.io/biocontainers/plastid", "aliases": {"counts_in_region": "/usr/local/bin/counts_in_region", "crossmap": "/usr/local/bin/crossmap", "cs": "/usr/local/bin/cs", "fasta_clipping_histogram.pl": "/usr/local/bin/fasta_clipping_histogram.pl", "fasta_formatter": "/usr/local/bin/fasta_formatter", "fasta_nucleotide_changer": "/usr/local/bin/fasta_nucleotide_changer", "fastq_masker": "/usr/local/bin/fastq_masker", "fastq_quality_boxplot_graph.sh": "/usr/local/bin/fastq_quality_boxplot_graph.sh", "fastq_quality_converter": "/usr/local/bin/fastq_quality_converter", "fastq_quality_filter": "/usr/local/bin/fastq_quality_filter", "fastq_quality_trimmer": "/usr/local/bin/fastq_quality_trimmer", "fastq_to_fasta": "/usr/local/bin/fastq_to_fasta", "fastx_artifacts_filter": "/usr/local/bin/fastx_artifacts_filter", "fastx_barcode_splitter.pl": "/usr/local/bin/fastx_barcode_splitter.pl", "fastx_clipper": "/usr/local/bin/fastx_clipper", "fastx_collapser": "/usr/local/bin/fastx_collapser", "fastx_nucleotide_distribution_graph.sh": "/usr/local/bin/fastx_nucleotide_distribution_graph.sh", "fastx_nucleotide_distribution_line_graph.sh": "/usr/local/bin/fastx_nucleotide_distribution_line_graph.sh", "fastx_quality_stats": "/usr/local/bin/fastx_quality_stats", "fastx_renamer": "/usr/local/bin/fastx_renamer", "fastx_reverse_complement": "/usr/local/bin/fastx_reverse_complement", "fastx_trimmer": "/usr/local/bin/fastx_trimmer", "fastx_uncollapser": "/usr/local/bin/fastx_uncollapser", "findjuncs": "/usr/local/bin/findjuncs", "get_count_vectors": "/usr/local/bin/get_count_vectors", "gff_parent_types": "/usr/local/bin/gff_parent_types", "make_wiggle": "/usr/local/bin/make_wiggle", "metagene": "/usr/local/bin/metagene", "phase_by_size": "/usr/local/bin/phase_by_size", "psite": "/usr/local/bin/psite", "reformat_transcripts": "/usr/local/bin/reformat_transcripts", "slidejuncs": "/usr/local/bin/slidejuncs", "test_table_equality": "/usr/local/bin/test_table_equality", "nosetests-3.9": "/usr/local/bin/nosetests-3.9", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "nosetests": "/usr/local/bin/nosetests", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plastid.
shpc-registry automated BioContainers addition for plastid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plastid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plastid:0.6.1--py39had3e4b6_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plastid/0.6.1--py39had3e4b6_2
$ module help quay.io/biocontainers/plastid/0.6.1--py39had3e4b6_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plastid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plastid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plastid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plastid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plastid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plastid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### counts_in_region

```bash
$ singularity exec <container> /usr/local/bin/counts_in_region
$ podman run --it --rm --entrypoint /usr/local/bin/counts_in_region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/counts_in_region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossmap

```bash
$ singularity exec <container> /usr/local/bin/crossmap
$ podman run --it --rm --entrypoint /usr/local/bin/crossmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cs

```bash
$ singularity exec <container> /usr/local/bin/cs
$ podman run --it --rm --entrypoint /usr/local/bin/cs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_clipping_histogram.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta_clipping_histogram.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_clipping_histogram.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_clipping_histogram.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_formatter

```bash
$ singularity exec <container> /usr/local/bin/fasta_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_nucleotide_changer

```bash
$ singularity exec <container> /usr/local/bin/fasta_nucleotide_changer
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_nucleotide_changer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_nucleotide_changer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_masker

```bash
$ singularity exec <container> /usr/local/bin/fastq_masker
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_quality_boxplot_graph.sh

```bash
$ singularity exec <container> /usr/local/bin/fastq_quality_boxplot_graph.sh
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_quality_boxplot_graph.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_quality_boxplot_graph.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_quality_converter

```bash
$ singularity exec <container> /usr/local/bin/fastq_quality_converter
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_quality_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_quality_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_quality_filter

```bash
$ singularity exec <container> /usr/local/bin/fastq_quality_filter
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_quality_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_quality_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_quality_trimmer

```bash
$ singularity exec <container> /usr/local/bin/fastq_quality_trimmer
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_quality_trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_quality_trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/fastq_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_artifacts_filter

```bash
$ singularity exec <container> /usr/local/bin/fastx_artifacts_filter
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_artifacts_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_artifacts_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_barcode_splitter.pl

```bash
$ singularity exec <container> /usr/local/bin/fastx_barcode_splitter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_barcode_splitter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_barcode_splitter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_clipper

```bash
$ singularity exec <container> /usr/local/bin/fastx_clipper
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_clipper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_clipper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_collapser

```bash
$ singularity exec <container> /usr/local/bin/fastx_collapser
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_collapser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_collapser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_nucleotide_distribution_graph.sh

```bash
$ singularity exec <container> /usr/local/bin/fastx_nucleotide_distribution_graph.sh
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_nucleotide_distribution_graph.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_nucleotide_distribution_graph.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_nucleotide_distribution_line_graph.sh

```bash
$ singularity exec <container> /usr/local/bin/fastx_nucleotide_distribution_line_graph.sh
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_nucleotide_distribution_line_graph.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_nucleotide_distribution_line_graph.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_quality_stats

```bash
$ singularity exec <container> /usr/local/bin/fastx_quality_stats
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_quality_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_quality_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_renamer

```bash
$ singularity exec <container> /usr/local/bin/fastx_renamer
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_renamer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_renamer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_reverse_complement

```bash
$ singularity exec <container> /usr/local/bin/fastx_reverse_complement
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_reverse_complement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_reverse_complement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_trimmer

```bash
$ singularity exec <container> /usr/local/bin/fastx_trimmer
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_uncollapser

```bash
$ singularity exec <container> /usr/local/bin/fastx_uncollapser
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_uncollapser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_uncollapser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findjuncs

```bash
$ singularity exec <container> /usr/local/bin/findjuncs
$ podman run --it --rm --entrypoint /usr/local/bin/findjuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findjuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_count_vectors

```bash
$ singularity exec <container> /usr/local/bin/get_count_vectors
$ podman run --it --rm --entrypoint /usr/local/bin/get_count_vectors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_count_vectors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_parent_types

```bash
$ singularity exec <container> /usr/local/bin/gff_parent_types
$ podman run --it --rm --entrypoint /usr/local/bin/gff_parent_types   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_parent_types   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_wiggle

```bash
$ singularity exec <container> /usr/local/bin/make_wiggle
$ podman run --it --rm --entrypoint /usr/local/bin/make_wiggle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_wiggle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagene

```bash
$ singularity exec <container> /usr/local/bin/metagene
$ podman run --it --rm --entrypoint /usr/local/bin/metagene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phase_by_size

```bash
$ singularity exec <container> /usr/local/bin/phase_by_size
$ podman run --it --rm --entrypoint /usr/local/bin/phase_by_size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phase_by_size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psite

```bash
$ singularity exec <container> /usr/local/bin/psite
$ podman run --it --rm --entrypoint /usr/local/bin/psite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformat_transcripts

```bash
$ singularity exec <container> /usr/local/bin/reformat_transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/reformat_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformat_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slidejuncs

```bash
$ singularity exec <container> /usr/local/bin/slidejuncs
$ podman run --it --rm --entrypoint /usr/local/bin/slidejuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slidejuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_table_equality

```bash
$ singularity exec <container> /usr/local/bin/test_table_equality
$ podman run --it --rm --entrypoint /usr/local/bin/test_table_equality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_table_equality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests-3.9

```bash
$ singularity exec <container> /usr/local/bin/nosetests-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
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