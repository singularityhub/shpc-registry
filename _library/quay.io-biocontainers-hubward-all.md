---
layout: container
name:  "quay.io/biocontainers/hubward-all"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hubward-all/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hubward-all/container.yaml"
updated_at: "2026-01-05 04:01:09.794465"
latest: "0.2.1--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/hubward-all"
aliases:
 - "CrossMap.py"
 - "annotate.pyc"
 - "bigBedToBed"
 - "bigWigToBedGraph"
 - "bigWigToWig"
 - "fab"
 - "fetchChromSizes"
 - "hubward"
 - "intersection_matrix.pyc"
 - "intron_exon_reads.pyc"
 - "inv"
 - "invoke"
 - "liftOver"
 - "pbt_plotting_example.pyc"
 - "peak_pie.pyc"
 - "venn_gchart.pyc"
 - "venn_mpl.pyc"
 - "wigToBigWig"
 - "bedGraphToBigWig"
 - "bedToBigBed"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
 - "bed_bigwig_profile.py"
versions:
 - "0.2.1--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for hubward-all"
config: {"url": "https://biocontainers.pro/tools/hubward-all", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hubward-all", "latest": {"0.2.1--hdfd78af_3": "sha256:9edb13a551985ca2b32984042c3ad732ada8484ce5bf2c4a8395729582284e45"}, "tags": {"0.2.1--hdfd78af_3": "sha256:9edb13a551985ca2b32984042c3ad732ada8484ce5bf2c4a8395729582284e45"}, "docker": "quay.io/biocontainers/hubward-all", "aliases": {"CrossMap.py": "/usr/local/bin/CrossMap.py", "annotate.pyc": "/usr/local/bin/annotate.pyc", "bigBedToBed": "/usr/local/bin/bigBedToBed", "bigWigToBedGraph": "/usr/local/bin/bigWigToBedGraph", "bigWigToWig": "/usr/local/bin/bigWigToWig", "fab": "/usr/local/bin/fab", "fetchChromSizes": "/usr/local/bin/fetchChromSizes", "hubward": "/usr/local/bin/hubward", "intersection_matrix.pyc": "/usr/local/bin/intersection_matrix.pyc", "intron_exon_reads.pyc": "/usr/local/bin/intron_exon_reads.pyc", "inv": "/usr/local/bin/inv", "invoke": "/usr/local/bin/invoke", "liftOver": "/usr/local/bin/liftOver", "pbt_plotting_example.pyc": "/usr/local/bin/pbt_plotting_example.pyc", "peak_pie.pyc": "/usr/local/bin/peak_pie.pyc", "venn_gchart.pyc": "/usr/local/bin/venn_gchart.pyc", "venn_mpl.pyc": "/usr/local/bin/venn_mpl.pyc", "wigToBigWig": "/usr/local/bin/wigToBigWig", "bedGraphToBigWig": "/usr/local/bin/bedGraphToBigWig", "bedToBigBed": "/usr/local/bin/bedToBigBed", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hubward-all.
shpc-registry automated BioContainers addition for hubward-all
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hubward-all
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hubward-all:0.2.1--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hubward-all/0.2.1--hdfd78af_3
$ module help quay.io/biocontainers/hubward-all/0.2.1--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hubward-all-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hubward-all-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hubward-all-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hubward-all-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hubward-all-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hubward-all-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CrossMap.py

```bash
$ singularity exec <container> /usr/local/bin/CrossMap.py
$ podman run --it --rm --entrypoint /usr/local/bin/CrossMap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CrossMap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.pyc

```bash
$ singularity exec <container> /usr/local/bin/annotate.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigBedToBed

```bash
$ singularity exec <container> /usr/local/bin/bigBedToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigBedToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigBedToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigToBedGraph

```bash
$ singularity exec <container> /usr/local/bin/bigWigToBedGraph
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigToWig

```bash
$ singularity exec <container> /usr/local/bin/bigWigToWig
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fab

```bash
$ singularity exec <container> /usr/local/bin/fab
$ podman run --it --rm --entrypoint /usr/local/bin/fab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchChromSizes

```bash
$ singularity exec <container> /usr/local/bin/fetchChromSizes
$ podman run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hubward

```bash
$ singularity exec <container> /usr/local/bin/hubward
$ podman run --it --rm --entrypoint /usr/local/bin/hubward   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hubward   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.pyc

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.pyc

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inv

```bash
$ singularity exec <container> /usr/local/bin/inv
$ podman run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invoke

```bash
$ singularity exec <container> /usr/local/bin/invoke
$ podman run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### liftOver

```bash
$ singularity exec <container> /usr/local/bin/liftOver
$ podman run --it --rm --entrypoint /usr/local/bin/liftOver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/liftOver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.pyc

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peak_pie.pyc

```bash
$ singularity exec <container> /usr/local/bin/peak_pie.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/peak_pie.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peak_pie.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_gchart.pyc

```bash
$ singularity exec <container> /usr/local/bin/venn_gchart.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/venn_gchart.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_gchart.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_mpl.pyc

```bash
$ singularity exec <container> /usr/local/bin/venn_mpl.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/venn_mpl.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_mpl.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedGraphToBigWig

```bash
$ singularity exec <container> /usr/local/bin/bedGraphToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBigBed

```bash
$ singularity exec <container> /usr/local/bin/bedToBigBed
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_print_template.py

```bash
$ singularity exec <container> /usr/local/bin/align_print_template.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_extract_ranges.py

```bash
$ singularity exec <container> /usr/local/bin/axt_extract_ranges.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_lav.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_lav.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_maf.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_maf.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_bigwig_profile.py

```bash
$ singularity exec <container> /usr/local/bin/bed_bigwig_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_bigwig_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_bigwig_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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