---
layout: container
name:  "quay.io/biocontainers/stacks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stacks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stacks/container.yaml"
updated_at: "2023-06-09 03:15:06.052502"
latest: "2.53--he513fc3_0"
container_url: "https://biocontainers.pro/tools/stacks"
aliases:
 - "clone_filter"
 - "convert_stacks.pl"
 - "count_fixed_catalog_snps.py"
 - "cstacks"
 - "denovo_map.pl"
 - "extract_interpop_chars.pl"
 - "gstacks"
 - "integrate_alignments.py"
 - "kmer_filter"
 - "phasedstacks"
 - "populations"
 - "process_radtags"
 - "process_shortreads"
 - "ref_map.pl"
 - "sstacks"
 - "stacks-count-reads-per-sample-per-locus"
 - "stacks-dist-extract"
 - "stacks-gdb"
 - "stacks-hist2d-loci-samples-coverage"
 - "stacks-integrate-alignments"
 - "stacks-samtools-tview"
 - "tsv2bam"
 - "ustacks"
 - "velvetg"
 - "velveth"
 - "gdlib-config"
 - "bp_find-blast-matches.pl"
 - "ace.pl"
 - "ccconfig"
 - "SOAPsh.pl"
 - "map"
 - "mirrorMappings"
 - "mkCSGB2312"
versions:
 - "2.53--he513fc3_0"
