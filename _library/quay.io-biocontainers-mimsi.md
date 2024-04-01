---
layout: container
name:  "quay.io/biocontainers/mimsi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mimsi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mimsi/container.yaml"
updated_at: "2024-04-01 04:06:45.515788"
latest: "0.4.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mimsi"
aliases:
 - "analyze"
 - "create_data"
 - "evaluate_sample"
 - "mi_msi_train_test"
 - "visualize_instance"
 - "nosetests-3.9"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "nosetests"
 - "f2py3.8"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.8"
versions:
 - "0.4.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mimsi"
config: {"url": "https://biocontainers.pro/tools/mimsi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mimsi", "latest": {"0.4.4--pyhdfd78af_0": "sha256:df14fd7ceb838661edc7b2d78073b55a500899c75e1d26aac659cdefec63e007"}, "tags": {"0.4.4--pyhdfd78af_0": "sha256:df14fd7ceb838661edc7b2d78073b55a500899c75e1d26aac659cdefec63e007"}, "docker": "quay.io/biocontainers/mimsi", "aliases": {"analyze": "/usr/local/bin/analyze", "create_data": "/usr/local/bin/create_data", "evaluate_sample": "/usr/local/bin/evaluate_sample", "mi_msi_train_test": "/usr/local/bin/mi_msi_train_test", "visualize_instance": "/usr/local/bin/visualize_instance", "nosetests-3.9": "/usr/local/bin/nosetests-3.9", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "nosetests": "/usr/local/bin/nosetests", "f2py3.8": "/usr/local/bin/f2py3.8", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.8": "/usr/local/bin/2to3-3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mimsi.
shpc-registry automated BioContainers addition for mimsi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mimsi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mimsi:0.4.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mimsi/0.4.4--pyhdfd78af_0
$ module help quay.io/biocontainers/mimsi/0.4.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mimsi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mimsi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mimsi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mimsi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mimsi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mimsi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### analyze

```bash
$ singularity exec <container> /usr/local/bin/analyze
$ podman run --it --rm --entrypoint /usr/local/bin/analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_data

```bash
$ singularity exec <container> /usr/local/bin/create_data
$ podman run --it --rm --entrypoint /usr/local/bin/create_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evaluate_sample

```bash
$ singularity exec <container> /usr/local/bin/evaluate_sample
$ podman run --it --rm --entrypoint /usr/local/bin/evaluate_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluate_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mi_msi_train_test

```bash
$ singularity exec <container> /usr/local/bin/mi_msi_train_test
$ podman run --it --rm --entrypoint /usr/local/bin/mi_msi_train_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mi_msi_train_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualize_instance

```bash
$ singularity exec <container> /usr/local/bin/visualize_instance
$ podman run --it --rm --entrypoint /usr/local/bin/visualize_instance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualize_instance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests-3.9

```bash
$ singularity exec <container> /usr/local/bin/nosetests-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-caffe2-to-onnx

```bash
$ singularity exec <container> /usr/local/bin/convert-caffe2-to-onnx
$ podman run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-onnx-to-caffe2

```bash
$ singularity exec <container> /usr/local/bin/convert-onnx-to-caffe2
$ podman run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ninja

```bash
$ singularity exec <container> /usr/local/bin/ninja
$ podman run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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