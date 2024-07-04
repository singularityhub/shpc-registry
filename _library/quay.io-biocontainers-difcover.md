---
layout: container
name:  "quay.io/biocontainers/difcover"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/difcover/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/difcover/container.yaml"
updated_at: "2024-07-04 02:53:32.406029"
latest: "3.0.1--h4ac6f70_1"
container_url: "https://biocontainers.pro/tools/difcover"
aliases:
 - "convert_exp_to_dec_in_unionbed.sh"
 - "from_DNAcopyout_to_p_fragments.sh"
 - "from_bams_to_unionbed.sh"
 - "from_ratio_per_window__to__DNAcopy_output.sh"
 - "from_unionbed_to_ratio_per_window_CC0"
 - "generate_DNAcopyout_len_histogram.sh"
 - "generate_DNAcopyout_len_vs_scores_histogram_bin0.5.sh"
 - "get_DNAcopyout_with_length_of_intervals.sh"
 - "run_DNAcopy_from_bash.R"
 - "run_difcover.sh"
 - "annot-tsv"
 - "shiftBed"
 - "hb-info"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "closestBed"
 - "clusterBed"
 - "complementBed"
 - "coverageBed"
 - "expandCols"
 - "fastaFromBed"
 - "flankBed"
 - "genomeCoverageBed"
 - "getOverlap"
 - "groupBy"
 - "intersectBed"
 - "linksBed"
 - "mapBed"
 - "maskFastaFromBed"
versions:
 - "3.0.1--h4ac6f70_1"
