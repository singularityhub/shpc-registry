---
layout: container
name:  "quay.io/biocontainers/r-rphylip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rphylip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-rphylip/container.yaml"
updated_at: "2024-12-03 03:53:31.928449"
latest: "0.1_23--r3.4.1_1"
container_url: "https://biocontainers.pro/tools/r-rphylip"
aliases:
 - "DrawGram.jar"
 - "DrawTree.jar"
 - "clique"
 - "consense"
 - "contml"
 - "contrast"
 - "dnacomp"
 - "dnadist"
 - "dnainvar"
 - "dnaml"
 - "dnamlk"
 - "dnamove"
 - "dnapars"
 - "dnapenny"
 - "dollop"
 - "dolmove"
 - "dolpenny"
 - "drawgram"
 - "drawgram_gui"
 - "drawtree"
 - "drawtree_gui"
 - "fitch"
 - "gendist"
 - "kitsch"
 - "mix"
 - "move"
 - "neighbor"
 - "pars"
 - "penny"
 - "phylip"
 - "proml"
 - "promlk"
 - "protdist"
 - "protpars"
 - "restdist"
 - "restml"
 - "retree"
 - "seqboot"
 - "treedist"
 - "factor"
 - "easy_install-3.6"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
versions:
 - "0.1_23--r3.4.1_1"
 - "0.1_23--r3.3.2_1"
