---
layout: container
name:  "quay.io/biocontainers/tcdemux"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tcdemux/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tcdemux/container.yaml"
updated_at: "2024-11-13 04:17:24.092209"
latest: "0.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tcdemux"
aliases:
 - "Xcalcmem.sh"
 - "bloomfilterparser.sh"
 - "eido"
 - "jwebserver"
 - "protoc-23.4.0"
 - "tcdemux"
 - "write_barcode_file.py"
 - "kmutate.sh"
 - "runhmm.sh"
 - "markdown-it"
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
 - "fetchproks.sh"
 - "filterqc.sh"
versions:
 - "0.0.13--pyhdfd78af_0"
 - "0.0.15--pyhdfd78af_0"
 - "0.0.24--pyhdfd78af_0"
 - "0.0.25--pyhdfd78af_1"
 - "0.0.26--pyhdfd78af_1"
 - "0.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for tcdemux"
config: {"url": "https://biocontainers.pro/tools/tcdemux", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tcdemux", "latest": {"0.1.1--pyhdfd78af_0": "sha256:e54462399fd9b61c3a29e1f95d8b7f927aa77d1f5d8cec3f72766586063b1b63"}, "tags": {"0.0.13--pyhdfd78af_0": "sha256:db69d9ff5ba15ddbec417470264584bd07de2a31dceced2bf1e337055823f942", "0.0.15--pyhdfd78af_0": "sha256:f0f53825c0c65e8962f1f312a9b9da601c07cbd87058fb6a706f4deaa122f5c9", "0.0.24--pyhdfd78af_0": "sha256:b3417fb12860e8da32dc3b6158f35c2c3e0a57651435781efeb8693cf05b6648", "0.0.25--pyhdfd78af_1": "sha256:6409853c5648d6f9eb1fa8fba4fc4cfe2451bfce36de2da128fda697d5b71b20", "0.0.26--pyhdfd78af_1": "sha256:e4b7aaafdaa07f422d73e46ea0d6472fdbb2f2f8a3e4e3c7d2dbffcf35c7cea0", "0.1.1--pyhdfd78af_0": "sha256:e54462399fd9b61c3a29e1f95d8b7f927aa77d1f5d8cec3f72766586063b1b63"}, "docker": "quay.io/biocontainers/tcdemux", "aliases": {"Xcalcmem.sh": "/usr/local/bin/Xcalcmem.sh", "bloomfilterparser.sh": "/usr/local/bin/bloomfilterparser.sh", "eido": "/usr/local/bin/eido", "jwebserver": "/usr/local/bin/jwebserver", "protoc-23.4.0": "/usr/local/bin/protoc-23.4.0", "tcdemux": "/usr/local/bin/tcdemux", "write_barcode_file.py": "/usr/local/bin/write_barcode_file.py", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "markdown-it": "/usr/local/bin/markdown-it", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "comparessu.sh": "/usr/local/bin/comparessu.sh", "filtersilva.sh": "/usr/local/bin/filtersilva.sh", "sketchblacklist2.sh": "/usr/local/bin/sketchblacklist2.sh", "splitribo.sh": "/usr/local/bin/splitribo.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh", "applyvariants.sh": "/usr/local/bin/applyvariants.sh", "bbcms.sh": "/usr/local/bin/bbcms.sh", "bloomfilter.sh": "/usr/local/bin/bloomfilter.sh", "callgenes.sh": "/usr/local/bin/callgenes.sh", "comparegff.sh": "/usr/local/bin/comparegff.sh", "consensus.sh": "/usr/local/bin/consensus.sh", "cutgff.sh": "/usr/local/bin/cutgff.sh", "fetchproks.sh": "/usr/local/bin/fetchproks.sh", "filterqc.sh": "/usr/local/bin/filterqc.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tcdemux.
singularity registry hpc automated addition for tcdemux
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tcdemux
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tcdemux:0.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tcdemux/0.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/tcdemux/0.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tcdemux-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tcdemux-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tcdemux-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tcdemux-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tcdemux-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tcdemux-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Xcalcmem.sh

```bash
$ singularity exec <container> /usr/local/bin/Xcalcmem.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Xcalcmem.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bloomfilterparser.sh

```bash
$ singularity exec <container> /usr/local/bin/bloomfilterparser.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bloomfilterparser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eido

```bash
$ singularity exec <container> /usr/local/bin/eido
$ podman run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-23.4.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-23.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-23.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-23.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tcdemux

```bash
$ singularity exec <container> /usr/local/bin/tcdemux
$ podman run --it --rm --entrypoint /usr/local/bin/tcdemux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tcdemux   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### write_barcode_file.py

```bash
$ singularity exec <container> /usr/local/bin/write_barcode_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/write_barcode_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/write_barcode_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fetchproks.sh

```bash
$ singularity exec <container> /usr/local/bin/fetchproks.sh
$ podman run --it --rm --entrypoint /usr/local/bin/fetchproks.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchproks.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterqc.sh

```bash
$ singularity exec <container> /usr/local/bin/filterqc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filterqc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterqc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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