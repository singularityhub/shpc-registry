---
layout: container
name:  "quay.io/biocontainers/metamate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metamate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metamate/container.yaml"
updated_at: "2024-06-04 03:00:49.751274"
latest: "0.4.3--pyr43h7cba7a3_0"
container_url: "https://biocontainers.pro/tools/metamate"
aliases:
 - "bbcrisprfinder.sh"
 - "bbsort.sh"
 - "bloomfilterparser.sh"
 - "checkstrand.sh"
 - "copyfile.sh"
 - "countbarcodes2.sh"
 - "countduplicates.sh"
 - "filtertranslate"
 - "findrepeats.sh"
 - "gawk-5.3.0"
 - "maketree.R"
 - "metaMATE"
 - "metamate"
 - "netfilter.sh"
 - "scoresequence.sh"
 - "seqtovec.sh"
 - "train.sh"
 - "gawkbug"
 - "Xcalcmem.sh"
 - "annot-tsv"
 - "kmutate.sh"
 - "runhmm.sh"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "summarizecoverage.sh"
 - "alltoall.sh"
 - "analyzesketchresults.sh"
 - "comparessu.sh"
 - "filtersilva.sh"
 - "sketchblacklist2.sh"
 - "splitribo.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
 - "applyvariants.sh"
 - "bbcms.sh"
 - "bloomfilter.sh"
 - "callgenes.sh"
 - "comparegff.sh"
 - "consensus.sh"
 - "cutgff.sh"
versions:
 - "0.4.3--pyr43h7cba7a3_0"
