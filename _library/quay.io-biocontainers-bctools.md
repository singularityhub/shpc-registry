---
layout: container
name:  "quay.io/biocontainers/bctools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bctools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bctools/container.yaml"
updated_at: "2024-12-24 03:13:31.121464"
latest: "0.2.2--2"
container_url: "https://biocontainers.pro/tools/bctools"
aliases:
 - "convert_bc_to_binary_RY.py"
 - "coords2clnt.py"
 - "datamash"
 - "extract_aln_ends.py"
 - "extract_bcs.py"
 - "merge_pcr_duplicates.py"
 - "remove_tail.py"
 - "rm_spurious_events.pl"
 - "rm_spurious_events.py"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
 - "f2py3.6"
 - "guess-ploidy.py"
versions:
 - "0.2.2--2"
description: "shpc-registry automated BioContainers addition for bctools"
config: {"url": "https://biocontainers.pro/tools/bctools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bctools", "latest": {"0.2.2--2": "sha256:c80fd13aa1b90b803ac327c1ca0df62a2f3219514acac984330d5a494434904a"}, "tags": {"0.2.2--2": "sha256:c80fd13aa1b90b803ac327c1ca0df62a2f3219514acac984330d5a494434904a"}, "docker": "quay.io/biocontainers/bctools", "aliases": {"convert_bc_to_binary_RY.py": "/usr/local/bin/convert_bc_to_binary_RY.py", "coords2clnt.py": "/usr/local/bin/coords2clnt.py", "datamash": "/usr/local/bin/datamash", "extract_aln_ends.py": "/usr/local/bin/extract_aln_ends.py", "extract_bcs.py": "/usr/local/bin/extract_bcs.py", "merge_pcr_duplicates.py": "/usr/local/bin/merge_pcr_duplicates.py", "remove_tail.py": "/usr/local/bin/remove_tail.py", "rm_spurious_events.pl": "/usr/local/bin/rm_spurious_events.pl", "rm_spurious_events.py": "/usr/local/bin/rm_spurious_events.py", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py", "f2py3.6": "/usr/local/bin/f2py3.6", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bctools.
shpc-registry automated BioContainers addition for bctools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bctools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bctools:0.2.2--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bctools/0.2.2--2
$ module help quay.io/biocontainers/bctools/0.2.2--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bctools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bctools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bctools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bctools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bctools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bctools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convert_bc_to_binary_RY.py

```bash
$ singularity exec <container> /usr/local/bin/convert_bc_to_binary_RY.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_bc_to_binary_RY.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_bc_to_binary_RY.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coords2clnt.py

```bash
$ singularity exec <container> /usr/local/bin/coords2clnt.py
$ podman run --it --rm --entrypoint /usr/local/bin/coords2clnt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coords2clnt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datamash

```bash
$ singularity exec <container> /usr/local/bin/datamash
$ podman run --it --rm --entrypoint /usr/local/bin/datamash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datamash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_aln_ends.py

```bash
$ singularity exec <container> /usr/local/bin/extract_aln_ends.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_aln_ends.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_aln_ends.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_bcs.py

```bash
$ singularity exec <container> /usr/local/bin/extract_bcs.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_bcs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_bcs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_pcr_duplicates.py

```bash
$ singularity exec <container> /usr/local/bin/merge_pcr_duplicates.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_pcr_duplicates.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_pcr_duplicates.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_tail.py

```bash
$ singularity exec <container> /usr/local/bin/remove_tail.py
$ podman run --it --rm --entrypoint /usr/local/bin/remove_tail.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_tail.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rm_spurious_events.pl

```bash
$ singularity exec <container> /usr/local/bin/rm_spurious_events.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rm_spurious_events.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rm_spurious_events.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rm_spurious_events.py

```bash
$ singularity exec <container> /usr/local/bin/rm_spurious_events.py
$ podman run --it --rm --entrypoint /usr/local/bin/rm_spurious_events.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rm_spurious_events.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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