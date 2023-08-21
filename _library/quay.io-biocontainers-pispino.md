---
layout: container
name:  "quay.io/biocontainers/pispino"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pispino/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pispino/container.yaml"
updated_at: "2023-08-21 02:26:58.296711"
latest: "1.1--pyh864c0ab_3"
container_url: "https://biocontainers.pro/tools/pispino"
aliases:
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
 - "pispino_createreadpairslist"
 - "pispino_seqprep"
 - "vsearch"
 - "nosetests"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.1--pyh864c0ab_3"
description: "shpc-registry automated BioContainers addition for pispino"
config: {"url": "https://biocontainers.pro/tools/pispino", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pispino", "latest": {"1.1--pyh864c0ab_3": "sha256:74c75150c6a6a7426bfedf4798a42c334744714e7b01ff9a92d575b5989dcfcb"}, "tags": {"1.1--pyh864c0ab_3": "sha256:74c75150c6a6a7426bfedf4798a42c334744714e7b01ff9a92d575b5989dcfcb"}, "docker": "quay.io/biocontainers/pispino", "aliases": {"fasta_clipping_histogram.pl": "/usr/local/bin/fasta_clipping_histogram.pl", "fasta_formatter": "/usr/local/bin/fasta_formatter", "fasta_nucleotide_changer": "/usr/local/bin/fasta_nucleotide_changer", "fastq_masker": "/usr/local/bin/fastq_masker", "fastq_quality_boxplot_graph.sh": "/usr/local/bin/fastq_quality_boxplot_graph.sh", "fastq_quality_converter": "/usr/local/bin/fastq_quality_converter", "fastq_quality_filter": "/usr/local/bin/fastq_quality_filter", "fastq_quality_trimmer": "/usr/local/bin/fastq_quality_trimmer", "fastq_to_fasta": "/usr/local/bin/fastq_to_fasta", "fastx_artifacts_filter": "/usr/local/bin/fastx_artifacts_filter", "fastx_barcode_splitter.pl": "/usr/local/bin/fastx_barcode_splitter.pl", "fastx_clipper": "/usr/local/bin/fastx_clipper", "fastx_collapser": "/usr/local/bin/fastx_collapser", "fastx_nucleotide_distribution_graph.sh": "/usr/local/bin/fastx_nucleotide_distribution_graph.sh", "fastx_nucleotide_distribution_line_graph.sh": "/usr/local/bin/fastx_nucleotide_distribution_line_graph.sh", "fastx_quality_stats": "/usr/local/bin/fastx_quality_stats", "fastx_renamer": "/usr/local/bin/fastx_renamer", "fastx_reverse_complement": "/usr/local/bin/fastx_reverse_complement", "fastx_trimmer": "/usr/local/bin/fastx_trimmer", "fastx_uncollapser": "/usr/local/bin/fastx_uncollapser", "pispino_createreadpairslist": "/usr/local/bin/pispino_createreadpairslist", "pispino_seqprep": "/usr/local/bin/pispino_seqprep", "vsearch": "/usr/local/bin/vsearch", "nosetests": "/usr/local/bin/nosetests", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pispino.
shpc-registry automated BioContainers addition for pispino
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pispino
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pispino:1.1--pyh864c0ab_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pispino/1.1--pyh864c0ab_3
$ module help quay.io/biocontainers/pispino/1.1--pyh864c0ab_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pispino-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pispino-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pispino-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pispino-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pispino-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pispino-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### pispino_createreadpairslist

```bash
$ singularity exec <container> /usr/local/bin/pispino_createreadpairslist
$ podman run --it --rm --entrypoint /usr/local/bin/pispino_createreadpairslist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pispino_createreadpairslist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pispino_seqprep

```bash
$ singularity exec <container> /usr/local/bin/pispino_seqprep
$ podman run --it --rm --entrypoint /usr/local/bin/pispino_seqprep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pispino_seqprep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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