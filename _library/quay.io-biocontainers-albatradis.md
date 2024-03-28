---
layout: container
name:  "quay.io/biocontainers/albatradis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/albatradis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/albatradis/container.yaml"
updated_at: "2024-03-28 02:40:29.043390"
latest: "1.0.4--py310h4b81fae_4"
container_url: "https://biocontainers.pro/tools/albatradis"
aliases:
 - "add_tradis_tags"
 - "albatradis"
 - "albatradis-annotation"
 - "albatradis-artemis_project"
 - "albatradis-gene_reports"
 - "albatradis-presence_absence"
 - "albatradis-scatterplot"
 - "bacteria_tradis"
 - "basqcol"
 - "check_tradis_tags"
 - "combine_tradis_plots"
 - "fetchseq"
 - "filter_tradis_tags"
 - "mixreads"
 - "readstats"
 - "remove_tradis_tags"
 - "simqual"
 - "simread"
 - "smalt"
 - "splitmates"
 - "splitreads"
 - "tradis_comparison.R"
 - "tradis_essentiality.R"
 - "tradis_gene_insert_sites"
 - "tradis_merge_plots"
 - "tradis_plot"
 - "trunkreads"
 - "fastaq"
 - "bp_aacomp"
 - "bp_bioflat_index"
 - "bp_biogetseq"
 - "bp_dbsplit"
 - "bp_extract_feature_seq"
 - "bp_fastam9_to_table"
 - "bp_fetch"
 - "bp_filter_search"
 - "bp_find-blast-matches"
versions:
 - "1.0.4--py36h91eb985_3"
 - "1.0.4--py310h4b81fae_4"
