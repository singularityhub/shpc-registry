---
layout: container
name:  "quay.io/biocontainers/binsanity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/binsanity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/binsanity/container.yaml"
updated_at: "2023-04-28 03:19:55.481285"
latest: "0.5.4--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/binsanity"
aliases:
 - "Binsanity"
 - "Binsanity-lc"
 - "Binsanity-profile"
 - "Binsanity-refine"
 - "Binsanity-wf"
 - "Binsanity2-beta"
 - "bin_evaluation"
 - "checkm"
 - "checkm_analysis"
 - "concat"
 - "detectionCall"
 - "exactSNP"
 - "featureCounts"
 - "flattenGTF"
 - "genRandomReads"
 - "get-ids"
 - "identifyHMM"
 - "propmapped"
 - "qualityScores"
 - "removeDup"
 - "repair"
 - "simplify-fasta"
 - "subindel"
 - "subjunc"
 - "sublong"
 - "subread-align"
 - "subread-buildindex"
 - "subread-fullscan"
 - "transform-coverage-profile"
 - "txUnique"
 - "rppr"
 - "guppy"
 - "pplacer"
 - "dendropy-format"
 - "sumlabels.py"
 - "sumtrees.py"
 - "prodigal"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
versions:
 - "0.5.4--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for binsanity"
config: {"url": "https://biocontainers.pro/tools/binsanity", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for binsanity", "latest": {"0.5.4--pyh5e36f6f_0": "sha256:f26930aa4e25a370288a7361a42844eaa7017c4b97c11642cfacff3113b99731"}, "tags": {"0.5.4--pyh5e36f6f_0": "sha256:f26930aa4e25a370288a7361a42844eaa7017c4b97c11642cfacff3113b99731"}, "docker": "quay.io/biocontainers/binsanity", "aliases": {"Binsanity": "/usr/local/bin/Binsanity", "Binsanity-lc": "/usr/local/bin/Binsanity-lc", "Binsanity-profile": "/usr/local/bin/Binsanity-profile", "Binsanity-refine": "/usr/local/bin/Binsanity-refine", "Binsanity-wf": "/usr/local/bin/Binsanity-wf", "Binsanity2-beta": "/usr/local/bin/Binsanity2-beta", "bin_evaluation": "/usr/local/bin/bin_evaluation", "checkm": "/usr/local/bin/checkm", "checkm_analysis": "/usr/local/bin/checkm_analysis", "concat": "/usr/local/bin/concat", "detectionCall": "/usr/local/bin/detectionCall", "exactSNP": "/usr/local/bin/exactSNP", "featureCounts": "/usr/local/bin/featureCounts", "flattenGTF": "/usr/local/bin/flattenGTF", "genRandomReads": "/usr/local/bin/genRandomReads", "get-ids": "/usr/local/bin/get-ids", "identifyHMM": "/usr/local/bin/identifyHMM", "propmapped": "/usr/local/bin/propmapped", "qualityScores": "/usr/local/bin/qualityScores", "removeDup": "/usr/local/bin/removeDup", "repair": "/usr/local/bin/repair", "simplify-fasta": "/usr/local/bin/simplify-fasta", "subindel": "/usr/local/bin/subindel", "subjunc": "/usr/local/bin/subjunc", "sublong": "/usr/local/bin/sublong", "subread-align": "/usr/local/bin/subread-align", "subread-buildindex": "/usr/local/bin/subread-buildindex", "subread-fullscan": "/usr/local/bin/subread-fullscan", "transform-coverage-profile": "/usr/local/bin/transform-coverage-profile", "txUnique": "/usr/local/bin/txUnique", "rppr": "/usr/local/bin/rppr", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "dendropy-format": "/usr/local/bin/dendropy-format", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "prodigal": "/usr/local/bin/prodigal", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/binsanity.
shpc-registry automated BioContainers addition for binsanity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/binsanity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/binsanity:0.5.4--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/binsanity/0.5.4--pyh5e36f6f_0
$ module help quay.io/biocontainers/binsanity/0.5.4--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### binsanity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### binsanity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### binsanity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### binsanity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### binsanity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### binsanity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Binsanity

```bash
$ singularity exec <container> /usr/local/bin/Binsanity
$ podman run --it --rm --entrypoint /usr/local/bin/Binsanity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Binsanity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Binsanity-lc

```bash
$ singularity exec <container> /usr/local/bin/Binsanity-lc
$ podman run --it --rm --entrypoint /usr/local/bin/Binsanity-lc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Binsanity-lc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Binsanity-profile

```bash
$ singularity exec <container> /usr/local/bin/Binsanity-profile
$ podman run --it --rm --entrypoint /usr/local/bin/Binsanity-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Binsanity-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Binsanity-refine

```bash
$ singularity exec <container> /usr/local/bin/Binsanity-refine
$ podman run --it --rm --entrypoint /usr/local/bin/Binsanity-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Binsanity-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Binsanity-wf

```bash
$ singularity exec <container> /usr/local/bin/Binsanity-wf
$ podman run --it --rm --entrypoint /usr/local/bin/Binsanity-wf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Binsanity-wf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Binsanity2-beta

```bash
$ singularity exec <container> /usr/local/bin/Binsanity2-beta
$ podman run --it --rm --entrypoint /usr/local/bin/Binsanity2-beta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Binsanity2-beta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bin_evaluation

```bash
$ singularity exec <container> /usr/local/bin/bin_evaluation
$ podman run --it --rm --entrypoint /usr/local/bin/bin_evaluation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bin_evaluation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm_analysis

```bash
$ singularity exec <container> /usr/local/bin/checkm_analysis
$ podman run --it --rm --entrypoint /usr/local/bin/checkm_analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm_analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concat

```bash
$ singularity exec <container> /usr/local/bin/concat
$ podman run --it --rm --entrypoint /usr/local/bin/concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### detectionCall

```bash
$ singularity exec <container> /usr/local/bin/detectionCall
$ podman run --it --rm --entrypoint /usr/local/bin/detectionCall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/detectionCall   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### flattenGTF

```bash
$ singularity exec <container> /usr/local/bin/flattenGTF
$ podman run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flattenGTF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genRandomReads

```bash
$ singularity exec <container> /usr/local/bin/genRandomReads
$ podman run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genRandomReads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-ids

```bash
$ singularity exec <container> /usr/local/bin/get-ids
$ podman run --it --rm --entrypoint /usr/local/bin/get-ids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-ids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### identifyHMM

```bash
$ singularity exec <container> /usr/local/bin/identifyHMM
$ podman run --it --rm --entrypoint /usr/local/bin/identifyHMM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/identifyHMM   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### simplify-fasta

```bash
$ singularity exec <container> /usr/local/bin/simplify-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/simplify-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simplify-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sublong

```bash
$ singularity exec <container> /usr/local/bin/sublong
$ podman run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sublong   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### subread-fullscan

```bash
$ singularity exec <container> /usr/local/bin/subread-fullscan
$ podman run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subread-fullscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transform-coverage-profile

```bash
$ singularity exec <container> /usr/local/bin/transform-coverage-profile
$ podman run --it --rm --entrypoint /usr/local/bin/transform-coverage-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transform-coverage-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### txUnique

```bash
$ singularity exec <container> /usr/local/bin/txUnique
$ podman run --it --rm --entrypoint /usr/local/bin/txUnique   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/txUnique   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easel

```bash
$ singularity exec <container> /usr/local/bin/easel
$ podman run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mixdchlet

```bash
$ singularity exec <container> /usr/local/bin/esl-mixdchlet
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
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