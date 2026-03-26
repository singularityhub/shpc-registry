---
layout: container
name:  "quay.io/biocontainers/opencv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/opencv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/opencv/container.yaml"
updated_at: "2026-03-26 04:48:26.336995"
latest: "4.13.0"
container_url: "https://biocontainers.pro/tools/opencv"
aliases:
 - "exr2aces"
 - "exrenvmap"
 - "exrheader"
 - "exrinfo"
 - "exrmakepreview"
 - "exrmaketiled"
 - "exrmanifest"
 - "exrmetrics"
 - "exrmultipart"
 - "exrmultiview"
 - "exrstdattr"
 - "glslang"
 - "glslangValidator"
 - "glslc"
 - "ojph_compress"
 - "ojph_expand"
 - "opencv_annotation"
 - "opencv_interactive-calibration"
 - "opencv_model_diagnostics"
 - "opencv_version"
 - "opencv_visualisation"
 - "opencv_waldboost_detector"
 - "setup_vars_opencv4.sh"
 - "spirv-diff"
 - "ffplay"
 - "sdl2-config"
 - "spirv-as"
 - "spirv-cfg"
 - "spirv-dis"
 - "spirv-lesspipe.sh"
 - "spirv-link"
 - "spirv-lint"
 - "spirv-objdump"
 - "spirv-opt"
 - "spirv-reduce"
 - "spirv-val"
 - "androiddeployqt6"
 - "assistant6"
 - "designer6"
 - "linguist6"
 - "pixeltool6"
 - "qdbus6"
 - "qdbusviewer6"
 - "qdistancefieldgenerator6"
 - "qmake6"
 - "qml6"
 - "qmleasing6"
 - "qmlls6"
 - "qmlpreview6"
versions:
 - "4.13.0"
