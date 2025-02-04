---
layout: container
name:  "quay.io/biocontainers/phylotoast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylotoast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylotoast/container.yaml"
updated_at: "2025-02-04 03:19:35.102535"
latest: "1.4.0rc2--py27_0"
container_url: "https://biocontainers.pro/tools/phylotoast"
aliases:
 - "LDA.py"
 - "LDA_bubble.py"
 - "PCoA.py"
 - "PCoA_bubble.py"
 - "assign_taxonomy_by_blast_result.py"
 - "barcode_filter.py"
 - "biom_relative_abundance.py"
 - "condense_workflow.py"
 - "core_overlap_plot.py"
 - "diversity.py"
 - "extract_shared_or_unique_otuids.py"
 - "filter_biom.py"
 - "filter_keep_otus_by_sample.py"
 - "filter_rep_set.py"
 - "iTol.py"
 - "iptest2"
 - "ipython2"
 - "merge_otu_results.py"
 - "multi_parallel_pick_otus.py"
 - "multi_qsub.py"
 - "network_plots_gephi.py"
 - "otu_condense.py"
 - "otu_to_tax_name.py"
 - "pick_otus_condense.py"
 - "primer_average.py"
 - "prune_otus.py"
 - "pyqi"
 - "restrict_repset.py"
 - "split_sequence_data.py"
 - "transform_biom.py"
 - "transpose_biom.py"
 - "biom"
 - "sample"
 - "easy_install-2.7"
 - "iptest"
 - "ipython"
 - "natsort"
 - "qhelpconverter"
 - "pygmentize"
 - "pylupdate5"
 - "pyrcc5"
versions:
 - "1.4.0rc2--py27_0"
