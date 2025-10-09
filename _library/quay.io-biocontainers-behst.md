---
layout: container
name:  "quay.io/biocontainers/behst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/behst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/behst/container.yaml"
updated_at: "2025-10-09 03:30:03.742979"
latest: "3.8--0"
container_url: "https://biocontainers.pro/tools/behst"
aliases:
 - "behst"
 - "behst-download-data"
 - "behst-download-data.sh"
 - "behst.orig"
 - "behst.py"
 - "chromRegionLength.r"
 - "dataframeSumAllValues.r"
 - "difference_from_first_TSS_script_mordor.r"
 - "difference_from_first_TSS_script_mordor_chrom_wide.r"
 - "download_behst_data.sh"
 - "gProfilerCall.r"
 - "gene_annotation_parser.py"
 - "gene_annotation_parser_load_pickled_files.py"
 - "hiC_parser.py"
 - "hiC_parser_load_pickle_file.py"
 - "list_of_files"
 - "plot_heatmaps.r"
 - "project.sh"
 - "project.sh.orig"
 - "pvaluesPlotGenerator.r"
 - "retrieveMinRowCol.r"
 - "script_all_heatmaps.sh"
 - "script_multi_project_run.sh"
 - "script_multi_project_run_WITHOUT_LOOP.sh"
 - "script_multi_project_run_input_parameters.sh"
 - "temp_test.sh"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
 - "idn2"
 - "shiftBed"
versions:
 - "3.8--0"