description: "shpc-registry automated BioContainers addition for albatradis"
config: {"url": "https://biocontainers.pro/tools/albatradis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for albatradis", "latest": {"1.0.4--py310h4b81fae_4": "sha256:2c5969bd316710f7c2fea2ca37605459f3a4dd4a1e5173e8551fb9a29263acde"}, "tags": {"1.0.4--py36h91eb985_3": "sha256:dbfb4e5ef61956a66895e4229b2807f553d2fd44a8307193f9fac46582248a76", "1.0.4--py310h4b81fae_4": "sha256:2c5969bd316710f7c2fea2ca37605459f3a4dd4a1e5173e8551fb9a29263acde"}, "docker": "quay.io/biocontainers/albatradis", "aliases": {"add_tradis_tags": "/usr/local/bin/add_tradis_tags", "albatradis": "/usr/local/bin/albatradis", "albatradis-annotation": "/usr/local/bin/albatradis-annotation", "albatradis-artemis_project": "/usr/local/bin/albatradis-artemis_project", "albatradis-gene_reports": "/usr/local/bin/albatradis-gene_reports", "albatradis-presence_absence": "/usr/local/bin/albatradis-presence_absence", "albatradis-scatterplot": "/usr/local/bin/albatradis-scatterplot", "bacteria_tradis": "/usr/local/bin/bacteria_tradis", "basqcol": "/usr/local/bin/basqcol", "check_tradis_tags": "/usr/local/bin/check_tradis_tags", "combine_tradis_plots": "/usr/local/bin/combine_tradis_plots", "fetchseq": "/usr/local/bin/fetchseq", "filter_tradis_tags": "/usr/local/bin/filter_tradis_tags", "mixreads": "/usr/local/bin/mixreads", "readstats": "/usr/local/bin/readstats", "remove_tradis_tags": "/usr/local/bin/remove_tradis_tags", "simqual": "/usr/local/bin/simqual", "simread": "/usr/local/bin/simread", "smalt": "/usr/local/bin/smalt", "splitmates": "/usr/local/bin/splitmates", "splitreads": "/usr/local/bin/splitreads", "tradis_comparison.R": "/usr/local/bin/tradis_comparison.R", "tradis_essentiality.R": "/usr/local/bin/tradis_essentiality.R", "tradis_gene_insert_sites": "/usr/local/bin/tradis_gene_insert_sites", "tradis_merge_plots": "/usr/local/bin/tradis_merge_plots", "tradis_plot": "/usr/local/bin/tradis_plot", "trunkreads": "/usr/local/bin/trunkreads", "fastaq": "/usr/local/bin/fastaq", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search", "bp_find-blast-matches": "/usr/local/bin/bp_find-blast-matches"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/albatradis.
shpc-registry automated BioContainers addition for albatradis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/albatradis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/albatradis:1.0.4--py310h4b81fae_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/albatradis/1.0.4--py310h4b81fae_4
$ module help quay.io/biocontainers/albatradis/1.0.4--py310h4b81fae_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### albatradis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### albatradis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### albatradis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### albatradis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### albatradis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### albatradis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/add_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/add_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### albatradis

```bash
$ singularity exec <container> /usr/local/bin/albatradis
$ podman run --it --rm --entrypoint /usr/local/bin/albatradis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/albatradis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### albatradis-annotation

```bash
$ singularity exec <container> /usr/local/bin/albatradis-annotation
$ podman run --it --rm --entrypoint /usr/local/bin/albatradis-annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/albatradis-annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### albatradis-artemis_project

```bash
$ singularity exec <container> /usr/local/bin/albatradis-artemis_project
$ podman run --it --rm --entrypoint /usr/local/bin/albatradis-artemis_project   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/albatradis-artemis_project   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### albatradis-gene_reports

```bash
$ singularity exec <container> /usr/local/bin/albatradis-gene_reports
$ podman run --it --rm --entrypoint /usr/local/bin/albatradis-gene_reports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/albatradis-gene_reports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### albatradis-presence_absence

```bash
$ singularity exec <container> /usr/local/bin/albatradis-presence_absence
$ podman run --it --rm --entrypoint /usr/local/bin/albatradis-presence_absence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/albatradis-presence_absence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### albatradis-scatterplot

```bash
$ singularity exec <container> /usr/local/bin/albatradis-scatterplot
$ podman run --it --rm --entrypoint /usr/local/bin/albatradis-scatterplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/albatradis-scatterplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bacteria_tradis

```bash
$ singularity exec <container> /usr/local/bin/bacteria_tradis
$ podman run --it --rm --entrypoint /usr/local/bin/bacteria_tradis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bacteria_tradis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basqcol

```bash
$ singularity exec <container> /usr/local/bin/basqcol
$ podman run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basqcol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/check_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/check_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_tradis_plots

```bash
$ singularity exec <container> /usr/local/bin/combine_tradis_plots
$ podman run --it --rm --entrypoint /usr/local/bin/combine_tradis_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_tradis_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchseq

```bash
$ singularity exec <container> /usr/local/bin/fetchseq
$ podman run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/filter_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/filter_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mixreads

```bash
$ singularity exec <container> /usr/local/bin/mixreads
$ podman run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mixreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readstats

```bash
$ singularity exec <container> /usr/local/bin/readstats
$ podman run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_tradis_tags

```bash
$ singularity exec <container> /usr/local/bin/remove_tradis_tags
$ podman run --it --rm --entrypoint /usr/local/bin/remove_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_tradis_tags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simqual

```bash
$ singularity exec <container> /usr/local/bin/simqual
$ podman run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simqual   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simread

```bash
$ singularity exec <container> /usr/local/bin/simread
$ podman run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smalt

```bash
$ singularity exec <container> /usr/local/bin/smalt
$ podman run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smalt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitmates

```bash
$ singularity exec <container> /usr/local/bin/splitmates
$ podman run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitmates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitreads

```bash
$ singularity exec <container> /usr/local/bin/splitreads
$ podman run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_comparison.R

```bash
$ singularity exec <container> /usr/local/bin/tradis_comparison.R
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_comparison.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_comparison.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_essentiality.R

```bash
$ singularity exec <container> /usr/local/bin/tradis_essentiality.R
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_essentiality.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_essentiality.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_gene_insert_sites

```bash
$ singularity exec <container> /usr/local/bin/tradis_gene_insert_sites
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_gene_insert_sites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_gene_insert_sites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_merge_plots

```bash
$ singularity exec <container> /usr/local/bin/tradis_merge_plots
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_merge_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_merge_plots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tradis_plot

```bash
$ singularity exec <container> /usr/local/bin/tradis_plot
$ podman run --it --rm --entrypoint /usr/local/bin/tradis_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tradis_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trunkreads

```bash
$ singularity exec <container> /usr/local/bin/trunkreads
$ podman run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trunkreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_dbsplit

```bash
$ singularity exec <container> /usr/local/bin/bp_dbsplit
$ podman run --it --rm --entrypoint /usr/local/bin/bp_dbsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_dbsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_extract_feature_seq

```bash
$ singularity exec <container> /usr/local/bin/bp_extract_feature_seq
$ podman run --it --rm --entrypoint /usr/local/bin/bp_extract_feature_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_extract_feature_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_fastam9_to_table

```bash
$ singularity exec <container> /usr/local/bin/bp_fastam9_to_table
$ podman run --it --rm --entrypoint /usr/local/bin/bp_fastam9_to_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_fastam9_to_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_fetch

```bash
$ singularity exec <container> /usr/local/bin/bp_fetch
$ podman run --it --rm --entrypoint /usr/local/bin/bp_fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_filter_search

```bash
$ singularity exec <container> /usr/local/bin/bp_filter_search
$ podman run --it --rm --entrypoint /usr/local/bin/bp_filter_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_filter_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
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