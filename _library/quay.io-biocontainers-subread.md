---
layout: container
name:  "quay.io/biocontainers/subread"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/subread/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/subread/container.yaml"
updated_at: "2023-09-15 02:55:05.230119"
latest: "2.0.6--he4a0461_0"
container_url: "https://biocontainers.pro/tools/subread"
aliases:
 - "detectionCall"
 - "exactSNP"
 - "featureCounts"
 - "flattenGTF"
 - "genRandomReads"
 - "propmapped"
 - "qualityScores"
 - "removeDup"
 - "repair"
 - "subindel"
 - "subjunc"
 - "sublong"
 - "subread-align"
 - "subread-buildindex"
 - "subread-fullscan"
 - "txUnique"
versions:
 - "2.0.1--h7132678_2"
 - "2.0.3--h7132678_0"
 - "2.0.3--h7132678_1"
 - "2.0.3--he4a0461_3"
 - "2.0.6--he4a0461_0"
description: "shpc-registry automated BioContainers addition for subread"
config: {"url": "https://biocontainers.pro/tools/subread", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for subread", "latest": {"2.0.6--he4a0461_0": "sha256:ea3bf25194820592a3e8124ddb04870ee195774ffb5c37e0a156d57b5c8854db"}, "tags": {"2.0.1--h7132678_2": "sha256:6f4696f9eb45f8de613b889ec9adfcb200be4658de651edd14404bdd606ce729", "2.0.3--h7132678_0": "sha256:b8168397dd5c80756a36f79e0895cc2db73088c913f1e6e4fb10e80700a4b450", "2.0.3--h7132678_1": "sha256:103bc8194681315ccd060f45910f96b7ef2c64d6b4936d782a5d5e4181dd97a1", "2.0.3--he4a0461_3": "sha256:d9f33f7b19615086e85d0adbd6e75d68edd1e3fa861e859a98d5a8d267e5bcb8", "2.0.6--he4a0461_0": "sha256:ea3bf25194820592a3e8124ddb04870ee195774ffb5c37e0a156d57b5c8854db"}, "docker": "quay.io/biocontainers/subread", "aliases": {"detectionCall": "/usr/local/bin/detectionCall", "exactSNP": "/usr/local/bin/exactSNP", "featureCounts": "/usr/local/bin/featureCounts", "flattenGTF": "/usr/local/bin/flattenGTF", "genRandomReads": "/usr/local/bin/genRandomReads", "propmapped": "/usr/local/bin/propmapped", "qualityScores": "/usr/local/bin/qualityScores", "removeDup": "/usr/local/bin/removeDup", "repair": "/usr/local/bin/repair", "subindel": "/usr/local/bin/subindel", "subjunc": "/usr/local/bin/subjunc", "sublong": "/usr/local/bin/sublong", "subread-align": "/usr/local/bin/subread-align", "subread-buildindex": "/usr/local/bin/subread-buildindex", "subread-fullscan": "/usr/local/bin/subread-fullscan", "txUnique": "/usr/local/bin/txUnique"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/subread.
shpc-registry automated BioContainers addition for subread
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/subread
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/subread:2.0.6--he4a0461_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/subread/2.0.6--he4a0461_0
$ module help quay.io/biocontainers/subread/2.0.6--he4a0461_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### subread-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### subread-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### subread-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### subread-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### subread-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### subread-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### txUnique

```bash
$ singularity exec <container> /usr/local/bin/txUnique
$ podman run --it --rm --entrypoint /usr/local/bin/txUnique   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/txUnique   -v ${PWD} -w ${PWD} <container> -c " $@"
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