description: "singularity registry hpc automated addition for metamate"
config: {"url": "https://biocontainers.pro/tools/metamate", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metamate", "latest": {"0.4.3--pyr43h7cba7a3_0": "sha256:62636f645bc5ab4ff56584d92df922175ff6b23288dc42b281e0316a624ed28a"}, "tags": {"0.4.3--pyr43h7cba7a3_0": "sha256:62636f645bc5ab4ff56584d92df922175ff6b23288dc42b281e0316a624ed28a"}, "docker": "quay.io/biocontainers/metamate", "aliases": {"bbcrisprfinder.sh": "/usr/local/bin/bbcrisprfinder.sh", "bbsort.sh": "/usr/local/bin/bbsort.sh", "bloomfilterparser.sh": "/usr/local/bin/bloomfilterparser.sh", "checkstrand.sh": "/usr/local/bin/checkstrand.sh", "copyfile.sh": "/usr/local/bin/copyfile.sh", "countbarcodes2.sh": "/usr/local/bin/countbarcodes2.sh", "countduplicates.sh": "/usr/local/bin/countduplicates.sh", "filtertranslate": "/usr/local/bin/filtertranslate", "findrepeats.sh": "/usr/local/bin/findrepeats.sh", "gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "maketree.R": "/usr/local/bin/maketree.R", "metaMATE": "/usr/local/bin/metaMATE", "metamate": "/usr/local/bin/metamate", "netfilter.sh": "/usr/local/bin/netfilter.sh", "scoresequence.sh": "/usr/local/bin/scoresequence.sh", "seqtovec.sh": "/usr/local/bin/seqtovec.sh", "train.sh": "/usr/local/bin/train.sh", "gawkbug": "/usr/local/bin/gawkbug", "Xcalcmem.sh": "/usr/local/bin/Xcalcmem.sh", "annot-tsv": "/usr/local/bin/annot-tsv", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "comparessu.sh": "/usr/local/bin/comparessu.sh", "filtersilva.sh": "/usr/local/bin/filtersilva.sh", "sketchblacklist2.sh": "/usr/local/bin/sketchblacklist2.sh", "splitribo.sh": "/usr/local/bin/splitribo.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh", "applyvariants.sh": "/usr/local/bin/applyvariants.sh", "bbcms.sh": "/usr/local/bin/bbcms.sh", "bloomfilter.sh": "/usr/local/bin/bloomfilter.sh", "callgenes.sh": "/usr/local/bin/callgenes.sh", "comparegff.sh": "/usr/local/bin/comparegff.sh", "consensus.sh": "/usr/local/bin/consensus.sh", "cutgff.sh": "/usr/local/bin/cutgff.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metamate.
singularity registry hpc automated addition for metamate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metamate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metamate:0.4.3--pyr43h7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metamate/0.4.3--pyr43h7cba7a3_0
$ module help quay.io/biocontainers/metamate/0.4.3--pyr43h7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metamate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metamate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metamate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metamate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metamate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metamate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bbcrisprfinder.sh

```bash
$ singularity exec <container> /usr/local/bin/bbcrisprfinder.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbcrisprfinder.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbcrisprfinder.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbsort.sh

```bash
$ singularity exec <container> /usr/local/bin/bbsort.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbsort.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbsort.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bloomfilterparser.sh

```bash
$ singularity exec <container> /usr/local/bin/bloomfilterparser.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkstrand.sh

```bash
$ singularity exec <container> /usr/local/bin/checkstrand.sh
$ podman run --it --rm --entrypoint /usr/local/bin/checkstrand.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkstrand.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copyfile.sh

```bash
$ singularity exec <container> /usr/local/bin/copyfile.sh
$ podman run --it --rm --entrypoint /usr/local/bin/copyfile.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copyfile.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### countbarcodes2.sh

```bash
$ singularity exec <container> /usr/local/bin/countbarcodes2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/countbarcodes2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/countbarcodes2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### countduplicates.sh

```bash
$ singularity exec <container> /usr/local/bin/countduplicates.sh
$ podman run --it --rm --entrypoint /usr/local/bin/countduplicates.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/countduplicates.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filtertranslate

```bash
$ singularity exec <container> /usr/local/bin/filtertranslate
$ podman run --it --rm --entrypoint /usr/local/bin/filtertranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filtertranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrepeats.sh

```bash
$ singularity exec <container> /usr/local/bin/findrepeats.sh
$ podman run --it --rm --entrypoint /usr/local/bin/findrepeats.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrepeats.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maketree.R

```bash
$ singularity exec <container> /usr/local/bin/maketree.R
$ podman run --it --rm --entrypoint /usr/local/bin/maketree.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maketree.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaMATE

```bash
$ singularity exec <container> /usr/local/bin/metaMATE
$ podman run --it --rm --entrypoint /usr/local/bin/metaMATE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaMATE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metamate

```bash
$ singularity exec <container> /usr/local/bin/metamate
$ podman run --it --rm --entrypoint /usr/local/bin/metamate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metamate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### netfilter.sh

```bash
$ singularity exec <container> /usr/local/bin/netfilter.sh
$ podman run --it --rm --entrypoint /usr/local/bin/netfilter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/netfilter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scoresequence.sh

```bash
$ singularity exec <container> /usr/local/bin/scoresequence.sh
$ podman run --it --rm --entrypoint /usr/local/bin/scoresequence.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scoresequence.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtovec.sh

```bash
$ singularity exec <container> /usr/local/bin/seqtovec.sh
$ podman run --it --rm --entrypoint /usr/local/bin/seqtovec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtovec.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train.sh

```bash
$ singularity exec <container> /usr/local/bin/train.sh
$ podman run --it --rm --entrypoint /usr/local/bin/train.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Xcalcmem.sh

```bash
$ singularity exec <container> /usr/local/bin/Xcalcmem.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerposition.sh

```bash
$ singularity exec <container> /usr/local/bin/kmerposition.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformatpb.sh

```bash
$ singularity exec <container> /usr/local/bin/reformatpb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizecoverage.sh

```bash
$ singularity exec <container> /usr/local/bin/summarizecoverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparessu.sh

```bash
$ singularity exec <container> /usr/local/bin/comparessu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filtersilva.sh

```bash
$ singularity exec <container> /usr/local/bin/filtersilva.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sketchblacklist2.sh

```bash
$ singularity exec <container> /usr/local/bin/sketchblacklist2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitribo.sh

```bash
$ singularity exec <container> /usr/local/bin/splitribo.sh
$ podman run --it --rm --entrypoint /usr/local/bin/splitribo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitribo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzeaccession.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzeaccession.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzegenes.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzegenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### applyvariants.sh

```bash
$ singularity exec <container> /usr/local/bin/applyvariants.sh
$ podman run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbcms.sh

```bash
$ singularity exec <container> /usr/local/bin/bbcms.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbcms.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbcms.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bloomfilter.sh

```bash
$ singularity exec <container> /usr/local/bin/bloomfilter.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bloomfilter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bloomfilter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### callgenes.sh

```bash
$ singularity exec <container> /usr/local/bin/callgenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/callgenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/callgenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparegff.sh

```bash
$ singularity exec <container> /usr/local/bin/comparegff.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparegff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparegff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus.sh

```bash
$ singularity exec <container> /usr/local/bin/consensus.sh
$ podman run --it --rm --entrypoint /usr/local/bin/consensus.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutgff.sh

```bash
$ singularity exec <container> /usr/local/bin/cutgff.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cutgff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutgff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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