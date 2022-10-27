---
layout: container
name:  "quay.io/biocontainers/makehub"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/makehub/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/makehub/container.yaml"
updated_at: "2022-10-27 01:02:26.691042"
latest: "1.0.5--1"
container_url: "https://biocontainers.pro/tools/makehub"
aliases:
 - "aa2nonred.pl"
 - "autoRun.pathInfo"
 - "compileSpliceCands"
 - "computeFlankingRegion.pl"
 - "espoca"
 - "eval_multi_gtf.pl"
 - "filterGenesIn.pl"
 - "findGffNamesInFasta.pl"
 - "genePredCheck"
 - "genePredToBigGenePred"
 - "getAnnoFastaFromJoingenes.py"
 - "getLinesMatching.pl"
 - "gtf2aa.pl"
 - "gth2gtf.pl"
 - "hgGcPercent"
 - "intron2exex.pl"
 - "ixIxx"
 - "make_hub.py"
 - "ratewig.pl"
 - "setStopCodonFreqs.pl"
 - "utrrnaseq"
 - "webserver-results.body"
versions:
 - "1.0.5--1"
description: "shpc-registry automated BioContainers addition for makehub"
config: {"url": "https://biocontainers.pro/tools/makehub", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for makehub", "latest": {"1.0.5--1": "sha256:bacc7df7a0af178ce0f37d361f72dd7388b689246d53e35384f0405601f63081"}, "tags": {"1.0.5--1": "sha256:bacc7df7a0af178ce0f37d361f72dd7388b689246d53e35384f0405601f63081"}, "docker": "quay.io/biocontainers/makehub", "aliases": {"aa2nonred.pl": "/usr/local/bin/aa2nonred.pl", "autoRun.pathInfo": "/usr/local/bin/autoRun.pathInfo", "compileSpliceCands": "/usr/local/bin/compileSpliceCands", "computeFlankingRegion.pl": "/usr/local/bin/computeFlankingRegion.pl", "espoca": "/usr/local/bin/espoca", "eval_multi_gtf.pl": "/usr/local/bin/eval_multi_gtf.pl", "filterGenesIn.pl": "/usr/local/bin/filterGenesIn.pl", "findGffNamesInFasta.pl": "/usr/local/bin/findGffNamesInFasta.pl", "genePredCheck": "/usr/local/bin/genePredCheck", "genePredToBigGenePred": "/usr/local/bin/genePredToBigGenePred", "getAnnoFastaFromJoingenes.py": "/usr/local/bin/getAnnoFastaFromJoingenes.py", "getLinesMatching.pl": "/usr/local/bin/getLinesMatching.pl", "gtf2aa.pl": "/usr/local/bin/gtf2aa.pl", "gth2gtf.pl": "/usr/local/bin/gth2gtf.pl", "hgGcPercent": "/usr/local/bin/hgGcPercent", "intron2exex.pl": "/usr/local/bin/intron2exex.pl", "ixIxx": "/usr/local/bin/ixIxx", "make_hub.py": "/usr/local/bin/make_hub.py", "ratewig.pl": "/usr/local/bin/ratewig.pl", "setStopCodonFreqs.pl": "/usr/local/bin/setStopCodonFreqs.pl", "utrrnaseq": "/usr/local/bin/utrrnaseq", "webserver-results.body": "/usr/local/bin/webserver-results.body"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/makehub.
shpc-registry automated BioContainers addition for makehub
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/makehub
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/makehub:1.0.5--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/makehub/1.0.5--1
$ module help quay.io/biocontainers/makehub/1.0.5--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### makehub-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### makehub-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### makehub-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### makehub-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### makehub-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### makehub-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aa2nonred.pl

```bash
$ singularity exec <container> /usr/local/bin/aa2nonred.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aa2nonred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aa2nonred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoRun.pathInfo

```bash
$ singularity exec <container> /usr/local/bin/autoRun.pathInfo
$ podman run --it --rm --entrypoint /usr/local/bin/autoRun.pathInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoRun.pathInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compileSpliceCands

```bash
$ singularity exec <container> /usr/local/bin/compileSpliceCands
$ podman run --it --rm --entrypoint /usr/local/bin/compileSpliceCands   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compileSpliceCands   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeFlankingRegion.pl

```bash
$ singularity exec <container> /usr/local/bin/computeFlankingRegion.pl
$ podman run --it --rm --entrypoint /usr/local/bin/computeFlankingRegion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeFlankingRegion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### espoca

```bash
$ singularity exec <container> /usr/local/bin/espoca
$ podman run --it --rm --entrypoint /usr/local/bin/espoca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/espoca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval_multi_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/eval_multi_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eval_multi_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval_multi_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterGenesIn.pl

```bash
$ singularity exec <container> /usr/local/bin/filterGenesIn.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filterGenesIn.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterGenesIn.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findGffNamesInFasta.pl

```bash
$ singularity exec <container> /usr/local/bin/findGffNamesInFasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/findGffNamesInFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findGffNamesInFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredCheck

```bash
$ singularity exec <container> /usr/local/bin/genePredCheck
$ podman run --it --rm --entrypoint /usr/local/bin/genePredCheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredCheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToBigGenePred

```bash
$ singularity exec <container> /usr/local/bin/genePredToBigGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToBigGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToBigGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getAnnoFastaFromJoingenes.py

```bash
$ singularity exec <container> /usr/local/bin/getAnnoFastaFromJoingenes.py
$ podman run --it --rm --entrypoint /usr/local/bin/getAnnoFastaFromJoingenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getAnnoFastaFromJoingenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getLinesMatching.pl

```bash
$ singularity exec <container> /usr/local/bin/getLinesMatching.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getLinesMatching.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getLinesMatching.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2aa.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf2aa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gth2gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/gth2gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gth2gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gth2gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hgGcPercent

```bash
$ singularity exec <container> /usr/local/bin/hgGcPercent
$ podman run --it --rm --entrypoint /usr/local/bin/hgGcPercent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hgGcPercent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron2exex.pl

```bash
$ singularity exec <container> /usr/local/bin/intron2exex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/intron2exex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron2exex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ixIxx

```bash
$ singularity exec <container> /usr/local/bin/ixIxx
$ podman run --it --rm --entrypoint /usr/local/bin/ixIxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ixIxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_hub.py

```bash
$ singularity exec <container> /usr/local/bin/make_hub.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_hub.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_hub.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ratewig.pl

```bash
$ singularity exec <container> /usr/local/bin/ratewig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ratewig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ratewig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setStopCodonFreqs.pl

```bash
$ singularity exec <container> /usr/local/bin/setStopCodonFreqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/setStopCodonFreqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setStopCodonFreqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### utrrnaseq

```bash
$ singularity exec <container> /usr/local/bin/utrrnaseq
$ podman run --it --rm --entrypoint /usr/local/bin/utrrnaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/utrrnaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webserver-results.body

```bash
$ singularity exec <container> /usr/local/bin/webserver-results.body
$ podman run --it --rm --entrypoint /usr/local/bin/webserver-results.body   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webserver-results.body   -v ${PWD} -w ${PWD} <container> -c " $@"
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