---
layout: container
name:  "quay.io/biocontainers/lr_gapcloser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lr_gapcloser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lr_gapcloser/container.yaml"
updated_at: "2025-12-07 04:01:40.316140"
latest: "1.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/lr_gapcloser"
aliases:
 - "LR_Gapcloser.sh"
 - "best-match-LR.pl"
 - "block_align.pl"
 - "change_case_fasta.pl"
 - "complete_retriver.pl"
 - "complete_substitute_limiter.pl"
 - "complete_ultimate_elect.pl"
 - "coverage_calculator.pl"
 - "coverage_filter.pl"
 - "find_sequnce_file.pl"
 - "form_sequence.pl"
 - "format_fa.pl"
 - "further_partial_select.pl"
 - "gap_bridging.pl"
 - "gap_finder.pl"
 - "group_partial.pl"
 - "info_formatter.pl"
 - "info_pacify.pl"
 - "join_LRlength.pl"
 - "last_Drepeat.pl"
 - "partial_ultimate_elect.pl"
 - "remove_wrong3.pl"
 - "retrieve-unique-alignment.pl"
 - "retriever_backfill.pl"
 - "same_filter.pl"
 - "tag_alignment_filter.pl"
 - "tag_distance_filter_classify.pl"
 - "tag_generator.pl"
 - "tag_orientation_corrector.pl"
 - "x86_64-conda-linux-gnu.cfg"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "sdust"
 - "bwa"
 - "paftools.js"
 - "k8"
 - "minimap2"
versions:
 - "1.0--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for lr_gapcloser"
