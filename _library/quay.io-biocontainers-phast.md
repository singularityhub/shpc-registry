---
layout: container
name:  "quay.io/biocontainers/phast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phast/container.yaml"
updated_at: "2023-09-02 02:47:25.607013"
latest: "1.5--h031d066_6"
container_url: "https://biocontainers.pro/tools/phast"
aliases:
 - "all_dists"
 - "base_evolve"
 - "chooseLines"
 - "clean_genes"
 - "consEntropy"
 - "convert_coords"
 - "display_rate_matrix"
 - "dless"
 - "dlessP"
 - "draw_tree"
 - "eval_predictions"
 - "exoniphy"
 - "hmm_train"
 - "hmm_tweak"
 - "hmm_view"
 - "indelFit"
 - "indelHistory"
 - "maf_parse"
 - "makeHKY"
 - "modFreqs"
 - "msa_diff"
 - "msa_split"
 - "msa_view"
 - "pbsDecode"
 - "pbsEncode"
 - "pbsScoreMatrix"
 - "pbsTrain"
 - "phast"
 - "phastBias"
 - "phastCons"
 - "phastMotif"
 - "phastOdds"
 - "phyloBoot"
 - "phyloFit"
 - "phyloP"
 - "prequel"
 - "refeature"
 - "stringiphy"
 - "treeGen"
 - "tree_doctor"
versions:
 - "1.5--hec16e2b_4"
 - "1.5--h031d066_6"