description: "singularity registry hpc automated addition for difcover"
config: {"url": "https://biocontainers.pro/tools/difcover", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for difcover", "latest": {"3.0.1--h4ac6f70_1": "sha256:4e535a7b9c4f02997625d5cf05b03358e9c39bef4fec7aa69457477c23f3083f"}, "tags": {"3.0.1--h4ac6f70_1": "sha256:4e535a7b9c4f02997625d5cf05b03358e9c39bef4fec7aa69457477c23f3083f"}, "docker": "quay.io/biocontainers/difcover", "aliases": {"convert_exp_to_dec_in_unionbed.sh": "/usr/local/bin/convert_exp_to_dec_in_unionbed.sh", "from_DNAcopyout_to_p_fragments.sh": "/usr/local/bin/from_DNAcopyout_to_p_fragments.sh", "from_bams_to_unionbed.sh": "/usr/local/bin/from_bams_to_unionbed.sh", "from_ratio_per_window__to__DNAcopy_output.sh": "/usr/local/bin/from_ratio_per_window__to__DNAcopy_output.sh", "from_unionbed_to_ratio_per_window_CC0": "/usr/local/bin/from_unionbed_to_ratio_per_window_CC0", "generate_DNAcopyout_len_histogram.sh": "/usr/local/bin/generate_DNAcopyout_len_histogram.sh", "generate_DNAcopyout_len_vs_scores_histogram_bin0.5.sh": "/usr/local/bin/generate_DNAcopyout_len_vs_scores_histogram_bin0.5.sh", "get_DNAcopyout_with_length_of_intervals.sh": "/usr/local/bin/get_DNAcopyout_with_length_of_intervals.sh", "run_DNAcopy_from_bash.R": "/usr/local/bin/run_DNAcopy_from_bash.R", "run_difcover.sh": "/usr/local/bin/run_difcover.sh", "annot-tsv": "/usr/local/bin/annot-tsv", "shiftBed": "/usr/local/bin/shiftBed", "hb-info": "/usr/local/bin/hb-info", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed", "clusterBed": "/usr/local/bin/clusterBed", "complementBed": "/usr/local/bin/complementBed", "coverageBed": "/usr/local/bin/coverageBed", "expandCols": "/usr/local/bin/expandCols", "fastaFromBed": "/usr/local/bin/fastaFromBed", "flankBed": "/usr/local/bin/flankBed", "genomeCoverageBed": "/usr/local/bin/genomeCoverageBed", "getOverlap": "/usr/local/bin/getOverlap", "groupBy": "/usr/local/bin/groupBy", "intersectBed": "/usr/local/bin/intersectBed", "linksBed": "/usr/local/bin/linksBed", "mapBed": "/usr/local/bin/mapBed", "maskFastaFromBed": "/usr/local/bin/maskFastaFromBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/difcover.
singularity registry hpc automated addition for difcover
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/difcover
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/difcover:3.0.1--h4ac6f70_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/difcover/3.0.1--h4ac6f70_1
$ module help quay.io/biocontainers/difcover/3.0.1--h4ac6f70_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### difcover-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### difcover-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### difcover-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### difcover-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### difcover-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### difcover-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convert_exp_to_dec_in_unionbed.sh

```bash
$ singularity exec <container> /usr/local/bin/convert_exp_to_dec_in_unionbed.sh
$ podman run --it --rm --entrypoint /usr/local/bin/convert_exp_to_dec_in_unionbed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_exp_to_dec_in_unionbed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from_DNAcopyout_to_p_fragments.sh

```bash
$ singularity exec <container> /usr/local/bin/from_DNAcopyout_to_p_fragments.sh
$ podman run --it --rm --entrypoint /usr/local/bin/from_DNAcopyout_to_p_fragments.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from_DNAcopyout_to_p_fragments.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from_bams_to_unionbed.sh

```bash
$ singularity exec <container> /usr/local/bin/from_bams_to_unionbed.sh
$ podman run --it --rm --entrypoint /usr/local/bin/from_bams_to_unionbed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from_bams_to_unionbed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from_ratio_per_window__to__DNAcopy_output.sh

```bash
$ singularity exec <container> /usr/local/bin/from_ratio_per_window__to__DNAcopy_output.sh
$ podman run --it --rm --entrypoint /usr/local/bin/from_ratio_per_window__to__DNAcopy_output.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from_ratio_per_window__to__DNAcopy_output.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from_unionbed_to_ratio_per_window_CC0

```bash
$ singularity exec <container> /usr/local/bin/from_unionbed_to_ratio_per_window_CC0
$ podman run --it --rm --entrypoint /usr/local/bin/from_unionbed_to_ratio_per_window_CC0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from_unionbed_to_ratio_per_window_CC0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_DNAcopyout_len_histogram.sh

```bash
$ singularity exec <container> /usr/local/bin/generate_DNAcopyout_len_histogram.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generate_DNAcopyout_len_histogram.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_DNAcopyout_len_histogram.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_DNAcopyout_len_vs_scores_histogram_bin0.5.sh

```bash
$ singularity exec <container> /usr/local/bin/generate_DNAcopyout_len_vs_scores_histogram_bin0.5.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generate_DNAcopyout_len_vs_scores_histogram_bin0.5.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_DNAcopyout_len_vs_scores_histogram_bin0.5.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_DNAcopyout_with_length_of_intervals.sh

```bash
$ singularity exec <container> /usr/local/bin/get_DNAcopyout_with_length_of_intervals.sh
$ podman run --it --rm --entrypoint /usr/local/bin/get_DNAcopyout_with_length_of_intervals.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_DNAcopyout_with_length_of_intervals.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_DNAcopy_from_bash.R

```bash
$ singularity exec <container> /usr/local/bin/run_DNAcopy_from_bash.R
$ podman run --it --rm --entrypoint /usr/local/bin/run_DNAcopy_from_bash.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_DNAcopy_from_bash.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_difcover.sh

```bash
$ singularity exec <container> /usr/local/bin/run_difcover.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_difcover.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_difcover.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closestBed

```bash
$ singularity exec <container> /usr/local/bin/closestBed
$ podman run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterBed

```bash
$ singularity exec <container> /usr/local/bin/clusterBed
$ podman run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complementBed

```bash
$ singularity exec <container> /usr/local/bin/complementBed
$ podman run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverageBed

```bash
$ singularity exec <container> /usr/local/bin/coverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### expandCols

```bash
$ singularity exec <container> /usr/local/bin/expandCols
$ podman run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaFromBed

```bash
$ singularity exec <container> /usr/local/bin/fastaFromBed
$ podman run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flankBed

```bash
$ singularity exec <container> /usr/local/bin/flankBed
$ podman run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomeCoverageBed

```bash
$ singularity exec <container> /usr/local/bin/genomeCoverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getOverlap

```bash
$ singularity exec <container> /usr/local/bin/getOverlap
$ podman run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groupBy

```bash
$ singularity exec <container> /usr/local/bin/groupBy
$ podman run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersectBed

```bash
$ singularity exec <container> /usr/local/bin/intersectBed
$ podman run --it --rm --entrypoint /usr/local/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linksBed

```bash
$ singularity exec <container> /usr/local/bin/linksBed
$ podman run --it --rm --entrypoint /usr/local/bin/linksBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linksBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapBed

```bash
$ singularity exec <container> /usr/local/bin/mapBed
$ podman run --it --rm --entrypoint /usr/local/bin/mapBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maskFastaFromBed

```bash
$ singularity exec <container> /usr/local/bin/maskFastaFromBed
$ podman run --it --rm --entrypoint /usr/local/bin/maskFastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maskFastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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