description: "shpc-registry automated BioContainers addition for r-rphylip"
config: {"url": "https://biocontainers.pro/tools/r-rphylip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rphylip", "latest": {"0.1_23--r3.4.1_1": "sha256:6a1c90527ea83e6ad140f4c9577b1a4f1bfde27fec597d4aa1248d0a23449f7e"}, "tags": {"0.1_23--r3.4.1_1": "sha256:6a1c90527ea83e6ad140f4c9577b1a4f1bfde27fec597d4aa1248d0a23449f7e", "0.1_23--r3.3.2_1": "sha256:88ecbd5e1aec1e74b8b2ab72d7ad573669fcef695a52c851f3114dcf84faad48"}, "docker": "quay.io/biocontainers/r-rphylip", "aliases": {"DrawGram.jar": "/usr/local/bin/DrawGram.jar", "DrawTree.jar": "/usr/local/bin/DrawTree.jar", "clique": "/usr/local/bin/clique", "consense": "/usr/local/bin/consense", "contml": "/usr/local/bin/contml", "contrast": "/usr/local/bin/contrast", "dnacomp": "/usr/local/bin/dnacomp", "dnadist": "/usr/local/bin/dnadist", "dnainvar": "/usr/local/bin/dnainvar", "dnaml": "/usr/local/bin/dnaml", "dnamlk": "/usr/local/bin/dnamlk", "dnamove": "/usr/local/bin/dnamove", "dnapars": "/usr/local/bin/dnapars", "dnapenny": "/usr/local/bin/dnapenny", "dollop": "/usr/local/bin/dollop", "dolmove": "/usr/local/bin/dolmove", "dolpenny": "/usr/local/bin/dolpenny", "drawgram": "/usr/local/bin/drawgram", "drawgram_gui": "/usr/local/bin/drawgram_gui", "drawtree": "/usr/local/bin/drawtree", "drawtree_gui": "/usr/local/bin/drawtree_gui", "fitch": "/usr/local/bin/fitch", "gendist": "/usr/local/bin/gendist", "kitsch": "/usr/local/bin/kitsch", "mix": "/usr/local/bin/mix", "move": "/usr/local/bin/move", "neighbor": "/usr/local/bin/neighbor", "pars": "/usr/local/bin/pars", "penny": "/usr/local/bin/penny", "phylip": "/usr/local/bin/phylip", "proml": "/usr/local/bin/proml", "promlk": "/usr/local/bin/promlk", "protdist": "/usr/local/bin/protdist", "protpars": "/usr/local/bin/protpars", "restdist": "/usr/local/bin/restdist", "restml": "/usr/local/bin/restml", "retree": "/usr/local/bin/retree", "seqboot": "/usr/local/bin/seqboot", "treedist": "/usr/local/bin/treedist", "factor": "/usr/local/bin/factor", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rphylip.
shpc-registry automated BioContainers addition for r-rphylip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rphylip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rphylip:0.1_23--r3.4.1_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rphylip/0.1_23--r3.4.1_1
$ module help quay.io/biocontainers/r-rphylip/0.1_23--r3.4.1_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rphylip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rphylip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rphylip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rphylip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rphylip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rphylip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DrawGram.jar

```bash
$ singularity exec <container> /usr/local/bin/DrawGram.jar
$ podman run --it --rm --entrypoint /usr/local/bin/DrawGram.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DrawGram.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DrawTree.jar

```bash
$ singularity exec <container> /usr/local/bin/DrawTree.jar
$ podman run --it --rm --entrypoint /usr/local/bin/DrawTree.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DrawTree.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clique

```bash
$ singularity exec <container> /usr/local/bin/clique
$ podman run --it --rm --entrypoint /usr/local/bin/clique   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clique   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consense

```bash
$ singularity exec <container> /usr/local/bin/consense
$ podman run --it --rm --entrypoint /usr/local/bin/consense   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consense   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contml

```bash
$ singularity exec <container> /usr/local/bin/contml
$ podman run --it --rm --entrypoint /usr/local/bin/contml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contrast

```bash
$ singularity exec <container> /usr/local/bin/contrast
$ podman run --it --rm --entrypoint /usr/local/bin/contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnacomp

```bash
$ singularity exec <container> /usr/local/bin/dnacomp
$ podman run --it --rm --entrypoint /usr/local/bin/dnacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadist

```bash
$ singularity exec <container> /usr/local/bin/dnadist
$ podman run --it --rm --entrypoint /usr/local/bin/dnadist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnainvar

```bash
$ singularity exec <container> /usr/local/bin/dnainvar
$ podman run --it --rm --entrypoint /usr/local/bin/dnainvar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnainvar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnaml

```bash
$ singularity exec <container> /usr/local/bin/dnaml
$ podman run --it --rm --entrypoint /usr/local/bin/dnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnamlk

```bash
$ singularity exec <container> /usr/local/bin/dnamlk
$ podman run --it --rm --entrypoint /usr/local/bin/dnamlk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnamlk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnamove

```bash
$ singularity exec <container> /usr/local/bin/dnamove
$ podman run --it --rm --entrypoint /usr/local/bin/dnamove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnamove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnapars

```bash
$ singularity exec <container> /usr/local/bin/dnapars
$ podman run --it --rm --entrypoint /usr/local/bin/dnapars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnapars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnapenny

```bash
$ singularity exec <container> /usr/local/bin/dnapenny
$ podman run --it --rm --entrypoint /usr/local/bin/dnapenny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnapenny   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dollop

```bash
$ singularity exec <container> /usr/local/bin/dollop
$ podman run --it --rm --entrypoint /usr/local/bin/dollop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dollop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dolmove

```bash
$ singularity exec <container> /usr/local/bin/dolmove
$ podman run --it --rm --entrypoint /usr/local/bin/dolmove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dolmove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dolpenny

```bash
$ singularity exec <container> /usr/local/bin/dolpenny
$ podman run --it --rm --entrypoint /usr/local/bin/dolpenny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dolpenny   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawgram

```bash
$ singularity exec <container> /usr/local/bin/drawgram
$ podman run --it --rm --entrypoint /usr/local/bin/drawgram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawgram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawgram_gui

```bash
$ singularity exec <container> /usr/local/bin/drawgram_gui
$ podman run --it --rm --entrypoint /usr/local/bin/drawgram_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawgram_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawtree

```bash
$ singularity exec <container> /usr/local/bin/drawtree
$ podman run --it --rm --entrypoint /usr/local/bin/drawtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawtree_gui

```bash
$ singularity exec <container> /usr/local/bin/drawtree_gui
$ podman run --it --rm --entrypoint /usr/local/bin/drawtree_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawtree_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitch

```bash
$ singularity exec <container> /usr/local/bin/fitch
$ podman run --it --rm --entrypoint /usr/local/bin/fitch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gendist

```bash
$ singularity exec <container> /usr/local/bin/gendist
$ podman run --it --rm --entrypoint /usr/local/bin/gendist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gendist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kitsch

```bash
$ singularity exec <container> /usr/local/bin/kitsch
$ podman run --it --rm --entrypoint /usr/local/bin/kitsch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kitsch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mix

```bash
$ singularity exec <container> /usr/local/bin/mix
$ podman run --it --rm --entrypoint /usr/local/bin/mix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### move

```bash
$ singularity exec <container> /usr/local/bin/move
$ podman run --it --rm --entrypoint /usr/local/bin/move   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/move   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### neighbor

```bash
$ singularity exec <container> /usr/local/bin/neighbor
$ podman run --it --rm --entrypoint /usr/local/bin/neighbor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/neighbor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pars

```bash
$ singularity exec <container> /usr/local/bin/pars
$ podman run --it --rm --entrypoint /usr/local/bin/pars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### penny

```bash
$ singularity exec <container> /usr/local/bin/penny
$ podman run --it --rm --entrypoint /usr/local/bin/penny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/penny   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylip

```bash
$ singularity exec <container> /usr/local/bin/phylip
$ podman run --it --rm --entrypoint /usr/local/bin/phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proml

```bash
$ singularity exec <container> /usr/local/bin/proml
$ podman run --it --rm --entrypoint /usr/local/bin/proml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promlk

```bash
$ singularity exec <container> /usr/local/bin/promlk
$ podman run --it --rm --entrypoint /usr/local/bin/promlk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promlk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protdist

```bash
$ singularity exec <container> /usr/local/bin/protdist
$ podman run --it --rm --entrypoint /usr/local/bin/protdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protpars

```bash
$ singularity exec <container> /usr/local/bin/protpars
$ podman run --it --rm --entrypoint /usr/local/bin/protpars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protpars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### restdist

```bash
$ singularity exec <container> /usr/local/bin/restdist
$ podman run --it --rm --entrypoint /usr/local/bin/restdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/restdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### restml

```bash
$ singularity exec <container> /usr/local/bin/restml
$ podman run --it --rm --entrypoint /usr/local/bin/restml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/restml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retree

```bash
$ singularity exec <container> /usr/local/bin/retree
$ podman run --it --rm --entrypoint /usr/local/bin/retree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqboot

```bash
$ singularity exec <container> /usr/local/bin/seqboot
$ podman run --it --rm --entrypoint /usr/local/bin/seqboot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqboot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treedist

```bash
$ singularity exec <container> /usr/local/bin/treedist
$ podman run --it --rm --entrypoint /usr/local/bin/treedist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treedist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### factor

```bash
$ singularity exec <container> /usr/local/bin/factor
$ podman run --it --rm --entrypoint /usr/local/bin/factor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/factor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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