description: "shpc-registry automated BioContainers addition for phast"
config: {"url": "https://biocontainers.pro/tools/phast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phast", "latest": {"1.5--h031d066_6": "sha256:9f1363615f5174af9ca3915360e0486add86a05f7bda2f7a915a039894ca022d"}, "tags": {"1.5--hec16e2b_4": "sha256:b5339a2be861216f9d8d8a8aa5a7488be46808f7cb1e74c752c2036a88817c90", "1.5--h031d066_6": "sha256:9f1363615f5174af9ca3915360e0486add86a05f7bda2f7a915a039894ca022d"}, "docker": "quay.io/biocontainers/phast", "aliases": {"all_dists": "/usr/local/bin/all_dists", "base_evolve": "/usr/local/bin/base_evolve", "chooseLines": "/usr/local/bin/chooseLines", "clean_genes": "/usr/local/bin/clean_genes", "consEntropy": "/usr/local/bin/consEntropy", "convert_coords": "/usr/local/bin/convert_coords", "display_rate_matrix": "/usr/local/bin/display_rate_matrix", "dless": "/usr/local/bin/dless", "dlessP": "/usr/local/bin/dlessP", "draw_tree": "/usr/local/bin/draw_tree", "eval_predictions": "/usr/local/bin/eval_predictions", "exoniphy": "/usr/local/bin/exoniphy", "hmm_train": "/usr/local/bin/hmm_train", "hmm_tweak": "/usr/local/bin/hmm_tweak", "hmm_view": "/usr/local/bin/hmm_view", "indelFit": "/usr/local/bin/indelFit", "indelHistory": "/usr/local/bin/indelHistory", "maf_parse": "/usr/local/bin/maf_parse", "makeHKY": "/usr/local/bin/makeHKY", "modFreqs": "/usr/local/bin/modFreqs", "msa_diff": "/usr/local/bin/msa_diff", "msa_split": "/usr/local/bin/msa_split", "msa_view": "/usr/local/bin/msa_view", "pbsDecode": "/usr/local/bin/pbsDecode", "pbsEncode": "/usr/local/bin/pbsEncode", "pbsScoreMatrix": "/usr/local/bin/pbsScoreMatrix", "pbsTrain": "/usr/local/bin/pbsTrain", "phast": "/usr/local/bin/phast", "phastBias": "/usr/local/bin/phastBias", "phastCons": "/usr/local/bin/phastCons", "phastMotif": "/usr/local/bin/phastMotif", "phastOdds": "/usr/local/bin/phastOdds", "phyloBoot": "/usr/local/bin/phyloBoot", "phyloFit": "/usr/local/bin/phyloFit", "phyloP": "/usr/local/bin/phyloP", "prequel": "/usr/local/bin/prequel", "refeature": "/usr/local/bin/refeature", "stringiphy": "/usr/local/bin/stringiphy", "treeGen": "/usr/local/bin/treeGen", "tree_doctor": "/usr/local/bin/tree_doctor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phast.
shpc-registry automated BioContainers addition for phast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phast:1.5--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phast/1.5--h031d066_6
$ module help quay.io/biocontainers/phast/1.5--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### all_dists

```bash
$ singularity exec <container> /usr/local/bin/all_dists
$ podman run --it --rm --entrypoint /usr/local/bin/all_dists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/all_dists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base_evolve

```bash
$ singularity exec <container> /usr/local/bin/base_evolve
$ podman run --it --rm --entrypoint /usr/local/bin/base_evolve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base_evolve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chooseLines

```bash
$ singularity exec <container> /usr/local/bin/chooseLines
$ podman run --it --rm --entrypoint /usr/local/bin/chooseLines   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chooseLines   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clean_genes

```bash
$ singularity exec <container> /usr/local/bin/clean_genes
$ podman run --it --rm --entrypoint /usr/local/bin/clean_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clean_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consEntropy

```bash
$ singularity exec <container> /usr/local/bin/consEntropy
$ podman run --it --rm --entrypoint /usr/local/bin/consEntropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consEntropy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_coords

```bash
$ singularity exec <container> /usr/local/bin/convert_coords
$ podman run --it --rm --entrypoint /usr/local/bin/convert_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### display_rate_matrix

```bash
$ singularity exec <container> /usr/local/bin/display_rate_matrix
$ podman run --it --rm --entrypoint /usr/local/bin/display_rate_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/display_rate_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dless

```bash
$ singularity exec <container> /usr/local/bin/dless
$ podman run --it --rm --entrypoint /usr/local/bin/dless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dlessP

```bash
$ singularity exec <container> /usr/local/bin/dlessP
$ podman run --it --rm --entrypoint /usr/local/bin/dlessP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dlessP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_tree

```bash
$ singularity exec <container> /usr/local/bin/draw_tree
$ podman run --it --rm --entrypoint /usr/local/bin/draw_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_tree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval_predictions

```bash
$ singularity exec <container> /usr/local/bin/eval_predictions
$ podman run --it --rm --entrypoint /usr/local/bin/eval_predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval_predictions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exoniphy

```bash
$ singularity exec <container> /usr/local/bin/exoniphy
$ podman run --it --rm --entrypoint /usr/local/bin/exoniphy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exoniphy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_train

```bash
$ singularity exec <container> /usr/local/bin/hmm_train
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_tweak

```bash
$ singularity exec <container> /usr/local/bin/hmm_tweak
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_tweak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_tweak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_view

```bash
$ singularity exec <container> /usr/local/bin/hmm_view
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_view   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indelFit

```bash
$ singularity exec <container> /usr/local/bin/indelFit
$ podman run --it --rm --entrypoint /usr/local/bin/indelFit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indelFit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indelHistory

```bash
$ singularity exec <container> /usr/local/bin/indelHistory
$ podman run --it --rm --entrypoint /usr/local/bin/indelHistory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indelHistory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf_parse

```bash
$ singularity exec <container> /usr/local/bin/maf_parse
$ podman run --it --rm --entrypoint /usr/local/bin/maf_parse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf_parse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeHKY

```bash
$ singularity exec <container> /usr/local/bin/makeHKY
$ podman run --it --rm --entrypoint /usr/local/bin/makeHKY   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeHKY   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### modFreqs

```bash
$ singularity exec <container> /usr/local/bin/modFreqs
$ podman run --it --rm --entrypoint /usr/local/bin/modFreqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modFreqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msa_diff

```bash
$ singularity exec <container> /usr/local/bin/msa_diff
$ podman run --it --rm --entrypoint /usr/local/bin/msa_diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa_diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msa_split

```bash
$ singularity exec <container> /usr/local/bin/msa_split
$ podman run --it --rm --entrypoint /usr/local/bin/msa_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msa_view

```bash
$ singularity exec <container> /usr/local/bin/msa_view
$ podman run --it --rm --entrypoint /usr/local/bin/msa_view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa_view   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbsDecode

```bash
$ singularity exec <container> /usr/local/bin/pbsDecode
$ podman run --it --rm --entrypoint /usr/local/bin/pbsDecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbsDecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbsEncode

```bash
$ singularity exec <container> /usr/local/bin/pbsEncode
$ podman run --it --rm --entrypoint /usr/local/bin/pbsEncode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbsEncode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbsScoreMatrix

```bash
$ singularity exec <container> /usr/local/bin/pbsScoreMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/pbsScoreMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbsScoreMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbsTrain

```bash
$ singularity exec <container> /usr/local/bin/pbsTrain
$ podman run --it --rm --entrypoint /usr/local/bin/pbsTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbsTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phast

```bash
$ singularity exec <container> /usr/local/bin/phast
$ podman run --it --rm --entrypoint /usr/local/bin/phast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phastBias

```bash
$ singularity exec <container> /usr/local/bin/phastBias
$ podman run --it --rm --entrypoint /usr/local/bin/phastBias   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phastBias   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phastCons

```bash
$ singularity exec <container> /usr/local/bin/phastCons
$ podman run --it --rm --entrypoint /usr/local/bin/phastCons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phastCons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phastMotif

```bash
$ singularity exec <container> /usr/local/bin/phastMotif
$ podman run --it --rm --entrypoint /usr/local/bin/phastMotif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phastMotif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phastOdds

```bash
$ singularity exec <container> /usr/local/bin/phastOdds
$ podman run --it --rm --entrypoint /usr/local/bin/phastOdds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phastOdds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloBoot

```bash
$ singularity exec <container> /usr/local/bin/phyloBoot
$ podman run --it --rm --entrypoint /usr/local/bin/phyloBoot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloBoot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFit

```bash
$ singularity exec <container> /usr/local/bin/phyloFit
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloP

```bash
$ singularity exec <container> /usr/local/bin/phyloP
$ podman run --it --rm --entrypoint /usr/local/bin/phyloP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prequel

```bash
$ singularity exec <container> /usr/local/bin/prequel
$ podman run --it --rm --entrypoint /usr/local/bin/prequel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prequel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refeature

```bash
$ singularity exec <container> /usr/local/bin/refeature
$ podman run --it --rm --entrypoint /usr/local/bin/refeature   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refeature   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringiphy

```bash
$ singularity exec <container> /usr/local/bin/stringiphy
$ podman run --it --rm --entrypoint /usr/local/bin/stringiphy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringiphy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeGen

```bash
$ singularity exec <container> /usr/local/bin/treeGen
$ podman run --it --rm --entrypoint /usr/local/bin/treeGen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeGen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tree_doctor

```bash
$ singularity exec <container> /usr/local/bin/tree_doctor
$ podman run --it --rm --entrypoint /usr/local/bin/tree_doctor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tree_doctor   -v ${PWD} -w ${PWD} <container> -c " $@"
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