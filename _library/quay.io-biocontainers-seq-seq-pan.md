---
layout: container
name:  "quay.io/biocontainers/seq-seq-pan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seq-seq-pan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seq-seq-pan/container.yaml"
updated_at: "2023-05-24 02:56:55.804453"
latest: "1.1.0--py_1"
container_url: "https://biocontainers.pro/tools/seq-seq-pan"
aliases:
 - "addUnalignedIntervals"
 - "alignmentProjector"
 - "backbone_global_to_local"
 - "bbAnalyze"
 - "bbFilter"
 - "coordinateTranslate"
 - "createBackboneMFA"
 - "extractBCITrees"
 - "faToNib"
 - "getAlignmentWindows"
 - "getOrthologList"
 - "gfClient"
 - "gfServer"
 - "makeBadgerMatrix"
 - "mauveAligner"
 - "mauveStatic"
 - "mauveToXMFA"
 - "mfa2xmfa"
 - "nibFrag"
 - "progressiveMauve"
 - "progressiveMauveStatic"
 - "projectAndStrip"
 - "pslPretty"
 - "pslReps"
 - "pslSort"
 - "randomGeneSample"
 - "repeatoire"
 - "scoreAlignment"
 - "seq-seq-pan"
 - "seq-seq-pan-consensus"
 - "seq-seq-pan-genomedescription"
 - "seq-seq-pan-wga"
 - "stripGapColumns"
 - "stripSubsetLCBs"
 - "toGrimmFormat"
 - "toMultiFastA"
 - "toRawSequence"
 - "uniqueMerCount"
 - "uniquifyTrees"
 - "xmfa2maf"
 - "twoBitToFa"
 - "blat"
 - "twoBitInfo"
 - "faToTwoBit"
 - "snakemake"
 - "snakemake-bash-completion"
 - "rst2html4.py"
 - "appletviewer"
 - "idlj"
 - "orbd"
versions:
 - "1.1.0--py_1"
