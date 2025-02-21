---
layout: container
name:  "quay.io/biocontainers/strainr2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strainr2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strainr2/container.yaml"
updated_at: "2025-02-21 03:02:25.559760"
latest: "2.1.0--r44h577a1d6_1"
container_url: "https://biocontainers.pro/tools/strainr2"
aliases:
 - "Plot.R"
 - "PreProcessR"
 - "StrainR"
 - "bloomfilterparser.sh"
 - "hashcounter.py"
 - "sourmash"
 - "subcontig"
 - "Xcalcmem.sh"
 - "jwebserver"
 - "screed"
 - "kmutate.sh"
 - "runhmm.sh"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "summarizecoverage.sh"
 - "alltoall.sh"
 - "analyzesketchresults.sh"
 - "comparessu.sh"
 - "filtersilva.sh"
 - "pcre2posix_test"
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
versions:
 - "1.0.0--py312r43h031d066_0"
 - "1.0.1--py312r43hf67a6ed_1"
 - "2.1.0--he4a0461_0"
 - "2.0.0--r43h031d066_1"
 - "2.1.0--r44h577a1d6_1"
description: "singularity registry hpc automated addition for strainr2"
config: {"url": "https://biocontainers.pro/tools/strainr2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for strainr2", "latest": {"2.1.0--r44h577a1d6_1": "sha256:16511c69028e3678f51a2772782bd81921abb8b3a6e363fc6b51d9418187d204"}, "tags": {"1.0.0--py312r43h031d066_0": "sha256:874eb1c063b537f4dfdf963bdd8316aa8905605e691f6dcd05039d8b8e6b8420", "1.0.1--py312r43hf67a6ed_1": "sha256:54e7ac8ac4824d1beef139a825c626eacd6533f8272a7e98a7782a07c113eedd", "2.1.0--he4a0461_0": "sha256:0c473e6e86aebd6f5c4cff4bb181240c13a4833a678ea57a10050e57692423ef", "2.0.0--r43h031d066_1": "sha256:365992ee3b7518f169d567bdbd3a9166fcad7d8ff67c7c321bc9c01f129e28a1", "2.1.0--r44h577a1d6_1": "sha256:16511c69028e3678f51a2772782bd81921abb8b3a6e363fc6b51d9418187d204"}, "docker": "quay.io/biocontainers/strainr2", "aliases": {"Plot.R": "/usr/local/bin/Plot.R", "PreProcessR": "/usr/local/bin/PreProcessR", "StrainR": "/usr/local/bin/StrainR", "bloomfilterparser.sh": "/usr/local/bin/bloomfilterparser.sh", "hashcounter.py": "/usr/local/bin/hashcounter.py", "sourmash": "/usr/local/bin/sourmash", "subcontig": "/usr/local/bin/subcontig", "Xcalcmem.sh": "/usr/local/bin/Xcalcmem.sh", "jwebserver": "/usr/local/bin/jwebserver", "screed": "/usr/local/bin/screed", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "comparessu.sh": "/usr/local/bin/comparessu.sh", "filtersilva.sh": "/usr/local/bin/filtersilva.sh", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "sketchblacklist2.sh": "/usr/local/bin/sketchblacklist2.sh", "splitribo.sh": "/usr/local/bin/splitribo.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh", "applyvariants.sh": "/usr/local/bin/applyvariants.sh", "bbcms.sh": "/usr/local/bin/bbcms.sh", "bloomfilter.sh": "/usr/local/bin/bloomfilter.sh", "callgenes.sh": "/usr/local/bin/callgenes.sh", "comparegff.sh": "/usr/local/bin/comparegff.sh", "consensus.sh": "/usr/local/bin/consensus.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strainr2.
singularity registry hpc automated addition for strainr2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strainr2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strainr2:2.1.0--r44h577a1d6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strainr2/2.1.0--r44h577a1d6_1
$ module help quay.io/biocontainers/strainr2/2.1.0--r44h577a1d6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strainr2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strainr2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strainr2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strainr2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strainr2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strainr2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Plot.R

```bash
$ singularity exec <container> /usr/local/bin/Plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/Plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PreProcessR

```bash
$ singularity exec <container> /usr/local/bin/PreProcessR
$ podman run --it --rm --entrypoint /usr/local/bin/PreProcessR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PreProcessR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StrainR

```bash
$ singularity exec <container> /usr/local/bin/StrainR
$ podman run --it --rm --entrypoint /usr/local/bin/StrainR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StrainR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bloomfilterparser.sh

```bash
$ singularity exec <container> /usr/local/bin/bloomfilterparser.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hashcounter.py

```bash
$ singularity exec <container> /usr/local/bin/hashcounter.py
$ podman run --it --rm --entrypoint /usr/local/bin/hashcounter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hashcounter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sourmash

```bash
$ singularity exec <container> /usr/local/bin/sourmash
$ podman run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subcontig

```bash
$ singularity exec <container> /usr/local/bin/subcontig
$ podman run --it --rm --entrypoint /usr/local/bin/subcontig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subcontig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Xcalcmem.sh

```bash
$ singularity exec <container> /usr/local/bin/Xcalcmem.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### screed

```bash
$ singularity exec <container> /usr/local/bin/screed
$ podman run --it --rm --entrypoint /usr/local/bin/screed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/screed   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
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