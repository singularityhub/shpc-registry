---
layout: container
name:  "quay.io/biocontainers/talon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/talon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/talon/container.yaml"
updated_at: "2023-09-04 02:47:57.581809"
latest: "v5.0--py_1"
container_url: "https://biocontainers.pro/tools/talon"
aliases:
 - "talon"
 - "talon_abundance"
 - "talon_create_GTF"
 - "talon_fetch_reads"
 - "talon_filter_transcripts"
 - "talon_generate_report"
 - "talon_get_sjs"
 - "talon_initialize_database"
 - "talon_label_reads"
 - "talon_reformat_gtf"
 - "talon_summarize"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
 - "faidx"
 - "f2py3.6"
versions:
 - "v5.0--py_1"
description: "shpc-registry automated BioContainers addition for talon"
config: {"url": "https://biocontainers.pro/tools/talon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for talon", "latest": {"v5.0--py_1": "sha256:0b4e548c453c4300f7be4b85db2c508ccee0d1b5f4f2b946005f16e2986da03a"}, "tags": {"v5.0--py_1": "sha256:0b4e548c453c4300f7be4b85db2c508ccee0d1b5f4f2b946005f16e2986da03a"}, "docker": "quay.io/biocontainers/talon", "aliases": {"talon": "/usr/local/bin/talon", "talon_abundance": "/usr/local/bin/talon_abundance", "talon_create_GTF": "/usr/local/bin/talon_create_GTF", "talon_fetch_reads": "/usr/local/bin/talon_fetch_reads", "talon_filter_transcripts": "/usr/local/bin/talon_filter_transcripts", "talon_generate_report": "/usr/local/bin/talon_generate_report", "talon_get_sjs": "/usr/local/bin/talon_get_sjs", "talon_initialize_database": "/usr/local/bin/talon_initialize_database", "talon_label_reads": "/usr/local/bin/talon_label_reads", "talon_reformat_gtf": "/usr/local/bin/talon_reformat_gtf", "talon_summarize": "/usr/local/bin/talon_summarize", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py", "faidx": "/usr/local/bin/faidx", "f2py3.6": "/usr/local/bin/f2py3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/talon.
shpc-registry automated BioContainers addition for talon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/talon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/talon:v5.0--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/talon/v5.0--py_1
$ module help quay.io/biocontainers/talon/v5.0--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### talon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### talon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### talon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### talon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### talon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### talon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### talon

```bash
$ singularity exec <container> /usr/local/bin/talon
$ podman run --it --rm --entrypoint /usr/local/bin/talon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_abundance

```bash
$ singularity exec <container> /usr/local/bin/talon_abundance
$ podman run --it --rm --entrypoint /usr/local/bin/talon_abundance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_abundance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_create_GTF

```bash
$ singularity exec <container> /usr/local/bin/talon_create_GTF
$ podman run --it --rm --entrypoint /usr/local/bin/talon_create_GTF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_create_GTF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_fetch_reads

```bash
$ singularity exec <container> /usr/local/bin/talon_fetch_reads
$ podman run --it --rm --entrypoint /usr/local/bin/talon_fetch_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_fetch_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_filter_transcripts

```bash
$ singularity exec <container> /usr/local/bin/talon_filter_transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/talon_filter_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_filter_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_generate_report

```bash
$ singularity exec <container> /usr/local/bin/talon_generate_report
$ podman run --it --rm --entrypoint /usr/local/bin/talon_generate_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_generate_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_get_sjs

```bash
$ singularity exec <container> /usr/local/bin/talon_get_sjs
$ podman run --it --rm --entrypoint /usr/local/bin/talon_get_sjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_get_sjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_initialize_database

```bash
$ singularity exec <container> /usr/local/bin/talon_initialize_database
$ podman run --it --rm --entrypoint /usr/local/bin/talon_initialize_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_initialize_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_label_reads

```bash
$ singularity exec <container> /usr/local/bin/talon_label_reads
$ podman run --it --rm --entrypoint /usr/local/bin/talon_label_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_label_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_reformat_gtf

```bash
$ singularity exec <container> /usr/local/bin/talon_reformat_gtf
$ podman run --it --rm --entrypoint /usr/local/bin/talon_reformat_gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_reformat_gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_summarize

```bash
$ singularity exec <container> /usr/local/bin/talon_summarize
$ podman run --it --rm --entrypoint /usr/local/bin/talon_summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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