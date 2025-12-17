---
layout: container
name:  "quay.io/biocontainers/mauvealigner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mauvealigner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mauvealigner/container.yaml"
updated_at: "2025-12-17 04:13:00.673266"
latest: "1.2.0--he153687_5"
container_url: "https://biocontainers.pro/tools/mauvealigner"
aliases:
 - "addUnalignedIntervals"
 - "alignmentProjector"
 - "backbone_global_to_local"
 - "bbAnalyze"
 - "bbFilter"
 - "coordinateTranslate"
 - "createBackboneMFA"
 - "extractBCITrees"
 - "getAlignmentWindows"
 - "getOrthologList"
 - "makeBadgerMatrix"
 - "mauveAligner"
 - "mauveStatic"
 - "mauveToXMFA"
 - "mfa2xmfa"
 - "progressiveMauve"
 - "progressiveMauveStatic"
 - "projectAndStrip"
 - "randomGeneSample"
 - "repeatoire"
 - "scoreAlignment"
 - "stripGapColumns"
 - "stripSubsetLCBs"
 - "toGrimmFormat"
 - "toMultiFastA"
 - "toRawSequence"
 - "uniqueMerCount"
 - "uniquifyTrees"
 - "xmfa2maf"
versions:
 - "1.2.0--h46c59ee_4"
 - "1.2.0--he153687_5"
