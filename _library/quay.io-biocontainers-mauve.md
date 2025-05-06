---
layout: container
name:  "quay.io/biocontainers/mauve"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mauve/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mauve/container.yaml"
updated_at: "2025-05-06 03:31:29.206445"
latest: "2.4.0.r4736--h43d4aaa_3"
container_url: "https://biocontainers.pro/tools/mauve"
aliases:
 - "Mauve"
 - "MauveCM"
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
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
 - "idlj"
 - "orbd"
versions:
 - "2.4.0.snapshot_2015_02_13--hdfd78af_4"
 - "2.4.0.r4736--h9bed127_2"
 - "2.4.0.r4736--h43d4aaa_3"
description: "shpc-registry automated BioContainers addition for mauve"
config: {"url": "https://biocontainers.pro/tools/mauve", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mauve", "latest": {"2.4.0.r4736--h43d4aaa_3": "sha256:2fdc8bb1abf112fb5003325d17c8d9990a1c8cc8239fd6fad5020ba210b1b5fa"}, "tags": {"2.4.0.snapshot_2015_02_13--hdfd78af_4": "sha256:6ade83c13e7430252285f568f3bcc6dfc378371b76630cb35da8d34c7fa10c2f", "2.4.0.r4736--h9bed127_2": "sha256:10ec3f8e1e7707c1aac8b3001e445b6773cf0c63203443f4e843a921666f70b6", "2.4.0.r4736--h43d4aaa_3": "sha256:2fdc8bb1abf112fb5003325d17c8d9990a1c8cc8239fd6fad5020ba210b1b5fa"}, "docker": "quay.io/biocontainers/mauve", "aliases": {"Mauve": "/usr/local/bin/Mauve", "MauveCM": "/usr/local/bin/MauveCM", "addUnalignedIntervals": "/usr/local/bin/addUnalignedIntervals", "alignmentProjector": "/usr/local/bin/alignmentProjector", "backbone_global_to_local": "/usr/local/bin/backbone_global_to_local", "bbAnalyze": "/usr/local/bin/bbAnalyze", "bbFilter": "/usr/local/bin/bbFilter", "coordinateTranslate": "/usr/local/bin/coordinateTranslate", "createBackboneMFA": "/usr/local/bin/createBackboneMFA", "extractBCITrees": "/usr/local/bin/extractBCITrees", "getAlignmentWindows": "/usr/local/bin/getAlignmentWindows", "getOrthologList": "/usr/local/bin/getOrthologList", "makeBadgerMatrix": "/usr/local/bin/makeBadgerMatrix", "mauveAligner": "/usr/local/bin/mauveAligner", "mauveStatic": "/usr/local/bin/mauveStatic", "mauveToXMFA": "/usr/local/bin/mauveToXMFA", "mfa2xmfa": "/usr/local/bin/mfa2xmfa", "progressiveMauve": "/usr/local/bin/progressiveMauve", "progressiveMauveStatic": "/usr/local/bin/progressiveMauveStatic", "projectAndStrip": "/usr/local/bin/projectAndStrip", "randomGeneSample": "/usr/local/bin/randomGeneSample", "repeatoire": "/usr/local/bin/repeatoire", "scoreAlignment": "/usr/local/bin/scoreAlignment", "stripGapColumns": "/usr/local/bin/stripGapColumns", "stripSubsetLCBs": "/usr/local/bin/stripSubsetLCBs", "toGrimmFormat": "/usr/local/bin/toGrimmFormat", "toMultiFastA": "/usr/local/bin/toMultiFastA", "toRawSequence": "/usr/local/bin/toRawSequence", "uniqueMerCount": "/usr/local/bin/uniqueMerCount", "uniquifyTrees": "/usr/local/bin/uniquifyTrees", "xmfa2maf": "/usr/local/bin/xmfa2maf", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mauve.
shpc-registry automated BioContainers addition for mauve
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mauve
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mauve:2.4.0.r4736--h43d4aaa_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mauve/2.4.0.r4736--h43d4aaa_3
$ module help quay.io/biocontainers/mauve/2.4.0.r4736--h43d4aaa_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mauve-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mauve-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mauve-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mauve-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mauve-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mauve-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Mauve

```bash
$ singularity exec <container> /usr/local/bin/Mauve
$ podman run --it --rm --entrypoint /usr/local/bin/Mauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Mauve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MauveCM

```bash
$ singularity exec <container> /usr/local/bin/MauveCM
$ podman run --it --rm --entrypoint /usr/local/bin/MauveCM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MauveCM   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### native2ascii

```bash
$ singularity exec <container> /usr/local/bin/native2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### policytool

```bash
$ singularity exec <container> /usr/local/bin/policytool
$ podman run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orbd

```bash
$ singularity exec <container> /usr/local/bin/orbd
$ podman run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
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