description: "shpc-registry automated BioContainers addition for stacks"
config: {"url": "https://biocontainers.pro/tools/stacks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stacks", "latest": {"2.53--he513fc3_0": "sha256:b05949757c84d6f35d8ccbb62027252d9dce3a8c22b871a0303d6bb9b274f73d"}, "tags": {"2.53--he513fc3_0": "sha256:b05949757c84d6f35d8ccbb62027252d9dce3a8c22b871a0303d6bb9b274f73d"}, "docker": "quay.io/biocontainers/stacks", "aliases": {"clone_filter": "/usr/local/bin/clone_filter", "convert_stacks.pl": "/usr/local/bin/convert_stacks.pl", "count_fixed_catalog_snps.py": "/usr/local/bin/count_fixed_catalog_snps.py", "cstacks": "/usr/local/bin/cstacks", "denovo_map.pl": "/usr/local/bin/denovo_map.pl", "extract_interpop_chars.pl": "/usr/local/bin/extract_interpop_chars.pl", "gstacks": "/usr/local/bin/gstacks", "integrate_alignments.py": "/usr/local/bin/integrate_alignments.py", "kmer_filter": "/usr/local/bin/kmer_filter", "phasedstacks": "/usr/local/bin/phasedstacks", "populations": "/usr/local/bin/populations", "process_radtags": "/usr/local/bin/process_radtags", "process_shortreads": "/usr/local/bin/process_shortreads", "ref_map.pl": "/usr/local/bin/ref_map.pl", "sstacks": "/usr/local/bin/sstacks", "stacks-count-reads-per-sample-per-locus": "/usr/local/bin/stacks-count-reads-per-sample-per-locus", "stacks-dist-extract": "/usr/local/bin/stacks-dist-extract", "stacks-gdb": "/usr/local/bin/stacks-gdb", "stacks-hist2d-loci-samples-coverage": "/usr/local/bin/stacks-hist2d-loci-samples-coverage", "stacks-integrate-alignments": "/usr/local/bin/stacks-integrate-alignments", "stacks-samtools-tview": "/usr/local/bin/stacks-samtools-tview", "tsv2bam": "/usr/local/bin/tsv2bam", "ustacks": "/usr/local/bin/ustacks", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth", "gdlib-config": "/usr/local/bin/gdlib-config", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "ace.pl": "/usr/local/bin/ace.pl", "ccconfig": "/usr/local/bin/ccconfig", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "map": "/usr/local/bin/map", "mirrorMappings": "/usr/local/bin/mirrorMappings", "mkCSGB2312": "/usr/local/bin/mkCSGB2312"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stacks.
shpc-registry automated BioContainers addition for stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stacks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stacks:2.53--he513fc3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stacks/2.53--he513fc3_0
$ module help quay.io/biocontainers/stacks/2.53--he513fc3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stacks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stacks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stacks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stacks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stacks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stacks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clone_filter

```bash
$ singularity exec <container> /usr/local/bin/clone_filter
$ podman run --it --rm --entrypoint /usr/local/bin/clone_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clone_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_stacks.pl

```bash
$ singularity exec <container> /usr/local/bin/convert_stacks.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convert_stacks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_stacks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count_fixed_catalog_snps.py

```bash
$ singularity exec <container> /usr/local/bin/count_fixed_catalog_snps.py
$ podman run --it --rm --entrypoint /usr/local/bin/count_fixed_catalog_snps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count_fixed_catalog_snps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cstacks

```bash
$ singularity exec <container> /usr/local/bin/cstacks
$ podman run --it --rm --entrypoint /usr/local/bin/cstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### denovo_map.pl

```bash
$ singularity exec <container> /usr/local/bin/denovo_map.pl
$ podman run --it --rm --entrypoint /usr/local/bin/denovo_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/denovo_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_interpop_chars.pl

```bash
$ singularity exec <container> /usr/local/bin/extract_interpop_chars.pl
$ podman run --it --rm --entrypoint /usr/local/bin/extract_interpop_chars.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_interpop_chars.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gstacks

```bash
$ singularity exec <container> /usr/local/bin/gstacks
$ podman run --it --rm --entrypoint /usr/local/bin/gstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### integrate_alignments.py

```bash
$ singularity exec <container> /usr/local/bin/integrate_alignments.py
$ podman run --it --rm --entrypoint /usr/local/bin/integrate_alignments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integrate_alignments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer_filter

```bash
$ singularity exec <container> /usr/local/bin/kmer_filter
$ podman run --it --rm --entrypoint /usr/local/bin/kmer_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phasedstacks

```bash
$ singularity exec <container> /usr/local/bin/phasedstacks
$ podman run --it --rm --entrypoint /usr/local/bin/phasedstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phasedstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### populations

```bash
$ singularity exec <container> /usr/local/bin/populations
$ podman run --it --rm --entrypoint /usr/local/bin/populations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/populations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_radtags

```bash
$ singularity exec <container> /usr/local/bin/process_radtags
$ podman run --it --rm --entrypoint /usr/local/bin/process_radtags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_radtags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_shortreads

```bash
$ singularity exec <container> /usr/local/bin/process_shortreads
$ podman run --it --rm --entrypoint /usr/local/bin/process_shortreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_shortreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref_map.pl

```bash
$ singularity exec <container> /usr/local/bin/ref_map.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ref_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sstacks

```bash
$ singularity exec <container> /usr/local/bin/sstacks
$ podman run --it --rm --entrypoint /usr/local/bin/sstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sstacks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stacks-count-reads-per-sample-per-locus

```bash
$ singularity exec <container> /usr/local/bin/stacks-count-reads-per-sample-per-locus
$ podman run --it --rm --entrypoint /usr/local/bin/stacks-count-reads-per-sample-per-locus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stacks-count-reads-per-sample-per-locus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stacks-dist-extract

```bash
$ singularity exec <container> /usr/local/bin/stacks-dist-extract
$ podman run --it --rm --entrypoint /usr/local/bin/stacks-dist-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stacks-dist-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stacks-gdb

```bash
$ singularity exec <container> /usr/local/bin/stacks-gdb
$ podman run --it --rm --entrypoint /usr/local/bin/stacks-gdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stacks-gdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stacks-hist2d-loci-samples-coverage

```bash
$ singularity exec <container> /usr/local/bin/stacks-hist2d-loci-samples-coverage
$ podman run --it --rm --entrypoint /usr/local/bin/stacks-hist2d-loci-samples-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stacks-hist2d-loci-samples-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stacks-integrate-alignments

```bash
$ singularity exec <container> /usr/local/bin/stacks-integrate-alignments
$ podman run --it --rm --entrypoint /usr/local/bin/stacks-integrate-alignments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stacks-integrate-alignments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stacks-samtools-tview

```bash
$ singularity exec <container> /usr/local/bin/stacks-samtools-tview
$ podman run --it --rm --entrypoint /usr/local/bin/stacks-samtools-tview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stacks-samtools-tview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv2bam

```bash
$ singularity exec <container> /usr/local/bin/tsv2bam
$ podman run --it --rm --entrypoint /usr/local/bin/tsv2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ustacks

```bash
$ singularity exec <container> /usr/local/bin/ustacks
$ podman run --it --rm --entrypoint /usr/local/bin/ustacks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ustacks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccconfig

```bash
$ singularity exec <container> /usr/local/bin/ccconfig
$ podman run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map

```bash
$ singularity exec <container> /usr/local/bin/map
$ podman run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirrorMappings

```bash
$ singularity exec <container> /usr/local/bin/mirrorMappings
$ podman run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkCSGB2312

```bash
$ singularity exec <container> /usr/local/bin/mkCSGB2312
$ podman run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
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