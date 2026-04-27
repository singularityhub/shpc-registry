---
layout: container
name:  "quay.io/biocontainers/majec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/majec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/majec/container.yaml"
updated_at: "2026-04-27 05:34:46.867671"
latest: "0.1.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/majec"
aliases:
 - "majec_add_norm_factors"
 - "majec_build_db"
 - "majec_calc_frag_len"
 - "majec_calc_thresholds"
 - "majec_precompute_annotations"
 - "majec_prepare_deseq2"
 - "majec_run_pipeline"
 - "majec_visualize"
 - "genRandomReads"
 - "flattenGTF"
 - "propmapped"
 - "qualityScores"
 - "removeDup"
 - "repair"
 - "sublong"
 - "subread-fullscan"
 - "exactSNP"
 - "featureCounts"
 - "subindel"
 - "subjunc"
 - "subread-align"
 - "subread-buildindex"
 - "ref-cache"
 - "annot-tsv"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
versions:
 - "0.1.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for majec"
config: {"url": "https://biocontainers.pro/tools/majec", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for majec", "latest": {"0.1.4--pyhdfd78af_0": "sha256:b61b262f88e6d67513304ab1936e634281f769ce2310360387c711d8eafea5b5"}, "tags": {"0.1.4--pyhdfd78af_0": "sha256:b61b262f88e6d67513304ab1936e634281f769ce2310360387c711d8eafea5b5"}, "docker": "quay.io/biocontainers/majec", "aliases": {"majec_add_norm_factors": "/usr/local/bin/majec_add_norm_factors", "majec_build_db": "/usr/local/bin/majec_build_db", "majec_calc_frag_len": "/usr/local/bin/majec_calc_frag_len", "majec_calc_thresholds": "/usr/local/bin/majec_calc_thresholds", "majec_precompute_annotations": "/usr/local/bin/majec_precompute_annotations", "majec_prepare_deseq2": "/usr/local/bin/majec_prepare_deseq2", "majec_run_pipeline": "/usr/local/bin/majec_run_pipeline", "majec_visualize": "/usr/local/bin/majec_visualize", "genRandomReads": "/usr/local/bin/genRandomReads", "flattenGTF": "/usr/local/bin/flattenGTF", "propmapped": "/usr/local/bin/propmapped", "qualityScores": "/usr/local/bin/qualityScores", "removeDup": "/usr/local/bin/removeDup", "repair": "/usr/local/bin/repair", "sublong": "/usr/local/bin/sublong", "subread-fullscan": "/usr/local/bin/subread-fullscan", "exactSNP": "/usr/local/bin/exactSNP", "featureCounts": "/usr/local/bin/featureCounts", "subindel": "/usr/local/bin/subindel", "subjunc": "/usr/local/bin/subjunc", "subread-align": "/usr/local/bin/subread-align", "subread-buildindex": "/usr/local/bin/subread-buildindex", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/majec.
singularity registry hpc automated addition for majec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/majec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/majec:0.1.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/majec/0.1.4--pyhdfd78af_0
$ module help quay.io/biocontainers/majec/0.1.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### majec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### majec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### majec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### majec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### majec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### majec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### majec_add_norm_factors

```bash
$ singularity exec <container> /usr/local/bin/majec_add_norm_factors
$ podman run --it --rm --entrypoint /usr/local/bin/majec_add_norm_factors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_add_norm_factors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majec_build_db

```bash
$ singularity exec <container> /usr/local/bin/majec_build_db
$ podman run --it --rm --entrypoint /usr/local/bin/majec_build_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_build_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majec_calc_frag_len

```bash
$ singularity exec <container> /usr/local/bin/majec_calc_frag_len
$ podman run --it --rm --entrypoint /usr/local/bin/majec_calc_frag_len   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_calc_frag_len   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majec_calc_thresholds

```bash
$ singularity exec <container> /usr/local/bin/majec_calc_thresholds
$ podman run --it --rm --entrypoint /usr/local/bin/majec_calc_thresholds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_calc_thresholds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majec_precompute_annotations

```bash
$ singularity exec <container> /usr/local/bin/majec_precompute_annotations
$ podman run --it --rm --entrypoint /usr/local/bin/majec_precompute_annotations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_precompute_annotations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majec_prepare_deseq2

```bash
$ singularity exec <container> /usr/local/bin/majec_prepare_deseq2
$ podman run --it --rm --entrypoint /usr/local/bin/majec_prepare_deseq2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_prepare_deseq2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majec_run_pipeline

```bash
$ singularity exec <container> /usr/local/bin/majec_run_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/majec_run_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_run_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### majec_visualize

```bash
$ singularity exec <container> /usr/local/bin/majec_visualize
$ podman run --it --rm --entrypoint /usr/local/bin/majec_visualize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/majec_visualize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genRandomReads

```bash
$ singularity exec <container> /usr/local/bin/genRandomReads
$ podman run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flattenGTF

```bash
$ singularity exec <container> /usr/local/bin/flattenGTF
$ podman run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### propmapped

```bash
$ singularity exec <container> /usr/local/bin/propmapped
$ podman run --it --rm --entrypoint /usr/local/bin/propmapped   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/propmapped   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualityScores

```bash
$ singularity exec <container> /usr/local/bin/qualityScores
$ podman run --it --rm --entrypoint /usr/local/bin/qualityScores   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualityScores   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### removeDup

```bash
$ singularity exec <container> /usr/local/bin/removeDup
$ podman run --it --rm --entrypoint /usr/local/bin/removeDup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/removeDup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repair

```bash
$ singularity exec <container> /usr/local/bin/repair
$ podman run --it --rm --entrypoint /usr/local/bin/repair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sublong

```bash
$ singularity exec <container> /usr/local/bin/sublong
$ podman run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-fullscan

```bash
$ singularity exec <container> /usr/local/bin/subread-fullscan
$ podman run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exactSNP

```bash
$ singularity exec <container> /usr/local/bin/exactSNP
$ podman run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exactSNP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featureCounts

```bash
$ singularity exec <container> /usr/local/bin/featureCounts
$ podman run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featureCounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subindel

```bash
$ singularity exec <container> /usr/local/bin/subindel
$ podman run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subindel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subjunc

```bash
$ singularity exec <container> /usr/local/bin/subjunc
$ podman run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subjunc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-align

```bash
$ singularity exec <container> /usr/local/bin/subread-align
$ podman run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subread-buildindex

```bash
$ singularity exec <container> /usr/local/bin/subread-buildindex
$ podman run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-buildindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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