description: "shpc-registry automated BioContainers addition for behst"
config: {"url": "https://biocontainers.pro/tools/behst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for behst", "latest": {"3.8--0": "sha256:a34870a64dd19ab3e9061a156709a7a6f44909797e309b86663dbd14c192cda2"}, "tags": {"3.8--0": "sha256:a34870a64dd19ab3e9061a156709a7a6f44909797e309b86663dbd14c192cda2"}, "docker": "quay.io/biocontainers/behst", "aliases": {"behst": "/usr/local/bin/behst", "behst-download-data": "/usr/local/bin/behst-download-data", "behst-download-data.sh": "/usr/local/bin/behst-download-data.sh", "behst.orig": "/usr/local/bin/behst.orig", "behst.py": "/usr/local/bin/behst.py", "chromRegionLength.r": "/usr/local/bin/chromRegionLength.r", "dataframeSumAllValues.r": "/usr/local/bin/dataframeSumAllValues.r", "difference_from_first_TSS_script_mordor.r": "/usr/local/bin/difference_from_first_TSS_script_mordor.r", "difference_from_first_TSS_script_mordor_chrom_wide.r": "/usr/local/bin/difference_from_first_TSS_script_mordor_chrom_wide.r", "download_behst_data.sh": "/usr/local/bin/download_behst_data.sh", "gProfilerCall.r": "/usr/local/bin/gProfilerCall.r", "gene_annotation_parser.py": "/usr/local/bin/gene_annotation_parser.py", "gene_annotation_parser_load_pickled_files.py": "/usr/local/bin/gene_annotation_parser_load_pickled_files.py", "hiC_parser.py": "/usr/local/bin/hiC_parser.py", "hiC_parser_load_pickle_file.py": "/usr/local/bin/hiC_parser_load_pickle_file.py", "list_of_files": "/usr/local/bin/list_of_files", "plot_heatmaps.r": "/usr/local/bin/plot_heatmaps.r", "project.sh": "/usr/local/bin/project.sh", "project.sh.orig": "/usr/local/bin/project.sh.orig", "pvaluesPlotGenerator.r": "/usr/local/bin/pvaluesPlotGenerator.r", "retrieveMinRowCol.r": "/usr/local/bin/retrieveMinRowCol.r", "script_all_heatmaps.sh": "/usr/local/bin/script_all_heatmaps.sh", "script_multi_project_run.sh": "/usr/local/bin/script_multi_project_run.sh", "script_multi_project_run_WITHOUT_LOOP.sh": "/usr/local/bin/script_multi_project_run_WITHOUT_LOOP.sh", "script_multi_project_run_input_parameters.sh": "/usr/local/bin/script_multi_project_run_input_parameters.sh", "temp_test.sh": "/usr/local/bin/temp_test.sh", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py", "idn2": "/usr/local/bin/idn2", "shiftBed": "/usr/local/bin/shiftBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/behst.
shpc-registry automated BioContainers addition for behst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/behst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/behst:3.8--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/behst/3.8--0
$ module help quay.io/biocontainers/behst/3.8--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### behst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### behst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### behst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### behst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### behst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### behst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### behst

```bash
$ singularity exec <container> /usr/local/bin/behst
$ podman run --it --rm --entrypoint /usr/local/bin/behst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/behst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### behst-download-data

```bash
$ singularity exec <container> /usr/local/bin/behst-download-data
$ podman run --it --rm --entrypoint /usr/local/bin/behst-download-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/behst-download-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### behst-download-data.sh

```bash
$ singularity exec <container> /usr/local/bin/behst-download-data.sh
$ podman run --it --rm --entrypoint /usr/local/bin/behst-download-data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/behst-download-data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### behst.orig

```bash
$ singularity exec <container> /usr/local/bin/behst.orig
$ podman run --it --rm --entrypoint /usr/local/bin/behst.orig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/behst.orig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### behst.py

```bash
$ singularity exec <container> /usr/local/bin/behst.py
$ podman run --it --rm --entrypoint /usr/local/bin/behst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/behst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chromRegionLength.r

```bash
$ singularity exec <container> /usr/local/bin/chromRegionLength.r
$ podman run --it --rm --entrypoint /usr/local/bin/chromRegionLength.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromRegionLength.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataframeSumAllValues.r

```bash
$ singularity exec <container> /usr/local/bin/dataframeSumAllValues.r
$ podman run --it --rm --entrypoint /usr/local/bin/dataframeSumAllValues.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataframeSumAllValues.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### difference_from_first_TSS_script_mordor.r

```bash
$ singularity exec <container> /usr/local/bin/difference_from_first_TSS_script_mordor.r
$ podman run --it --rm --entrypoint /usr/local/bin/difference_from_first_TSS_script_mordor.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/difference_from_first_TSS_script_mordor.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### difference_from_first_TSS_script_mordor_chrom_wide.r

```bash
$ singularity exec <container> /usr/local/bin/difference_from_first_TSS_script_mordor_chrom_wide.r
$ podman run --it --rm --entrypoint /usr/local/bin/difference_from_first_TSS_script_mordor_chrom_wide.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/difference_from_first_TSS_script_mordor_chrom_wide.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_behst_data.sh

```bash
$ singularity exec <container> /usr/local/bin/download_behst_data.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download_behst_data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_behst_data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gProfilerCall.r

```bash
$ singularity exec <container> /usr/local/bin/gProfilerCall.r
$ podman run --it --rm --entrypoint /usr/local/bin/gProfilerCall.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gProfilerCall.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_annotation_parser.py

```bash
$ singularity exec <container> /usr/local/bin/gene_annotation_parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/gene_annotation_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_annotation_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_annotation_parser_load_pickled_files.py

```bash
$ singularity exec <container> /usr/local/bin/gene_annotation_parser_load_pickled_files.py
$ podman run --it --rm --entrypoint /usr/local/bin/gene_annotation_parser_load_pickled_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_annotation_parser_load_pickled_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hiC_parser.py

```bash
$ singularity exec <container> /usr/local/bin/hiC_parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/hiC_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiC_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hiC_parser_load_pickle_file.py

```bash
$ singularity exec <container> /usr/local/bin/hiC_parser_load_pickle_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/hiC_parser_load_pickle_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiC_parser_load_pickle_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list_of_files

```bash
$ singularity exec <container> /usr/local/bin/list_of_files
$ podman run --it --rm --entrypoint /usr/local/bin/list_of_files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list_of_files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_heatmaps.r

```bash
$ singularity exec <container> /usr/local/bin/plot_heatmaps.r
$ podman run --it --rm --entrypoint /usr/local/bin/plot_heatmaps.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_heatmaps.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### project.sh

```bash
$ singularity exec <container> /usr/local/bin/project.sh
$ podman run --it --rm --entrypoint /usr/local/bin/project.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/project.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### project.sh.orig

```bash
$ singularity exec <container> /usr/local/bin/project.sh.orig
$ podman run --it --rm --entrypoint /usr/local/bin/project.sh.orig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/project.sh.orig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvaluesPlotGenerator.r

```bash
$ singularity exec <container> /usr/local/bin/pvaluesPlotGenerator.r
$ podman run --it --rm --entrypoint /usr/local/bin/pvaluesPlotGenerator.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pvaluesPlotGenerator.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retrieveMinRowCol.r

```bash
$ singularity exec <container> /usr/local/bin/retrieveMinRowCol.r
$ podman run --it --rm --entrypoint /usr/local/bin/retrieveMinRowCol.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retrieveMinRowCol.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### script_all_heatmaps.sh

```bash
$ singularity exec <container> /usr/local/bin/script_all_heatmaps.sh
$ podman run --it --rm --entrypoint /usr/local/bin/script_all_heatmaps.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/script_all_heatmaps.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### script_multi_project_run.sh

```bash
$ singularity exec <container> /usr/local/bin/script_multi_project_run.sh
$ podman run --it --rm --entrypoint /usr/local/bin/script_multi_project_run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/script_multi_project_run.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### script_multi_project_run_WITHOUT_LOOP.sh

```bash
$ singularity exec <container> /usr/local/bin/script_multi_project_run_WITHOUT_LOOP.sh
$ podman run --it --rm --entrypoint /usr/local/bin/script_multi_project_run_WITHOUT_LOOP.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/script_multi_project_run_WITHOUT_LOOP.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### script_multi_project_run_input_parameters.sh

```bash
$ singularity exec <container> /usr/local/bin/script_multi_project_run_input_parameters.sh
$ podman run --it --rm --entrypoint /usr/local/bin/script_multi_project_run_input_parameters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/script_multi_project_run_input_parameters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### temp_test.sh

```bash
$ singularity exec <container> /usr/local/bin/temp_test.sh
$ podman run --it --rm --entrypoint /usr/local/bin/temp_test.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/temp_test.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.py

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.py

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.py
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peak_pie.py

```bash
$ singularity exec <container> /usr/local/bin/peak_pie.py
$ podman run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybedtools

```bash
$ singularity exec <container> /usr/local/bin/pybedtools
$ podman run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_gchart.py

```bash
$ singularity exec <container> /usr/local/bin/venn_gchart.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_mpl.py

```bash
$ singularity exec <container> /usr/local/bin/venn_mpl.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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