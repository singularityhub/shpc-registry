---
layout: container
name:  "quay.io/biocontainers/sat-bsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sat-bsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sat-bsa/container.yaml"
updated_at: "2024-04-08 03:08:58.680449"
latest: "1.12--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/sat-bsa"
aliases:
 - "1_1_select_reads_name_from_bam.pl"
 - "1_2_pick_up_reads.pl"
 - "1_3_fa_size.pl"
 - "3_1_filter_mapQ_for_sam.pl"
 - "4_1_fa_size.pl"
 - "4_1_promoter_transcription_region.pl"
 - "4_2_select_pileup.pl"
 - "4_3_mut_count_pileup.pl"
 - "4_4_Fisher.R"
 - "4_5_select_mut_pileup.pl"
 - "4_6_match_pileup.pl"
 - "4_7_result.pl"
 - "5_1_make_script.pl"
 - "5_2_make_format.pl"
 - "5_make_graph.R"
 - "Sat-BSA"
 - "make_Local_de_novo_assembly.pl"
 - "make_Local_reads_selection.pl"
 - "make_Long_reads_alignment.pl"
 - "make_SVs_detection.pl"
 - "perl5.32.0"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
versions:
 - "1.12--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for sat-bsa"
config: {"url": "https://biocontainers.pro/tools/sat-bsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sat-bsa", "latest": {"1.12--hdfd78af_1": "sha256:5c03c4e1e3a1969fcaa81392c991f61ed3a4b3145afd8cbed5885f881aeac757"}, "tags": {"1.12--hdfd78af_1": "sha256:5c03c4e1e3a1969fcaa81392c991f61ed3a4b3145afd8cbed5885f881aeac757"}, "docker": "quay.io/biocontainers/sat-bsa", "aliases": {"1_1_select_reads_name_from_bam.pl": "/usr/local/bin/1_1_select_reads_name_from_bam.pl", "1_2_pick_up_reads.pl": "/usr/local/bin/1_2_pick_up_reads.pl", "1_3_fa_size.pl": "/usr/local/bin/1_3_fa_size.pl", "3_1_filter_mapQ_for_sam.pl": "/usr/local/bin/3_1_filter_mapQ_for_sam.pl", "4_1_fa_size.pl": "/usr/local/bin/4_1_fa_size.pl", "4_1_promoter_transcription_region.pl": "/usr/local/bin/4_1_promoter_transcription_region.pl", "4_2_select_pileup.pl": "/usr/local/bin/4_2_select_pileup.pl", "4_3_mut_count_pileup.pl": "/usr/local/bin/4_3_mut_count_pileup.pl", "4_4_Fisher.R": "/usr/local/bin/4_4_Fisher.R", "4_5_select_mut_pileup.pl": "/usr/local/bin/4_5_select_mut_pileup.pl", "4_6_match_pileup.pl": "/usr/local/bin/4_6_match_pileup.pl", "4_7_result.pl": "/usr/local/bin/4_7_result.pl", "5_1_make_script.pl": "/usr/local/bin/5_1_make_script.pl", "5_2_make_format.pl": "/usr/local/bin/5_2_make_format.pl", "5_make_graph.R": "/usr/local/bin/5_make_graph.R", "Sat-BSA": "/usr/local/bin/Sat-BSA", "make_Local_de_novo_assembly.pl": "/usr/local/bin/make_Local_de_novo_assembly.pl", "make_Local_reads_selection.pl": "/usr/local/bin/make_Local_reads_selection.pl", "make_Long_reads_alignment.pl": "/usr/local/bin/make_Long_reads_alignment.pl", "make_SVs_detection.pl": "/usr/local/bin/make_SVs_detection.pl", "perl5.32.0": "/usr/local/bin/perl5.32.0", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sat-bsa.
shpc-registry automated BioContainers addition for sat-bsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sat-bsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sat-bsa:1.12--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sat-bsa/1.12--hdfd78af_1
$ module help quay.io/biocontainers/sat-bsa/1.12--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sat-bsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sat-bsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sat-bsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sat-bsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sat-bsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sat-bsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 1_1_select_reads_name_from_bam.pl

```bash
$ singularity exec <container> /usr/local/bin/1_1_select_reads_name_from_bam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/1_1_select_reads_name_from_bam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/1_1_select_reads_name_from_bam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 1_2_pick_up_reads.pl

```bash
$ singularity exec <container> /usr/local/bin/1_2_pick_up_reads.pl
$ podman run --it --rm --entrypoint /usr/local/bin/1_2_pick_up_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/1_2_pick_up_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 1_3_fa_size.pl

```bash
$ singularity exec <container> /usr/local/bin/1_3_fa_size.pl
$ podman run --it --rm --entrypoint /usr/local/bin/1_3_fa_size.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/1_3_fa_size.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 3_1_filter_mapQ_for_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/3_1_filter_mapQ_for_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/3_1_filter_mapQ_for_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/3_1_filter_mapQ_for_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_1_fa_size.pl

```bash
$ singularity exec <container> /usr/local/bin/4_1_fa_size.pl
$ podman run --it --rm --entrypoint /usr/local/bin/4_1_fa_size.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_1_fa_size.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_1_promoter_transcription_region.pl

```bash
$ singularity exec <container> /usr/local/bin/4_1_promoter_transcription_region.pl
$ podman run --it --rm --entrypoint /usr/local/bin/4_1_promoter_transcription_region.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_1_promoter_transcription_region.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_2_select_pileup.pl

```bash
$ singularity exec <container> /usr/local/bin/4_2_select_pileup.pl
$ podman run --it --rm --entrypoint /usr/local/bin/4_2_select_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_2_select_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_3_mut_count_pileup.pl

```bash
$ singularity exec <container> /usr/local/bin/4_3_mut_count_pileup.pl
$ podman run --it --rm --entrypoint /usr/local/bin/4_3_mut_count_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_3_mut_count_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_4_Fisher.R

```bash
$ singularity exec <container> /usr/local/bin/4_4_Fisher.R
$ podman run --it --rm --entrypoint /usr/local/bin/4_4_Fisher.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_4_Fisher.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_5_select_mut_pileup.pl

```bash
$ singularity exec <container> /usr/local/bin/4_5_select_mut_pileup.pl
$ podman run --it --rm --entrypoint /usr/local/bin/4_5_select_mut_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_5_select_mut_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_6_match_pileup.pl

```bash
$ singularity exec <container> /usr/local/bin/4_6_match_pileup.pl
$ podman run --it --rm --entrypoint /usr/local/bin/4_6_match_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_6_match_pileup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 4_7_result.pl

```bash
$ singularity exec <container> /usr/local/bin/4_7_result.pl
$ podman run --it --rm --entrypoint /usr/local/bin/4_7_result.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/4_7_result.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 5_1_make_script.pl

```bash
$ singularity exec <container> /usr/local/bin/5_1_make_script.pl
$ podman run --it --rm --entrypoint /usr/local/bin/5_1_make_script.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/5_1_make_script.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 5_2_make_format.pl

```bash
$ singularity exec <container> /usr/local/bin/5_2_make_format.pl
$ podman run --it --rm --entrypoint /usr/local/bin/5_2_make_format.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/5_2_make_format.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 5_make_graph.R

```bash
$ singularity exec <container> /usr/local/bin/5_make_graph.R
$ podman run --it --rm --entrypoint /usr/local/bin/5_make_graph.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/5_make_graph.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Sat-BSA

```bash
$ singularity exec <container> /usr/local/bin/Sat-BSA
$ podman run --it --rm --entrypoint /usr/local/bin/Sat-BSA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Sat-BSA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_Local_de_novo_assembly.pl

```bash
$ singularity exec <container> /usr/local/bin/make_Local_de_novo_assembly.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_Local_de_novo_assembly.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_Local_de_novo_assembly.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_Local_reads_selection.pl

```bash
$ singularity exec <container> /usr/local/bin/make_Local_reads_selection.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_Local_reads_selection.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_Local_reads_selection.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_Long_reads_alignment.pl

```bash
$ singularity exec <container> /usr/local/bin/make_Long_reads_alignment.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_Long_reads_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_Long_reads_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_SVs_detection.pl

```bash
$ singularity exec <container> /usr/local/bin/make_SVs_detection.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_SVs_detection.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_SVs_detection.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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