description: "shpc-registry automated BioContainers addition for phylotoast"
config: {"url": "https://biocontainers.pro/tools/phylotoast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylotoast", "latest": {"1.4.0rc2--py27_0": "sha256:07809e3cb2d992a1338a71f506067f80880f56067274d0c9a93f9b7467c60114"}, "tags": {"1.4.0rc2--py27_0": "sha256:07809e3cb2d992a1338a71f506067f80880f56067274d0c9a93f9b7467c60114"}, "docker": "quay.io/biocontainers/phylotoast", "aliases": {"LDA.py": "/usr/local/bin/LDA.py", "LDA_bubble.py": "/usr/local/bin/LDA_bubble.py", "PCoA.py": "/usr/local/bin/PCoA.py", "PCoA_bubble.py": "/usr/local/bin/PCoA_bubble.py", "assign_taxonomy_by_blast_result.py": "/usr/local/bin/assign_taxonomy_by_blast_result.py", "barcode_filter.py": "/usr/local/bin/barcode_filter.py", "biom_relative_abundance.py": "/usr/local/bin/biom_relative_abundance.py", "condense_workflow.py": "/usr/local/bin/condense_workflow.py", "core_overlap_plot.py": "/usr/local/bin/core_overlap_plot.py", "diversity.py": "/usr/local/bin/diversity.py", "extract_shared_or_unique_otuids.py": "/usr/local/bin/extract_shared_or_unique_otuids.py", "filter_biom.py": "/usr/local/bin/filter_biom.py", "filter_keep_otus_by_sample.py": "/usr/local/bin/filter_keep_otus_by_sample.py", "filter_rep_set.py": "/usr/local/bin/filter_rep_set.py", "iTol.py": "/usr/local/bin/iTol.py", "iptest2": "/usr/local/bin/iptest2", "ipython2": "/usr/local/bin/ipython2", "merge_otu_results.py": "/usr/local/bin/merge_otu_results.py", "multi_parallel_pick_otus.py": "/usr/local/bin/multi_parallel_pick_otus.py", "multi_qsub.py": "/usr/local/bin/multi_qsub.py", "network_plots_gephi.py": "/usr/local/bin/network_plots_gephi.py", "otu_condense.py": "/usr/local/bin/otu_condense.py", "otu_to_tax_name.py": "/usr/local/bin/otu_to_tax_name.py", "pick_otus_condense.py": "/usr/local/bin/pick_otus_condense.py", "primer_average.py": "/usr/local/bin/primer_average.py", "prune_otus.py": "/usr/local/bin/prune_otus.py", "pyqi": "/usr/local/bin/pyqi", "restrict_repset.py": "/usr/local/bin/restrict_repset.py", "split_sequence_data.py": "/usr/local/bin/split_sequence_data.py", "transform_biom.py": "/usr/local/bin/transform_biom.py", "transpose_biom.py": "/usr/local/bin/transpose_biom.py", "biom": "/usr/local/bin/biom", "sample": "/usr/local/bin/sample", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "iptest": "/usr/local/bin/iptest", "ipython": "/usr/local/bin/ipython", "natsort": "/usr/local/bin/natsort", "qhelpconverter": "/usr/local/bin/qhelpconverter", "pygmentize": "/usr/local/bin/pygmentize", "pylupdate5": "/usr/local/bin/pylupdate5", "pyrcc5": "/usr/local/bin/pyrcc5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylotoast.
shpc-registry automated BioContainers addition for phylotoast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylotoast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylotoast:1.4.0rc2--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylotoast/1.4.0rc2--py27_0
$ module help quay.io/biocontainers/phylotoast/1.4.0rc2--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylotoast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylotoast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylotoast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylotoast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylotoast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylotoast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LDA.py

```bash
$ singularity exec <container> /usr/local/bin/LDA.py
$ podman run --it --rm --entrypoint /usr/local/bin/LDA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LDA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LDA_bubble.py

```bash
$ singularity exec <container> /usr/local/bin/LDA_bubble.py
$ podman run --it --rm --entrypoint /usr/local/bin/LDA_bubble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LDA_bubble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PCoA.py

```bash
$ singularity exec <container> /usr/local/bin/PCoA.py
$ podman run --it --rm --entrypoint /usr/local/bin/PCoA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PCoA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PCoA_bubble.py

```bash
$ singularity exec <container> /usr/local/bin/PCoA_bubble.py
$ podman run --it --rm --entrypoint /usr/local/bin/PCoA_bubble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PCoA_bubble.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assign_taxonomy_by_blast_result.py

```bash
$ singularity exec <container> /usr/local/bin/assign_taxonomy_by_blast_result.py
$ podman run --it --rm --entrypoint /usr/local/bin/assign_taxonomy_by_blast_result.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assign_taxonomy_by_blast_result.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barcode_filter.py

```bash
$ singularity exec <container> /usr/local/bin/barcode_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/barcode_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barcode_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom_relative_abundance.py

```bash
$ singularity exec <container> /usr/local/bin/biom_relative_abundance.py
$ podman run --it --rm --entrypoint /usr/local/bin/biom_relative_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom_relative_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### condense_workflow.py

```bash
$ singularity exec <container> /usr/local/bin/condense_workflow.py
$ podman run --it --rm --entrypoint /usr/local/bin/condense_workflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/condense_workflow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### core_overlap_plot.py

```bash
$ singularity exec <container> /usr/local/bin/core_overlap_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/core_overlap_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/core_overlap_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diversity.py

```bash
$ singularity exec <container> /usr/local/bin/diversity.py
$ podman run --it --rm --entrypoint /usr/local/bin/diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_shared_or_unique_otuids.py

```bash
$ singularity exec <container> /usr/local/bin/extract_shared_or_unique_otuids.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_shared_or_unique_otuids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_shared_or_unique_otuids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_biom.py

```bash
$ singularity exec <container> /usr/local/bin/filter_biom.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_biom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_biom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_keep_otus_by_sample.py

```bash
$ singularity exec <container> /usr/local/bin/filter_keep_otus_by_sample.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_keep_otus_by_sample.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_keep_otus_by_sample.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_rep_set.py

```bash
$ singularity exec <container> /usr/local/bin/filter_rep_set.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_rep_set.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_rep_set.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iTol.py

```bash
$ singularity exec <container> /usr/local/bin/iTol.py
$ podman run --it --rm --entrypoint /usr/local/bin/iTol.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iTol.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest2

```bash
$ singularity exec <container> /usr/local/bin/iptest2
$ podman run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython2

```bash
$ singularity exec <container> /usr/local/bin/ipython2
$ podman run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_otu_results.py

```bash
$ singularity exec <container> /usr/local/bin/merge_otu_results.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_otu_results.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_otu_results.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi_parallel_pick_otus.py

```bash
$ singularity exec <container> /usr/local/bin/multi_parallel_pick_otus.py
$ podman run --it --rm --entrypoint /usr/local/bin/multi_parallel_pick_otus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_parallel_pick_otus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi_qsub.py

```bash
$ singularity exec <container> /usr/local/bin/multi_qsub.py
$ podman run --it --rm --entrypoint /usr/local/bin/multi_qsub.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_qsub.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### network_plots_gephi.py

```bash
$ singularity exec <container> /usr/local/bin/network_plots_gephi.py
$ podman run --it --rm --entrypoint /usr/local/bin/network_plots_gephi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/network_plots_gephi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### otu_condense.py

```bash
$ singularity exec <container> /usr/local/bin/otu_condense.py
$ podman run --it --rm --entrypoint /usr/local/bin/otu_condense.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/otu_condense.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### otu_to_tax_name.py

```bash
$ singularity exec <container> /usr/local/bin/otu_to_tax_name.py
$ podman run --it --rm --entrypoint /usr/local/bin/otu_to_tax_name.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/otu_to_tax_name.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pick_otus_condense.py

```bash
$ singularity exec <container> /usr/local/bin/pick_otus_condense.py
$ podman run --it --rm --entrypoint /usr/local/bin/pick_otus_condense.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pick_otus_condense.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primer_average.py

```bash
$ singularity exec <container> /usr/local/bin/primer_average.py
$ podman run --it --rm --entrypoint /usr/local/bin/primer_average.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primer_average.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prune_otus.py

```bash
$ singularity exec <container> /usr/local/bin/prune_otus.py
$ podman run --it --rm --entrypoint /usr/local/bin/prune_otus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prune_otus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyqi

```bash
$ singularity exec <container> /usr/local/bin/pyqi
$ podman run --it --rm --entrypoint /usr/local/bin/pyqi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyqi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### restrict_repset.py

```bash
$ singularity exec <container> /usr/local/bin/restrict_repset.py
$ podman run --it --rm --entrypoint /usr/local/bin/restrict_repset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/restrict_repset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_sequence_data.py

```bash
$ singularity exec <container> /usr/local/bin/split_sequence_data.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_sequence_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_sequence_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transform_biom.py

```bash
$ singularity exec <container> /usr/local/bin/transform_biom.py
$ podman run --it --rm --entrypoint /usr/local/bin/transform_biom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transform_biom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transpose_biom.py

```bash
$ singularity exec <container> /usr/local/bin/transpose_biom.py
$ podman run --it --rm --entrypoint /usr/local/bin/transpose_biom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transpose_biom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample

```bash
$ singularity exec <container> /usr/local/bin/sample
$ podman run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylupdate5

```bash
$ singularity exec <container> /usr/local/bin/pylupdate5
$ podman run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrcc5

```bash
$ singularity exec <container> /usr/local/bin/pyrcc5
$ podman run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
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