description: "shpc-registry automated BioContainers addition for seq-seq-pan"
config: {"url": "https://biocontainers.pro/tools/seq-seq-pan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seq-seq-pan", "latest": {"1.1.0--py_1": "sha256:c98387c8641568767ec544db4174415b9da26ebfbaddeaf2d692aee2ee3b19a8"}, "tags": {"1.1.0--py_1": "sha256:c98387c8641568767ec544db4174415b9da26ebfbaddeaf2d692aee2ee3b19a8"}, "docker": "quay.io/biocontainers/seq-seq-pan", "aliases": {"addUnalignedIntervals": "/usr/local/bin/addUnalignedIntervals", "alignmentProjector": "/usr/local/bin/alignmentProjector", "backbone_global_to_local": "/usr/local/bin/backbone_global_to_local", "bbAnalyze": "/usr/local/bin/bbAnalyze", "bbFilter": "/usr/local/bin/bbFilter", "coordinateTranslate": "/usr/local/bin/coordinateTranslate", "createBackboneMFA": "/usr/local/bin/createBackboneMFA", "extractBCITrees": "/usr/local/bin/extractBCITrees", "faToNib": "/usr/local/bin/faToNib", "getAlignmentWindows": "/usr/local/bin/getAlignmentWindows", "getOrthologList": "/usr/local/bin/getOrthologList", "gfClient": "/usr/local/bin/gfClient", "gfServer": "/usr/local/bin/gfServer", "makeBadgerMatrix": "/usr/local/bin/makeBadgerMatrix", "mauveAligner": "/usr/local/bin/mauveAligner", "mauveStatic": "/usr/local/bin/mauveStatic", "mauveToXMFA": "/usr/local/bin/mauveToXMFA", "mfa2xmfa": "/usr/local/bin/mfa2xmfa", "nibFrag": "/usr/local/bin/nibFrag", "progressiveMauve": "/usr/local/bin/progressiveMauve", "progressiveMauveStatic": "/usr/local/bin/progressiveMauveStatic", "projectAndStrip": "/usr/local/bin/projectAndStrip", "pslPretty": "/usr/local/bin/pslPretty", "pslReps": "/usr/local/bin/pslReps", "pslSort": "/usr/local/bin/pslSort", "randomGeneSample": "/usr/local/bin/randomGeneSample", "repeatoire": "/usr/local/bin/repeatoire", "scoreAlignment": "/usr/local/bin/scoreAlignment", "seq-seq-pan": "/usr/local/bin/seq-seq-pan", "seq-seq-pan-consensus": "/usr/local/bin/seq-seq-pan-consensus", "seq-seq-pan-genomedescription": "/usr/local/bin/seq-seq-pan-genomedescription", "seq-seq-pan-wga": "/usr/local/bin/seq-seq-pan-wga", "stripGapColumns": "/usr/local/bin/stripGapColumns", "stripSubsetLCBs": "/usr/local/bin/stripSubsetLCBs", "toGrimmFormat": "/usr/local/bin/toGrimmFormat", "toMultiFastA": "/usr/local/bin/toMultiFastA", "toRawSequence": "/usr/local/bin/toRawSequence", "uniqueMerCount": "/usr/local/bin/uniqueMerCount", "uniquifyTrees": "/usr/local/bin/uniquifyTrees", "xmfa2maf": "/usr/local/bin/xmfa2maf", "twoBitToFa": "/usr/local/bin/twoBitToFa", "blat": "/usr/local/bin/blat", "twoBitInfo": "/usr/local/bin/twoBitInfo", "faToTwoBit": "/usr/local/bin/faToTwoBit", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "rst2html4.py": "/usr/local/bin/rst2html4.py", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seq-seq-pan.
shpc-registry automated BioContainers addition for seq-seq-pan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seq-seq-pan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seq-seq-pan:1.1.0--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seq-seq-pan/1.1.0--py_1
$ module help quay.io/biocontainers/seq-seq-pan/1.1.0--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seq-seq-pan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seq-seq-pan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seq-seq-pan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seq-seq-pan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seq-seq-pan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seq-seq-pan-inspect-deffile:

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


#### faToNib

```bash
$ singularity exec <container> /usr/local/bin/faToNib
$ podman run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gfClient

```bash
$ singularity exec <container> /usr/local/bin/gfClient
$ podman run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### nibFrag

```bash
$ singularity exec <container> /usr/local/bin/nibFrag
$ podman run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pslPretty

```bash
$ singularity exec <container> /usr/local/bin/pslPretty
$ podman run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslReps

```bash
$ singularity exec <container> /usr/local/bin/pslReps
$ podman run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslSort

```bash
$ singularity exec <container> /usr/local/bin/pslSort
$ podman run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### seq-seq-pan

```bash
$ singularity exec <container> /usr/local/bin/seq-seq-pan
$ podman run --it --rm --entrypoint /usr/local/bin/seq-seq-pan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-seq-pan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq-seq-pan-consensus

```bash
$ singularity exec <container> /usr/local/bin/seq-seq-pan-consensus
$ podman run --it --rm --entrypoint /usr/local/bin/seq-seq-pan-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-seq-pan-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq-seq-pan-genomedescription

```bash
$ singularity exec <container> /usr/local/bin/seq-seq-pan-genomedescription
$ podman run --it --rm --entrypoint /usr/local/bin/seq-seq-pan-genomedescription   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-seq-pan-genomedescription   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq-seq-pan-wga

```bash
$ singularity exec <container> /usr/local/bin/seq-seq-pan-wga
$ podman run --it --rm --entrypoint /usr/local/bin/seq-seq-pan-wga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-seq-pan-wga   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blat

```bash
$ singularity exec <container> /usr/local/bin/blat
$ podman run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitInfo

```bash
$ singularity exec <container> /usr/local/bin/twoBitInfo
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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