---
layout: container
name:  "quay.io/biocontainers/gecko"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gecko/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gecko/container.yaml"
updated_at: "2023-12-16 02:49:06.926758"
latest: "1.2--h031d066_4"
container_url: "https://biocontainers.pro/tools/gecko"
aliases:
 - "FragHits"
 - "allVsAll.sh"
 - "combineFrags"
 - "comparison.sh"
 - "csvExtractBorders"
 - "csvFrags2text"
 - "dictionary.sh"
 - "filterFrags"
 - "filterHits"
 - "fragStat"
 - "frags2align.sh"
 - "frags2borders.sh"
 - "frags2text"
 - "getInfo"
 - "hdStat"
 - "hits"
 - "hitsStat"
 - "indexmaker"
 - "matrix.mat"
 - "reverseComplement"
 - "sortHits"
 - "sortWords"
 - "w2hd"
 - "words"
 - "wordsStat"
 - "workflow.sh"
versions:
 - "1.2--hec16e2b_2"
 - "1.2--h031d066_4"
description: "shpc-registry automated BioContainers addition for gecko"
config: {"url": "https://biocontainers.pro/tools/gecko", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gecko", "latest": {"1.2--h031d066_4": "sha256:c96e11a77761da6e2a7de6f01fec38fab8b4cdb1ab7c35e5094ce6e613b6c954"}, "tags": {"1.2--hec16e2b_2": "sha256:7a96fe171453939e9d97798567247715d861220e5a9b1c20aa2a235b0a75d8a6", "1.2--h031d066_4": "sha256:c96e11a77761da6e2a7de6f01fec38fab8b4cdb1ab7c35e5094ce6e613b6c954"}, "docker": "quay.io/biocontainers/gecko", "aliases": {"FragHits": "/usr/local/bin/FragHits", "allVsAll.sh": "/usr/local/bin/allVsAll.sh", "combineFrags": "/usr/local/bin/combineFrags", "comparison.sh": "/usr/local/bin/comparison.sh", "csvExtractBorders": "/usr/local/bin/csvExtractBorders", "csvFrags2text": "/usr/local/bin/csvFrags2text", "dictionary.sh": "/usr/local/bin/dictionary.sh", "filterFrags": "/usr/local/bin/filterFrags", "filterHits": "/usr/local/bin/filterHits", "fragStat": "/usr/local/bin/fragStat", "frags2align.sh": "/usr/local/bin/frags2align.sh", "frags2borders.sh": "/usr/local/bin/frags2borders.sh", "frags2text": "/usr/local/bin/frags2text", "getInfo": "/usr/local/bin/getInfo", "hdStat": "/usr/local/bin/hdStat", "hits": "/usr/local/bin/hits", "hitsStat": "/usr/local/bin/hitsStat", "indexmaker": "/usr/local/bin/indexmaker", "matrix.mat": "/usr/local/bin/matrix.mat", "reverseComplement": "/usr/local/bin/reverseComplement", "sortHits": "/usr/local/bin/sortHits", "sortWords": "/usr/local/bin/sortWords", "w2hd": "/usr/local/bin/w2hd", "words": "/usr/local/bin/words", "wordsStat": "/usr/local/bin/wordsStat", "workflow.sh": "/usr/local/bin/workflow.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gecko.
shpc-registry automated BioContainers addition for gecko
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gecko
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gecko:1.2--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gecko/1.2--h031d066_4
$ module help quay.io/biocontainers/gecko/1.2--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gecko-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gecko-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gecko-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gecko-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gecko-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gecko-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FragHits

```bash
$ singularity exec <container> /usr/local/bin/FragHits
$ podman run --it --rm --entrypoint /usr/local/bin/FragHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### allVsAll.sh

```bash
$ singularity exec <container> /usr/local/bin/allVsAll.sh
$ podman run --it --rm --entrypoint /usr/local/bin/allVsAll.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/allVsAll.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineFrags

```bash
$ singularity exec <container> /usr/local/bin/combineFrags
$ podman run --it --rm --entrypoint /usr/local/bin/combineFrags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineFrags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparison.sh

```bash
$ singularity exec <container> /usr/local/bin/comparison.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparison.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparison.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvExtractBorders

```bash
$ singularity exec <container> /usr/local/bin/csvExtractBorders
$ podman run --it --rm --entrypoint /usr/local/bin/csvExtractBorders   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvExtractBorders   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvFrags2text

```bash
$ singularity exec <container> /usr/local/bin/csvFrags2text
$ podman run --it --rm --entrypoint /usr/local/bin/csvFrags2text   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvFrags2text   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dictionary.sh

```bash
$ singularity exec <container> /usr/local/bin/dictionary.sh
$ podman run --it --rm --entrypoint /usr/local/bin/dictionary.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dictionary.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterFrags

```bash
$ singularity exec <container> /usr/local/bin/filterFrags
$ podman run --it --rm --entrypoint /usr/local/bin/filterFrags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterFrags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterHits

```bash
$ singularity exec <container> /usr/local/bin/filterHits
$ podman run --it --rm --entrypoint /usr/local/bin/filterHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragStat

```bash
$ singularity exec <container> /usr/local/bin/fragStat
$ podman run --it --rm --entrypoint /usr/local/bin/fragStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### frags2align.sh

```bash
$ singularity exec <container> /usr/local/bin/frags2align.sh
$ podman run --it --rm --entrypoint /usr/local/bin/frags2align.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/frags2align.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### frags2borders.sh

```bash
$ singularity exec <container> /usr/local/bin/frags2borders.sh
$ podman run --it --rm --entrypoint /usr/local/bin/frags2borders.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/frags2borders.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### frags2text

```bash
$ singularity exec <container> /usr/local/bin/frags2text
$ podman run --it --rm --entrypoint /usr/local/bin/frags2text   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/frags2text   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getInfo

```bash
$ singularity exec <container> /usr/local/bin/getInfo
$ podman run --it --rm --entrypoint /usr/local/bin/getInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdStat

```bash
$ singularity exec <container> /usr/local/bin/hdStat
$ podman run --it --rm --entrypoint /usr/local/bin/hdStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hits

```bash
$ singularity exec <container> /usr/local/bin/hits
$ podman run --it --rm --entrypoint /usr/local/bin/hits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hitsStat

```bash
$ singularity exec <container> /usr/local/bin/hitsStat
$ podman run --it --rm --entrypoint /usr/local/bin/hitsStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hitsStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexmaker

```bash
$ singularity exec <container> /usr/local/bin/indexmaker
$ podman run --it --rm --entrypoint /usr/local/bin/indexmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matrix.mat

```bash
$ singularity exec <container> /usr/local/bin/matrix.mat
$ podman run --it --rm --entrypoint /usr/local/bin/matrix.mat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matrix.mat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reverseComplement

```bash
$ singularity exec <container> /usr/local/bin/reverseComplement
$ podman run --it --rm --entrypoint /usr/local/bin/reverseComplement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reverseComplement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortHits

```bash
$ singularity exec <container> /usr/local/bin/sortHits
$ podman run --it --rm --entrypoint /usr/local/bin/sortHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortWords

```bash
$ singularity exec <container> /usr/local/bin/sortWords
$ podman run --it --rm --entrypoint /usr/local/bin/sortWords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortWords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### w2hd

```bash
$ singularity exec <container> /usr/local/bin/w2hd
$ podman run --it --rm --entrypoint /usr/local/bin/w2hd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/w2hd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### words

```bash
$ singularity exec <container> /usr/local/bin/words
$ podman run --it --rm --entrypoint /usr/local/bin/words   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/words   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wordsStat

```bash
$ singularity exec <container> /usr/local/bin/wordsStat
$ podman run --it --rm --entrypoint /usr/local/bin/wordsStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wordsStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### workflow.sh

```bash
$ singularity exec <container> /usr/local/bin/workflow.sh
$ podman run --it --rm --entrypoint /usr/local/bin/workflow.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/workflow.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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