description: "singularity registry hpc automated addition for opencv"
config: {"url": "https://biocontainers.pro/tools/opencv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for opencv", "latest": {"4.13.0": "sha256:94446d12ce894986195d3cf746bebbd06e9ff3a7b11de21f630cd18c86d7e56b"}, "tags": {"4.13.0": "sha256:94446d12ce894986195d3cf746bebbd06e9ff3a7b11de21f630cd18c86d7e56b"}, "docker": "quay.io/biocontainers/opencv", "aliases": {"exr2aces": "/usr/local/bin/exr2aces", "exrenvmap": "/usr/local/bin/exrenvmap", "exrheader": "/usr/local/bin/exrheader", "exrinfo": "/usr/local/bin/exrinfo", "exrmakepreview": "/usr/local/bin/exrmakepreview", "exrmaketiled": "/usr/local/bin/exrmaketiled", "exrmanifest": "/usr/local/bin/exrmanifest", "exrmetrics": "/usr/local/bin/exrmetrics", "exrmultipart": "/usr/local/bin/exrmultipart", "exrmultiview": "/usr/local/bin/exrmultiview", "exrstdattr": "/usr/local/bin/exrstdattr", "glslang": "/usr/local/bin/glslang", "glslangValidator": "/usr/local/bin/glslangValidator", "glslc": "/usr/local/bin/glslc", "ojph_compress": "/usr/local/bin/ojph_compress", "ojph_expand": "/usr/local/bin/ojph_expand", "opencv_annotation": "/usr/local/bin/opencv_annotation", "opencv_interactive-calibration": "/usr/local/bin/opencv_interactive-calibration", "opencv_model_diagnostics": "/usr/local/bin/opencv_model_diagnostics", "opencv_version": "/usr/local/bin/opencv_version", "opencv_visualisation": "/usr/local/bin/opencv_visualisation", "opencv_waldboost_detector": "/usr/local/bin/opencv_waldboost_detector", "setup_vars_opencv4.sh": "/usr/local/bin/setup_vars_opencv4.sh", "spirv-diff": "/usr/local/bin/spirv-diff", "ffplay": "/usr/local/bin/ffplay", "sdl2-config": "/usr/local/bin/sdl2-config", "spirv-as": "/usr/local/bin/spirv-as", "spirv-cfg": "/usr/local/bin/spirv-cfg", "spirv-dis": "/usr/local/bin/spirv-dis", "spirv-lesspipe.sh": "/usr/local/bin/spirv-lesspipe.sh", "spirv-link": "/usr/local/bin/spirv-link", "spirv-lint": "/usr/local/bin/spirv-lint", "spirv-objdump": "/usr/local/bin/spirv-objdump", "spirv-opt": "/usr/local/bin/spirv-opt", "spirv-reduce": "/usr/local/bin/spirv-reduce", "spirv-val": "/usr/local/bin/spirv-val", "androiddeployqt6": "/usr/local/bin/androiddeployqt6", "assistant6": "/usr/local/bin/assistant6", "designer6": "/usr/local/bin/designer6", "linguist6": "/usr/local/bin/linguist6", "pixeltool6": "/usr/local/bin/pixeltool6", "qdbus6": "/usr/local/bin/qdbus6", "qdbusviewer6": "/usr/local/bin/qdbusviewer6", "qdistancefieldgenerator6": "/usr/local/bin/qdistancefieldgenerator6", "qmake6": "/usr/local/bin/qmake6", "qml6": "/usr/local/bin/qml6", "qmleasing6": "/usr/local/bin/qmleasing6", "qmlls6": "/usr/local/bin/qmlls6", "qmlpreview6": "/usr/local/bin/qmlpreview6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/opencv.
singularity registry hpc automated addition for opencv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/opencv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/opencv:4.13.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/opencv/4.13.0
$ module help quay.io/biocontainers/opencv/4.13.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### opencv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### opencv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### opencv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### opencv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### opencv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### opencv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### exr2aces

```bash
$ singularity exec <container> /usr/local/bin/exr2aces
$ podman run --it --rm --entrypoint /usr/local/bin/exr2aces   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exr2aces   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrenvmap

```bash
$ singularity exec <container> /usr/local/bin/exrenvmap
$ podman run --it --rm --entrypoint /usr/local/bin/exrenvmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrenvmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrheader

```bash
$ singularity exec <container> /usr/local/bin/exrheader
$ podman run --it --rm --entrypoint /usr/local/bin/exrheader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrheader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrinfo

```bash
$ singularity exec <container> /usr/local/bin/exrinfo
$ podman run --it --rm --entrypoint /usr/local/bin/exrinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmakepreview

```bash
$ singularity exec <container> /usr/local/bin/exrmakepreview
$ podman run --it --rm --entrypoint /usr/local/bin/exrmakepreview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmakepreview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmaketiled

```bash
$ singularity exec <container> /usr/local/bin/exrmaketiled
$ podman run --it --rm --entrypoint /usr/local/bin/exrmaketiled   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmaketiled   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmanifest

```bash
$ singularity exec <container> /usr/local/bin/exrmanifest
$ podman run --it --rm --entrypoint /usr/local/bin/exrmanifest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmanifest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmetrics

```bash
$ singularity exec <container> /usr/local/bin/exrmetrics
$ podman run --it --rm --entrypoint /usr/local/bin/exrmetrics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmetrics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmultipart

```bash
$ singularity exec <container> /usr/local/bin/exrmultipart
$ podman run --it --rm --entrypoint /usr/local/bin/exrmultipart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmultipart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmultiview

```bash
$ singularity exec <container> /usr/local/bin/exrmultiview
$ podman run --it --rm --entrypoint /usr/local/bin/exrmultiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmultiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrstdattr

```bash
$ singularity exec <container> /usr/local/bin/exrstdattr
$ podman run --it --rm --entrypoint /usr/local/bin/exrstdattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrstdattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glslang

```bash
$ singularity exec <container> /usr/local/bin/glslang
$ podman run --it --rm --entrypoint /usr/local/bin/glslang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glslang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glslangValidator

```bash
$ singularity exec <container> /usr/local/bin/glslangValidator
$ podman run --it --rm --entrypoint /usr/local/bin/glslangValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glslangValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glslc

```bash
$ singularity exec <container> /usr/local/bin/glslc
$ podman run --it --rm --entrypoint /usr/local/bin/glslc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glslc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ojph_compress

```bash
$ singularity exec <container> /usr/local/bin/ojph_compress
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ojph_expand

```bash
$ singularity exec <container> /usr/local/bin/ojph_expand
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_annotation

```bash
$ singularity exec <container> /usr/local/bin/opencv_annotation
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_interactive-calibration

```bash
$ singularity exec <container> /usr/local/bin/opencv_interactive-calibration
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_interactive-calibration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_interactive-calibration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_model_diagnostics

```bash
$ singularity exec <container> /usr/local/bin/opencv_model_diagnostics
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_model_diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_model_diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_version

```bash
$ singularity exec <container> /usr/local/bin/opencv_version
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_visualisation

```bash
$ singularity exec <container> /usr/local/bin/opencv_visualisation
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_visualisation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_visualisation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_waldboost_detector

```bash
$ singularity exec <container> /usr/local/bin/opencv_waldboost_detector
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_waldboost_detector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_waldboost_detector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup_vars_opencv4.sh

```bash
$ singularity exec <container> /usr/local/bin/setup_vars_opencv4.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-diff

```bash
$ singularity exec <container> /usr/local/bin/spirv-diff
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffplay

```bash
$ singularity exec <container> /usr/local/bin/ffplay
$ podman run --it --rm --entrypoint /usr/local/bin/ffplay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffplay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdl2-config

```bash
$ singularity exec <container> /usr/local/bin/sdl2-config
$ podman run --it --rm --entrypoint /usr/local/bin/sdl2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdl2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-as

```bash
$ singularity exec <container> /usr/local/bin/spirv-as
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-cfg

```bash
$ singularity exec <container> /usr/local/bin/spirv-cfg
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-dis

```bash
$ singularity exec <container> /usr/local/bin/spirv-dis
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-lesspipe.sh

```bash
$ singularity exec <container> /usr/local/bin/spirv-lesspipe.sh
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-lesspipe.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-lesspipe.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-link

```bash
$ singularity exec <container> /usr/local/bin/spirv-link
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-lint

```bash
$ singularity exec <container> /usr/local/bin/spirv-lint
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-objdump

```bash
$ singularity exec <container> /usr/local/bin/spirv-objdump
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-opt

```bash
$ singularity exec <container> /usr/local/bin/spirv-opt
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-reduce

```bash
$ singularity exec <container> /usr/local/bin/spirv-reduce
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-val

```bash
$ singularity exec <container> /usr/local/bin/spirv-val
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-val   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-val   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### androiddeployqt6

```bash
$ singularity exec <container> /usr/local/bin/androiddeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant6

```bash
$ singularity exec <container> /usr/local/bin/assistant6
$ podman run --it --rm --entrypoint /usr/local/bin/assistant6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### designer6

```bash
$ singularity exec <container> /usr/local/bin/designer6
$ podman run --it --rm --entrypoint /usr/local/bin/designer6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/designer6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linguist6

```bash
$ singularity exec <container> /usr/local/bin/linguist6
$ podman run --it --rm --entrypoint /usr/local/bin/linguist6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linguist6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pixeltool6

```bash
$ singularity exec <container> /usr/local/bin/pixeltool6
$ podman run --it --rm --entrypoint /usr/local/bin/pixeltool6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pixeltool6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbus6

```bash
$ singularity exec <container> /usr/local/bin/qdbus6
$ podman run --it --rm --entrypoint /usr/local/bin/qdbus6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbus6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbusviewer6

```bash
$ singularity exec <container> /usr/local/bin/qdbusviewer6
$ podman run --it --rm --entrypoint /usr/local/bin/qdbusviewer6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbusviewer6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator6

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator6
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmake6

```bash
$ singularity exec <container> /usr/local/bin/qmake6
$ podman run --it --rm --entrypoint /usr/local/bin/qmake6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmake6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qml6

```bash
$ singularity exec <container> /usr/local/bin/qml6
$ podman run --it --rm --entrypoint /usr/local/bin/qml6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qml6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmleasing6

```bash
$ singularity exec <container> /usr/local/bin/qmleasing6
$ podman run --it --rm --entrypoint /usr/local/bin/qmleasing6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmleasing6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlls6

```bash
$ singularity exec <container> /usr/local/bin/qmlls6
$ podman run --it --rm --entrypoint /usr/local/bin/qmlls6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlls6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlpreview6

```bash
$ singularity exec <container> /usr/local/bin/qmlpreview6
$ podman run --it --rm --entrypoint /usr/local/bin/qmlpreview6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlpreview6   -v ${PWD} -w ${PWD} <container> -c " $@"
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