description: "shpc-registry automated BioContainers addition for mauvealigner"
config: {"url": "https://biocontainers.pro/tools/mauvealigner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mauvealigner", "latest": {"1.2.0--he153687_5": "sha256:6063b041b711b6350f1510694b13495300dd0bc34a3cbdd4eddfeccabf93dfd9"}, "tags": {"1.2.0--h46c59ee_4": "sha256:ca39c349ec8a579035650243993cc3ddc6eea9d7c5f06abdbb83facbc410fe43", "1.2.0--he153687_5": "sha256:6063b041b711b6350f1510694b13495300dd0bc34a3cbdd4eddfeccabf93dfd9"}, "docker": "quay.io/biocontainers/mauvealigner", "aliases": {"addUnalignedIntervals": "/usr/local/bin/addUnalignedIntervals", "alignmentProjector": "/usr/local/bin/alignmentProjector", "backbone_global_to_local": "/usr/local/bin/backbone_global_to_local", "bbAnalyze": "/usr/local/bin/bbAnalyze", "bbFilter": "/usr/local/bin/bbFilter", "coordinateTranslate": "/usr/local/bin/coordinateTranslate", "createBackboneMFA": "/usr/local/bin/createBackboneMFA", "extractBCITrees": "/usr/local/bin/extractBCITrees", "getAlignmentWindows": "/usr/local/bin/getAlignmentWindows", "getOrthologList": "/usr/local/bin/getOrthologList", "makeBadgerMatrix": "/usr/local/bin/makeBadgerMatrix", "mauveAligner": "/usr/local/bin/mauveAligner", "mauveStatic": "/usr/local/bin/mauveStatic", "mauveToXMFA": "/usr/local/bin/mauveToXMFA", "mfa2xmfa": "/usr/local/bin/mfa2xmfa", "progressiveMauve": "/usr/local/bin/progressiveMauve", "progressiveMauveStatic": "/usr/local/bin/progressiveMauveStatic", "projectAndStrip": "/usr/local/bin/projectAndStrip", "randomGeneSample": "/usr/local/bin/randomGeneSample", "repeatoire": "/usr/local/bin/repeatoire", "scoreAlignment": "/usr/local/bin/scoreAlignment", "stripGapColumns": "/usr/local/bin/stripGapColumns", "stripSubsetLCBs": "/usr/local/bin/stripSubsetLCBs", "toGrimmFormat": "/usr/local/bin/toGrimmFormat", "toMultiFastA": "/usr/local/bin/toMultiFastA", "toRawSequence": "/usr/local/bin/toRawSequence", "uniqueMerCount": "/usr/local/bin/uniqueMerCount", "uniquifyTrees": "/usr/local/bin/uniquifyTrees", "xmfa2maf": "/usr/local/bin/xmfa2maf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mauvealigner.
shpc-registry automated BioContainers addition for mauvealigner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mauvealigner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mauvealigner:1.2.0--he153687_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mauvealigner/1.2.0--he153687_5
$ module help quay.io/biocontainers/mauvealigner/1.2.0--he153687_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mauvealigner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mauvealigner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mauvealigner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mauvealigner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mauvealigner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mauvealigner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addUnalignedIntervals

```bash
$ singularity exec <container> /usr/local/bin/addUnalignedIntervals
$ podman run --it --rm --entrypoint /usr/local/bin/addUnalignedIntervals   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addUnalignedIntervals   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alignmentProjector

```bash
$ singularity exec <container> /usr/local/bin/alignmentProjector
$ podman run --it --rm --entrypoint /usr/local/bin/alignmentProjector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignmentProjector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### backbone_global_to_local

```bash
$ singularity exec <container> /usr/local/bin/backbone_global_to_local
$ podman run --it --rm --entrypoint /usr/local/bin/backbone_global_to_local   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/backbone_global_to_local   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbAnalyze

```bash
$ singularity exec <container> /usr/local/bin/bbAnalyze
$ podman run --it --rm --entrypoint /usr/local/bin/bbAnalyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbAnalyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbFilter

```bash
$ singularity exec <container> /usr/local/bin/bbFilter
$ podman run --it --rm --entrypoint /usr/local/bin/bbFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coordinateTranslate

```bash
$ singularity exec <container> /usr/local/bin/coordinateTranslate
$ podman run --it --rm --entrypoint /usr/local/bin/coordinateTranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coordinateTranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createBackboneMFA

```bash
$ singularity exec <container> /usr/local/bin/createBackboneMFA
$ podman run --it --rm --entrypoint /usr/local/bin/createBackboneMFA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createBackboneMFA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractBCITrees

```bash
$ singularity exec <container> /usr/local/bin/extractBCITrees
$ podman run --it --rm --entrypoint /usr/local/bin/extractBCITrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractBCITrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getAlignmentWindows

```bash
$ singularity exec <container> /usr/local/bin/getAlignmentWindows
$ podman run --it --rm --entrypoint /usr/local/bin/getAlignmentWindows   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getAlignmentWindows   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getOrthologList

```bash
$ singularity exec <container> /usr/local/bin/getOrthologList
$ podman run --it --rm --entrypoint /usr/local/bin/getOrthologList   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getOrthologList   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeBadgerMatrix

```bash
$ singularity exec <container> /usr/local/bin/makeBadgerMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/makeBadgerMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeBadgerMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mauveAligner

```bash
$ singularity exec <container> /usr/local/bin/mauveAligner
$ podman run --it --rm --entrypoint /usr/local/bin/mauveAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mauveAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mauveStatic

```bash
$ singularity exec <container> /usr/local/bin/mauveStatic
$ podman run --it --rm --entrypoint /usr/local/bin/mauveStatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mauveStatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mauveToXMFA

```bash
$ singularity exec <container> /usr/local/bin/mauveToXMFA
$ podman run --it --rm --entrypoint /usr/local/bin/mauveToXMFA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mauveToXMFA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mfa2xmfa

```bash
$ singularity exec <container> /usr/local/bin/mfa2xmfa
$ podman run --it --rm --entrypoint /usr/local/bin/mfa2xmfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfa2xmfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### progressiveMauve

```bash
$ singularity exec <container> /usr/local/bin/progressiveMauve
$ podman run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### progressiveMauveStatic

```bash
$ singularity exec <container> /usr/local/bin/progressiveMauveStatic
$ podman run --it --rm --entrypoint /usr/local/bin/progressiveMauveStatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/progressiveMauveStatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projectAndStrip

```bash
$ singularity exec <container> /usr/local/bin/projectAndStrip
$ podman run --it --rm --entrypoint /usr/local/bin/projectAndStrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/projectAndStrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randomGeneSample

```bash
$ singularity exec <container> /usr/local/bin/randomGeneSample
$ podman run --it --rm --entrypoint /usr/local/bin/randomGeneSample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randomGeneSample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repeatoire

```bash
$ singularity exec <container> /usr/local/bin/repeatoire
$ podman run --it --rm --entrypoint /usr/local/bin/repeatoire   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repeatoire   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scoreAlignment

```bash
$ singularity exec <container> /usr/local/bin/scoreAlignment
$ podman run --it --rm --entrypoint /usr/local/bin/scoreAlignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scoreAlignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stripGapColumns

```bash
$ singularity exec <container> /usr/local/bin/stripGapColumns
$ podman run --it --rm --entrypoint /usr/local/bin/stripGapColumns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stripGapColumns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stripSubsetLCBs

```bash
$ singularity exec <container> /usr/local/bin/stripSubsetLCBs
$ podman run --it --rm --entrypoint /usr/local/bin/stripSubsetLCBs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stripSubsetLCBs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toGrimmFormat

```bash
$ singularity exec <container> /usr/local/bin/toGrimmFormat
$ podman run --it --rm --entrypoint /usr/local/bin/toGrimmFormat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toGrimmFormat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toMultiFastA

```bash
$ singularity exec <container> /usr/local/bin/toMultiFastA
$ podman run --it --rm --entrypoint /usr/local/bin/toMultiFastA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toMultiFastA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toRawSequence

```bash
$ singularity exec <container> /usr/local/bin/toRawSequence
$ podman run --it --rm --entrypoint /usr/local/bin/toRawSequence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toRawSequence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniqueMerCount

```bash
$ singularity exec <container> /usr/local/bin/uniqueMerCount
$ podman run --it --rm --entrypoint /usr/local/bin/uniqueMerCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniqueMerCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniquifyTrees

```bash
$ singularity exec <container> /usr/local/bin/uniquifyTrees
$ podman run --it --rm --entrypoint /usr/local/bin/uniquifyTrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniquifyTrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmfa2maf

```bash
$ singularity exec <container> /usr/local/bin/xmfa2maf
$ podman run --it --rm --entrypoint /usr/local/bin/xmfa2maf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmfa2maf   -v ${PWD} -w ${PWD} <container> -c " $@"
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