config: {"url": "https://biocontainers.pro/tools/lr_gapcloser", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lr_gapcloser", "latest": {"1.0--pl5321hdfd78af_0": "sha256:58f8b2c747066be261e3366e98349be0190f8d7ac107e9ee33e639aee407c4af"}, "tags": {"1.0--pl5321hdfd78af_0": "sha256:58f8b2c747066be261e3366e98349be0190f8d7ac107e9ee33e639aee407c4af"}, "docker": "quay.io/biocontainers/lr_gapcloser", "aliases": {"LR_Gapcloser.sh": "/usr/local/bin/LR_Gapcloser.sh", "best-match-LR.pl": "/usr/local/bin/best-match-LR.pl", "block_align.pl": "/usr/local/bin/block_align.pl", "change_case_fasta.pl": "/usr/local/bin/change_case_fasta.pl", "complete_retriver.pl": "/usr/local/bin/complete_retriver.pl", "complete_substitute_limiter.pl": "/usr/local/bin/complete_substitute_limiter.pl", "complete_ultimate_elect.pl": "/usr/local/bin/complete_ultimate_elect.pl", "coverage_calculator.pl": "/usr/local/bin/coverage_calculator.pl", "coverage_filter.pl": "/usr/local/bin/coverage_filter.pl", "find_sequnce_file.pl": "/usr/local/bin/find_sequnce_file.pl", "form_sequence.pl": "/usr/local/bin/form_sequence.pl", "format_fa.pl": "/usr/local/bin/format_fa.pl", "further_partial_select.pl": "/usr/local/bin/further_partial_select.pl", "gap_bridging.pl": "/usr/local/bin/gap_bridging.pl", "gap_finder.pl": "/usr/local/bin/gap_finder.pl", "group_partial.pl": "/usr/local/bin/group_partial.pl", "info_formatter.pl": "/usr/local/bin/info_formatter.pl", "info_pacify.pl": "/usr/local/bin/info_pacify.pl", "join_LRlength.pl": "/usr/local/bin/join_LRlength.pl", "last_Drepeat.pl": "/usr/local/bin/last_Drepeat.pl", "partial_ultimate_elect.pl": "/usr/local/bin/partial_ultimate_elect.pl", "remove_wrong3.pl": "/usr/local/bin/remove_wrong3.pl", "retrieve-unique-alignment.pl": "/usr/local/bin/retrieve-unique-alignment.pl", "retriever_backfill.pl": "/usr/local/bin/retriever_backfill.pl", "same_filter.pl": "/usr/local/bin/same_filter.pl", "tag_alignment_filter.pl": "/usr/local/bin/tag_alignment_filter.pl", "tag_distance_filter_classify.pl": "/usr/local/bin/tag_distance_filter_classify.pl", "tag_generator.pl": "/usr/local/bin/tag_generator.pl", "tag_orientation_corrector.pl": "/usr/local/bin/tag_orientation_corrector.pl", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "sdust": "/usr/local/bin/sdust", "bwa": "/usr/local/bin/bwa", "paftools.js": "/usr/local/bin/paftools.js", "k8": "/usr/local/bin/k8", "minimap2": "/usr/local/bin/minimap2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lr_gapcloser.
singularity registry hpc automated addition for lr_gapcloser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lr_gapcloser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lr_gapcloser:1.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lr_gapcloser/1.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/lr_gapcloser/1.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lr_gapcloser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lr_gapcloser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lr_gapcloser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lr_gapcloser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lr_gapcloser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lr_gapcloser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LR_Gapcloser.sh

```bash
$ singularity exec <container> /usr/local/bin/LR_Gapcloser.sh
$ podman run --it --rm --entrypoint /usr/local/bin/LR_Gapcloser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LR_Gapcloser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### best-match-LR.pl

```bash
$ singularity exec <container> /usr/local/bin/best-match-LR.pl
$ podman run --it --rm --entrypoint /usr/local/bin/best-match-LR.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/best-match-LR.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### block_align.pl

```bash
$ singularity exec <container> /usr/local/bin/block_align.pl
$ podman run --it --rm --entrypoint /usr/local/bin/block_align.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/block_align.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### change_case_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/change_case_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/change_case_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/change_case_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complete_retriver.pl

```bash
$ singularity exec <container> /usr/local/bin/complete_retriver.pl
$ podman run --it --rm --entrypoint /usr/local/bin/complete_retriver.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complete_retriver.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complete_substitute_limiter.pl

```bash
$ singularity exec <container> /usr/local/bin/complete_substitute_limiter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/complete_substitute_limiter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complete_substitute_limiter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complete_ultimate_elect.pl

```bash
$ singularity exec <container> /usr/local/bin/complete_ultimate_elect.pl
$ podman run --it --rm --entrypoint /usr/local/bin/complete_ultimate_elect.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complete_ultimate_elect.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_calculator.pl

```bash
$ singularity exec <container> /usr/local/bin/coverage_calculator.pl
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_calculator.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_calculator.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/coverage_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_sequnce_file.pl

```bash
$ singularity exec <container> /usr/local/bin/find_sequnce_file.pl
$ podman run --it --rm --entrypoint /usr/local/bin/find_sequnce_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_sequnce_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### form_sequence.pl

```bash
$ singularity exec <container> /usr/local/bin/form_sequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/form_sequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/form_sequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### format_fa.pl

```bash
$ singularity exec <container> /usr/local/bin/format_fa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/format_fa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/format_fa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### further_partial_select.pl

```bash
$ singularity exec <container> /usr/local/bin/further_partial_select.pl
$ podman run --it --rm --entrypoint /usr/local/bin/further_partial_select.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/further_partial_select.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gap_bridging.pl

```bash
$ singularity exec <container> /usr/local/bin/gap_bridging.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gap_bridging.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gap_bridging.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gap_finder.pl

```bash
$ singularity exec <container> /usr/local/bin/gap_finder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gap_finder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gap_finder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### group_partial.pl

```bash
$ singularity exec <container> /usr/local/bin/group_partial.pl
$ podman run --it --rm --entrypoint /usr/local/bin/group_partial.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/group_partial.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### info_formatter.pl

```bash
$ singularity exec <container> /usr/local/bin/info_formatter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/info_formatter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/info_formatter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### info_pacify.pl

```bash
$ singularity exec <container> /usr/local/bin/info_pacify.pl
$ podman run --it --rm --entrypoint /usr/local/bin/info_pacify.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/info_pacify.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### join_LRlength.pl

```bash
$ singularity exec <container> /usr/local/bin/join_LRlength.pl
$ podman run --it --rm --entrypoint /usr/local/bin/join_LRlength.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/join_LRlength.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last_Drepeat.pl

```bash
$ singularity exec <container> /usr/local/bin/last_Drepeat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/last_Drepeat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last_Drepeat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### partial_ultimate_elect.pl

```bash
$ singularity exec <container> /usr/local/bin/partial_ultimate_elect.pl
$ podman run --it --rm --entrypoint /usr/local/bin/partial_ultimate_elect.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/partial_ultimate_elect.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_wrong3.pl

```bash
$ singularity exec <container> /usr/local/bin/remove_wrong3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/remove_wrong3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_wrong3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retrieve-unique-alignment.pl

```bash
$ singularity exec <container> /usr/local/bin/retrieve-unique-alignment.pl
$ podman run --it --rm --entrypoint /usr/local/bin/retrieve-unique-alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retrieve-unique-alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retriever_backfill.pl

```bash
$ singularity exec <container> /usr/local/bin/retriever_backfill.pl
$ podman run --it --rm --entrypoint /usr/local/bin/retriever_backfill.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retriever_backfill.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### same_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/same_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/same_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/same_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tag_alignment_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/tag_alignment_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/tag_alignment_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tag_alignment_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tag_distance_filter_classify.pl

```bash
$ singularity exec <container> /usr/local/bin/tag_distance_filter_classify.pl
$ podman run --it --rm --entrypoint /usr/local/bin/tag_distance_filter_classify.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tag_distance_filter_classify.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tag_generator.pl

```bash
$ singularity exec <container> /usr/local/bin/tag_generator.pl
$ podman run --it --rm --entrypoint /usr/local/bin/tag_generator.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tag_generator.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tag_orientation_corrector.pl

```bash
$ singularity exec <container> /usr/local/bin/tag_orientation_corrector.pl
$ podman run --it --rm --entrypoint /usr/local/bin/tag_orientation_corrector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tag_orientation_corrector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
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