---
layout: container
name:  "quay.io/biocontainers/spatialproteomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spatialproteomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spatialproteomics/container.yaml"
updated_at: "2026-11-06 18:31:10.999557"
latest: "0.9.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/spatialproteomics"
aliases:
 - "harmonydeployqt6"
 - "kmap2qmap6"
 - "lcheck6"
 - "lconvert6"
 - "lrelease-pro6"
 - "lrelease6"
 - "ltext2id6"
 - "lupdate-pro6"
 - "lupdate6"
 - "setup_vars_opencv5.sh"
 - "wasmdeployqt6"
 - "glslang"
 - "glslangValidator"
 - "glslc"
 - "exrmanifest"
 - "exrmetrics"
 - "exr2aces"
 - "exrenvmap"
 - "exrheader"
 - "exrinfo"
 - "exrmakepreview"
 - "exrmaketiled"
 - "exrmultipart"
 - "exrmultiview"
 - "exrstdattr"
 - "spirv-diff"
 - "ffplay"
 - "sdl2-config"
 - "ojph_compress"
 - "ojph_expand"
 - "opencv_model_diagnostics"
 - "opencv_annotation"
 - "opencv_version"
 - "opencv_visualisation"
 - "opencv_waldboost_detector"
 - "androiddeployqt6"
versions:
 - "0.9.0--pyh106432d_0"
description: "singularity registry hpc automated addition for spatialproteomics"
config: {"url": "https://biocontainers.pro/tools/spatialproteomics", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for spatialproteomics", "latest": {"0.9.0--pyh106432d_0": "sha256:4471bcd228d6da81267e9749f95de5a17174ee73bb1622e1805f6b392e1cacfb"}, "tags": {"0.9.0--pyh106432d_0": "sha256:4471bcd228d6da81267e9749f95de5a17174ee73bb1622e1805f6b392e1cacfb"}, "docker": "quay.io/biocontainers/spatialproteomics", "aliases": {"harmonydeployqt6": "/usr/local/bin/harmonydeployqt6", "kmap2qmap6": "/usr/local/bin/kmap2qmap6", "lcheck6": "/usr/local/bin/lcheck6", "lconvert6": "/usr/local/bin/lconvert6", "lrelease-pro6": "/usr/local/bin/lrelease-pro6", "lrelease6": "/usr/local/bin/lrelease6", "ltext2id6": "/usr/local/bin/ltext2id6", "lupdate-pro6": "/usr/local/bin/lupdate-pro6", "lupdate6": "/usr/local/bin/lupdate6", "setup_vars_opencv5.sh": "/usr/local/bin/setup_vars_opencv5.sh", "wasmdeployqt6": "/usr/local/bin/wasmdeployqt6", "glslang": "/usr/local/bin/glslang", "glslangValidator": "/usr/local/bin/glslangValidator", "glslc": "/usr/local/bin/glslc", "exrmanifest": "/usr/local/bin/exrmanifest", "exrmetrics": "/usr/local/bin/exrmetrics", "exr2aces": "/usr/local/bin/exr2aces", "exrenvmap": "/usr/local/bin/exrenvmap", "exrheader": "/usr/local/bin/exrheader", "exrinfo": "/usr/local/bin/exrinfo", "exrmakepreview": "/usr/local/bin/exrmakepreview", "exrmaketiled": "/usr/local/bin/exrmaketiled", "exrmultipart": "/usr/local/bin/exrmultipart", "exrmultiview": "/usr/local/bin/exrmultiview", "exrstdattr": "/usr/local/bin/exrstdattr", "spirv-diff": "/usr/local/bin/spirv-diff", "ffplay": "/usr/local/bin/ffplay", "sdl2-config": "/usr/local/bin/sdl2-config", "ojph_compress": "/usr/local/bin/ojph_compress", "ojph_expand": "/usr/local/bin/ojph_expand", "opencv_model_diagnostics": "/usr/local/bin/opencv_model_diagnostics", "opencv_annotation": "/usr/local/bin/opencv_annotation", "opencv_version": "/usr/local/bin/opencv_version", "opencv_visualisation": "/usr/local/bin/opencv_visualisation", "opencv_waldboost_detector": "/usr/local/bin/opencv_waldboost_detector", "androiddeployqt6": "/usr/local/bin/androiddeployqt6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spatialproteomics.
singularity registry hpc automated addition for spatialproteomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spatialproteomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spatialproteomics:0.9.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spatialproteomics/0.9.0--pyh106432d_0
$ module help quay.io/biocontainers/spatialproteomics/0.9.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spatialproteomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spatialproteomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spatialproteomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spatialproteomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spatialproteomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spatialproteomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### harmonydeployqt6

```bash
$ singularity exec <container> /usr/local/bin/harmonydeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/harmonydeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/harmonydeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmap2qmap6

```bash
$ singularity exec <container> /usr/local/bin/kmap2qmap6
$ podman run --it --rm --entrypoint /usr/local/bin/kmap2qmap6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmap2qmap6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lcheck6

```bash
$ singularity exec <container> /usr/local/bin/lcheck6
$ podman run --it --rm --entrypoint /usr/local/bin/lcheck6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lcheck6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lconvert6

```bash
$ singularity exec <container> /usr/local/bin/lconvert6
$ podman run --it --rm --entrypoint /usr/local/bin/lconvert6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lconvert6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease-pro6

```bash
$ singularity exec <container> /usr/local/bin/lrelease-pro6
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease6

```bash
$ singularity exec <container> /usr/local/bin/lrelease6
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ltext2id6

```bash
$ singularity exec <container> /usr/local/bin/ltext2id6
$ podman run --it --rm --entrypoint /usr/local/bin/ltext2id6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ltext2id6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate-pro6

```bash
$ singularity exec <container> /usr/local/bin/lupdate-pro6
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate6

```bash
$ singularity exec <container> /usr/local/bin/lupdate6
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup_vars_opencv5.sh

```bash
$ singularity exec <container> /usr/local/bin/setup_vars_opencv5.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv5.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv5.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wasmdeployqt6

```bash
$ singularity exec <container> /usr/local/bin/wasmdeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/wasmdeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wasmdeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### opencv_model_diagnostics

```bash
$ singularity exec <container> /usr/local/bin/opencv_model_diagnostics
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_model_diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_model_diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_annotation

```bash
$ singularity exec <container> /usr/local/bin/opencv_annotation
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### androiddeployqt6

```bash
$ singularity exec <container> /usr/local/bin/androiddeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
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